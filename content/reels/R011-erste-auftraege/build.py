# Builds R011 from Maik's raw selfie video: jump cuts, punch-in zooms, b/w grade, word captions (ASS), voice cleanup + music bed.
# usage: python3 build.py <raw.mov> <words.json>
import json, subprocess, sys, os
RAW, WORDS = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
MUSIC = os.path.join(HERE, "../../musik/frei/uplifting-bass.mp3")

# (src_start, src_end, zoom) – order = story order; the hook is pulled to the front
SEG = [
    (33.50, 35.10, 1.18),   # habe ich jetzt auch schon die ersten Aufträge.
    (35.42, 37.66, 1.00),   # bevor überhaupt das Coaching angefangen hat
    (11.98, 13.16, 1.12),   # ich habe gerade
    (15.36, 17.92, 1.12),   # ab dem 2. November ein Business-Coaching
    (29.50, 33.26, 1.00),   # seitdem ich mit so vielen Leuten drüber geredet habe
    (38.70, 41.16, 1.22),   # das finde ich schon ziemlich, ziemlich geil
    (43.48, 44.40, 1.00),   # hätte ich jetzt nie gedacht
    (45.40, 46.70, 1.10),   # weil eigentlich die ganze Zeit
    (47.84, 49.46, 1.10),   # schwierig war, an Kunden zu kommen
    (54.40, 54.90, 1.00),   # an euch,
    (57.70, 59.34, 1.00),   # die sich selbstständig machen wollen
    (60.20, 64.46, 1.16),   # tragt eure Message da draußen, was ihr anzubieten habt
    (64.70, 66.40, 1.16),   # wo ihr einen Skill habt
    (66.37, 68.52, 1.00),   # und dann läuft es irgendwie.
    (79.24, 83.66, 1.10),   # man sieht sich vielleicht am Montag im Workshop
    (84.48, 86.46, 1.00),   # da machen wir nämlich mit KI
    (87.14, 89.30, 1.18),   # bauen wir deine Personal Brand auf.
    (90.14, 91.98, 1.00),   # Ich freue mich auf euch. Ciao!
]
FIX_AT = {84.52: "da", 65.40: "einen", 55.20: "die", 55.54: "", 55.88: ""}
BLUE = {"aufträge", "coaching", "november", "kunden", "message", "skill", "läuft", "workshop", "ki", "personal", "brand", "geil", "montag"}

words = [w for s in json.load(open(WORDS)) for w in s["w"]]
# map source words into the output timeline
cap, t0 = [], 0.0
for a, b, z in SEG:
    for ws, we, w in words:
        if ws >= a - .02 and we <= b + .05:
            w = FIX_AT.get(round(ws, 2), w.strip())
            if not w: continue
            cap.append((t0 + max(0, ws - a), t0 + min(b, we) - a, w))
    if a == 57.70: cap.insert(len(cap) - 4, (t0, t0 + .1, "die"))
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
    clean = w.strip(".,!?").lower()
    txt = w.upper().replace("2.", "2.")
    return ("{\\c&HFF5B2F&}" + txt + "{\\c&HFFFFFF&}") if clean in BLUE else txt

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
    # pop-in, each word appears on its own start time
    parts = []
    for ws, we, w in ch:
        d = int((ws - st) * 1000)
        parts.append("{\\alpha&HFF&\\t(%d,%d,\\alpha&H00&)}" % (d, d + 60) + word(w))
    ass.append(f"Dialogue: 1,{ts(st)},{ts(en)},Cap,,0,0,0,,{{\\fscx92\\fscy92\\t(0,90,\\fscx100\\fscy100)}}" + " ".join(parts))
