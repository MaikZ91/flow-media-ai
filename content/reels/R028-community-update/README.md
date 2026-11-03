# R028 – Community-Update: 3 Dinge (Talking Head + Flow-Animationen)

Stand: 03.11.2026 · Reel 1080×1920, 75,5 s · Status: **fertig (`R028.mp4`)** · Säule `weg` / `community` · Test-Variable `format = talkinghead-animiert`

Quelle: Maiks Selfie-Video (Drive RAW, `copy_933EB88B….mov`, 95,6 s, Farbe, 60 fps). In **Farbe gelassen**, auf 74,5 s geschnitten: alle „Ähm“, Doppelungen („Und“, „Also“, „quasi“, „genau“) und Pausen raus (`cut.py`, Schnittliste oben). Das unklare Wort bei 34 s ist laut large-v3 „KI“ („Über KI“).

Animationen als transparente Ebene (`overlay.html` → `overlay.mov`) im Flow-Look (schwarz, weiß, Blau #2F5BFF, Oswald):
| Abschnitt | Animation |
|---|---|
| Intro | „Community-Update“ + Kapitel-Chips 01/02/03 |
| 01 Wir wachsen | Netzwerk wächst Knoten für Knoten („So viele Persönlichkeiten.“) · **Atemkreis** dehnt sich aus („Einatmen …“) bei Breathwork · Buch blättert, Zeilen schreiben sich bei „Bücher schreiben“ · Chips „KI-Begeisterte ⚡“ |
| 02 Café | Slam „02“ · Rentner-Ehepaar am Tisch mit Kaffee-Dampf + Sprechblasen · „Worüber? 🤔“ · Slam blau „ÜBER KI.“ · Balken „Gefühlt auf dem Stand bei KI“ (Rentner vs. unsere Generation, als Eindruck markiert) · „Traurig 😕 → …aber cool 😎“ |
| 03 KI-Videos | Slam „03“ · 3×3-Kacheln generieren sich aus Rauschen + Prompt tippt · „Stories erzeugen 🎬“ · „Süchtig 🎰“ mit Credits-Balken, der leerläuft · Bertrand-Cutaway (R022, KI-generiert) bei „Sitcoms mit dem Charakter“ |
| Outro | „Dein Zug.“ Prompt „Probier's einfach aus.“ · „Schönen Abend 👋“ · Logo |
Untertitel wortgenau (aktuelles Wort blau). Musik: „Cat Walk“ (Mixkit, Stock Music Free License) ab 28 s, unter der Stimme geduckt.

## Caption
```
3 Dinge, die mich gerade beschäftigen 👇

1️⃣ Unsere Community wächst – und wie unterschiedlich wir sind: Breathwork, Bücher schreiben, KI-Begeisterte. Genau so soll es sein.

2️⃣ Heute im Café saß neben mir ein Rentner-Ehepaar. Ihr Thema? KI. Ehrlich: ein bisschen traurig, dass die gefühlt weiter sind als unsere Generation. Aber auch ziemlich cool.

3️⃣ Ich bin gerade komplett drin in Bild- und Video-Generierung. Stories bauen, Sitcoms mit Bertrand – hat mich schon einiges an Credits gekostet. Es wird also öfter was geben. 🍌

Probiert selbst mal was aus. Kreativ sein macht mit KI einfach Spaß.

Was beschäftigt dich gerade? Schreib's mir in die Kommentare.

#KI #Community #KIVideo #BuildInPublic #FlowMediaAI
```
Grund zum Senden: „Schick das jemandem, dessen Eltern mehr über KI wissen als er.“
Posten: abends 18–20 Uhr. Label „Mit KI erstellt“ setzen (Bertrand-Cutaway).

## Neu rendern
`raw/src.mov` aus RAW laden, `raw/words.json` per faster-whisper → `python3 cut.py` → `overlay.tpl.html` → `overlay.html` (CUTS/CAPS/TOTAL einsetzen) → `node render.js` (overlay.mov, qtrle mit Alpha) → ffmpeg: overlay auf `edit.mp4`, Stimme + Musik `cat-walk.mp3 -ss 28`, sidechaincompress, loudnorm −14, crf 25.
