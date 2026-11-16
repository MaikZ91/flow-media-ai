#!/bin/bash
# Setzt die gerenderten Bilder mit Musik zusammen -> R045.mp4
# Musik: „Uplifting Bass“ (Mixkit, Stock Music Free License), ab 0,03 s: der Einsatz bei 14,36 s im Track fällt auf den Sprung nach „2026.“ (14,33 s im Reel).
cd "$(dirname "$0")"
ffmpeg -y -v error -framerate 30 -i frames/f_%05d.jpg -ss 0.03 -t 30.4 -i ../../musik/frei/uplifting-bass.mp3 \
  -filter_complex "[1:a]afade=t=in:d=0.04,afade=t=out:st=28.9:d=1.5,loudnorm=I=-14.5:TP=-2:LRA=9,alimiter=limit=0.85[a]" \
  -map 0:v -map "[a]" -c:v libx264 -crf 20 -preset slow -pix_fmt yuv420p -r 30 -c:a aac -b:a 256k -shortest -movflags +faststart R045.mp4
ffprobe -v error -show_entries format=duration,size -of csv=p=0 R045.mp4
