"""Magazin-Cover im Flow-Look: S/W-Porträt, durch ein riesiges M versetzt (inspiriert von Buchcover-Typografie, eigene Umsetzung)."""
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps
import pathlib, subprocess
D = pathlib.Path(__file__).parent
W, H = 1080, 1350

def fit(im, scale=1.0, dx=0, dy=0):
    im = ImageOps.grayscale(im).convert("RGB")
    s = max(W / im.width, H / im.height) * scale
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    x = (im.width - W) // 2 - dx; y = int(im.height * 0.06) - dy
    return im.crop((x, y, x + W, y + H))

src = Image.open(D / "portrait.jpg")
base = ImageEnhance.Brightness(ImageEnhance.Contrast(fit(src, 1.0)).enhance(1.1)).enhance(0.62)
alt = ImageEnhance.Brightness(ImageEnhance.Contrast(fit(src, 1.08, dx=-45, dy=40)).enhance(1.15)).enhance(1.12)

# giant M: two legs + V, spanning most of the frame (from y=330 down to bottom)
top, bot = 360, H + 40
L, R, st = 120, W - 120, 210
mid = W // 2
poly_left = [(L, bot), (L, top), (L + st, top), (mid, top + 520), (mid, top + 760), (L + st, top + 240), (L + st, bot)]
poly_right = [(R, bot), (R, top), (R - st, top), (mid, top + 520), (mid, top + 760), (R - st, top + 240), (R - st, bot)]
mask = Image.new("L", (W, H), 0); d = ImageDraw.Draw(mask)
d.polygon(poly_left, fill=255); d.polygon(poly_right, fill=255)
out = Image.composite(alt, base, mask)
# thin light edge along the letter
edge = mask.filter(ImageFilter.FIND_EDGES).point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(3))
out = Image.composite(Image.new("RGB", (W, H), (235, 235, 235)), out, edge.point(lambda v: int(v * 0.35)))
# darken top for the title
grad = Image.linear_gradient("L").resize((W, H)).point(lambda v: 0 if v > 110 else int((110 - v) / 110 * 235))
out = Image.composite(Image.new("RGB", (W, H), (11, 11, 11)), out, grad)
bg2 = Image.linear_gradient("L").resize((W, H)).point(lambda v: 0 if v < 190 else int((v - 190) / 65 * 230))
out = Image.composite(Image.new("RGB", (W, H), (11, 11, 11)), out, bg2)
out.save(D / "bg.jpg", quality=95)

html = (D / "cover.html")
html.write_text("""<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Montserrat:wght@500;600&family=Inter:wght@500&display=swap" rel="stylesheet"><style>
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1350px;position:relative;background:#0B0B0B url(bg.jpg) 0 0/1080px 1350px;color:#fff;overflow:hidden}
.k{position:absolute;top:70px;left:0;right:0;text-align:center;font:600 30px Montserrat;letter-spacing:.42em;text-transform:uppercase;color:rgba(255,255,255,.9)}
h1{position:absolute;top:104px;left:0;right:0;text-align:center;font:700 250px/1 Oswald;letter-spacing:.02em;color:#2F5BFF}
.sub{position:absolute;left:0;right:0;bottom:92px;text-align:center;font:500 40px/1.3 Inter;text-shadow:0 2px 18px rgba(0,0,0,.8)}
.pub{position:absolute;left:0;right:0;bottom:44px;text-align:center}.pub img{height:30px}
</style></head><body><div class="k">Flow Media AI</div><h1>MAIK</h1>
<div class="sub">Ideen. KI. Umsetzung.</div><div class="pub"><img src="logo_flow.png"></div></body></html>""", encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium"); pg = b.new_page(viewport={"width": W, "height": H})
    pg.goto(html.resolve().as_uri()); pg.wait_for_timeout(1500); pg.screenshot(path=str(D / "cover.png")); b.close()
html.unlink()
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(D / "cover.png"), "-q:v", "2", str(D / "cover.jpg")], check=True)
print("ok")
