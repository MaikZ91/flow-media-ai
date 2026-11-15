#!/bin/bash
# Setzt die gerenderten Bilder mit Musik zusammen -> R044.mp4
# Musik: „Digital Clouds“ (Mixkit, Stock Music Free License), ab 15,288 s: der Drop liegt bei 14,88 s im Reel (Schwarm-Szene).
cd "$(dirname "$0")"
ffmpeg -y -v error -framerate 30 -i frames/f_%05d.jpg -ss 15.288 -t 29.9 -i ../../musik/frei/digital-clouds.mp3 \
  -filter_complex "[1:a]afade=t=in:d=0.04,afade=t=out:st=28.3:d=1.45,loudnorm=I=-14:TP=-1.2:LRA=9[a]" \
  -map 0:v -map "[a]" -c:v libx264 -crf 20 -preset slow -pix_fmt yuv420p -r 30 -c:a aac -b:a 256k -shortest -movflags +faststart R044.mp4
ffprobe -v error -show_entries format=duration,size -of csv=p=0 R044.mp4
