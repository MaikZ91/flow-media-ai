# Builds R014 from the screen recording of the tensile test (live force curve + camera) of Maik's study project (portfolio site): portrait crop,
# slow push-in, b/w grade, story text on the beat, Maik as a circle (placeholder until his avatar video arrives), music.
# Same format as R012. usage: python3 build.py <source.mp4>
import subprocess, sys, os
SRC = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "R014.mp4"
MUSIC = os.path.join(HERE, "../../musik/frei/close-up.mp3")
B, M0, BEATS = 0.5715, 17.27, 8        # "Close Up" (Mixkit), grid from 17.27 s, 8 beats per scene
SCENE = BEATS * B
# ("crop", src_start, src_end, crop_w, crop_h, center_x, center_y)  – 9:16 crop, fills the frame
# ("card", src_start, src_end, x, y, w, h)                            – landscape card on a blurred background
SEG = [
    ("card", 2.0, 7.5, 300, 110, 1570, 890),     # whole screen: curve + camera
    ("card", 10.5, 16.0, 300, 220, 770, 520),    # force curve
    ("card", 26.0, 31.5, 1090, 170, 770, 740),   # camera: the mesh under tension
    ("card", 41.0, 46.5, 300, 110, 1570, 890),   # whole screen
]
BL = "{\\c&HFF5B2F&}"; WH = "{\\c&HFFFFFF&}"
TXT = [  # (kicker, headline with \N, small line)
    ("STUDIENPROJEKT · MESSTECHNIK", f"SO SIEHT\\N{BL}ZUGKRAFT AUS.{WH}", ""),
    ("DIE KURVE", f"KRAFT.\\N{BL}LIVE GEMESSEN.{WH}", "Messsoftware · LabVIEW"),
    ("DIE KAMERA", f"DAS NETZ.\\N{BL}UNTER ZUG.{WH}", "Roboter zieht, Software zeichnet auf."),
    ("UND HEUTE", f"AUS DATEN WERDEN\\N{BL}ANTWORTEN. MIT KI.{WH}", "Flow Media AI · Build. Connect. Enable."),
]

def ts(x):
    return f"0:{int(x // 60):02d}:{x % 60:05.2f}"
TOTAL = SCENE * len(SEG)
ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "",
       "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Kick,Montserrat Medium,30,&H00E6E6E6,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,6,0,1,0,2,7,76,76,250,1",
       "Style: Big,Oswald,112,&H00FFFFFF,&H00FFFFFF,&H00000000,&H78000000,1,0,0,0,100,100,0,0,1,0,6,7,76,76,330,1",
       "Style: Small,Inter,40,&H00E6E6E6,&H00FFFFFF,&H00000000,&H78000000,0,0,0,0,100,100,0,0,1,0,3,7,76,76,600,1",
       "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for i, (k, h, s) in enumerate(TXT):
    a, b = i * SCENE, (i + 1) * SCENE
    ass.append(f"Dialogue: 1,{ts(a)},{ts(b)},Kick,,0,0,0,,{{\\fad(120,0)}}{k}")
    ass.append(f"Dialogue: 1,{ts(a + B * .5)},{ts(b)},Big,,0,0,0,,{{\\fad(150,0)\\fscx94\\fscy94\\t(0,140,\\fscx100\\fscy100)}}{h}")
    if s: ass.append(f"Dialogue: 1,{ts(a + B * 3)},{ts(b)},Small,,0,0,0,,{{\\fad(200,0)}}{s}")
open(os.path.join(HERE, "captions.ass"), "w").write("\n".join(ass) + "\n")

push = "zoompan=z='1+0.0009*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30"
fc = [f"[0:v]fps=30,split={len(SEG)}" + "".join(f"[s{i}]" for i in range(len(SEG)))]
for i, seg in enumerate(SEG):
    kind, a, b = seg[:3]
    sp = (b - a) / SCENE
    base = f"[s{i}]trim={a}:{b},setpts=(PTS-STARTPTS)/{sp:.4f}"
    if kind == "crop":
        w, h, cx, cy = seg[3:]
        fc.append(f"{base},crop={w}:{h}:{cx - w // 2}:{cy - h // 2},scale=1080:1920:flags=lanczos,{push},"
                  f"trim=duration={SCENE:.4f},setpts=PTS-STARTPTS,setsar=1[v{i}]")
    else:                                   # card: blurred full frame behind, the region sharp in front
        x, y, w, h = seg[3:]
        fc.append(f"{base},split[bg{i}][fg{i}]")
        fc.append(f"[bg{i}]crop=608:1080:656:0,scale=1080:1920,boxblur=30:2,eq=brightness=-0.25[bb{i}]")
        fc.append(f"[fg{i}]crop={w}:{h}:{x}:{y},scale=1000:600:force_original_aspect_ratio=decrease:flags=lanczos,pad=iw+8:ih+8:4:4:color=0xFFFFFF[ff{i}]")
        fc.append(f"[bb{i}][ff{i}]overlay=(W-w)/2:690+(600-h)/2,{push},trim=duration={SCENE:.4f},setpts=PTS-STARTPTS,setsar=1[v{i}]")
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
    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", os.path.join(HERE, OUT)], check=True)
print("total", round(TOTAL, 2))
