#!/bin/bash
# usage: ./make.sh <srcdir> <workdir>   (srcdir: Portfolio-Videos w_*.mp4 + spin.mov)
set -e; cd "$(dirname "$0")"; SRC=$1; WORK=$2
python3 cut.py "$SRC" "$WORK"
node render.js
ffmpeg -v error -y -i "$WORK/edit.mp4" -i overlay.mov -ss 29.92 -i ../../musik/frei/digital-clouds.mp3 -filter_complex \
 "[0:v]noise=alls=7:allf=t[b];[b][1:v]overlay=format=auto,format=yuv420p[v];[2:a]atrim=duration=25.083,afade=t=out:st=23.6:d=1.48,loudnorm=I=-14:TP=-1.5[a]" \
 -map "[v]" -map "[a]" -t 25.083 -c:v libx264 -crf 22 -preset slow -c:a aac -b:a 192k -movflags +faststart R032.mp4
