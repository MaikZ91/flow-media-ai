#!/usr/bin/env python3
"""Holt aktuelle KI-News aus offenen RSS-Feeds und schreibt flow-dna/news.js (window.NEWS) + flow-dna/news.json.
Nur Titel, Kurzbeschreibung (gekürzt), Quelle, Datum und Link – der volle Text bleibt beim Verlag."""
import json, re, html, os, sys, urllib.request, email.utils, datetime as dt
import xml.etree.ElementTree as ET
KI = r"\b(KI|AI|künstliche Intelligenz|OpenAI|ChatGPT|GPT|Claude|Anthropic|Gemini|LLM|Sprachmodell|Copilot|Mistral|DeepSeek|Chatbot|Agent)"
FEEDS = [
    ("The Decoder", "https://the-decoder.de/feed/", None, "de"),
    ("t3n", "https://t3n.de/tag/kuenstliche-intelligenz/rss.xml", "KI", "de"),
    ("heise", "https://www.heise.de/rss/heise-atom.xml", "KI", "de"),
    ("OpenAI", "https://openai.com/news/rss.xml", None, "en"),
]
YT = [  # YouTube-Kanäle (RSS ohne API-Key): (Name, Kanal-ID, Sprache) – hier ergänzen
    ("Everlast AI", "UC8T5gQ4U4GbI2h8kYCkEcvg", "de"),
    ("Everlast Robotics", "UCrsjdqXseSxCpRgeSbdimTg", "de"),
    ("Everlast AI Clips", "UCMSjKPOf6yQc746Ka1tZwfQ", "de"),
    ("Cinetiq", "UC6Y1kbmjgVozhs41nQ6QT8A", "de"),
    ("Anthropic", "UCrDwWp7EBBv4NwvScIpBDOA", "en"),
    ("OpenAI", "UCXZCJLdBC09xxGZ6gcdrc6A", "en"),
    ("Google DeepMind", "UCP7jMXSY2xbc3KCAE0MHQ-A", "en"),
    ("Two Minute Papers", "UCbfYPyITQ-7l4upoX8nvctg", "en"),
]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "flow-dna")
def clean(s, n=220):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or "")); s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"(Der Beitrag|The post) .* erschien zuerst auf .*$", "", s).strip()
    return (s[:n].rsplit(" ", 1)[0] + " …") if len(s) > n else s
def when(s):
    if not s: return None
    try: return email.utils.parsedate_to_datetime(s).astimezone(dt.timezone.utc)
    except Exception: pass
    try: return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(dt.timezone.utc)
    except Exception: return None
def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "FlowMediaAI-News/1.0"})
    return urllib.request.urlopen(req, timeout=25).read()
items = []
for name, url, flt, lang in FEEDS:
    try: root = ET.fromstring(fetch(url))
    except Exception as e: print("skip", name, e, file=sys.stderr); continue
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entries = root.findall(".//item") or root.findall(".//a:entry", ns)
    n = 0
    for it in entries:
        g = lambda tag: (it.findtext(tag) or it.findtext("a:" + tag, namespaces=ns) or "")
        title = clean(g("title"), 160)
        link = g("link").strip()
        if not link:
            l = it.find("a:link", ns); link = l.get("href") if l is not None else ""
        desc = clean(g("description") or g("summary") or g("content"))
        d = when(g("pubDate") or g("published") or g("updated"))
        if not title or not link or not d: continue
        if flt and (not re.search(KI, title) or title.startswith("heise-Angebot")): continue
        items.append({"t": title, "s": desc, "q": name, "l": link, "d": d.isoformat(), "lang": lang}); n += 1
        if n >= 12: break
items.sort(key=lambda x: x["d"], reverse=True)
seen, out = set(), []
for x in items:
    k = re.sub(r"\W+", "", x["t"].lower())[:50]
    if k in seen: continue
    seen.add(k); out.append(x)
out = out[:30]
vids = []
YNS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015", "media": "http://search.yahoo.com/mrss/"}
for name, cid, lang in YT:
    try: root = ET.fromstring(fetch("https://www.youtube.com/feeds/videos.xml?channel_id=" + cid))
    except Exception as e: print("skip", name, e, file=sys.stderr); continue
    for en in root.findall("a:entry", YNS)[:5]:
        vid = en.findtext("yt:videoId", namespaces=YNS); t = en.findtext("a:title", namespaces=YNS) or ""
        d = when(en.findtext("a:published", namespaces=YNS))
        if not vid or not d or "#shorts" in t.lower(): continue
        vids.append({"id": vid, "t": clean(t, 140), "q": name, "d": d.isoformat(), "lang": lang})
vids.sort(key=lambda x: x["d"], reverse=True); vids = vids[:40]
data = {"stand": dt.datetime.now(dt.timezone.utc).isoformat(timespec="minutes"), "quellen": [f[0] for f in FEEDS], "items": out, "kanaele": [y[0] for y in YT], "videos": vids}
open(os.path.join(OUT, "news.json"), "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, indent=1))
open(os.path.join(OUT, "news.js"), "w", encoding="utf-8").write("window.NEWS = " + json.dumps(data, ensure_ascii=False) + ";\n")
print(len(out), "News")
