# R002 "Mein ganzes Firmen-Tool. An einem Tag gebaut." – renders the reel from the screens shot by shoot.js.
# usage: python3 render_reel.py <work-dir with shots/ and fonts/> <out.mp4> [avatar.mp4]
# Without an avatar video a placeholder circle is drawn and only music plays; with one, the avatar sits in the circle
# and its audio (Maik's voice) leads, music ducked underneath.
import os, subprocess, sys, glob
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WD, OUT = sys.argv[1], sys.argv[2]
AVATAR = sys.argv[3] if len(sys.argv) > 3 else None
MUSIC = '/home/user/the-tribe-bot/instagram_autopilot/music/motivating-mornings.mp3'  # Mixkit Free License
# B-roll: only clips under the Mixkit Stock Video Free License (company social media allowed); <work-dir>/broll/<id>.mp4
STOCK = {1808: 'close-up-shot-of-a-person-typing-on-a-laptop', 1746: 'a-person-typing-in-a-laptop-at-a-coffee-shop',
         4907: 'person-typing-on-a-computer-in-detail', 1781: 'typing-on-a-laptop-close-up', 4827: 'hands-of-a-man-typing-on-a-laptop'}
W, H, FPS = 1080, 1920, 30
BG, INK, MUTED, BLUE, LINE = (246, 246, 242), (18, 21, 18), (91, 98, 92), (47, 91, 255), (223, 225, 219)
F_DISPLAY = f'{WD}/fonts/bri800.woff'
F_SEMI = f'{WD}/fonts/plex600.woff'
CARD = (40, 470, 1000, 1050)  # x, y, w, h of the screen card

_img = {}
def shot(n):
    if n not in _img: _img[n] = Image.open(f'{WD}/shots/{n}.png').convert('RGB')
    return _img[n]
def ease(t): return t * t * (3 - 2 * t)
def lerp(a, b, t): return a + (b - a) * t

def crop_view(n, r0, r1, t):
    """Ken-Burns between two source rects (x, y, w); height follows the card aspect."""
    x, y, w = (lerp(a, b, ease(t)) for a, b in zip(r0, r1))
    h = w * CARD[3] / CARD[2]
    return shot(n).crop((int(x), int(y), int(x + w), int(y + h))).resize(CARD[2:], Image.BILINEAR)

def tall_view(n, y0, y1, t):
    """Scroll a tall phone screenshot (landing page) through the card."""
    im = shot(n); w = im.width; h = int(w * CARD[3] / CARD[2]); y = int(lerp(y0, y1, ease(t)))
    return im.crop((0, y, w, y + h)).resize(CARD[2:], Image.BILINEAR)

