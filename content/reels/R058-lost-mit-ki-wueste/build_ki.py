"""R058-KI (Variante mit Higgsfield-Clip in Szene 1)

R058 · „Gründer und lost mit KI?“ – Wüsten-Einstieg (aus dem Wüsten-Reel), dann Tipp am Arbeitsplatz. ~10 s.

Gelernt aus dem Wüsten-Reel (961 Views, 44,5 % übersprungen, Ø 5,4 s): Der Einstieg hält, die Pointe nach 20 s sieht
kaum jemand. Darum: Thema KI + Gründer in Sekunde 0, Tipp in Sekunde 4, Bertrand raus, eine durchgehende Musik.
"""
import subprocess, pathlib
D = pathlib.Path(__file__).parent
WU = D / "../R041-wueste-ad/wueste_1080.mp4"
KI = D / "ki_karte_higgsfield.mp4"  # Higgsfield Seedance 2.5, Startbild aus dem Wüsten-Reel, 4 s
FOTO = D / "../../personal/arbeitsplatz/arbeitsplatz-buero-blazer.png"
MUSIK = D / "../../musik/frei/driving-ambition.mp3"

# (Szene, Kicker, Headline, Untertitel, Position)
TEXTS = [
    ("Für Gründer & Selbstständige", "Lost mit <span>KI?</span>", "", "top"),
    ("Mein Tipp", "Fang mit <span>einer</span> Aufgabe an.", "Mit der, die dich jede Woche Zeit kostet.", "bottom"),
    ("Flow Media AI", "Wir lösen es <span>gemeinsam.</span>", "Folge mir für konkrete KI-Schritte.", "bottom"),
]
HTML = """<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Montserrat:wght@600&family=Inter:wght@500&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent}body{width:1080px;height:1920px;position:relative;overflow:hidden;color:#fff;font-family:Inter,sans-serif}
.sh{position:absolute;inset:0;background:__GRAD__}
.c{position:absolute;left:70px;right:70px;__POS__}.k{font:600 40px Montserrat;letter-spacing:.18em;text-transform:uppercase;color:#2F5BFF}
h1{margin-top:18px;font:700 150px/.95 Oswald;text-transform:uppercase}h1 span{color:#2F5BFF}p{margin-top:28px;font:500 46px/1.3 Inter;color:rgba(255,255,255,.92)}
.logo{position:absolute;left:70px;__LOGOPOS__;height:44px}
</style></head><body><div class="sh"></div><img class="logo" src="logo_flow.png"><div class="c"><div class="k">__K__</div><h1>__H__</h1>__P__</div></body></html>"""
GRAD_TOP = "linear-gradient(180deg,rgba(10,10,10,1) 0%,rgba(10,10,10,.97) 5%,rgba(10,10,10,.6) 16%,rgba(10,10,10,0) 26%)"
GRAD_BOT = "linear-gradient(180deg,rgba(10,10,10,.35) 0%,rgba(10,10,10,0) 25%,rgba(10,10,10,0) 45%,rgba(10,10,10,.85) 68%,#0A0A0A 100%)"


def overlays():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for i, (k, h, p, pos) in enumerate(TEXTS):
            top = pos == "top"
            html = (HTML.replace("__GRAD__", GRAD_TOP if top else GRAD_BOT)
                    .replace("__POS__", "top:95px" if top else "bottom:300px")
                    .replace("__LOGOPOS__", "bottom:150px" if top else "top:110px")
                    .replace("__K__", k).replace("__H__", h).replace("__P__", f"<p>{p}</p>" if p else ""))
            f = D / f"ov{i}.html"; f.write_text(html, encoding="utf-8")
            pg.goto(f.resolve().as_uri()); pg.wait_for_timeout(900)
            pg.screenshot(path=str(D / f"ov{i}.png"), omit_background=True); f.unlink()
        b.close()


def run(*a): subprocess.run(a, check=True)


def build():
    fc = (
        "[0:v]trim=0:4.0,setpts=PTS-STARTPTS,fps=30,format=yuv420p[w1];"
        "[1:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,"
        "zoompan=z='1+0.0008*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=180:s=1080x1920:fps=30,format=yuv420p[f];"
        "[f]split[f1][f2];[f1]trim=0:3.2,setpts=PTS-STARTPTS[p1];[f2]trim=3.2:6.0,setpts=PTS-STARTPTS[p2];"
        "[w1][2:v]overlay=0:0:shortest=1[a1];[p1][3:v]overlay=0:0:shortest=1[a3];[p2][4:v]overlay=0:0:shortest=1[a4];"
        "[a1][a3][a4]concat=n=3:v=1:a=0,fps=30,format=yuv420p[v];"
        "[6:a]atrim=0:4.0,asetpts=PTS-STARTPTS,afade=t=out:st=3.4:d=0.6[wa];"
        "[5:a]atrim=0:6.0,asetpts=PTS-STARTPTS,afade=t=in:d=0.3,afade=t=out:st=5.0:d=1.0[ma];"
        "[wa][ma]concat=n=2:v=0:a=1[a]"
    )
    run("ffmpeg", "-y", "-v", "error", "-i", str(KI), "-loop", "1", "-i", str(FOTO),
        *sum([["-loop", "1", "-i", str(D / f"ov{i}.png")] for i in range(3)], []),
        "-i", str(MUSIK), "-i", str(WU), "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-t", "10",
        "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart", str(D / "R058-ki.mp4"))
    run("ffmpeg", "-y", "-v", "error", "-ss", "0.6", "-i", str(D / "R058-ki.mp4"), "-frames:v", "1", "-q:v", "3", str(D / "cover-ki.jpg"))
    for i in range(3): (D / f"ov{i}.png").unlink()


if __name__ == "__main__":
    overlays(); build(); print("ok")