# hook kicker + CTA card
ass.append(f"Dialogue: 2,{ts(0)},{ts(3.9)},Kick,,0,0,0,,{{\\fad(0,200)}}BUILD IN PUBLIC · FLOW MEDIA AI")
ass.append(f"Dialogue: 2,{ts(0)},{ts(3.9)},Big,,0,0,0,,{{\\fad(0,200)}}ERSTE AUFTRÄGE –\\NVOR DEM ERSTEN\\N{{\\c&HFF5B2F&}}COACHING-TAG.")
cta = sum(b - a for a, b, z in SEG[:14])
ass.append(f"Dialogue: 2,{ts(cta)},{ts(TOTAL)},Kick,,0,0,0,,{{\\fad(200,0)}}DIGITALER STAMMTISCH #1 · MO 26.10. · 18 UHR")
ass.append(f"Dialogue: 2,{ts(cta + .25)},{ts(TOTAL)},Big,,0,0,0,,{{\\fad(200,0)}}MIT KI ZUR\\N{{\\c&HFF5B2F&}}PERSONAL BRAND.{{\\c&HFFFFFF&}}\\N{{\\fnInter\\fs40\\b0\\bord0\\shad2}}15 € · live · Link in Bio")
open(os.path.join(HERE, "captions.ass"), "w").write("\n".join(ass) + "\n")

# video: HLG -> SDR, trim, punch-in, concat, b/w grade, captions, logo
tm = "zscale=t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p"
fc = [f"[0:v]{tm},fps=30,split={len(SEG)}" + "".join(f"[s{i}]" for i in range(len(SEG)))]
fc += [f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,asplit={len(SEG)}" + "".join(f"[r{i}]" for i in range(len(SEG)))]
for i, (a, b, z) in enumerate(SEG):
    fc.append(f"[s{i}]trim={a}:{b},setpts=PTS-STARTPTS,crop=iw/{z}:ih/{z}:(iw-iw/{z})/2:(ih-ih/{z})*0.3,scale=1080:1920:flags=lanczos,setsar=1[v{i}]")
    fc.append(f"[r{i}]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={b - a - 0.015:.3f}:d=0.015[a{i}]")
fc.append("".join(f"[v{i}][a{i}]" for i in range(len(SEG))) + f"concat=n={len(SEG)}:v=1:a=1[vc][ac]")
fc.append("[vc]hue=s=0,eq=gamma=1.3:contrast=1.25:brightness=-0.03,unsharp=5:5:0.8,noise=alls=3:allf=t[vg];[3:v]format=rgba[sh];[vg][sh]overlay=0:0,"
          f"ass={os.path.join(HERE, 'captions.ass')}:fontsdir={os.path.join(HERE, 'fonts')}[vs]")
fc.append("[1:v]scale=170:-1,format=rgba,colorchannelmixer=aa=0.9[lg];[vs][lg]overlay=W-w-70:150[vout]")
# voice: clean + level; music bed ducked under the voice
fc.append("[ac]highpass=f=85,afftdn=nf=-28,equalizer=f=200:t=q:w=1:g=-2,equalizer=f=3200:t=q:w=1.2:g=2.5,"
          "acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=4,loudnorm=I=-15:TP=-1.5:LRA=7[vo]")
fc.append(f"[2:a]atrim=start=0.5:duration={TOTAL + .5},asetpts=PTS-STARTPTS,aresample=48000,volume=0.16,"
          f"afade=t=in:d=0.6,afade=t=out:st={TOTAL - 1.6:.2f}:d=1.6[mu]")
fc.append("[vo]asplit[vo1][vo2];[mu][vo2]sidechaincompress=threshold=0.04:ratio=6:attack=15:release=300[mud];"
          "[vo1][mud]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.9[aout]")
cmd = ["ffmpeg", "-v", "error", "-y", "-i", RAW, "-i", os.path.join(HERE, "logo_flow.png"), "-i", MUSIC, "-i", os.path.join(HERE, "shade.png"),
       "-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]", "-t", f"{TOTAL:.3f}",
       "-c:v", "libx264", "-crf", "23", "-preset", "slow", "-maxrate", "9M", "-bufsize", "18M", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
       "-movflags", "+faststart", os.path.join(HERE, "R011.mp4")]
subprocess.run(cmd, check=True)
print("total", round(TOTAL, 2), "chunks", len(chunks))
