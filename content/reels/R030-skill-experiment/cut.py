# cut out fillers/pauses, write edit.mp4 (color, 30 fps) + voice.wav + cuts.json + captions.json
import json, subprocess, os
CUTS = [  # [section, in, out, optional caption override]
 ["hook", 3.30, 4.86], ["sonntag", 6.40, 9.48], ["cocktail", 10.34, 13.48],
 ["kunde", 15.00, 16.70], ["kunde", 17.66, 21.24], ["kunde", 21.20, 24.02],
 ["workflow", 34.86, 38.20], ["workflow", 39.50, 40.80],
 ["exp", 44.44, 46.38], ["skill", 47.18, 50.06], ["skill", 51.76, 53.78],
 ["zeit", 58.34, 61.82], ["zeit", 64.02, 67.22], ["test", 69.82, 72.02], ["test", 72.58, 73.86], ["bescheid", 81.70, 83.60],
 ["cta", 84.54, 87.16], ["cta", 87.22, 88.90], ["cta", 89.24, 93.24], ["cta", 93.46, 98.20], ["cta", 98.90, 99.96], ["bye", 106.88, 107.42],
]
GRADE = """zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,crop=940:1670:70:250,scale=1080:1920:flags=lanczos,curves=master='0/0 0.2/0.27 0.5/0.6 0.85/0.9 1/0.98',eq=saturation=1.15:contrast=1.03,unsharp=5:5:0.5"""
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
