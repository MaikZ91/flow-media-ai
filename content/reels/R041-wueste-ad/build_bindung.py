"""Wüsten-Reel mit eingeblendeter Zuschauerbindung (geschätzt).

Daten (Instagram-Insights, Stand 27.11.2026): 961 Views, 44,5 % übersprungen, Ø 5,4 s Wiedergabe bei 30 s Länge.
Instagram gibt die sekundengenaue Kurve nicht über die Schnittstelle heraus. Darum geschätzt:
0–3 s linear von 100 % auf 55,5 % (die übrigen 44,5 % wischen weg), danach exponentiell so, dass der
Durchschnitt genau 5,4 s ergibt. Im Video als „Schätzung“ gekennzeichnet.
"""
import math, subprocess, pathlib
from PIL import Image, ImageDraw, ImageFont

D = pathlib.Path(__file__).parent
SRC = D / "wueste_1080.mp4"
OUT = D / "wueste_bindung.mp4"
VIEWS, DUR, KEEP3 = 961, 30.0, 0.555


def solve_k():
    mean = lambda k: 3 * (1 + KEEP3) / 2 + KEEP3 / k * (1 - math.exp(-(DUR - 3) * k))
    lo, hi = 0.01, 2.0
    for _ in range(60):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if mean(m) > 5.4 else (lo, m)
    return (lo + hi) / 2


K = solve_k()
S = lambda t: 1 - (1 - KEEP3) / 3 * t if t < 3 else KEEP3 * math.exp(-K * (t - 3))

# Panel geometry (1080×1920 canvas)
PX, PY, PW, PH = 20, 18, 1040, 470
CX0, CX1, CY0, CY1 = PX + 80, PX + PW - 40, PY + 130, PY + PH - 95
F = "/usr/share/fonts/opentype/inter/"
bold, semi, reg = (ImageFont.truetype(F + n, s) for n, s in (("Inter-Bold.otf", 40), ("Inter-SemiBold.otf", 26), ("Inter-Regular.otf", 22)))


def panel():
    im = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((PX, PY, PX + PW, PY + PH), 28, fill=(10, 10, 10, 205))
    d.text((PX + 34, PY + 26), "Wie viele schauen noch?", font=semi, fill=(255, 255, 255, 230))
    for p in (0, 25, 50, 75, 100):
        y = CY1 - (CY1 - CY0) * p / 100
        d.line((CX0, y, CX1, y), fill=(255, 255, 255, 40), width=1)
        d.text((CX0 - 12, y), f"{p}%", font=reg, fill=(255, 255, 255, 150), anchor="rm")
    pts = [(CX0 + (CX1 - CX0) * t / DUR, CY1 - (CY1 - CY0) * S(t)) for t in [i / 10 for i in range(int(DUR * 10) + 1)]]
    d.polygon(pts + [(CX1, CY1), (CX0, CY1)], fill=(47, 91, 255, 70))
    d.line(pts, fill=(47, 91, 255, 255), width=5, joint="curve")
    for s in (0, 10, 20, 30):
        x = CX0 + (CX1 - CX0) * s / DUR
        d.text((x, CY1 + 14), f"{s} s", font=reg, fill=(255, 255, 255, 150), anchor="mt")
    d.text((PX + PW - 34, PY + PH - 16), "Schätzung aus 961 Views · 44,5 % wischen sofort · Ø 5,4 s", font=reg, fill=(255, 255, 255, 140), anchor="rb")
    im.save(D / "bindung_panel.png")


def esc(s):
    return s.replace(":", r"\:").replace("%", r"\%").replace(",", r"\,")


def build():
    panel()
    pct = f"if(lt(t\\,3)\\,100-{(1 - KEEP3) / 3 * 100:.4f}*t\\,{KEEP3 * 100}*exp(-{K:.6f}*(t-3)))"
    x = f"{CX0}+({CX1 - CX0})*t/{DUR}"
    y = f"{CY1}-({CY1 - CY0})*({pct})/100"
    bar = Image.new("RGBA", (6, CY1 - CY0), (255, 255, 255, 230)); bar.save(D / "bindung_bar.png")
    vf = (
        f"[0:v][1:v]overlay=0:0[b];[b][2:v]overlay=x='{x}-3':y={CY0}[c];"
        f"[c]drawtext=fontfile={F}Inter-Bold.otf:fontsize=60:fontcolor=white:x={PX + PW - 34 - 58}-tw:y={PY + 20}:"
        f"text='%{{eif\\:{pct}\\:d}}',"
        f"drawtext=fontfile={F}Inter-Bold.otf:fontsize=60:fontcolor=white:x={PX + PW - 34}-tw:y={PY + 20}:expansion=none:text='%',"
        f"drawtext=fontfile={F}Inter-Regular.otf:fontsize=24:fontcolor=white@0.8:x={PX + PW - 34}-tw:y={PY + 88}:"
        f"text='≈ %{{eif\\:{VIEWS}*({pct})/100\\:d}} von {VIEWS} noch dabei'"
    )
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(SRC), "-loop", "1", "-i", str(D / "bindung_panel.png"), "-loop", "1", "-i", str(D / "bindung_bar.png"),
                    "-filter_complex", vf, "-t", str(DUR), "-c:v", "libx264", "-crf", "19", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", str(OUT)], check=True)


if __name__ == "__main__":
    build()
    print("k =", round(K, 4), "· am Ende noch", round(S(DUR) * VIEWS), "von", VIEWS)
