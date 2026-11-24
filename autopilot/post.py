"""Publish one approved and due Instagram post per workflow run."""

import base64
from datetime import datetime, timedelta, timezone
import json
import os
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

STATE_BRANCH = "instagram-autopilot-state"


class ApiError(Exception):
    def __init__(self, service, status):
        self.status = status
        super().__init__(f"{service}: HTTP {status}")


def request(service, url, token, method="GET", data=None):
    headers = {"Authorization": f"Bearer {token}"}
    body = None
    if data is not None:
        if service == "GitHub":
            headers["Content-Type"] = "application/json"
            body = json.dumps(data).encode()
        else:
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            body = urlencode(data).encode()
    try:
        with urlopen(Request(url, body, headers, method=method), timeout=20) as response:
            return json.load(response)
    except HTTPError as error:
        raise ApiError(service, error.code) from None
    except (URLError, TimeoutError, ValueError):
        raise RuntimeError(f"{service}: keine verwertbare Antwort.") from None


def queue(raw, now):
    entries = json.loads(raw)
    if not isinstance(entries, list):
        raise ValueError("IG_POST_QUEUE muss eine JSON-Liste sein.")
    ids = set()
    ready = []
    for post in entries:
        if not isinstance(post, dict):
            raise ValueError("Ungültiger Eintrag in IG_POST_QUEUE.")
        post_id = post.get("id")
        if not isinstance(post_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", post_id) or post_id in ids:
            raise ValueError("Jeder Beitrag braucht eine eindeutige ID aus a–z, 0–9 und Bindestrichen.")
        ids.add(post_id)
        if post.get("approved") is not True:
            continue
        timestamp = datetime.fromisoformat(post["publish_at"].replace("Z", "+00:00"))
        if timestamp.utcoffset() is None:
            raise ValueError("publish_at muss einen UTC-Offset enthalten.")
        kind = post["format"]
        urls = post["media_urls"]
        if kind not in {"image", "reel", "carousel"} or not isinstance(urls, list):
            raise ValueError("Unterstützte Formate sind image, reel und carousel.")
        if not (2 <= len(urls) <= 10 if kind == "carousel" else len(urls) == 1):
            raise ValueError("Ungültige Medienanzahl.")
        for url in urls:
            parts = urlsplit(url)
            if parts.scheme != "https" or not parts.hostname or parts.username or parts.password:
                raise ValueError("Medien benötigen eine abrufbare HTTPS-URL.")
        if not isinstance(post["caption"], str) or len(post["caption"]) > 2200:
            raise ValueError("Die Caption darf höchstens 2200 Zeichen haben.")
        if now - timedelta(hours=24) <= timestamp <= now:
            ready.append((timestamp, post_id, post))
    return sorted(ready)


def github(path, method="GET", data=None):
    base = f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}"
    return request("GitHub", base + path, os.environ["GH_STATE_TOKEN"], method, data)


def ensure_state_branch():
    try:
        github(f"/git/ref/heads/{STATE_BRANCH}")
    except ApiError as error:
        if error.status != 404:
            raise
        github("/git/refs", "POST", {"ref": f"refs/heads/{STATE_BRANCH}", "sha": os.environ["GITHUB_SHA"]})


def read_state(post_id):
    try:
        item = github(f"/contents/autopilot-state/{post_id}.json?ref={STATE_BRANCH}")
    except ApiError as error:
        if error.status == 404:
            return {}, None
        raise
    return json.loads(base64.b64decode(item["content"])), item["sha"]


def write_state(post_id, state, sha):
    data = {
        "branch": STATE_BRANCH,
        "message": f"Record Instagram post {post_id}",
        "content": base64.b64encode(json.dumps(state).encode()).decode(),
    }
    if sha:
        data["sha"] = sha
    result = github(f"/contents/autopilot-state/{post_id}.json", "PUT", data)
    return result["content"]["sha"]


def instagram(path, method="GET", data=None):
    version = os.environ["IG_API_VERSION"]
    return request("Instagram", f"https://graph.instagram.com/{version}/{path}",
                   os.environ["IG_TOKEN"], method, data)


def container_status(container):
    return instagram(f"{container}?fields=status_code")["status_code"]


def wait_ready(container):
    for _ in range(12):
        status = container_status(container)
        if status in {"FINISHED", "PUBLISHED"}:
            return status
        if status in {"ERROR", "EXPIRED"}:
            raise RuntimeError(f"Instagram-Container: {status}.")
        time.sleep(10)
    raise RuntimeError("Instagram hat das Medium noch nicht verarbeitet.")


def create_container(post, account):
    urls = post["media_urls"]
    data = {"caption": post["caption"]}
    if post["format"] == "carousel":
        children = []
        for url in urls:
            child = instagram(f"{account}/media", "POST", {
                "image_url": url, "is_carousel_item": "true",
            })["id"]
            wait_ready(child)
            children.append(child)
        data.update(media_type="CAROUSEL", children=",".join(children))
    elif post["format"] == "reel":
        data.update(media_type="REELS", video_url=urls[0])
    else:
        data["image_url"] = urls[0]
    return instagram(f"{account}/media", "POST", data)["id"]


def main():
    raw = os.getenv("IG_POST_QUEUE")
    publish = os.getenv("IG_PUBLISH") == "true"
    if not raw:
        raise ValueError("Das GitHub Secret IG_POST_QUEUE fehlt.")
    ready = queue(raw, datetime.now(timezone.utc))
    if not publish:
        print(f"Vorschau: {len(ready)} freigegebene, fällige Einträge.")
        return
    if not ready:
        print("Kein freigegebener Beitrag fällig.")
        return
    account = os.getenv("IG_USER_ID", "")
    if not account.isdecimal() or not os.getenv("IG_TOKEN"):
        raise ValueError("Die GitHub Secrets IG_USER_ID und IG_TOKEN müssen eingerichtet sein.")
    if not re.fullmatch(r"v[0-9]+\.[0-9]+", os.getenv("IG_API_VERSION", "")):
        raise ValueError("Die Repository-Variable IG_API_VERSION muss gesetzt sein.")
    ensure_state_branch()
    for _, post_id, post in ready:
        state, sha = read_state(post_id)
        if state.get("published"):
            continue
        container = state.get("container")
        if container is None:
            container = create_container(post, account)
            state = {"container": container}
            sha = write_state(post_id, state, sha)
        if state.get("attempted"):
            if container_status(container) == "PUBLISHED":
                write_state(post_id, {**state, "published": True}, sha)
                print("Frühere Veröffentlichung bestätigt.")
                return
            raise RuntimeError("Veröffentlichung schon versucht. Vor Wiederholung Instagram prüfen.")
        wait_ready(container)
        state["attempted"] = True
        sha = write_state(post_id, state, sha)
        media_id = instagram(f"{account}/media_publish", "POST", {"creation_id": container})["id"]
        write_state(post_id, {**state, "published": True, "media_id": media_id}, sha)
        print("Instagram hat die Veröffentlichung bestätigt.")
        return
    print("Alle fälligen Beiträge wurden bereits veröffentlicht.")


if __name__ == "__main__":
    try:
        main()
    except (KeyError, TypeError, AttributeError, ValueError):
        raise SystemExit("Ungültige oder fehlende Konfiguration in GitHub oder in der Warteschlange.") from None
    except (ApiError, RuntimeError) as error:
        raise SystemExit(str(error)) from None
