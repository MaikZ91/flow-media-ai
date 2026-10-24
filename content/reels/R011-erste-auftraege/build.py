# Builds R011 from Maik's raw selfie video: long takes with cuts only in real pauses, b/w grade,
# word captions (ASS), voice cleanup + ducked music bed.
# usage: python3 build.py <raw.mov> <words.json>
import json, subprocess, sys, os
import numpy as np
RAW, WORDS = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
MUSIC = os.path.join(HERE, "../../musik/frei/uplifting-bass.mp3")

# (src_start, src_end, zoom) – story order, the hook is pulled to the front.
# Long continuous takes; only pauses and slips are cut. Boundaries are snapped into the quietest spot nearby.
SEG = [
    (33.45, 37.75, 1.10),   # habe ich jetzt auch schon die ersten Aufträge. Also, bevor überhaupt das Coaching angefangen hat
    (11.95, 13.18, 1.00),   # ich habe gerade
    (15.34, 17.95, 1.00),   # ab dem 2. November ein Business-Coaching
    (28.15, 33.30, 1.10),   # und jetzt irgendwie, seitdem ich mit so vielen Leuten drüber geredet habe
    (38.25, 44.45, 1.00),   # das finde ich schon ziemlich geil, ziemlich überraschend, hätte ich nie gedacht
    (45.38, 46.72, 1.10),   # weil eigentlich die ganze Zeit
    (47.80, 49.50, 1.00),   # schwierig war, an Kunden zu kommen
    (54.40, 54.92, 1.10),   # an euch,
    (57.68, 59.40, 1.10),   # (die) sich selbstständig machen wollen
    (60.15, 68.55, 1.10),   # tragt eure Message da draußen ... und dann läuft es irgendwie.
    (79.20, 83.68, 1.00),   # man sieht sich vielleicht am Montag im Workshop
    (84.45, 89.35, 1.00),   # da machen wir nämlich mit KI, bauen wir deine Personal Brand auf.
    (90.10, 92.10, 1.10),   # Ich freue mich auf euch. Ciao!
]
CTA_FROM = 10               # index of the first take that gets the workshop card
FIX_AT = {84.52: "da", 65.40: "einen"}   # whisper slips inside the used takes (by word start time)
BLUE = {"aufträge", "coaching", "november", "kunden", "message", "skill", "läuft", "workshop", "ki", "personal", "brand", "geil", "montag"}

pcm = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", RAW, "-ac", "1", "-ar", "8000", "-f", "s16le", "-"],
                                   capture_output=True).stdout, np.int16).astype(float)
def quiet(t, lo, hi):
    best, bt = 1e18, t
    for c in np.arange(t + lo, t + hi + 1e-9, .01):
        i = int(c * 8000); e = float(np.mean(pcm[max(0, i - 80):i + 80] ** 2))
        if e < best: best, bt = e, c
    return round(float(bt), 3)
SEG = [(quiet(a, -.15, .02), quiet(b, -.02, .12), z) for a, b, z in SEG]   # never move into a word

words = [w for s in json.load(open(WORDS)) for w in s["w"]]
# map source words into the output timeline
cap, t0 = [], 0.0
for k, (a, b, z) in enumerate(SEG):
    n0 = len(cap)
    for ws, we, w in words:
        if ws >= a - .02 and we <= b + .05:
            w = FIX_AT.get(round(ws, 2), w.strip())
            cap.append((t0 + max(0, ws - a), t0 + min(b, we) - a, w))
    if k == 8: cap.insert(n0, (t0, t0 + .1, "die"))   # caption only: "an euch, die sich selbstständig machen wollen"
    t0 += b - a
TOTAL = t0
# group into caption chunks of up to 3 words, break on punctuation
chunks, cur = [], []
for c in cap:
    cur.append(c)
    if len(cur) == 3 or c[2][-1] in ".,!?":
        chunks.append(cur); cur = []
if cur: chunks.append(cur)

