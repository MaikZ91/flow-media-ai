"""R062 · „Vom Storyboard zum Video“ – wie aus EINEM Storyboard-Bild mit MAGI-2 ein 15-s-Film wird (~17 s).

0–2,0 s    Hook: Szene aus dem fertigen Film + „Dieses Video kommt aus EINEM Bild.“
2,0–3,6 s  Schritt 1: das Storyboard (6 Szenen in einem Bild), Zoom
3,6–4,6 s  Schritt 2: Bild rein in MAGI-2 (Higgsfield)
4,6–15,4 s 6× Storyboard-Bild (0,6 s) → passende Szene im Video (1,2 s)
15,4–17,4 s Endkarte
Material: ../R060-magi2/storyboard.png, ../R060-magi2/magi2_raw.mp4 (beides KI, Higgsfield).
"""
import subprocess, pathlib
from PIL import Image
D = pathlib.Path(__file__).parent
SRC = D / "../R060-magi2"
SB, VID = SRC / "storyboard.png", SRC / "magi2_raw.mp4"
MUSIK = D / "../../musik/frei/driving-ambition.mp3"
F = 2688 / 1200  # Faktor Vorschau → Original
BOX = [(5,5,385,388),(390,5,675,388),(5,392,337,773),(342,392,675,773),(5,777,337,1195),(342,777,675,1195)]
NAMES = ["Wüste, alte Karte", "Karte wird digital", "Neon-Stadt", "Skizze wird Auto", "Cello & Klangwellen", "Galaxie im Auge"]
SEG = [(0.5,1.7),(3.2,4.4),(5.4,6.6),(8.3,9.5),(11.0,12.2),(13.3,14.5)]
HOOK = (5.2, 7.2)

HEAD = """<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Montserrat:wght@700&family=Inter:wght@500;600&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent}body{width:1080px;height:1920px;position:relative;overflow:hidden;color:#fff;font-family:Inter,sans-serif}
.k{font:700 44px Montserrat;text-transform:uppercase;letter-spacing:.03em;text-shadow:0 2px 14px rgba(0,0,0,.7)}
h1{font:700 128px/1.32 Oswald;text-transform:uppercase;margin-top:12px}h1 span{background:#2F5BFF;padding:.02em .12em 0;border-radius:6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
p{font:600 48px/1.3 Inter;margin-top:22px}.c{position:absolute;left:70px;right:70px}.logo{position:absolute;left:70px;height:44px}
.tag{display:inline-block;font:700 40px Montserrat;letter-spacing:.06em;text-transform:uppercase;background:#2F5BFF;padding:10px 22px;border-radius:8px}
.tag.w{background:#fff;color:#0A0A0A}
</style></head><body>"""
TOPGRAD = '<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.92) 0%,rgba(10,10,10,.5) 22%,rgba(10,10,10,0) 36%)"></div>'

def html_pages():
    pages = {}
    pages["hook"] = HEAD + TOPGRAD + '<img class="logo" src="logo_flow.png" style="top:170px"><div class="c" style="top:260px"><div class="k">MAGI-2 · Higgsfield</div><h1>Dieses Video kommt aus <span>einem Bild.</span></h1></div></body></html>'
    pages["s1"] = HEAD + TOPGRAD + '<img class="logo" src="logo_flow.png" style="top:170px"><div class="c" style="top:260px"><div class="k">Schritt 1</div><h1 style="font-size:112px">Ein <span>Storyboard.</span></h1><p>6 Szenen in einem Bild.</p></div></body></html>'
    pages["s2"] = HEAD.replace("html,body{background:transparent}","html,body{background:#0A0A0A}") + '<img class="logo" src="logo_flow.png" style="top:250px"><div class="c" style="top:560px"><div class="k" style="color:#9A9A9A">Schritt 2</div><h1 style="font-size:120px">Bild rein in <span>MAGI-2.</span></h1><p>Dazu ein Prompt: Folge dem Storyboard Szene für Szene, nahtlose Übergänge, 15 Sekunden, mit Ton.</p></div></body></html>'
    for i, n in enumerate(NAMES):
        pages[f"p{i}"] = HEAD.replace("html,body{background:transparent}","html,body{background:#0A0A0A}") + f'''
<div style="position:absolute;inset:-40px;background:url(panel{i}.jpg) center/cover;filter:blur(40px) brightness(.35)"></div>
<div class="c" style="top:250px"><span class="tag w">Storyboard {i+1}/6</span><p style="margin-top:26px">{n}</p></div>
<img src="panel{i}.jpg" style="position:absolute;left:70px;right:70px;width:940px;top:560px;max-height:1080px;object-fit:contain;border-radius:18px;border:3px solid #fff;box-shadow:0 30px 80px rgba(0,0,0,.7)"></body></html>'''
    pages["v"] = HEAD + TOPGRAD + '<div class="c" style="top:250px"><span class="tag">→ Video</span></div></body></html>'
    pages["end"] = HEAD.replace("html,body{background:transparent}","html,body{background:#0A0A0A}") + '''<img class="logo" src="logo_flow.png" style="top:250px"><div class="c" style="top:520px">
<div class="k" style="color:#9A9A9A">So geht's</div><h1 style="font-size:116px">1 Bild. 1 Prompt. <span>15 s Film.</span></h1>
<p>Mit Ton, im Reel-Format, 37,5 Credits.</p><p style="font:700 60px Oswald;text-transform:uppercase;margin-top:60px">Folg mir für mehr KI-Workflows</p></div></body></html>'''
    return pages

