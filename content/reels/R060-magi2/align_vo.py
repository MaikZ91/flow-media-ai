"""Legt die sieben Sätze einer Sprecheraufnahme auf die Szenenanfänge des Spots (Pausen per silencedetect)."""
import re, subprocess, sys
src, out = sys.argv[1], sys.argv[2]
TARGET = [0.15, 2.7, 4.7, 7.5, 10.3, 12.75, 14.5]
log = subprocess.run(["ffmpeg", "-i", src, "-af", "silencedetect=noise=-35dB:d=0.25", "-f", "null", "-"], capture_output=True, text=True).stderr
st = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", log)]; en = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", log)]
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src], capture_output=True, text=True).stdout)
gaps = [(s, e) for s, e in zip(st, en) if s > 1.2]  # ignore the dramatic pause inside sentence 1
assert len(gaps) >= 6, gaps
gaps = sorted(gaps, key=lambda g: g[1] - g[0], reverse=True)[:6]; gaps.sort()
cuts = [0.0] + [(s + e) / 2 for s, e in gaps] + [dur]
fc, labels = "", []
for i in range(7):
    a, b = cuts[i], cuts[i + 1]
    fc += f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,adelay={int(TARGET[i]*1000)}|{int(TARGET[i]*1000)}[p{i}];"; labels.append(f"[p{i}]")
fc += "".join(labels) + f"amix=inputs=7:normalize=0:duration=longest[a]"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-filter_complex", fc, "-map", "[a]", out], check=True)
print("cuts", [round(c, 2) for c in cuts])
