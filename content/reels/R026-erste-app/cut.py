# cut the talking-head raw into the edit, write edit.mp4 (video, tonemapped SDR) + voice.wav + cuts.json + captions.json
import json, subprocess
CUTS = [  # [step, src_in, src_out]
 ["hook", 19.80, 21.95],
 ["s1", 24.85, 25.72], ["s1", 26.20, 29.05], ["s1", 29.05, 31.20],
 ["s2", 41.05, 43.78], ["s2", 51.88, 55.98],
 ["s3", 59.68, 61.85], ["s3", 62.70, 63.80], ["s3", 64.58, 66.42],
 ["s4", 82.95, 88.18], ["s4", 98.85, 101.38],
 ["s5", 104.90, 108.98], ["s5", 110.88, 112.98], ["punch", 113.52, 115.00],
 ["cta", 115.68, 119.48], ["cta", 127.18, 129.98], ["cta", 142.90, 145.12],
]
W = json.load(open("raw/words.json"))
fix = {"Möchtest": "Meld", "-Meisterklasse": "-Masterclass", "AI": "KI"}
t = 0; cuts = []; caps = []
for st, a, b in CUTS:
    cuts.append({"step": st, "in": a, "out": b, "t": round(t, 3)})
    for ws, we, w in W:
        if ws >= a - 0.05 and ws < b - 0.05:
            caps.append([round(t + ws - a, 2), round(t + min(we, b) - a, 2), fix.get(w.rstrip(".,?!"), w.rstrip(".,?!")) if w.rstrip(".,?!") in fix else w])
    t += b - a
json.dump({"cuts": cuts, "total": round(t, 3)}, open("cuts.json", "w"), indent=1)
json.dump(caps, open("captions.json", "w"), ensure_ascii=False)
tm = "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,fps=30"
import os; os.makedirs("seg", exist_ok=True); lst = open("seg/list.txt", "w")
for i, (_, a, b) in enumerate(CUTS):
    d = b - a
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-threads", "2", "-ss", str(a), "-i", "raw/src.mov", "-t", f"{d:.3f}", "-map", "0:v:0", "-map", "0:a:0",
                    "-vf", tm, "-af", f"afade=t=in:d=0.02,afade=t=out:st={d-0.03:.3f}:d=0.03", "-c:v", "libx264", "-crf", "16", "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "1", f"seg/{i:02d}.mov"], check=True)
    lst.write(f"file '{i:02d}.mov'\n")
lst.close()
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-i", "seg/list.txt", "-map", "0:v", "-c:v", "copy", "edit.mp4", "-map", "0:a", "voice.wav"], check=True)
print("total", t, "captions", len(caps))
