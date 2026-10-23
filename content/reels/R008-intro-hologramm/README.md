# R008 · Intro „Welcome to Flow Media AI“ (Hologramm)

Stand: 23.10.2026 · Format: Reel/Intro 1080×1920, 14 s, mit eigenem Sounddesign · Status: **fertig (`R008.mp4`)**

Säule: `ki` / `design` · Kein Erklärvideo, sondern ein cineastisches Intro (Maiks Wunsch 23.10.2026): abgefahren, spacig, Blitze, Flow-Elemente, Build · Connect · Enable. Verwendbar als Reel, als Story, als Intro vor anderen Reels oder für Website/Workshop-Start.

## Ablauf
| Zeit | Bild | Ton |
|---|---|---|
| 0–1,2 s | Warp durch Sterne, erster Blitz in der Ferne | Warp-Woosh, Knistern |
| 1,15 s | Blitz schlägt in die Plattform ein | Donner + Bass-Einschlag |
| 1,2–3,8 s | 120.000 Lichtteilchen wirbeln heran und setzen sich von unten nach oben zu Maik zusammen, Kamera fährt heran | Riser |
| 3,8–6 s | Hologramm dreht sich, Glitch, Blitzbögen links und rechts am Kopf, Ringe und Wellenlinien (Flow) | Glitch-Blips, Zaps |
| 6,0 s | **BUILD.** + Blitz, Gitterboden baut sich auf | Einschlag |
| 7,2 s | **CONNECT.** + Blitz, Lichtpunkte umkreisen den Kopf und verbinden sich | Einschlag |
| 8,4 s | **ENABLE.** + Blitz, Lichtsäule steigt auf, Partikel steigen | Einschlag, Sub-Swell |
| 10,4–14 s | Doppelblitz → **WELCOME TO / FLOW MEDIA AI / BUILD · CONNECT · ENABLE**, Maik als Hologramm dahinter | großer Einschlag, Glitzern, Ausklang |

## Technik
- Tiefe aus Maiks freigegebenem Porträt mit Depth Anything V2 (wie R007), daraus 300×400 Punkte in three.js.
- Bloom (UnrealBloomPass), chromatische Aberration, Filmkorn, Scanlines; Blitze per Mittelpunkt-Verschiebung mit Verzweigungen, jede Szene deterministisch (feste Zufallszahlen).
- Sound komplett synthetisch (`sound.py`, numpy/scipy) – keine Samples, keine Lizenzen.
- Grenze: aus einem Foto nur die Vorderseite → Drehung ca. ±20–30°. Rundum-Modell siehe R007-README.

## Caption (Vorschlag)
Welcome to Flow Media AI. ⚡

Dieses Intro hab ich komplett mit KI und Code gebaut: ein Foto von mir, eine KI, die daraus 3D macht, 120.000 Lichtpunkte, Blitze – und der Sound ist auch selbst erzeugt.

Build. Connect. Enable. – darum geht's hier.

#KI #3D #Hologramm #FlowMediaAI #BuildInPublic

**Grund zum Senden:** „Schick das jemandem, der denkt, für so was braucht man ein Filmstudio.“

## Neu bauen
`python3 sound.py` → `sound.wav` · Ordner per `python3 -m http.server 8766` ausliefern, `node render.js` (Playwright, WebGL/SwiftShader) → `video_only.mp4` · `ffmpeg -i video_only.mp4 -i sound.wav -map 0:v -map 1:a -c:v libx264 -crf 24 -c:a aac -b:a 192k -shortest R008.mp4`
