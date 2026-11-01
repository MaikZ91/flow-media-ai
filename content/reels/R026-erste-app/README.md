# R026 – Deine erste App in 5 Schritten (How-to + Masterclass-CTA)

Stand: 01.11.2026 · Reel 1080×1920, 46,8 s · Status: **fertig (`R026.mp4`)** · Säule `lernen` / `apps` · Test-Variable `format = howto-talkinghead-steps` · Nebencharakter Bertrand (kurzer Cutaway)

Quelle: Maiks Selfie-Video `IMG_1321.MOV` (Drive RAW, 2:28 min, HLG → SDR getonemappt, schwarz-weiß). Maiks **echte Stimme**, auf 44 s geschnitten (Jump-Cuts mit wechselndem Zoom), Wort-Untertitel aus faster-whisper.

## Ablauf
| Zeit | Schritt | Overlay |
|---|---|---|
| 0–2,2 s | Hook | „How-to · in 5 Schritten – DEINE ERSTE APP.“ |
| 2,2–8,0 s | 1 Stell dir Fragen | Chips: Was muss sie können? · Welche Features? · Welches Ziel? |
| 8,0–14,9 s | 2 Content sammeln | Ordner + Bilder/Videos/Design → „Ein Ordner = Kontext für die KI“ |
| 14,9–20,0 s | 3 5 Versionen bauen lassen | Prompt „Claude, bau mir 5 Versionen meiner App.“, Bertrand-Cutaway (aus R022) „Bertrand baut alle 5.“, 5 App-Kacheln |
| 20,0–27,7 s | 4 Die beste auswählen | V3 leuchtet blau ✓ → „Dann den Prototyp verfeinern“ |
| 27,7–33,9 s | 5 Online stellen | Play Store oder Web-App → „Fertig ✓“ |
| 33,9–35,4 s | Punch | „Gar nicht so kompliziert.“ |
| 35,4–44,2 s | CTA | AI Masterclass – „Deine erste App. Mit mir.“ · „Schreib mir per DM“ |
| 44,2–46,8 s | Endkarte | „Bau deine erste App.“ · Schreib mir „APP“ per DM |

Ton: Maiks Originalstimme + „Pop Track 03“ (Mixkit, Stock Music Free License) ab 9 s, per `sidechaincompress` unter der Stimme geduckt, `loudnorm=I=-14`. Badge „BERTRAND · KI-GENERIERT“ während des Cutaways.

## Caption
```
Deine erste App in 5 Schritten. Ohne Programmieren. 📱

1️⃣ Stell dir Fragen: Was muss die App können? Welche Features, welches Ziel?
2️⃣ Sammle deinen Content in einem Ordner: Bilder, Videos, Design. Das ist der Kontext für die KI.
3️⃣ Sag Claude oder Codex: Bau mir 5 Versionen meiner App.
4️⃣ Nimm die beste und verfeinere den Prototyp.
5️⃣ Online stellen: als Web-App oder im Play Store.

Klingt simpel? Ist es auch. Der schwierigste Schritt ist der erste.

Genau das machen wir in meiner AI Masterclass: KI-Skills lernen und deine erste eigene App als Prototyp bauen. Für dein Business, deine Idee, deine Prozesse.

Schreib mir „APP“ per DM, wenn du dabei sein willst. 👇

#KI #AppEntwicklung #ClaudeCode #Codex #FlowMediaAI
```
Grund zum Speichern/Senden: „Speicher dir die 5 Schritte für deine erste App.“ / „Schick das jemandem, der seit Jahren von einer App-Idee redet.“
Posten: abends 18–20 Uhr. Label „Mit KI erstellt“ setzen (Bertrand-Cutaway).

## Neu rendern
1. `raw/src.mov` aus Drive RAW laden (curl, siehe CLAUDE.md), `raw/words.json` per faster-whisper (Wort-Zeitstempel).
2. `python3 cut.py` → `seg/*.mov`, `edit.mp4`, `voice.wav`, `cuts.json`, `captions.json` (Schnittliste oben in `cut.py`); Frames `ffmpeg -i edit.mp4 -q:v 3 raw/edit/%04d.jpg`; Bertrand-Frames aus `R022/raw/s2` nach `raw/bert`.
3. `reel.tpl.html` → `reel.html` (CUTS/CAPS/TOTAL einsetzen), `node frames.js $PWD reel.html` → `video_only.mp4`.
4. Ton: Stimme + Musik `-ss 9`, sidechaincompress, loudnorm −14, dann crf 23.
