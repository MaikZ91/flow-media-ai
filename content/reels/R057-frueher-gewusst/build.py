"""R057 · Tag 5/31 – „Das hätte ich gerne früher gewusst“ (B-Roll-Reel aus echten Fotos + Text-Overlay)."""
import json, subprocess, pathlib
D = pathlib.Path(__file__).parent
P = D / "../../personal"
SCENES = [
    # (photo, seconds, kicker, headline-html, sub)
    (P / "arbeitsplatz/arbeitsplatz-buero-blazer.png", 2.6, "Tag 5/31 · Learnings", "5 Dinge über KI, die ich gerne <span>früher</span> gewusst hätte.", ""),
    (P / "strand-sonnenbrille.jpg", 3.0, "01", "Fang mit dem <span>Problem</span> an.", "Nicht mit dem Tool."),
    (P / "arbeitsplatz/arbeitsplatz-labor.jpg", 3.0, "02", "Starte mit <span>einer</span> Aufgabe.", "Am besten eine, die dich jede Woche Zeit kostet."),
    (P / "arbeitsplatz/arbeitsplatz-hololens.jpg", 3.0, "03", "Erst bauen. Dann <span>verbessern.</span>", "Perfekt kommt später."),
    (P / "cafe-weinglas.jpg", 3.0, "04", "Allein rausfinden kostet am <span>meisten</span> Zeit.", "Frag Leute, die schon weiter sind."),
    (D / "pulli-ohne-wasserzeichen.jpg", 3.0, "05", "KI ersetzt nicht dein <span>Denken.</span>", "Sie macht es schneller."),
    (P / "muenster-prinzipalmarkt-tag.jpg", 3.2, "Und du?", "Welcher Punkt <span>trifft</span> dich?", "Schreib die Nummer in die Kommentare."),
]
HTML = """<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Montserrat:wght@600&family=Inter:wght@400;500&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent}body{width:1080px;height:1920px;position:relative;overflow:hidden;color:#fff;font-family:Inter,sans-serif}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.55),rgba(10,10,10,0) 22%,rgba(10,10,10,0) 42%,rgba(10,10,10,.85) 66%,#0A0A0A 100%)}
.top{position:absolute;left:70px;right:70px;top:120px;display:flex;justify-content:space-between;align-items:center}.top img{height:44px}
.tag{font:600 20px Montserrat;letter-spacing:.2em;text-transform:uppercase;border:1px solid rgba(255,255,255,.45);border-radius:999px;padding:12px 22px;background:rgba(10,10,10,.5)}
.c{position:absolute;left:70px;right:70px;bottom:330px}.k{font:600 42px Montserrat;letter-spacing:.2em;text-transform:uppercase;color:#2F5BFF}
h1{margin-top:20px;font:700 __SIZE__px/.95 Oswald;text-transform:uppercase}h1 span{color:#2F5BFF}p{margin-top:30px;font:500 44px/1.35 Inter;color:rgba(255,255,255,.9)}
</style></head><body><div class="sh"></div><div class="top"><img src="logo_flow.png"><span class="tag">#31TageSichtbar</span></div>
<div class="c"><div class="k">__K__</div><h1>__H__</h1>__P__</div></body></html>"""

def run(*a): subprocess.run(a, check=True)

def overlays():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium"); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for i, (_, _, k, h, p) in enumerate(SCENES):
            size = 150 if i == 0 else 160
            html = HTML.replace("__SIZE__", str(size)).replace("__K__", k).replace("__H__", h).replace("__P__", f"<p>{p}</p>" if p else "")
            f = D / f"ov{i}.html"; f.write_text(html, encoding="utf-8")
            pg.goto(f.resolve().as_uri()); pg.wait_for_timeout(900)
            pg.screenshot(path=str(D / f"ov{i}.png"), omit_background=True)
            f.unlink()
        b.close()

def clips():
    parts = []
    for i, (ph, sec, *_ ) in enumerate(SCENES):
        n = int(sec * 30); out = D / f"s{i}.mp4"
        zin = "1+0.0009*on" if i % 2 == 0 else "1.08-0.0009*on"
        run("ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", str(ph), "-loop", "1", "-i", str(D / f"ov{i}.png"),
            "-filter_complex",
            f"[0]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,zoompan=z='{zin}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps=30,eq=saturation=0.92[bg];[bg][1]overlay=0:0,format=yuv420p",
            "-frames:v", str(n), "-r", "30", str(out))
        parts.append(out)
    lst = D / "list.txt"; lst.write_text("".join(f"file '{p.name}'\n" for p in parts))
    total = sum(s[1] for s in SCENES)
    run("ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-ss", "3",
        "-i", str(D / "../../musik/eigene/mz9_independence-2-1.m4a"),
        "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p",
        "-af", f"afade=t=in:d=0.15,afade=t=out:st={total-1.2}:d=1.2", "-c:a", "aac", "-b:a", "192k", "-t", str(total), "-movflags", "+faststart", str(D / "R057.mp4"))
    run("ffmpeg", "-y", "-v", "error", "-ss", "1.2", "-i", str(D / "R057.mp4"), "-frames:v", "1", "-q:v", "3", str(D / "cover.jpg"))
    for p in parts: p.unlink()
    lst.unlink()

if __name__ == "__main__":
    overlays(); clips(); print("ok")
