# R002 "Mein ganzes Firmen-Tool. An einem Tag gebaut." – renders the reel from the screens shot by shoot.js.
# usage: python3 render_reel.py <work-dir with shots/ and fonts/> <out.mp4> [avatar.mp4]
# Without an avatar video a placeholder circle is drawn and only music plays; with one, the avatar sits in the circle
# and its audio (Maik's voice) leads, music ducked underneath.
import os, subprocess, sys, glob
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WD, OUT = sys.argv[1], sys.argv[2]
AVATAR = sys.argv[3] if len(sys.argv) > 3 else None
MUSIC = '/home/user/the-tribe-bot/instagram_autopilot/music/motivating-mornings.mp3'  # Mixkit Free License
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

def headline(fr, lines, chip=None, t=1.0):
    """Big text above the card; pops in over the first frames of a scene."""
    a = min(1, t); off = int((1 - ease(a)) * 24)
    d = ImageDraw.Draw(fr, 'RGBA'); f = ImageFont.truetype(F_DISPLAY, 86); lh = 96
    top = 150 if chip else 190
    for i, l in enumerate(lines):
        tw = d.textlength(l, font=f); d.text(((W - tw) / 2, top + off + i * lh), l, font=f, fill=INK + (int(255 * a),))
    if chip:
        fc = ImageFont.truetype(F_SEMI, 42); cw = d.textlength(chip, font=fc); cy = top + off + len(lines) * lh + 18
        d.rounded_rectangle(((W - cw) / 2 - 30, cy, (W + cw) / 2 + 30, cy + 74), 37, fill=BLUE + (int(255 * a),))
        d.text(((W - cw) / 2, cy + 12), chip, font=fc, fill=(255, 255, 255, int(255 * a)))

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
        s = min(src.size); sx = (src.width - s) // 2; sy = max(0, (src.height - s) // 4)
        face = src.crop((sx, sy, sx + s, sy + s)).resize((d, d), Image.BILINEAR)
    else:
        face = Image.new('RGB', (d, d), BLUE); fd = ImageDraw.Draw(face); f = ImageFont.truetype(F_SEMI, max(26, d // 9))
        for k, l in enumerate(['Dein', 'Avatar']):
            tw = fd.textlength(l, font=f); fd.text(((d - tw) / 2, d / 2 - f.size * (1.1 - k * 1.2)), l, font=f, fill=(255, 255, 255))
    m = Image.new('L', (d, d), 0); ImageDraw.Draw(m).ellipse((0, 0, d, d), fill=255)
    fr.paste(face, (cx - r, cy - r), m)

# avatar positions: big in hook and outro, small bubble lower left during the demo
BIG, SMALL = (540, 1290, 470), (205, 1395, 290)
def av_pos(scene, t):
    if scene == 'hook': a = BIG if t < 0.8 else tuple(lerp(b, s, ease((t - 0.8) / 0.2)) for b, s in zip(BIG, SMALL))
    elif scene == 'outro': a = tuple(lerp(s, b, ease(min(1, t / 0.2))) for s, b in zip(SMALL, BIG))
    else: a = SMALL
    return a

FLICK = [('board', (0, 0, 1500)), ('cal', (60, 180, 1350)), ('fin', (0, 60, 1714)), ('invoice', (700, 180, 1500)), ('stats', (0, 60, 1500))]
DRAG = sorted(os.path.basename(p)[:-4] for p in glob.glob(f'{WD}/shots/drag_*.png'))
# scene: (name, seconds, view(t), headline lines, chip, tag) – timing follows the voice-over script in README.md
SCENES = [
    ('hook', 3.0, lambda t: crop_view(*FLICK[int(t * 3.0 / 0.3) % len(FLICK)], FLICK[int(t * 3.0 / 0.3) % len(FLICK)][1], 0),
     ['Mein komplettes', 'Firmen-Tool.'], 'An einem Tag gebaut. Mit KI.', None),
    ('board', 3.0, lambda t: crop_view('board', (0, 0, 1500), (1380, 0, 1500), t) if t < 0.7 else crop_view('matrix', (0, 0, 1700), (100, 0, 1600), (t - 0.7) / 0.3),
     ['Alle Aufgaben.', 'Nach Priorität.'], None, None),
    ('cal', 4.0, lambda t: crop_view('cal', (0, 150, 1500), (60, 180, 1350), t / 0.35) if t < 0.35 else
        (crop_view(DRAG[min(len(DRAG) - 1, int((t - 0.35) / 0.4 * len(DRAG)))], (60, 180, 1350), (60, 180, 1350), 0) if t < 0.75 else crop_view('cal_after', (60, 180, 1350), (60, 180, 1350), 0)),
     ['Termine ziehen', 'wie in Outlook.'], None, None),
    ('fin', 5.0, lambda t: crop_view('fin', (0, 60, 1714), (500, 60, 1300), t),
     ['Buchhaltung', 'gleich mit drin.'], None, 'Beispieldaten'),
    ('invoice', 2.5, lambda t: crop_view('invoice', (700, 180, 1500), (760, 560, 1100), t),
     ['Rechnung?', 'Ein Klick. PDF.'], None, 'Beispieldaten'),
    ('landing', 3.0, lambda t: tall_view('landing', 0, 2600, t),
     ['Meine neue', 'Landingpage.'], None, None),
    ('stats', 2.5, lambda t: crop_view('stats', (0, 60, 1500), (0, 60, 1300), t),
     ['Besucher live', 'im Board.'], None, None),
    ('grid', 2.0, grid_view, ['Ein Tool', 'statt fünf Apps.'], None, None),
    ('outro', 3.0, lambda t: grid_view(1) if t < 0.9 else crop_view(*FLICK[0], FLICK[0][1], 0),
     ['Schick das jemandem,', 'der Rechnungen', 'noch in Word schreibt.'], None, None),
]

total = sum(s[1] for s in SCENES)
raw = OUT + '.video.mp4'
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', raw], stdin=subprocess.PIPE)
i = 0
for name, dur, view, lines, chip, tag in SCENES:
    n = int(round(dur * FPS))
    for k in range(n):
        t = k / max(1, n - 1)
        fr = Image.new('RGB', (W, H), BG)
        card(fr, view(t), tag)
        headline(fr, lines, chip, k / 6)
        cx, cy, d = av_pos(name, t); avatar(fr, i, int(cx), int(cy), d)
        enc.stdin.write(fr.tobytes()); i += 1
enc.stdin.close(); enc.wait()

# audio: voice from the avatar video (if any) over ducked music; music alone otherwise
if AVATAR:
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', raw, '-i', AVATAR, '-ss', '11.5', '-i', MUSIC, '-filter_complex',
           f'[2:a]volume=0.12,afade=t=out:st={total - 1.2}:d=1.2[m];[1:a][m]amix=inputs=2:duration=first:normalize=0[a]',
           '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', str(total), OUT]
else:
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', raw, '-ss', '11.5', '-i', MUSIC, '-filter_complex',
           f'[1:a]volume=0.8,afade=t=in:d=0.3,afade=t=out:st={total - 1.2}:d=1.2[a]',
           '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', str(total), OUT]
subprocess.run(cmd, check=True); os.remove(raw)
print(OUT, f'{total:.1f}s', i, 'frames')
