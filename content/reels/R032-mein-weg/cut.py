# R032 base edit: photos (Ken Burns), robot footage, AI spin video -> edit.mp4 (1080x1920, 30 fps, no audio)
# usage: python3 cut.py <srcdir> <workdir>
#   srcdir holds: w_8f2b...mp4 (robot arm), w_772b...mp4 (pull test close-up), w_2297...mp4 (force curve), spin.mov (AI video)
import subprocess, sys, os
import numpy as np
from PIL import Image

SRC, WORK = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(WORK, exist_ok=True)
FPS, W, H = 30, 1080, 1920
B = 0.4645                                   # beat of "Digital Clouds"
GRADE = "format=gray,curves=all='0/0.04 0.5/0.48 1/1',eq=contrast=1.12,unsharp=5:5:0.6,format=yuv420p"

# (name, kind, beats, params)
SEG = [
    ("a_robo_photo", "photo", 8, dict(img="img/maik_roboter_ki.jpg", z0=1.0, z1=1.15, cx=0.62, cy=0.45)),
    ("b_arm",        "video", 8, dict(src="w_8f2b5d9c6b914d0d865917d1a6e3c17b.mp4", ss=9.0, crop=(506, 900, 737, 100), extra="eq=contrast=1.3:brightness=-0.07,")),
    ("c_pull",       "video", 4, dict(src="w_772be53dec504fd7920a7fa89d4fa60c.mp4", ss=18.0, crop=(608, 1080, 560, 0))),
    ("d_curve",      "video", 4, dict(src="w_2297ff977a9d426bb597b156b88d0d1c.mp4", ss=20.6, crop=(608, 1080, 420, 0), deflicker=True)),
    ("e_ar2017",     "photo", 4, dict(img="img/maik_hololens_ar_2017.jpg", z0=1.0, z1=1.08, cx=0.80, cy=0.45)),
    ("f_arki",       "photo", 4, dict(img="img/maik_hololens_ki.jpg", z0=1.12, z1=1.0, cx=0.55, cy=0.45)),
    ("g_spin",       "spin", 14, dict(src="spin.mov")),
    ("h_cta",        "still", 8, dict()),
]

def ff(args): subprocess.run(["ffmpeg", "-v", "error", "-y"] + args, check=True)

def pipe_frames(out, frames_iter, grade=True):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-vf", GRADE if grade else "format=yuv420p",
                          "-c:v", "libx264", "-crf", "16", "-preset", "fast", out], stdin=subprocess.PIPE)
    for fr in frames_iter: p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()

def ken_burns(img, n, z0, z1, cx, cy):
    im = Image.open(os.path.join(HERE, img)).convert("RGB")
    s = max(W / im.width, H / im.height)
    for i in range(n):
        t = i / max(1, n - 1); t = t * t * (3 - 2 * t)
        z = s * (z0 + (z1 - z0) * t)
        cw, ch = W / z, H / z
        x = min(max(cx * im.width - cw / 2, 0), im.width - cw)
        y = min(max(cy * im.height - ch / 2, 0), im.height - ch)
        yield np.asarray(im.resize((W, H), Image.LANCZOS, box=(x, y, x + cw, y + ch)))

def spin_frames(src, n):
    """AI video: grayscale, purple glow -> Flow blue #2F5BFF; time-compressed to n frames."""
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", src, "-vf", f"scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         stdout=subprocess.PIPE)
    raw = p.stdout.read(); p.wait()
    fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
    idx = np.linspace(0, len(fr) - 1, n).round().astype(int)
    blue = np.array([47, 91, 255], np.float32)
    for i in idx:
        f = fr[i].astype(np.float32)
        r, g, b = f[..., 0], f[..., 1], f[..., 2]
        gray = 0.299 * r + 0.587 * g + 0.114 * b
        gray = np.clip((gray - 10) * 1.1, 0, 255)
        s = np.clip((np.minimum(r, b) - g - 10) / 60, 0, 1)[..., None]   # violet/purple only (skin has b < g)
        tint = np.clip(blue * (0.25 + 1.1 * gray[..., None] / 255), 0, 255)
        tint = np.maximum(tint, gray[..., None] * (gray[..., None] > 225))   # keep hot whites white
        out = gray[..., None] * (1 - s) + tint * s
        yield out.clip(0, 255).astype(np.uint8)

parts = []
for name, kind, beats, p in SEG:
    out = os.path.join(WORK, name + ".mp4"); dur = beats * B; n = round(dur * FPS)
    if kind == "photo":
        pipe_frames(out, ken_burns(p["img"], n, p["z0"], p["z1"], p["cx"], p["cy"]))
    elif kind == "video":
        w, h, x, y = p["crop"]
        ff(["-ss", str(p["ss"]), "-i", os.path.join(SRC, p["src"]), "-frames:v", str(n),
            "-vf", f"fps={FPS},crop={w}:{h}:{x}:{y},scale={W}:{H}:flags=lanczos,{p.get('extra', '')}{GRADE}",
            "-an", "-c:v", "libx264", "-crf", "16", "-preset", "fast", out])
        if p.get("deflicker"):   # monitor flicker: blank plot frames -> hold last good frame
            tmp = out + ".tmp.mp4"; os.replace(out, tmp)
            r = subprocess.run(["ffmpeg", "-v", "error", "-i", tmp, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
            fr = np.frombuffer(r, np.uint8).reshape(-1, H, W, 3)
            def held():
                last = None
                for f in fr:
                    dark = (f[500:1200, 100:1000, 0] < 80).mean()   # share of curve pixels in the plot band
                    if dark > 0.03 or last is None: last = f
                    yield last
            pipe_frames(out, held(), grade=False); os.remove(tmp)
    elif kind == "spin":
        pipe_frames(out, spin_frames(os.path.join(SRC, p["src"]), n), grade=False)
    else:   # CTA background: last spin frame, darkened and blurred
        last = os.path.join(WORK, "g_spin.mp4")
        ff(["-sseof", "-0.1", "-i", last, "-frames:v", "1", os.path.join(WORK, "last.png")])
        ff(["-loop", "1", "-i", os.path.join(WORK, "last.png"), "-frames:v", str(n), "-r", str(FPS),
            "-vf", "gblur=sigma=40,eq=brightness=-0.42,format=yuv420p", "-c:v", "libx264", "-crf", "16", out])
    parts.append(out)

with open(os.path.join(WORK, "list.txt"), "w") as fh:
    fh.writelines(f"file '{x}'\n" for x in parts)
ff(["-f", "concat", "-safe", "0", "-i", os.path.join(WORK, "list.txt"), "-c", "copy", os.path.join(WORK, "edit.mp4")])
print("total", sum(s[2] for s in SEG) * B)
