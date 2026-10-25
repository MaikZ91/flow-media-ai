# Builds R012 from the robot-arm clip of Maik's study project (portfolio site): portrait crop, slow push-in,
# b/w grade, story text on the beat, Maik as a circle (placeholder until his avatar video arrives), music.
# usage: python3 build.py <robo.mp4> [avatar.mp4]
import subprocess, sys, os
SRC = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
MUSIC = os.path.join(HERE, "../../musik/frei/digital-clouds.mp3")
B = 0.4645                    # beat of "Digital Clouds" (Mixkit), grid from 29.92 s
M0 = 29.92
SCENE = 10 * B                # each scene = 10 beats
# (src_start, src_end, crop_w, crop_h, center_x, center_y) – robot in the middle of the lab
SEG = [
    (0.5, 6.3, 608, 1080, 1010, 540),
    (8.0, 13.8, 608, 1080, 1010, 540),
    (15.0, 20.8, 608, 1080, 1010, 540),
    (26.6, 31.25, 608, 1080, 960, 540),
]
TOTAL = SCENE * len(SEG)

def ts(x):
    return f"0:{int(x // 60):02d}:{x % 60:05.2f}"
BL = "{\\c&HFF5B2F&}"; WH = "{\\c&HFFFFFF&}"
TXT = [  # (kicker, headline with \N, small line)
    ("STUDIUM · MEDICAL ENGINEERING", f"HIER HAT ES\\N{BL}ANGEFANGEN.{WH}", ""),
    ("MEIN STUDIENPROJEKT", f"EIN ROBOTERARM.\\N{BL}GESTEUERT MIT KI.{WH}", "Noch von Hand trainiert – lange vor Claude."),
    ("DER MOMENT", f"AUTOMATISIEREN\\NIST {BL}MEIN DING.{WH}", "Ideen und Technik, die das Leben einfacher machen."),
    ("UND HEUTE", f"BAUE ICH GENAU DAS.\\N{BL}MIT KI.{WH}", "Flow Media AI · Build. Connect. Enable."),
]
ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "",
       "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Kick,Montserrat Medium,30,&H00E6E6E6,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,6,0,1,0,2,7,76,76,250,1",
       "Style: Big,Oswald,118,&H00FFFFFF,&H00FFFFFF,&H00000000,&H78000000,1,0,0,0,100,100,0,0,1,0,6,7,76,76,330,1",
       "Style: Small,Inter,40,&H00E6E6E6,&H00FFFFFF,&H00000000,&H78000000,0,0,0,0,100,100,0,0,1,0,3,7,76,76,610,1",
       "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for i, (k, h, s) in enumerate(TXT):
    a, b = i * SCENE, (i + 1) * SCENE
    ass.append(f"Dialogue: 1,{ts(a)},{ts(b)},Kick,,0,0,0,,{{\\fad(120,0)}}{k}")
    ass.append(f"Dialogue: 1,{ts(a + B * .5)},{ts(b)},Big,,0,0,0,,{{\\fad(150,0)\\fscx94\\fscy94\\t(0,140,\\fscx100\\fscy100)}}{h}")
    if s: ass.append(f"Dialogue: 1,{ts(a + B * 3)},{ts(b)},Small,,0,0,0,,{{\\fad(200,0)}}{s}")
open(os.path.join(HERE, "captions.ass"), "w").write("\n".join(ass) + "\n")

fc = [f"[0:v]fps=30,split={len(SEG)}" + "".join(f"[s{i}]" for i in range(len(SEG)))]
for i, (a, b, w, h, cx, cy) in enumerate(SEG):
    sp = (b - a) / SCENE
    fc.append(f"[s{i}]trim={a}:{b},setpts=(PTS-STARTPTS)/{sp:.4f},crop={w}:{h}:{cx - w // 2}:{cy - h // 2},"
              f"scale=1080:1920:flags=lanczos,zoompan=z='1+0.0009*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,"
              f"trim=duration={SCENE:.4f},setpts=PTS-STARTPTS,setsar=1[v{i}]")
fc.append("".join(f"[v{i}]" for i in range(len(SEG))) + f"concat=n={len(SEG)}:v=1:a=0[vc]")
fc.append("[vc]hue=s=0,eq=contrast=1.15:gamma=0.95,unsharp=5:5:0.6,noise=alls=3:allf=t[vg];[3:v]format=rgba[sh];[vg][sh]overlay=0:0,"
          f"ass={os.path.join(HERE, 'captions.ass')}:fontsdir={os.path.join(HERE, 'fonts')}[vs]")
fc.append("[1:v]scale=170:-1,format=rgba,colorchannelmixer=aa=0.9[lg];[vs][lg]overlay=W-w-70:150[vl]")
fc.append(f"[4:v]format=rgba,fade=t=in:st={B * 2:.2f}:d=0.3:alpha=1[av];[vl][av]overlay=30:1290[vout]")
fc.append(f"[2:a]atrim=start={M0}:duration={TOTAL:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.05,afade=t=out:st={TOTAL - 1.2:.2f}:d=1.2,"
          "loudnorm=I=-14:TP=-1.0:LRA=9[aout]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-i", os.path.join(HERE, "logo_flow.png"), "-i", MUSIC,
    "-i", os.path.join(HERE, "shade.png"), "-loop", "1", "-i", os.path.join(HERE, "img/avatar_circle.png"),
    "-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]", "-t", f"{TOTAL:.3f}",
    "-c:v", "libx264", "-crf", "21", "-preset", "slow", "-maxrate", "9M", "-bufsize", "18M", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", os.path.join(HERE, "R012.mp4")], check=True)
print("total", round(TOTAL, 2))
