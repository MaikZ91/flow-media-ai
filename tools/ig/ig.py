#!/usr/bin/env python3
"""Instagram Graph API helper for @flow.media.ai.

The access token is never stored here: the cloud environment's network secret
for graph.facebook.com injects the Authorization header. If IG_TOKEN is set in
the environment it is used instead (local runs).

  ig.py insights                 refresh content/autopilot/insights.json, print table
  ig.py today                    posts published today (Europe/Berlin)
  ig.py wait-url URL [secs]      wait until a public URL answers 200 (Pages deploy)
  ig.py reel VIDEO_URL CAPTION_FILE [COVER_URL]
  ig.py carousel CAPTION_FILE IMG_URL [IMG_URL ...]   (2-10 JPEG)
  ig.py image CAPTION_FILE IMG_URL
  ig.py story MEDIA_URL          image (jpg) or video (mp4) story
  ig.py stories                  save insights of live stories (<24 h) into content/autopilot/stories.json
"""
import json, os, sys, time, urllib.parse, urllib.request, urllib.error
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

IG = os.environ.get("IG_USER_ID", "17841419830106399")  # @flow.media.ai; set IG_USER_ID for another account
API = "https://graph.facebook.com/v21.0/"
BER = ZoneInfo("Europe/Berlin")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "content", "autopilot", "insights.json")
METRICS = "views,reach,saved,shares,likes,comments,total_interactions"


def call(path, params=None, post=False):
    params = dict(params or {})
    headers = {}
    if os.environ.get("IG_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["IG_TOKEN"]
    q = urllib.parse.urlencode(params)
    url = API + path
    req = urllib.request.Request(url if post else (url + ("?" + q if q else "")),
                                 data=q.encode() if post else None, headers=headers,
                                 method="POST" if post else "GET")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        sys.exit(f"Graph API {e.code}: {body[:600]}")


def berlin(ts):
    return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S%z").astimezone(BER)


def insights():
    acc = call(IG, {"fields": "followers_count,media_count"})
    rows, nxt = [], f"{IG}/media"
    params = {"fields": f"id,timestamp,media_type,media_product_type,permalink,caption,insights.metric({METRICS})", "limit": 50}
    data = call(nxt, params)
    for m in data.get("data", []):
        ins = {i["name"]: i["values"][0]["value"] for i in m.get("insights", {}).get("data", [])}
        b = berlin(m["timestamp"])
        rows.append({"id": m["id"], "zeit": b.strftime("%Y-%m-%d %H:%M"), "wochentag": b.strftime("%a"),
                     "stunde": b.hour, "typ": m.get("media_product_type"), "format": m.get("media_type"),
                     "permalink": m.get("permalink"), "caption": (m.get("caption") or "")[:160], **ins})
    snap = {"abgerufen": datetime.now(BER).strftime("%Y-%m-%d %H:%M"), "follower": acc.get("followers_count"), "posts": rows}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(snap, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"Follower {snap['follower']} · {len(rows)} Posts · Stand {snap['abgerufen']}")
    print("zeit             tag typ    views reach saves shares likes  caption")
    for r in rows:
        print(f"{r['zeit']} {r['wochentag']} {str(r['typ'])[:6]:6} {r.get('views','-'):>5} {r.get('reach','-'):>5} "
              f"{r.get('saved','-'):>5} {r.get('shares','-'):>6} {r.get('likes','-'):>5}  {r['caption'][:50].replace(chr(10),' ')}")


def stories():
    path = os.path.join(ROOT, "content", "autopilot", "stories.json")
    try: known = {r["id"]: r for r in json.load(open(path))}
    except Exception: known = {}
    d = call(f"{IG}/stories", {"fields": "id,timestamp,media_type,insights.metric(views,reach,replies,shares,navigation)"})
    for m in d.get("data", []):
        ins = {i["name"]: i["values"][0]["value"] for i in m.get("insights", {}).get("data", [])}
        old = known.get(m["id"], {})
        known[m["id"]] = {**old, "id": m["id"], "zeit": berlin(m["timestamp"]).strftime("%Y-%m-%d %H:%M"),
                          "format": m.get("media_type"), **ins, "stand": datetime.now(BER).strftime("%Y-%m-%d %H:%M")}
    rows = sorted(known.values(), key=lambda r: r["zeit"], reverse=True)
    json.dump(rows, open(path, "w"), ensure_ascii=False, indent=1)
    for r in rows[:15]:
        print(r["zeit"], r["format"], "views", r.get("views"), "reach", r.get("reach"), "replies", r.get("replies"),
              "navigation", r.get("navigation"), r.get("inhalt", ""))


def today():
    d = call(f"{IG}/media", {"fields": "timestamp,permalink,caption", "limit": 10})
    now = datetime.now(BER).date()
    hits = [m for m in d.get("data", []) if berlin(m["timestamp"]).date() == now]
    for m in hits:
        print(berlin(m["timestamp"]).strftime("%H:%M"), m["permalink"], (m.get("caption") or "")[:50].replace("\n", " "))
    print(f"{len(hits)} Post(s) heute")


def wait_url(url, secs=600):
    t0 = time.time()
    while time.time() - t0 < secs:
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=30) as r:
                if r.status == 200:
                    print("online:", url); return
        except Exception:
            pass
        time.sleep(15)
    sys.exit("nicht erreichbar: " + url)


def finish(cid):
    for _ in range(60):
        s = call(cid, {"fields": "status_code,status"})
        if s.get("status_code") == "FINISHED":
            break
        if s.get("status_code") in ("ERROR", "EXPIRED"):
            sys.exit("Container-Fehler: " + json.dumps(s))
        time.sleep(10)
    else:
        sys.exit("Container nicht fertig nach 10 Min")
    pub = call(f"{IG}/media_publish", {"creation_id": cid}, post=True)
    m = call(pub["id"], {"fields": "permalink,timestamp"})
    print("GEPOSTET", m.get("permalink"), m.get("timestamp"))


def cap(path):
    return open(path, encoding="utf-8").read().strip()


def main(a):
    if not a:
        sys.exit(__doc__)
    cmd = a[0]
    if cmd == "insights": insights()
    elif cmd == "today": today()
    elif cmd == "stories": stories()
    elif cmd == "wait-url": wait_url(a[1], int(a[2]) if len(a) > 2 else 600)
    elif cmd == "reel":
        p = {"media_type": "REELS", "video_url": a[1], "caption": cap(a[2]), "share_to_feed": "true"}
        if len(a) > 3: p["cover_url"] = a[3]
        finish(call(f"{IG}/media", p, post=True)["id"])
    elif cmd == "carousel":
        kids = [call(f"{IG}/media", {"image_url": u, "is_carousel_item": "true"}, post=True)["id"] for u in a[2:]]
        finish(call(f"{IG}/media", {"media_type": "CAROUSEL", "children": ",".join(kids), "caption": cap(a[1])}, post=True)["id"])
    elif cmd == "image":
        finish(call(f"{IG}/media", {"image_url": a[2], "caption": cap(a[1])}, post=True)["id"])
    elif cmd == "story":
        key = "video_url" if a[1].lower().endswith(".mp4") else "image_url"
        finish(call(f"{IG}/media", {"media_type": "STORIES", key: a[1]}, post=True)["id"])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