def grid_view(t):
    tiles = [('board', (0, 0, 1500)), ('cal', (60, 180, 1350)), ('fin', (0, 60, 1714)),
             ('invoice', (700, 180, 1500)), ('landing', None), ('stats', (0, 60, 1500))]
    g = 16; cw = (CARD[2] - 3 * g) // 2; ch = (CARD[3] - 4 * g) // 3
    canvas = Image.new('RGB', CARD[2:], BG)
    for i, (n, r) in enumerate(tiles):
        if r is None: im = shot(n); src = im.crop((0, 0, im.width, int(im.width * ch / cw)))
        else: x, y, w = r; src = shot(n).crop((x, y, x + w, int(y + w * ch / cw)))
        tile = src.resize((cw, ch), Image.BILINEAR)
        mask = Image.new('L', (cw, ch), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, cw, ch), 18, fill=255)
        s = 1 - 0.04 * (1 - ease(min(1, t * 3 - i * 0.25 if t * 3 - i * 0.25 > 0 else 0)))
        canvas.paste(tile, (g + (i % 2) * (cw + g), g + (i // 2) * (ch + g)), mask)
    return canvas

def card(fr, view, tag=None):
    x, y, w, h = CARD
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).rounded_rectangle((x, y + 18, x + w, y + h + 18), 34, fill=70)
    fr.paste((18, 21, 18), (0, 0), sh.filter(ImageFilter.GaussianBlur(26)))
    mask = Image.new('L', (w, h), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, w, h), 30, fill=255)
    fr.paste(view, (x, y), mask)
    d = ImageDraw.Draw(fr); d.rounded_rectangle((x, y, x + w, y + h), 30, outline=LINE, width=2)
    if tag:
        f = ImageFont.truetype(F_SEMI, 30); tw = d.textlength(tag, font=f)
        d.rounded_rectangle((x + w - tw - 64, y + 24, x + w - 24, y + 76), 26, fill=(255, 255, 255), outline=LINE, width=2)
        d.text((x + w - tw - 44, y + 32), tag, font=f, fill=MUTED)

def headline(fr, lines, chip=None, t=1.0, ink=INK):
    """Big text above the card; pops in over the first frames of a scene."""
    a = min(1, t); off = int((1 - ease(a)) * 24)
    d = ImageDraw.Draw(fr, 'RGBA'); f = ImageFont.truetype(F_DISPLAY, 86); lh = 96
    top = 150 if chip else 190
    for i, l in enumerate(lines):
        tw = d.textlength(l, font=f); d.text(((W - tw) / 2, top + off + i * lh), l, font=f, fill=ink + (int(255 * a),))
    if chip:
        fc = ImageFont.truetype(F_SEMI, 42); cw = d.textlength(chip, font=fc); cy = top + off + len(lines) * lh + 18
        d.rounded_rectangle(((W - cw) / 2 - 30, cy, (W + cw) / 2 + 30, cy + 74), 37, fill=BLUE + (int(255 * a),))
        d.text(((W - cw) / 2, cy + 12), chip, font=fc, fill=(255, 255, 255, int(255 * a)))

def stock_frames(cid, start, dur, cx):
    """Graded vertical cut of a stock clip: centre crop to 9:16, darker, cooler, vignette, light grain."""
    d = f'{WD}/broll_frames/{cid}_{start}_{cx}'
    if not glob.glob(f'{d}/*.png'):
        os.makedirs(d, exist_ok=True)
        vf = (f'crop=ih*9/16:ih:{cx}-ih*9/32:0,scale=1080:1920:flags=lanczos,eq=brightness=-0.09:contrast=1.18:saturation=0.72,'
              'colorbalance=bs=0.16:bm=0.06:bh=-0.04,vignette=PI/4.2,noise=alls=5:allf=t,fps=30')
        subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(start), '-t', str(dur + 0.2), '-i', f'{WD}/broll/{cid}.mp4', '-vf', vf, f'{d}/%04d.png'], check=True)
    return sorted(glob.glob(f'{d}/*.png'))

def stock_view(cid, start, dur, cx=960):
    """cx: horizontal centre of the 9:16 crop in the 1920-wide source (where the hands are)."""
    files = []
    def v(t):
        nonlocal files
        if not files: files = stock_frames(cid, start, dur, cx)
        return Image.open(files[min(len(files) - 1, int(t * dur * FPS))]).convert('RGB')
    return v

_stage = None
def stage():
    """Dark stage with a blue and a violet glow, like a product shot."""
    global _stage
    if _stage is None:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        img = np.zeros((H, W, 3), np.float32) + np.array([7, 9, 18], np.float32)
        for (cx, cy, rad, col) in [(260, 700, 900, (47, 91, 255)), (880, 1450, 850, (122, 60, 255))]:
            g = np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * (rad / 2.2) ** 2))[..., None]
            img += g * np.array(col, np.float32) * 0.55
        _stage = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    return _stage.copy()

def persp_coeffs(dst, src):
    """Coefficients for Image.transform(PERSPECTIVE) mapping output quad dst onto source rect corners src."""
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()

def tilt_view(n, t, swing=1):
    """The board as a floating screen in perspective, slow push-in and turn."""
    fr = stage(); im = shot(n); sw, sh = im.size
    e = ease(t); s = lerp(0.84, 1.0, e); cx, cy = W / 2, H * 0.56
    w, h = 1000 * s, 1000 * s * sh / sw; k = lerp(0.18, 0.10, e) * swing  # depth of the far edge
    quad = [(cx - w / 2, cy - h / 2 + h * k * (swing < 0)), (cx + w / 2, cy - h / 2 + h * k * (swing > 0)),
            (cx + w / 2, cy + h / 2 - h * k * (swing > 0)), (cx - w / 2, cy + h / 2 - h * k * (swing < 0))]
    glow = Image.new('L', (W, H), 0); ImageDraw.Draw(glow).polygon(quad, fill=150)
    fr.paste((70, 120, 255), (0, 0), glow.filter(ImageFilter.GaussianBlur(60)))
    warped = im.transform((W, H), Image.PERSPECTIVE, persp_coeffs(quad, [(0, 0), (sw, 0), (sw, sh), (0, sh)]), Image.BILINEAR)
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).polygon(quad, fill=255)
    fr.paste(warped, (0, 0), m)
    return fr

