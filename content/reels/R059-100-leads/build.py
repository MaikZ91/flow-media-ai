"""R059 · „Ich hab KI gesagt: Hol mir 1000 Leads.“ (~14 s)

Szene 1: Maiks Zug-Selfie (27.11.2026), Hook.
Szene 2: der echte Chat (nachgebaut, Wortlaut aus der Session vom 27.11.2026), Nachrichten erscheinen nacheinander.
Szene 3: das echte Ergebnis (100 neue Leads, Branchen-Verteilung aus dem Flow Board, keine Namen).
Szene 4: Pointe + CTA, wieder das Foto.
"""
import subprocess, pathlib
D = pathlib.Path(__file__).parent
MUSIK = D / "../../musik/frei/driving-ambition.mp3"
HEAD = """<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Montserrat:wght@500;600;700&family=Inter:wght@500;600&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1920px;position:relative;overflow:hidden;background:#0B0B0B;color:#fff;font-family:Inter,sans-serif}
.logo{position:absolute;left:76px;top:110px;height:44px}
.k{font:600 40px Montserrat;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.85)}
h1{font:700 116px/1.22 Oswald;text-transform:uppercase}h1 span{background:#2F5BFF;padding:0 .1em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.ph{position:absolute;left:0;right:0;bottom:0;height:1120px;background:url(zug.jpg) 55% 50%/auto 100% no-repeat;filter:grayscale(1) contrast(1.15) brightness(.95)}
.ph:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,#0B0B0B 0%,rgba(11,11,11,.7) 12%,rgba(11,11,11,0) 38%,rgba(11,11,11,0) 70%,rgba(11,11,11,.6) 100%)}
.c{position:absolute;left:76px;right:76px}
.rule{width:60px;height:3px;background:#fff;margin:34px 0}
.chat{position:absolute;left:76px;right:76px;top:400px;display:flex;flex-direction:column;gap:40px}
.m{max-width:84%;padding:36px 44px;font:500 54px/1.3 Inter;border-radius:30px}
.me{align-self:flex-end;background:#fff;color:#0B0B0B;border-bottom-right-radius:6px}
.ai{align-self:flex-start;background:#1A1A1A;border:1.5px solid #2A2A2A;border-bottom-left-radius:6px}
.who{font:600 28px Montserrat;letter-spacing:.16em;text-transform:uppercase;color:#9A9A9A;margin-bottom:12px}
.me .who{color:#6B6B66}
table{width:100%;border-collapse:collapse;margin-top:10px}td{font:500 40px Inter;padding:15px 0;border-bottom:1px solid #2A2A2A}td:last-child{text-align:right;font:700 46px Oswald}
.big{font:700 300px/.9 Oswald}
.small{font:500 34px/1.35 Inter;color:rgba(255,255,255,.8)}
</style></head><body>"""
LOGO = '<img class="logo" src="logo_flow.png">'

S1 = LOGO + """<div class="ph"></div><div class="c" style="top:220px"><div class="k">Für Gründer &amp; Selbstständige</div>
<h1 style="margin-top:22px">Ich hab KI gesagt:<br><span>Hol mir 1000 Leads.</span></h1></div>"""

MSGS = [
    ("me", "Maik", "Hol dir 1000 Leads."),
    ("ai", "Claude", "1000 auf einmal schreibst du nie an. Lass uns mit 30 pro Tag starten."),
    ("me", "Maik", "Dann hole 100 jetzt."),
    ("ai", "Claude", "Erledigt ✓ 100 neue Leads im Flow Board – jeder mit fertigem DM-Entwurf."),
]
def chat(n):
    b = "".join(f'<div class="m {w}"><div class="who">{who}</div>{t}</div>' for w, who, t in MSGS[:n])
    return LOGO + f'<div class="c" style="top:200px"><div class="k">Mein Chat · 27.11.</div></div><div class="chat">{b}</div>'

ROWS = [("Beauty &amp; Kosmetik", 23), ("Coaching", 21), ("Gesundheit &amp; Ernährung", 14), ("Fotografie", 13), ("Design &amp; Web", 9), ("Immobilien", 7), ("Weitere Branchen", 13)]
S3 = LOGO + f"""<div class="c" style="top:260px"><div class="k">Das Ergebnis</div>
<div class="big" style="margin-top:20px"><span style="color:#2F5BFF">100</span></div><h1 style="font-size:96px">neue Leads.</h1>
<div class="small" style="margin-top:24px">Aus öffentlichen Firmenprofilen. Ins CRM, mit DM-Entwurf je Branche.</div>
<table style="margin-top:40px">{''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in ROWS)}</table></div>"""

S4 = LOGO + """<div class="ph"></div><div class="c" style="top:220px"><div class="k">Aber:</div>
<h1 style="margin-top:22px">Die Nachricht<br>schreib ich<br><span>selbst.</span></h1>
<div class="small" style="margin-top:28px;font-size:40px">KI sucht. Ich rede mit Menschen.<br>Folge mir für konkrete KI-Schritte.</div></div>"""

SCENES = [("s1", S1, 3.4), ("c1", chat(1), 1.4), ("c2", chat(2), 2.0), ("c3", chat(3), 1.3), ("c4", chat(4), 2.4), ("s3", S3, 3.2), ("s4", S4, 3.6)]


def render():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium"); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for name, body, _ in SCENES:
            f = D / f"{name}.html"; f.write_text(HEAD + body + "</body></html>", encoding="utf-8")
            pg.goto(f.resolve().as_uri()); pg.wait_for_timeout(1200)
            pg.screenshot(path=str(D / f"{name}.png")); f.unlink()
        b.close()


def build():
    parts = []
    for i, (name, _, sec) in enumerate(SCENES):
        n = int(sec * 30); out = D / f"p{i}.mp4"
        z = "1+0.0006*on" if name in ("s1", "s4", "s3") else "1"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", str(D / f"{name}.png"), "-vf",
                        f"scale=2160:3840,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps=30,format=yuv420p",
                        "-frames:v", str(n), str(out)], check=True)
        parts.append(out)
    lst = D / "list.txt"; lst.write_text("".join(f"file '{p.name}'\n" for p in parts))
    total = sum(s[2] for s in SCENES)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", str(MUSIK),
                    "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p",
                    "-af", f"afade=t=in:d=0.1,afade=t=out:st={total-1}:d=1", "-c:a", "aac", "-b:a", "192k", "-t", str(total),
                    "-movflags", "+faststart", str(D / "R059.mp4")], check=True)
    subprocess.run(["cp", str(D / "c4.png"), str(D / "screenshot-chat.png")], check=True)
    subprocess.run(["cp", str(D / "s1.png"), str(D / "cover.png")], check=True)
    for p in parts: p.unlink()
    lst.unlink()
    for name, _, _ in SCENES: (D / f"{name}.png").unlink()


if __name__ == "__main__":
    render(); build(); print("ok")
