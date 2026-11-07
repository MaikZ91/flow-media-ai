#!/bin/bash
# final mix: edit.mp4 + overlay.mov + voice.wav + music (Deep Urban, Mixkit) with ducking
set -e; cd "$(dirname "$0")"
T=$(python3 -c "import json;print(json.load(open('cuts.json'))['total']+0.6)")
ffmpeg -v error -y -i edit.mp4 -i overlay.mov -i voice.wav -ss 16 -i ../../musik/frei/deep-urban.mp3 -filter_complex \
"[0:v]tpad=stop_mode=clone:stop_duration=0.6[b];[b][1:v]overlay=format=auto,format=yuv420p[v];\
[2:a]highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=120:makeup=3,apad=whole_dur=$T,asplit=2[vo][sc];\
[3:a]atrim=duration=$T,volume=0.55,afade=t=in:d=0.4,afade=t=out:st=$(python3 -c "print($T-1.5)"):d=1.5[m];\
[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[md];\
[vo][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5[a]" \
-map "[v]" -map "[a]" -t $T -c:v libx264 -crf 22 -preset medium -c:a aac -b:a 192k -movflags +faststart R034.mp4
