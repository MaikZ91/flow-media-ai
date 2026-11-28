"""R060-Spot · MAGI-2-Video als Werbespot für Gründer & Selbstständige (~18 s).
Story: lost mit KI → Werkzeug-Chaos → keiner zeigt den Weg → aus der Idee wird etwas Echtes → nicht allein → Flow Media AI / Community.
Bild: MAGI-2 (Higgsfield) aus einem Storyboard-Bild; Stimme: ElevenLabs „Chloe“ (Erzählerin, nicht Maik); Schluss: Maiks Büro-Foto.
"""
import subprocess, pathlib
D = pathlib.Path(__file__).parent
import os
SRC = D / "magi2_raw.mp4"; VO = D / os.environ.get("VO", "vo.mp3"); OUT = os.environ.get("OUT", "R060-spot.mp4")
FOTO = D / "../../personal/arbeitsplatz/arbeitsplatz-buero-blazer.png"
MUSIK = D / "../../musik/frei/driving-ambition.mp3"
# (src_start, src_end, out_len, kicker, headline, sub, pos)
SC = [
    (0.0, 2.5, float(os.environ.get("L1",2.6)), "Für Gründer &amp; Selbstständige", "Lost mit <span>KI?</span>", "", "top"),
    (2.5, 4.5, float(os.environ.get("L2",2.0)), "", "Jede Woche ein <span>neues Tool.</span>", "", "top"),
    (5.0, 7.5, float(os.environ.get("L3",2.8)), "", "Keiner zeigt dir <span>den Weg.</span>", "", "top"),
    (7.5, 10.3, float(os.environ.get("L4",2.8)), "", "Aus deiner Idee wird <span>etwas Echtes.</span>", "", "top"),
    (10.1, 12.7, float(os.environ.get("L5",2.4)), "", "Du musst es nicht <span>allein</span> rausfinden.", "", "bottom"),
    (13.0, 14.9, float(os.environ.get("L5b",1.0)), "", "", "", "none"),
]
END = (float(os.environ.get("L6",5.4)), "Hey, ich bin Maik 👋 · Flow Media AI", "Komm in die <span>Community.</span>",
       "Kostenlos in WhatsApp. Stammtisch hybrid – online, Münster &amp; Bielefeld. Link unten ↓")
HTML = """<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Montserrat:wght@700&family=Inter:wght@500;600&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent}body{width:1080px;height:1920px;position:relative;overflow:hidden;color:#fff;font-family:Inter,sans-serif}
.sh{position:absolute;inset:0;background:__GRAD__}
.c{position:absolute;left:70px;right:70px;__POS__}.k{font:700 44px Montserrat;letter-spacing:.01em;text-transform:uppercase;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.6)}
h1{margin-top:14px;font:700 __H1__px/1.18 Oswald;text-transform:uppercase;text-shadow:0 4px 24px rgba(0,0,0,.45)}h1 span{color:#fff;background:#2F5BFF;padding:0 .12em;border-radius:6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
p{margin-top:26px;font:600 46px/1.3 Inter;color:rgba(255,255,255,.95)}
.logo{position:absolute;left:70px;__LOGOPOS__;height:44px}.cred{position:absolute;right:70px;__CREDPOS__;font:500 24px Inter;color:rgba(255,255,255,.7)}
</style></head><body><div class="sh"></div><img class="logo" src="logo_flow.png"><div class="c">__K__<h1>__H__</h1>__P__</div>__CRED__</body></html>"""
GT = "linear-gradient(180deg,rgba(10,10,10,.85) 0%,rgba(10,10,10,.55) 14%,rgba(10,10,10,0) 30%)"
GB = "linear-gradient(180deg,rgba(10,10,10,.35) 0%,rgba(10,10,10,0) 25%,rgba(10,10,10,0) 42%,rgba(10,10,10,.88) 66%,#0A0A0A 100%)"


def overlays():
    from playwright.sync_api import sync_playwright
    items = [(k, h, p, pos, "", 116 if i else 150) for i, (_, _, _, k, h, p, pos) in enumerate(SC)]
    items.append((END[1], END[2], END[3], "bottom", '<div class="cred">Spot mit KI erstellt: MAGI-2 auf Higgsfield</div>', 140))
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium"); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for i, (k, h, p, pos, cred, size) in enumerate(items):
            top = pos == "top"
            html = (HTML.replace("__GRAD__", "none" if pos == "none" else (GT if top else GB)).replace("__POS__", "top:110px" if top else "bottom:290px")
                    .replace("__LOGOPOS__", "bottom:150px" if top else "top:110px").replace("__CREDPOS__", "top:118px")
                    .replace("__H1__", str(size)).replace("__K__", f'<div class="k">{k}</div>' if k else "")
                    .replace("<h1>__H__</h1>", f"<h1>{h}</h1>" if h else "").replace("__H__", h).replace("__P__", f"<p>{p}</p>" if p else "").replace("__CRED__", cred))
            f = D / f"o{i}.html"; f.write_text(html, encoding="utf-8")
            pg.goto(f.resolve().as_uri()); pg.wait_for_timeout(900)
            pg.screenshot(path=str(D / f"o{i}.png"), omit_background=True); f.unlink()
        b.close()


def build():
    n = len(SC); parts_v, parts_a = [], []
    fc = ""
    for i, (s, e, L, *_rest) in enumerate(SC):
        sp = (e - s) / L  # stretch to output length
        fc += (f"[0:v]trim={s}:{e},setpts=(PTS-STARTPTS)/{sp:.4f},fps=30,format=yuv420p[v{i}];"
               f"[v{i}][{3+i}:v]overlay=0:0:shortest=1[a{i}];"
               f"[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS,atempo={sp:.4f},volume=0.35[m{i}];")
        parts_v.append(f"[a{i}]"); parts_a.append(f"[m{i}]")
    L = END[0]; k = 3 + n
    fc += (f"[1:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,zoompan=z='1+0.0007*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(L*30)}:s=1080x1920:fps=30,format=yuv420p,trim=0:{L},setpts=PTS-STARTPTS[pe];"
           f"[pe][{k}:v]overlay=0:0:shortest=1[ae];"
           f"{''.join(parts_v)}[ae]concat=n={n+1}:v=1:a=0,format=yuv420p[v];"
           f"{''.join(parts_a)}concat=n={n}:v=0:a=1[mag];"
           f"[2:a]atrim=0:{L+0.5},asetpts=PTS-STARTPTS,afade=t=in:d=0.3,afade=t=out:st={L-0.8}:d=0.8,volume=0.8[mu];"
           f"[mag][mu]concat=n=2:v=0:a=1[bed];"
           f"[{k+1}:a]adelay=150|150,volume=1.5[vo];[bed][vo]amix=inputs=2:duration=first:normalize=0[a]")
    total = sum(x[2] for x in SC) + L
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", str(SRC), "-loop", "1", "-i", str(FOTO), "-i", str(MUSIK)]
    for i in range(n + 1): cmd += ["-loop", "1", "-i", str(D / f"o{i}.png")]
    cmd += ["-i", str(VO), "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-t", f"{total:.2f}",
            "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart", str(D / OUT)]
    subprocess.run(cmd, check=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "0.9", "-i", str(D / OUT), "-frames:v", "1", "-q:v", "3", str(D / "cover-spot.jpg")], check=True)
    for i in range(n + 1): (D / f"o{i}.png").unlink()


if __name__ == "__main__":
    overlays(); build(); print("ok")
