"""Challenge Tag 6/31 · Story: Maiks echte Morgenroutine „kalt duschen“ (KI-Clip MAGI-2, Job a03ec078) + Umfrage als Text."""
import subprocess, pathlib
D = pathlib.Path(__file__).parent
HTML = """<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Montserrat:wght@700&family=Inter:wght@500;600&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent}body{width:1080px;height:1920px;position:relative;overflow:hidden;color:#fff;font-family:Inter,sans-serif}
.g{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.85) 0%,rgba(10,10,10,.3) 26%,rgba(10,10,10,0) 40%,rgba(10,10,10,0) 58%,rgba(10,10,10,.85) 78%,#0A0A0A 100%)}
.c{position:absolute;left:70px;right:70px}.k{font:700 40px Montserrat;text-transform:uppercase;letter-spacing:.04em}
h1{font:700 132px/1.32 Oswald;text-transform:uppercase;margin-top:10px}h1 span{background:#2F5BFF;padding:.02em .12em 0;border-radius:6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.poll{display:grid;gap:18px;margin-top:26px}.o{display:flex;align-items:center;gap:20px;padding:22px 30px;border-radius:999px;background:rgba(255,255,255,.95);color:#0A0A0A;font:700 50px Oswald;text-transform:uppercase}
.o b{display:inline-grid;place-items:center;width:64px;height:64px;border-radius:50%;background:#2F5BFF;color:#fff;font:700 40px Oswald}
.q{font:700 64px/1.2 Oswald;text-transform:uppercase}.s{font:500 30px Inter;color:rgba(255,255,255,.75);margin-top:20px}
.logo{position:absolute;left:70px;top:250px;height:40px}
</style></head><body><div class="g"></div><img class="logo" src="logo_flow.png">
<div class="c" style="top:330px"><div class="k">Tag 6/31 · Meine Morgenroutine</div><h1>Kalt <span>duschen.</span><br>Mein Start.</h1></div>
<div class="c" style="bottom:330px"><div class="q">Und du?</div><div class="poll"><div class="o"><b>A</b>Mach ich auch 🥶</div><div class="o"><b>B</b>Niemals 🔥</div></div>
<div class="s">Antwort per DM: A oder B · Clip mit KI erstellt (Higgsfield MAGI-2)</div></div></body></html>"""
f = D / "_o.html"; f.write_text(HTML, encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium"); pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto(f.resolve().as_uri()); pg.wait_for_timeout(1300); pg.screenshot(path=str(D / "overlay.png"), omit_background=True); b.close()
f.unlink()
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(D / "clip_raw.mp4"), "-i", str(D / "overlay.png"), "-filter_complex",
                "[0:v]scale=1080:1920,fps=30[b];[b][1:v]overlay=0:0,format=yuv420p[v]", "-map", "[v]", "-map", "0:a?",
                "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(D / "story.mp4")], check=True)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "2.5", "-i", str(D / "story.mp4"), "-frames:v", "1", "-vf", "scale=540:-1", str(D / "preview.jpg")], check=True)
print("ok")
