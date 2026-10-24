# R008 · Intro „Welcome to Flow Media AI“ – System-Boot

Stand: 23.10.2026 (Version 2 – die erste Version „fetzte nicht“, Maik) · Format: Reel/Intro 1080×1920, 15 s · Status: **fertig (`R008.mp4`)**

Säule: `kreativ` · Kein Erklärvideo, sondern ein Intro, das knallt: auf Maiks eigenen Track geschnitten, mit KI-Systemstimme, Blitzen und Build · Connect · Enable.

## Idee
Flow Media AI „bootet“ wie ein System. Vor dem Drop fährt ein Terminal hoch, auf dem Drop schlägt ein Blitz ein und Maik steht als Hologramm da. Danach wird auf jeden Beat geschnitten (143,55 BPM, ein Beat = 0,418 s): Kamera-Punch, Strobe, Bildzeilen-Glitch, Wörter, Blitze. Am Ende sagt die Systemstimme „Welcome to Flow Media AI“.

## Ablauf (Beat 0 = Drop bei 4,0 s)
| Zeit | Bild | Ton |
|---|---|---|
| 0–4 s | Terminal: `boot flow_media_ai --mode=holo` … `system online_`, Teilchen sammeln sich im Dunkeln | Breakdown des Tracks · Stimme: „Initializing.“ / „System online.“ · Riser |
| 4,0 s (Beat 0) | **Drop:** weißer Blitz, Blitzeinschlag, Schockwellen-Ring, Hologramm steht | Drop + Bass-Einschlag |
| Beat 2 | **BUILD.** + Blitz, Gitterboden | Stimme: „Build.“ |
| Beat 4 | Hologramm mit Scan-Streifen | |
| Beat 6 | **CONNECT.** + Blitz, Lichtpunkte vernetzen sich um den Kopf | Stimme: „Connect.“ |
| Beat 8 | Tiefenscan-Ansicht (blau, Scanlinie läuft durch) | |
| Beat 10 | **ENABLE.** + Blitz, Lichtsäule, Partikel steigen | Stimme: „Enable.“ |
| Beat 12–15 | Hologramm dreht sich, Blitzbögen links/rechts auf jedem Beat | |
| Beat 16 (≈10,7 s) | Doppelblitz → **WELCOME TO / FLOW MEDIA AI / BUILD · CONNECT · ENABLE** | Stimme: „Welcome to Flow Media AI.“ · Einschlag |

## Ton
- **Musik:** MZ.9 – Track aus dem Reel `Dcony8TtVD3` (`content/musik/eigene/mz9_track_Dcony8.m4a`), Ausschnitt 69,0–84,0 s, Drop bei 73,0 s. *Titel bei Maik erfragen und in die Caption schreiben.*
- **Stimme:** KI-Systemstimme (Piper TTS, Stimme „Amy“, mit Chorus/Echo verfremdet) – bewusst **nicht** Maiks Stimme, sondern ein „Bordcomputer“. Die Regel „keine Computerstimme als Maik“ bleibt gewahrt.
- **Effekte:** Bass-Einschläge, Zaps, Riser – synthetisch (`mix.py`).

## Caption (Vorschlag)
Welcome to Flow Media AI. ⚡

Hologramm, Blitze, Systemstimme – alles mit KI und Code gebaut. Und der Track ist von mir.

Build. Connect. Enable.

🎵 MZ.9 – [Titel] · @mz.9_nyc

#KI #3D #Hologramm #FlowMediaAI #BuildInPublic

**Grund zum Senden:** „Schick das jemandem, der denkt, für so was braucht man ein Filmstudio.“

## Neu bauen
Ordner per `python3 -m http.server 8767` ausliefern → `node render.js` (Playwright, WebGL/SwiftShader, ca. 6 Min.) → `python3 mix.py` → `ffmpeg -i video_only.mp4 -i mix.wav -map 0:v -map 1:a -c:v libx264 -crf 24 -c:a aac -b:a 192k -shortest R008.mp4`.
Stimme neu erzeugen: `echo "Welcome to Flow Media A I." | python3 -m piper -m en_US-amy-medium.onnx -f v5.wav`, danach `ffmpeg -af "highpass=f=120,asetrate=22050*0.94,aresample=48000,atempo=1.06,chorus=0.6:0.9:40|60:0.3|0.25:0.25|0.4:2|1.5,aecho=0.8:0.6:60|120:0.25|0.15,volume=1.6"`.
