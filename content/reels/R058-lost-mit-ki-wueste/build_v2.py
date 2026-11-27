"""R058-v2 (Anzeigen-Test 27.11.): KI-Karte 1 s statt 2 s, Kommentar-Stichwort am Ende. Basis: R058-POV · „POV: Du gründest … und bist komplett lost mit KI.“ (~11,5 s)

Szene 1 (0–3,5 s): Wüste, ratlos (Original-Reel), POV-Text + Sprecherstimme (edge-tts de-DE-ConradNeural,
   Erzähler, spricht den Zuschauer an – keine KI-Stimme als Maik) über dem Original-Wüstenton.
Szene 2 (3,5–5,5 s): Higgsfield-Clip, die Karte leuchtet als KI auf (Aha), Wüstenton läuft weiter.
Szene 3/4 (5,5–11,5 s): Büro-Foto, „Hey, ich bin Maik“ + Tipp, dann „Wir lösen es gemeinsam“, Musik.
"""
import subprocess, pathlib
D = pathlib.Path(__file__).parent
WU = D / "../R041-wueste-ad/wueste_1080.mp4"
KI = D / "ki_karte_higgsfield.mp4"
FOTO = D / "../../personal/arbeitsplatz/arbeitsplatz-buero-blazer.png"
MUSIK = D / "../../musik/frei/driving-ambition.mp3"
STIMME = D / "hook_stimme.mp3"  # ElevenLabs „Chloe“ über Higgsfield, Erzählerin (nicht Maik)

TEXTS = [  # (Kicker, Headline, Untertitel, Position)
    ("Für Gründer & Selbstständige", "Du gründest &amp; bist <span>lost</span> mit KI?", "", "top"),
    ("Bis du merkst:", "KI ist nur ein <span>Werkzeug.</span>", "", "top"),
    ("Hey, ich bin Maik 👋", "Fang mit <span>einer</span> Aufgabe an.", "Mit der, die dich jede Woche Zeit kostet.", "bottom"),
    ("Dein KI-Sparringspartner", "Schreib <span>„KI“</span> in die Kommentare.", "Ich sag dir, womit du anfängst.", "bottom"),
]
HTML = """<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Montserrat:wght@700&family=Inter:wght@600&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent}body{width:1080px;height:1920px;position:relative;overflow:hidden;color:#fff;font-family:Inter,sans-serif}
.sh{position:absolute;inset:0;background:__GRAD__}
.c{position:absolute;left:70px;right:70px;__POS__}.k{font:700 46px Montserrat;letter-spacing:.01em;text-transform:uppercase;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.6)}
h1{margin-top:14px;font:700 __H1__px/1.18 Oswald;text-transform:uppercase}h1 span{color:#fff;background:#2F5BFF;padding:0 .12em;border-radius:6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}p{margin-top:28px;font:600 52px/1.3 Inter;color:rgba(255,255,255,.95)}
.logo{position:absolute;left:70px;__LOGOPOS__;height:44px}
</style></head><body><div class="sh"></div><img class="logo" src="logo_flow.png"><div class="c"><div class="k">__K__</div><h1>__H__</h1>__P__</div></body></html>"""
GRAD_TOP = "linear-gradient(180deg,rgba(10,10,10,1) 0%,rgba(10,10,10,.97) 5%,rgba(10,10,10,.6) 18%,rgba(10,10,10,0) 30%)"
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
                    .replace("__H1__", "112" if i <= 1 else ("118" if i == 3 else "140")).replace("__K__", k).replace("__H__", h).replace("__P__", f"<p>{p}</p>" if p else ""))
            f = D / f"pov{i}.html"; f.write_text(html, encoding="utf-8")
            pg.goto(f.resolve().as_uri()); pg.wait_for_timeout(900)
            pg.screenshot(path=str(D / f"pov{i}.png"), omit_background=True); f.unlink()
        b.close()


def build():
    fc = (
        "[0:v]trim=0.2:3.7,setpts=PTS-STARTPTS,fps=30,format=yuv420p[s1];"
        "[1:v]trim=2.6:3.6,setpts=PTS-STARTPTS,fps=30,format=yuv420p[s2];"
        "[2:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,"
        "zoompan=z='1+0.0008*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=180:s=1080x1920:fps=30,format=yuv420p,split[f1][f2];"
        "[f1]trim=0:3.2,setpts=PTS-STARTPTS[p1];[f2]trim=3.2:6.0,setpts=PTS-STARTPTS[p2];"
        "[s1][3:v]overlay=0:0:shortest=1[a1];[s2][4:v]overlay=0:0:shortest=1[a2];"
        "[p1][5:v]overlay=0:0:shortest=1[a3];[p2][6:v]overlay=0:0:shortest=1[a4];"
        "[a1][a2][a3][a4]concat=n=4:v=1:a=0,fps=30,format=yuv420p[v];"
        # Wüstenton 0–3,5 s (leiser unter der Stimme), Stimme ab 0,1 s, Musik setzt beim Aufleuchten der Karte ein
        "[0:a]atrim=0.2:3.7,asetpts=PTS-STARTPTS,volume=0.5,afade=t=out:st=3.3:d=0.2[wa];"
        "[8:a]adelay=150|150,volume=1.4[vo];"
        "[wa][vo]amix=inputs=2:duration=first:normalize=0[intro];"
        "[7:a]atrim=0:7.0,asetpts=PTS-STARTPTS,afade=t=in:d=0.08,afade=t=out:st=6.0:d=1.0[ma];"
        "[intro][ma]concat=n=2:v=0:a=1[a]"
    )
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(WU), "-i", str(KI), "-loop", "1", "-i", str(FOTO),
                    *sum([["-loop", "1", "-i", str(D / f"pov{i}.png")] for i in range(4)], []),
                    "-i", str(MUSIK), "-i", str(STIMME), "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
                    "-movflags", "+faststart", str(D / "R058-v2.mp4")], check=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "0.8", "-i", str(D / "R058-v2.mp4"), "-frames:v", "1", "-q:v", "3", str(D / "cover-v2.jpg")], check=True)
    for i in range(4): (D / f"pov{i}.png").unlink()


if __name__ == "__main__":
    overlays(); build(); print("ok")
