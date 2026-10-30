# R020 – Ad „AI Community“ (5 s, Community-Aufbau)

Stand: 30.10.2026 · Reel/Ad 1080×1920, 5,0 s · Status: **fertig (`R020.mp4`)** · Ziel: Ad, die auf die Flow-Media-AI-Community (WhatsApp) verlinkt · Säule `weg` / `engineering` · Branding bewusst frei (Maik: „ignoriere erstmal mein Branding“) – Rot #E10600, Weiß, Schwarz

## Ablauf (Beat-Raster „Pop Track 03“, Mixkit, Drop bei 4,481 s = Bild 1, B = 0,557 s)
| Zeit | Bild | Text |
|---|---|---|
| 0–1,1 s | Roter Screen, riesiges **AI** knallt rein (Flash + Shake), Maiks Roboterarm (Studienprojekt, 3× beschleunigt, s/w) **in den Buchstaben** | „Die Community für“ |
| 1,1–2,2 s | Kamera fliegt durchs „I“ ins Video, Roboterarm schwenkt im Vollbild | – |
| 2,2–3,3 s | Nahaufnahme Roboterarm, Wörter im Halbtakt | AUTOMATION. · ROBOTIK. · KI-TOOLS. · PROJEKTE. |
| 3,3–5,0 s | Endkarte rot | Für Macher, die mit KI bauen · **AI COMMUNITY** · Lernen. Bauen. Connecten. · Workshops · Austausch · Projekte · **Jetzt beitreten →** |

Material: Maiks eigenes Video (Portfolio, Wix-ID `8f2b5d9c6b914d0d865917d1a6e3c17b`, Ausschnitt 17,5–24,2 s und 28,9–30,8 s). Musik: „Pop Track 03“, Mixkit – Stock Music Free License, ab 4,46 s.

## Ad-Texte (Meta Ads Manager)
- **Primärtext:** Du baust mit KI, automatisierst Abläufe oder tüftelst an Robotik? In der Flow Media AI Community tauschen wir uns aus, zeigen Projekte und lernen in Workshops voneinander. Komm rein. 👇
- **Überschrift:** Die AI Community für Macher
- **Beschreibung:** Workshops · Austausch · Projekte
- **Button:** „Mehr dazu“ oder „Jetzt beitreten“ (falls verfügbar) · **Ziel-URL:** WhatsApp-Einladungslink der Community-Gruppe
- Keine Mitgliederzahlen oder Erfolgsversprechen im Ad, solange es keine echten Zahlen gibt.

## Hook-Test (empfohlen)
Gleicher Body, nur die ersten 1,1 s tauschen: Variante A (dieses Reel, „AI“ + Roboter in den Buchstaben) gegen Variante B (Maik-Selfie 1 s: „Du baust mit KI?“). Kennzahl: 3-Sekunden-Views / Impressionen (Hook-Rate).

## Neu rendern
RAW-Frames (nicht im Repo): Video per curl von `https://video.wixstatic.com/video/97c2a9_8f2b5d9c6b914d0d865917d1a6e3c17b/1080p/mp4/file.mp4`, dann
`wide`: `-ss 17.5 -t 6.7`, `setpts=PTS/3,fps=30,crop=560:996:720:60,scale=1080:1920` · `close`: `-ss 28.9 -t 1.9`, `setpts=PTS/1.5,fps=30,crop=608:1080:780:0,scale=1080:1920` · Grade `hue=s=0,eq=contrast=1.35:brightness=-0.06:gamma=0.95,unsharp=5:5:0.6`
`node frames.js <ordner>` → `video_only.mp4`, dann
`ffmpeg -i video_only.mp4 -ss 4.46 -i ../../musik/frei/pop-track-03.mp3 -t 5.013 -filter_complex "[1:a]afade=t=out:st=4.6:d=0.41,loudnorm=I=-12:TP=-1:LRA=7[a]" -map 0:v -map "[a]" -c:v libx264 -crf 19 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart R020.mp4`
