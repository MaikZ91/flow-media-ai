"""R061 · Community-Reel nach Drehbuch Nr. 2, Variante B („Wüste kurz“), ~7,5 s.

0–3,0 s   MAGI-2-Clip: Maik ratlos mit Karte, die Karte wird zum blauen KI-Hologramm → Hook oben
3,0–6,1 s MAGI-2-Clip: futuristisches Camp (Hologramm-Feuer, KI-Screens), er geht hin → Lösung oben
6,1–8,7 s Endkarte im Flow-Look: Community + Stammtisch + Link unten (Schnitt zurück in die Wüste = Loop)
Ton: MAGI-Umgebungston (Wind, Feuer) + freie Musik mit Einsatz auf Frame 0.
"""
import subprocess, pathlib, sys
D = pathlib.Path(__file__).parent
CLIP = D / (sys.argv[1] if len(sys.argv) > 1 else "magi_raw.mp4")
MUSIK = D / "../../musik/frei/driving-ambition.mp3"
T1, T2, T3 = 3.0, 3.1, 2.6
import os
VO = os.environ.get("VO")            # z. B. stimmen/orion.mp3
SEG = os.environ.get("SEG", "")      # "a1,b1;a2,b2;a3,b3" = drei Sätze im VO (Sekunden)
OUT = os.environ.get("OUT", "R061.mp4")

HEAD = """<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Montserrat:wght@700&family=Inter:wght@500;600&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent}body{width:1080px;height:1920px;position:relative;overflow:hidden;color:#fff;font-family:Inter,sans-serif}
.k{font:700 46px Montserrat;text-transform:uppercase;letter-spacing:.02em;text-shadow:0 2px 14px rgba(0,0,0,.7)}
h1{font:700 150px/1.32 Oswald;text-transform:uppercase;margin-top:14px}h1 span{background:#2F5BFF;padding:.02em .12em 0;border-radius:6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
p{font:600 50px/1.3 Inter;margin-top:26px}.c{position:absolute;left:70px;right:70px}
.logo{position:absolute;left:70px;height:44px}
</style></head><body>"""
O1 = HEAD + """<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.95) 0%,rgba(10,10,10,.55) 20%,rgba(10,10,10,0) 34%)"></div>
<img class="logo" src="logo_flow.png" style="top:170px"><div class="c" style="top:260px"><div class="k">Gründer &amp; Selbstständige</div><h1>Lost mit <span>KI?</span></h1></div></body></html>"""
O2 = HEAD + """<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.9) 0%,rgba(10,10,10,.45) 22%,rgba(10,10,10,0) 36%)"></div>
<img class="logo" src="logo_flow.png" style="top:170px"><div class="c" style="top:260px"><div class="k">Musst du nicht allein lösen.</div><h1 style="font-size:118px">Komm in die <span>Community.</span></h1></div></body></html>"""
O3 = HEAD.replace("html,body{background:transparent}", "html,body{background:#0A0A0A}") + """
<img class="logo" src="logo_flow.png" style="top:250px"><div class="c" style="top:470px"><div class="k" style="color:#9A9A9A">Flow Business Community</div>
<h1 style="font-size:132px">Kostenlos in <span>WhatsApp.</span></h1>
<p>Für Gründer &amp; Selbstständige, die mit KI weiterkommen wollen.</p>
<p style="margin-top:44px;font-weight:600"><span style="background:#fff;color:#0A0A0A;padding:6px 18px;border-radius:6px">KI-Stammtisch Fr. 19 Uhr</span></p>
<p style="font-size:42px;color:rgba(255,255,255,.8);margin-top:20px">online oder vor Ort in Münster &amp; Bielefeld</p>
<p style="font:700 64px Oswald;text-transform:uppercase;margin-top:54px">Link unten ↓</p></div></body></html>"""


def overlays():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium"); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for n, html in (("o1", O1), ("o2", O2), ("o3", O3)):
            f = D / f"{n}.html"; f.write_text(html, encoding="utf-8"); pg.goto(f.resolve().as_uri()); pg.wait_for_timeout(1200)
            pg.screenshot(path=str(D / f"{n}.png"), omit_background=(n != "o3")); f.unlink()
        b.close()


def build():
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(CLIP)]))
    s = max(0.0, min(dur - (T1 + T2), 0.0))  # Clip vom Anfang an
    total = T1 + T2 + T3
    fc = (f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p,split[a][b];"
          f"[a]trim={s}:{s+T1},setpts=PTS-STARTPTS[v1];[b]trim={s+T1}:{s+T1+T2},setpts=PTS-STARTPTS[v2];"
          f"[v1][1:v]overlay=0:0[w1];[v2][2:v]overlay=0:0[w2];"
          f"[3:v]loop=-1:1,trim=0:{T3},setpts=PTS-STARTPTS,fps=30,format=yuv420p,"
          f"zoompan=z='1+0.0005*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30[w3];"
          f"[w1][w2][w3]concat=n=3:v=1:a=0,format=yuv420p[v];"
          f"[0:a]atrim={s}:{s+T1+T2},asetpts=PTS-STARTPTS,volume={0.3 if VO else 0.55},apad,atrim=0:{total}[amb];"
          f"[4:a]atrim=0:{total},volume={0.32 if VO else 0.8},afade=t=out:st={total-0.8}:d=0.8[mus];")
    inputs = []
    if VO:
        starts = [0.1, T1 + 0.15, T1 + T2 + 0.1]
        segs = [tuple(map(float, x.split(","))) for x in SEG.split(";")]
        for i, ((a, b), st) in enumerate(zip(segs, starts)):
            fc += (f"[5:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={b-a-0.05}:d=0.05,"
                   f"adelay={int(st*1000)}|{int(st*1000)},volume=1.6[vo{i}];")
        fc += "[amb][mus][vo0][vo1][vo2]amix=inputs=5:normalize=0,alimiter=limit=0.95[aud]"
        inputs = ["-i", str(D / VO)]
    else:
        fc += "[amb][mus]amix=inputs=2:normalize=0[aud]"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(CLIP), "-i", str(D/"o1.png"), "-i", str(D/"o2.png"), "-i", str(D/"o3.png"),
                    "-i", str(MUSIK), *inputs, "-filter_complex", fc, "-map", "[v]", "-map", "[aud]", "-t", str(total),
                    "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
                    "-movflags", "+faststart", str(D / OUT)], check=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "0.6", "-i", str(D / OUT), "-frames:v", "1", "-q:v", "2", str(D / "cover.jpg")], check=True)


if __name__ == "__main__":
    overlays(); build(); print("ok")