def render():
    sb = Image.open(SB).convert("RGB")
    for i, (a, b, c, d) in enumerate(BOX):
        sb.crop((int(a*F)+6, int(b*F)+6, int(c*F)-6, int(d*F)-6)).save(D / f"panel{i}.jpg", quality=92)
    full = sb.copy(); full.thumbnail((1080, 1920)); bg = Image.new("RGB", (1080, 1920), (10, 10, 10))
    bg.paste(full, ((1080 - full.width) // 2, (1920 - full.height) // 2)); bg.save(D / "sb_full.jpg", quality=92)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        br = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium"); pg = br.new_page(viewport={"width": 1080, "height": 1920})
        for n, h in html_pages().items():
            f = D / f"_{n}.html"; f.write_text(h, encoding="utf-8"); pg.goto(f.resolve().as_uri()); pg.wait_for_timeout(1300)
            pg.screenshot(path=str(D / f"o_{n}.png"), omit_background=n in ("hook", "s1", "v")); f.unlink()
        br.close()

def build():
    parts = []  # (file, seconds)
    def vid(a, b, ov, out):
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", str(a), "-t", str(b - a), "-i", str(VID), "-i", str(D / ov),
                        "-filter_complex", "[0:v]scale=1080:1920,fps=30[x];[x][1:v]overlay=0:0,format=yuv420p[v];[0:a]aresample=48000,aformat=channel_layouts=stereo[a]",
                        "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", str(D / out)], check=True)
        parts.append(out)
    def still(img, sec, out, zoom="1+0.0006*on", ov=None):
        n = int(sec * 30)
        inputs = ["-loop", "1", "-t", str(sec), "-i", str(D / img)] + (["-loop", "1", "-t", str(sec), "-i", str(D / ov)] if ov else [])
        fc = f"[0:v]scale=2160:3840,zoompan=z='{zoom}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps=30,trim=0:{sec},setpts=PTS-STARTPTS[b]"
        fc += ";[b][1:v]overlay=0:0,format=yuv420p[v]" if ov else ";[b]format=yuv420p[v]"
        subprocess.run(["ffmpeg", "-y", "-v", "error", *inputs, "-f", "lavfi", "-t", str(sec), "-i", "anullsrc=r=48000:cl=stereo",
                        "-filter_complex", fc, "-map", "[v]", "-map", f"{2 if ov else 1}:a", "-t", str(sec),
                        "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", str(D / out)], check=True)
        parts.append(out)
    vid(*HOOK, "o_hook.png", "q0.mp4")
    still("sb_full.jpg", 1.6, "q1.mp4", zoom="1.25-0.0045*on", ov="o_s1.png")
    still("o_s2.png", 1.0, "q2.mp4")
    for i, (a, b) in enumerate(SEG):
        still(f"o_p{i}.png", 0.6, f"q3_{i}a.mp4", zoom="1+0.0012*on")
        vid(a, b, "o_v.png", f"q3_{i}b.mp4")
    still("o_end.png", 2.0, "q4.mp4", zoom="1+0.0004*on")
    lst = D / "list.txt"; lst.write_text("".join(f"file '{p}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(D / "_cat.mp4")], check=True)
    total = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(D / "_cat.mp4")]))
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(D / "_cat.mp4"), "-i", str(MUSIK), "-filter_complex",
                    f"[0:a]volume=0.9[s];[1:a]atrim=0:{total},volume=0.5,afade=t=out:st={total-1}:d=1[m];[s][m]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(D / "R062.mp4")], check=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "0.8", "-i", str(D / "R062.mp4"), "-frames:v", "1", "-q:v", "2", str(D / "cover.jpg")], check=True)
    for p in parts + ["_cat.mp4", "list.txt"]: (D / p).unlink()

if __name__ == "__main__":
    render(); build(); print("ok")
