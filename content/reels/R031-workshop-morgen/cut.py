# cut out fillers/pauses, write edit.mp4 (color, 30 fps) + voice.wav + cuts.json + captions.json
import json, subprocess, os
CUTS = [  # [section, in, out, optional caption override]
 ["intro", 1.30, 3.02], ["morgen", 3.50, 7.02], ["thema", 7.40, 11.12],
 ["skill", 11.74, 14.02], ["gleich", 14.86, 17.16], ["gleich", 18.64, 19.42],
 ["brand", 19.46, 22.94], ["brand", 23.40, 25.04], ["brand", 25.62, 31.04],
 ["generisch", 31.56, 33.58], ["generisch", 33.70, 35.72, "kriegst nicht mehr dieses Generische"], ["workflows", 36.48, 39.60],
 ["basis", 39.70, 41.48], ["basis", 41.68, 45.26, "um halt mit KI effizient umzugehen."],
 ["los", 45.50, 47.18], ["los", 47.36, 48.92], ["cta", 49.66, 50.14], ["cta", 51.32, 54.08], ["cta", 54.58, 56.14, "dann melde dich bei mir."], ["bye", 57.00, 58.86],
]
GRADE = """zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,crop=940:1670:70:250,scale=1080:1920:flags=lanczos,curves=master='0/0 0.2/0.27 0.5/0.6 0.85/0.9 1/0.98',eq=saturation=1.15:contrast=1.03,colorbalance=rs=-0.03:bs=0.05:rm=-0.04:bm=0.06:rh=-0.03:bh=0.04,unsharp=5:5:0.5"""
W = json.load(open("raw/words.json"))
fix = {"AI": "AI"}
t = 0; cuts = []; caps = []
for c in CUTS:
    st, a, b = c[:3]
    cuts.append({"sec": st, "in": a, "out": b, "t": round(t, 3)})
    if len(c) > 3:
        ws = c[3].split(); d = (b - a) / len(ws)
        for i, w in enumerate(ws): caps.append([round(t + i * d, 2), round(t + (i + 1) * d, 2), w])
    else:
        for s, e, w in W:
            if s >= a - 0.06 and s < b - 0.05 and w.lower().strip(",.") not in ("ähm", "äh"):
                caps.append([round(t + max(s, a) - a, 2), round(t + min(e, b) - a, 2), fix.get(w, w)])
    t += b - a
os.makedirs("seg", exist_ok=True); lst = open("seg/list.txt", "w")
for i, c in enumerate(CUTS):
    a, b = c[1], c[2]; d = b - a
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-threads", "2", "-ss", str(a), "-i", "raw/src.mov", "-t", f"{d:.3f}", "-map", "0:v:0", "-map", "0:a:0",
                    "-vf", GRADE + ",fps=30,format=yuv420p", "-af", f"afade=t=in:d=0.015,afade=t=out:st={d-0.025:.3f}:d=0.025",
                    "-c:v", "libx264", "-crf", "17", "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "1", f"seg/{i:02d}.mov"], check=True)
    n = int(subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", f"seg/{i:02d}.mov"], capture_output=True, text=True).stdout.strip())
    cuts[i]["nf"] = n
    lst.write(f"file '{i:02d}.mov'\n")
lst.close()
# re-time cuts by actual frame counts so video and audio stay in sync
acc = 0
for c in cuts: c["vt"] = round(acc / 30, 3); acc += c["nf"]
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-i", "seg/list.txt", "-map", "0:v", "-c:v", "copy", "edit.mp4"], check=True)
# audio rebuilt with per-segment padding to the video length of each segment
fc = "".join(f"[{i}:a]apad=whole_dur={c['nf']/30:.4f}[a{i}];" for i, c in enumerate(cuts)) + "".join(f"[a{i}]" for i in range(len(cuts))) + f"concat=n={len(cuts)}:v=0:a=1[o]"
args = ["ffmpeg", "-y", "-v", "error"]
for i in range(len(cuts)): args += ["-i", f"seg/{i:02d}.mov"]
subprocess.run(args + ["-filter_complex", fc, "-map", "[o]", "voice.wav"], check=True)
# shift captions to video time
def vt(x):
    for c in reversed(cuts):
        if x >= c["t"] - 1e-6: return round(c["vt"] + (x - c["t"]), 3)
    return x
caps = [[vt(s), vt(s) + (e - s), w] for s, e, w in caps]
for c in cuts: c["t"] = c["vt"]
json.dump({"cuts": cuts, "total": round(acc / 30, 3)}, open("cuts.json", "w"), indent=1)
json.dump(caps, open("captions.json", "w"), ensure_ascii=False)
print("total", acc / 30, "caps", len(caps))