_av = None
def avatar_frame(i):
    global _av
    if not AVATAR: return None
    if _av is None:
        _av = f'{WD}/avatar_frames'; os.makedirs(_av, exist_ok=True)
        if not glob.glob(f'{_av}/*.png'):
            subprocess.run(['ffmpeg', '-v', 'error', '-i', AVATAR, '-vf', f'fps={FPS}', f'{_av}/%05d.png'], check=True)
    files = sorted(glob.glob(f'{_av}/*.png'))
    return Image.open(files[min(i, len(files) - 1)]).convert('RGB') if files else None

def avatar(fr, i, cx, cy, d):
    """Round face bubble with white ring; placeholder until the HeyGen video exists."""
    d = int(d); r = d // 2
    ring = ImageDraw.Draw(fr); ring.ellipse((cx - r - 10, cy - r - 10, cx + r + 10, cy + r + 10), fill=(255, 255, 255))
    src = avatar_frame(i)
    if src:
        x0, y0, x1, y1 = AV_CROP if src.size == (720, 1280) else ((src.width - min(src.size)) // 2, 0, (src.width + min(src.size)) // 2, min(src.size))
        face = src.crop((x0, y0, x1, y1)).resize((d, d), Image.LANCZOS)
    else:
        face = Image.new('RGB', (d, d), BLUE); fd = ImageDraw.Draw(face); f = ImageFont.truetype(F_SEMI, max(26, d // 9))
        for k, l in enumerate(['Dein', 'Avatar']):
            tw = fd.textlength(l, font=f); fd.text(((d - tw) / 2, d / 2 - f.size * (1.1 - k * 1.2)), l, font=f, fill=(255, 255, 255))
    m = Image.new('L', (d, d), 0); ImageDraw.Draw(m).ellipse((0, 0, d, d), fill=255)
    fr.paste(face, (cx - r, cy - r), m)

AV_CROP = (180, 440, 560, 820)  # face and shoulders in the 720x1280 HeyGen export
# avatar positions: big in hook, "Zukunft" and outro, small bubble lower left during the demo
BIG, SMALL = (540, 1290, 470), (205, 1395, 290)
def av_pos(scene, t):
    if scene == 'hook': a = BIG if t < 0.8 else tuple(lerp(b, s, ease((t - 0.8) / 0.2)) for b, s in zip(BIG, SMALL))
    elif scene in ('outro', 'talk'): a = tuple(lerp(s, b, ease(min(1, t / 0.2))) for s, b in zip(SMALL, BIG))
    else: a = SMALL
    return a

FLICK = [('board', (0, 0, 1500)), ('cal', (60, 180, 1350)), ('fin', (0, 60, 1714)), ('invoice', (700, 180, 1500)), ('stats', (0, 60, 1500))]
DRAG = sorted(os.path.basename(p)[:-4] for p in glob.glob(f'{WD}/shots/drag_*.png'))
# scene: (name, start s, view(t), headline lines, chip, tag); starts follow the word timestamps of Maik's edited
# voice track (avatar_edit.mp4, 39.67 s); each scene ends where the next starts
END = 39.67
SCENES = [
    ('hook', 0.00, lambda t: crop_view(*FLICK[int(t * 4.08 / 0.3) % len(FLICK)], FLICK[int(t * 4.08 / 0.3) % len(FLICK)][1], 0),
     ['Mein eigenes', 'Firmen-Tool.'], 'Heute gebaut. Mit KI.', None),
    ('broll', 4.08, stock_view(1808, 6.0, 1.82, 760), ['Ehrlich gesagt:'], None, None),
    ('broll', 5.90, lambda t: tilt_view('board_dark', t, 1), ['Ziemlich geil, was', 'heute möglich ist.'], None, None),
    ('board', 8.42, lambda t: crop_view('board', (0, 0, 1500), (900, 0, 1500), t), ['Mein eigenes', 'Dashboard.'], None, None),
    ('fin', 10.18, lambda t: crop_view('fin', (0, 60, 1714), (300, 60, 1450), t), ['Buchhaltung.'], None, 'Beispieldaten'),
    ('cal', 12.14, lambda t: crop_view('cal', (0, 150, 1500), (60, 180, 1350), t), ['Kalender.'], None, None),
    ('landing', 13.70, lambda t: tall_view('landing', 0, 1800, t), ['Landingpage', 'im Blick.'], None, None),
    ('stats', 15.64, lambda t: crop_view('stats', (0, 60, 1500), (0, 60, 1300), t), ['Tracken, was auf der', 'Website passiert.'], None, None),
    ('grid', 18.20, grid_view, ['Alles an', 'einem Ort.'], 'Auf mich zugeschnitten.', None),
    ('broll', 21.80, stock_view(1746, 3.0, 1.56, 800), ['Das Verrückte', 'daran:'], None, None),
    ('broll', 23.36, lambda t: tilt_view('cal_dark', t, -1), ['Nicht monatelang', 'entwickeln.'], None, None),
    ('broll', 26.00, stock_view(4827, 3.0, 1.24, 920), ['Keine Agentur.'], None, None),
    ('cal', 27.24, lambda t: crop_view(DRAG[min(len(DRAG) - 1, int(t / 0.8 * len(DRAG)))], (60, 180, 1350), (60, 180, 1350), 0) if t < 0.8 else crop_view('cal_after', (60, 180, 1350), (60, 180, 1350), 0),
     ['Idee genommen.'], None, None),
    ('invoice', 29.04, lambda t: crop_view('invoice', (700, 180, 1500), (760, 560, 1100), t), ['Mit KI', 'umgesetzt.'], None, 'Beispieldaten'),
    ('talk', 31.18, lambda t: tilt_view('fin_dark', t, 1), ['Das ist für mich', 'die Zukunft.'], None, None),
    ('broll', 33.18, stock_view(1781, 3.0, 1.48, 960), ['Nicht nur', 'KI benutzen.'], None, None),
    ('broll', 34.66, lambda t: tilt_view('board_dark', t, -1), ['Ideen in echte', 'Produkte verwandeln.'], None, None),
    ('outro', 38.20, lambda t: grid_view(1) if t < 0.85 else crop_view(*FLICK[0], FLICK[0][1], 0),
     ['Und das ist erst', 'der Anfang.'], None, None),
]

total = END
raw = OUT + '.video.mp4'
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', raw], stdin=subprocess.PIPE)
i = 0
for j, (name, start, view, lines, chip, tag) in enumerate(SCENES):
    stop = SCENES[j + 1][1] if j + 1 < len(SCENES) else END
    n = int(round(stop * FPS)) - int(round(start * FPS))
    for k in range(n):
        t = k / max(1, n - 1)
        if name in ('broll', 'talk'):
            fr = view(t)
            scrim = Image.new('L', (W, H), 0); ImageDraw.Draw(scrim).rectangle((0, 0, W, 520), fill=120)
            fr.paste((0, 0, 0), (0, 0), scrim.filter(ImageFilter.GaussianBlur(80)))
            headline(fr, lines, chip, k / 4, ink=(255, 255, 255))
        else:
            fr = Image.new('RGB', (W, H), BG)
            card(fr, view(t), tag)
            headline(fr, lines, chip, k / 6)
        cx, cy, d = av_pos(name, t); avatar(fr, i, int(cx), int(cy), d)
        enc.stdin.write(fr.tobytes()); i += 1
enc.stdin.close(); enc.wait()

# audio: voice from the avatar video (if any) over ducked music; music alone otherwise
if AVATAR:
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', raw, '-i', AVATAR, '-ss', '11.5', '-i', MUSIC, '-filter_complex',
           f'[1:a]loudnorm=I=-15:TP=-1.5[v];[2:a]volume=0.10,afade=t=out:st={total - 1.2}:d=1.2[m];[v][m]amix=inputs=2:duration=first:normalize=0[a]',
           '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', str(total), OUT]
else:
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', raw, '-ss', '11.5', '-i', MUSIC, '-filter_complex',
           f'[1:a]volume=0.8,afade=t=in:d=0.3,afade=t=out:st={total - 1.2}:d=1.2[a]',
           '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', str(total), OUT]
subprocess.run(cmd, check=True); os.remove(raw)
print(OUT, f'{total:.1f}s', i, 'frames')
