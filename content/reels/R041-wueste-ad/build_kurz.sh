#!/bin/sh
# Wüsten-Reel neu geschnitten (~15 s): Pointe früher, Mitte kürzer. Quelle: wueste_1080.mp4 (Original-Reel hochgerechnet)
set -e
F=/usr/share/fonts/opentype/inter/Inter-Bold.otf
ffmpeg -v error -y -i wueste_1080.mp4 -filter_complex "
[0:v]trim=0:5.1,setpts=PTS-STARTPTS[v1];[0:a]atrim=0:5.1,asetpts=PTS-STARTPTS[a1];
[0:v]trim=5.2:7.0,setpts=PTS-STARTPTS[v2];[0:a]atrim=5.2:7.0,asetpts=PTS-STARTPTS[a2];
[0:v]trim=9.9:12.2,setpts=PTS-STARTPTS[v3];[0:a]atrim=9.9:12.2,asetpts=PTS-STARTPTS[a3];
[0:v]trim=15.4:18.4,setpts=PTS-STARTPTS[v4];[0:a]atrim=15.4:18.4,asetpts=PTS-STARTPTS[a4];
[0:v]trim=27.0:30.0,setpts=PTS-STARTPTS[v5];[0:a]atrim=27.0:30.0,asetpts=PTS-STARTPTS[a5];
[v1][a1][v2][a2][v3][a3][v4][a4][v5][a5]concat=n=5:v=1:a=1[v][a];
[v]drawbox=x=0:y=0:w=iw:h=150:color=black@0.55:t=fill:enable='lt(t,6.9)',
drawtext=fontfile=$F:fontsize=58:fontcolor=white:x=(w-tw)/2:y=48:text='Warte auf Bertrand …':enable='lt(t,6.9)',
drawbox=x=0:y=0:w=iw:h=150:color=black@0.55:t=fill:enable='gte(t,6.9)'[vo];
[a]afade=t=in:d=0.05,afade=t=out:st=14.4:d=0.8[ao]" \
-map "[vo]" -map "[ao]" -c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart wueste_neu_15s.mp4
