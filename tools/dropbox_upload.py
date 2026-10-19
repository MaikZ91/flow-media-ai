#!/usr/bin/env python3
"""Upload local files (PDF, PNG, MP4, ...) to Maik's Dropbox via the Dropbox HTTP API.

The Dropbox connector can only create text files and never overwrite. This script
fills the gap: binary files, and overwriting existing files (mode=overwrite).

Credentials come only from the environment (never commit them):
  DROPBOX_APP_KEY, DROPBOX_APP_SECRET, DROPBOX_REFRESH_TOKEN

Usage:
  python3 tools/dropbox_upload.py <local file> "/Flow Media AI/<folder>/<name>"
  python3 tools/dropbox_upload.py a.pdf b.png "/Flow Media AI/<folder>/"   # trailing slash = folder
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

MAX_SIMPLE_UPLOAD = 150 * 1024 * 1024  # Dropbox limit for /files/upload


def access_token():
    need = ("DROPBOX_APP_KEY", "DROPBOX_APP_SECRET", "DROPBOX_REFRESH_TOKEN")
    missing = [k for k in need if not os.environ.get(k)]
    if missing:
        sys.exit("Fehlende Umgebungsvariablen: " + ", ".join(missing))
    data = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "refresh_token": os.environ["DROPBOX_REFRESH_TOKEN"],
        "client_id": os.environ["DROPBOX_APP_KEY"],
        "client_secret": os.environ["DROPBOX_APP_SECRET"],
    }).encode()
    with urllib.request.urlopen("https://api.dropboxapi.com/oauth2/token", data) as r:
        return json.load(r)["access_token"]


def upload(token, local, remote):
    size = os.path.getsize(local)
    if size > MAX_SIMPLE_UPLOAD:
        sys.exit(f"{local}: {size // 2**20} MB ist zu groß für den einfachen Upload (max. 150 MB).")
    # Dropbox-API-Arg must be ASCII: json.dumps escapes umlauts as \uXXXX.
    arg = json.dumps({"path": remote, "mode": "overwrite", "autorename": False, "mute": True})
    with open(local, "rb") as f:
        req = urllib.request.Request("https://content.dropboxapi.com/2/files/upload", data=f.read(), headers={
            "Authorization": "Bearer " + token,
            "Dropbox-API-Arg": arg,
            "Content-Type": "application/octet-stream",
        })
    try:
        with urllib.request.urlopen(req) as r:
            meta = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"{local}: Upload fehlgeschlagen ({e.code}): {e.read().decode(errors='replace')}")
    print(f"ok  {meta['path_display']}  ({meta['size']} Bytes)")


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    *locals_, target = argv
    if len(locals_) > 1 and not target.endswith("/"):
        sys.exit("Bei mehreren Dateien muss das Ziel ein Ordner sein (mit / am Ende).")
    token = access_token()
    for local in locals_:
        remote = target + os.path.basename(local) if target.endswith("/") else target
        upload(token, local, remote)


if __name__ == "__main__":
    main(sys.argv[1:])