def ts(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"
def word(w):
    txt = w.upper()
    return ("{\\c&HFF5B2F&}" + txt + "{\\c&HFFFFFF&}") if w.strip(".,!?").lower() in BLUE else txt

ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "",
       "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Cap,Oswald,108,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,3,4,2,70,70,400,1",
       "Style: Kick,Montserrat Medium,30,&H00E6E6E6,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,6,0,1,0,3,7,76,76,150,1",
       "Style: Big,Oswald,96,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,0,6,7,76,76,250,1",
       "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for i, ch in enumerate(chunks):
    st = ch[0][0]; en = chunks[i + 1][0][0] if i + 1 < len(chunks) else TOTAL
    en = min(en, ch[-1][1] + .6)
    parts = []                                        # pop-in, each word appears on its own start time
    for ws, we, w in ch:
        d = int((ws - st) * 1000)
        parts.append("{\\alpha&HFF&\\t(%d,%d,\\alpha&H00&)}" % (d, d + 60) + word(w))
    ass.append(f"Dialogue: 1,{ts(st)},{ts(en)},Cap,,0,0,0,,{{\\fscx92\\fscy92\\t(0,90,\\fscx100\\fscy100)}}" + " ".join(parts))
# hook + workshop card
ass.append(f"Dialogue: 2,{ts(0)},{ts(3.9)},Kick,,0,0,0,,{{\\fad(0,200)}}BUILD IN PUBLIC · FLOW MEDIA AI")
ass.append(f"Dialogue: 2,{ts(0)},{ts(3.9)},Big,,0,0,0,,{{\\fad(0,200)}}ERSTE AUFTRÄGE –\\NVOR DEM ERSTEN\\N{{\\c&HFF5B2F&}}COACHING-TAG.")
cta = sum(b - a for a, b, z in SEG[:CTA_FROM])
ass.append(f"Dialogue: 2,{ts(cta)},{ts(TOTAL)},Kick,,0,0,0,,{{\\fad(200,0)}}DIGITALER STAMMTISCH #1 · MO 26.10. · 18 UHR")
ass.append(f"Dialogue: 2,{ts(cta + .25)},{ts(TOTAL)},Big,,0,0,0,,{{\\fad(200,0)}}MIT KI ZUR\\N{{\\c&HFF5B2F&}}PERSONAL BRAND.{{\\c&HFFFFFF&}}\\N{{\\fnInter\\fs40\\b0\\bord0\\shad2}}15 € · live · Link in Bio")
open(os.path.join(HERE, "captions.ass"), "w").write("\n".join(ass) + "\n")

# 1) cut every take with picture and sound together (keeps A/V in sync); short audio fades sit inside the pauses
tm = "zscale=t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p"
tmp = os.path.join(HERE, "_clips"); os.makedirs(tmp, exist_ok=True)
lst = []
for i, (a, b, z) in enumerate(SEG):
    d = b - a; out = os.path.join(tmp, f"c{i:02d}.mov"); lst.append(f"file '{out}'")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-i", RAW, "-t", f"{d:.3f}",
        "-vf", f"{tm},fps=30,crop=iw/{z}:ih/{z}:(iw-iw/{z})/2:(ih-ih/{z})*0.3,scale=1080:1920:flags=lanczos,setsar=1",
        "-af", f"aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.04,afade=t=out:st={d - 0.05:.3f}:d=0.05,apad,atrim=0:{d:.3f}",
        "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-c:a", "pcm_s16le", out], check=True)
open(os.path.join(tmp, "list.txt"), "w").write("\n".join(lst) + "\n")
cut = os.path.join(tmp, "cut.mov")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "list.txt"), "-c", "copy", cut], check=True)

# 2) grade, captions, logo; voice cleanup + music bed ducked under the voice
fc = ["[0:v]hue=s=0,eq=gamma=1.3:contrast=1.25:brightness=-0.03,unsharp=5:5:0.8,noise=alls=3:allf=t[vg];[3:v]format=rgba[sh];[vg][sh]overlay=0:0,"
      f"ass={os.path.join(HERE, 'captions.ass')}:fontsdir={os.path.join(HERE, 'fonts')}[vs]",
      "[1:v]scale=170:-1,format=rgba,colorchannelmixer=aa=0.9[lg];[vs][lg]overlay=W-w-70:150[vout]",
      "[0:a]highpass=f=85,afftdn=nf=-28,equalizer=f=200:t=q:w=1:g=-2,equalizer=f=3200:t=q:w=1.2:g=2.5,"
      f"acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=4,loudnorm=I=-15:TP=-1.5:LRA=7,aresample=48000,apad=whole_dur={TOTAL:.3f}[vo]",
      f"[2:a]atrim=start=0.5:duration={TOTAL + .5},asetpts=PTS-STARTPTS,aresample=48000,volume=0.16,"
      f"afade=t=in:d=0.6,afade=t=out:st={TOTAL - 1.6:.2f}:d=1.6[mu]",
      "[vo]asplit[vo1][vo2];[mu][vo2]sidechaincompress=threshold=0.04:ratio=6:attack=15:release=300[mud];"
      "[vo1][mud]amix=inputs=2:normalize=0:duration=longest,alimiter=limit=0.9[aout]"]
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", cut, "-i", os.path.join(HERE, "logo_flow.png"), "-i", MUSIC, "-i", os.path.join(HERE, "shade.png"),
    "-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]", "-t", f"{TOTAL:.3f}",
    "-c:v", "libx264", "-crf", "23", "-preset", "slow", "-maxrate", "9M", "-bufsize", "18M", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", os.path.join(HERE, "R011.mp4")], check=True)
print("total", round(TOTAL, 2), "chunks", len(chunks), "segments", SEG)
