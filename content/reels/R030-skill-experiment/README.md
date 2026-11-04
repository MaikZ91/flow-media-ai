# R030 – Das Skill-Experiment: Masterclass in 1 statt 2 Stunden?

Stand: 04.11.2026 · Reel 1080×1920, 54,8 s · Status: **fertig (`R030.mp4`)** · Säule `lernen` / `weg` · Test-Variable `format = talkinghead-animiert-farbe`

Quelle: Maiks Selfie-Video `IMG_1362.MOV` (Drive RAW, 1:48 min, HLG). Bild verbessert (`grade.txt`): HLG→SDR getonemappt, leicht gezoomt (Gesicht größer), Schatten aufgehellt (curves), etwas mehr Sättigung, Schärfe. **Farbe**, kein Schwarz-Weiß. Auf 54 s geschnitten (Ähms, „Also“, „So“, „genau“, Pausen und der Satz „damit kann er jetzt selber…“ mit langen Pausen raus).

Animationen (transparente Ebene, Flow-Look):
| Abschnitt | Animation |
|---|---|
| Hook | 🧪 „Ein Experiment.“ |
| Masterclass | „Sonntag · Meine 1. AI Masterclass“ · „Gebaut: Cocktail-App“ mit Cocktailglas, das sich blau füllt |
| Kunde | Kette 💡 Idee → 📱 Prototyp → 🧠 KI-Skills, synchron zu den Worten |
| Workflow | 5 Knoten leuchten nacheinander: Fragen · Content · 5 Versionen · Auswahl · Launch |
| Experiment | Slam „EXPERIMENT.“ mit Blitz · die 5 Knoten fliegen in die Datei `skills/app-in-varianten/SKILL.md` („App in Varianten“) · „↻ immer wieder verwendbar“ |
| Zeit | Karte „2 Stunden. Oder 1?“ – Balken Sonntag 2:00 h vs. heute nur mit Skill 1:00 h |
| Test | „Gleiches Ergebnis? …“ · 🔔 „Update folgt“ |
| CTA | Karte „Nächster Workshop · Skills & Workflows mit Claude oder Codex · Fr 06.11. · 17 Uhr · Plätze frei – schreib mir“ |
Untertitel wortgenau (aktuelles Wort blau). Musik: „Driving Ambition“ (Mixkit, Stock Music Free License) ab 39 s, geduckt. Kunde ohne Namen, keine Screens aus seiner App.

## Caption
```
Mein Experiment für heute 🧪

Sonntag hatte ich meine erste AI Masterclass. In 2 Stunden haben wir zusammen eine Cocktail-App gebaut – der Kunde kam mit der Idee, ging mit einem Prototyp und eigenen KI-Skills raus.

Meinen Workflow dafür hab ich danach in einen Skill gegossen.
Heute gebe ich die nächste Masterclass – in 1 Stunde. Nur mit diesem Skill.

Gleiches Ergebnis in der halben Zeit? Ich sag euch Bescheid. 🔔

Du willst lernen, wie man Skills und Workflows mit Claude oder Codex baut?
Nächster Workshop: Freitag, 06.11., 17 Uhr. Es sind noch Plätze frei – schreib mir.

#KI #ClaudeCode #Codex #Workflow #FlowMediaAI
```
Grund zum Folgen: „Folge mir, um zu sehen, ob das Experiment klappt.“
Posten: heute 18–20 Uhr (Experiment läuft heute, Workshop Freitag).

## Neu rendern
`raw/src.mov` aus RAW → `raw/words.json` (faster-whisper medium) → `python3 cut.py` (Grade aus `grade.txt`) → `overlay.tpl.html` → `overlay.html` → `node render.js` → ffmpeg overlay + Stimme + Musik `driving-ambition.mp3 -ss 39`, sidechaincompress, loudnorm −14, crf 24.
