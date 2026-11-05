# R031 – Morgen: Workshop „Mit KI zur Personal Brand“ (Promo, Talking Head + Animationen)

Stand: 05.11.2026 · Reel 1080×1920, 48 s · Status: **fertig (`R031.mp4`)** · Säule `lernen` · Test-Variable `format = talkinghead-animiert-farbe` (Workshop-Promo)

Quelle: Maiks Selfie-Video `IMG_1369.MOV` (Drive RAW, 59 s, HLG). Bild: getonemappt, leicht gezoomt, Schatten aufgehellt, Gelbstich etwas ausgeglichen (`colorbalance`), Schärfe. Farbe. Auf 47,5 s geschnitten (Ähms, „besser“/„wieder“-Doppler, Pausen raus); Untertitel korrigiert: „effizient“ (statt „Epizent“), „melde dich bei mir“.

Animationen: ☀️ „Guten Morgen!“ · Kalender klappt auf „NOV 06 FREITAG“ + „Morgen Workshop 17 Uhr“ · Slam „Mit KI zur Personal Brand.“ · Datei `skills/deine-brand/SKILL.md` „Deine Brand als Skill“ · 3 Posts im gleichen Look mit ✓ · Chips 🎨 Styling / 🌐 Website / 📱 Apps · „Generisch“ durchgestrichen vs. „Nach dir ✓“ · Workflow Idee → Skill → Content → Post · Stapel „Die Basis für KI“ · Workshop-Karte (Fr 06.11., 17 Uhr, Inhalte, „Noch nicht angemeldet? Schreib mir“) · „Bis morgen 👋“.
Musik: „Talent in the Air“ (Mixkit, Stock Music Free License) ab 15,7 s, geduckt. Preis 15 € (Fr 17–18 Uhr) nur in der Caption, nicht im Video.

## Caption
```
Morgen ist Workshop-Tag. 🎙️

„Mit KI zur Personal Brand“
📅 Freitag, 06.11., 17–18 Uhr
💶 15 €

Du baust dir einen eigenen Brand-Skill. Damit sieht dein Content immer nach dir aus – nicht mehr generisch nach KI. Für Posts, deine Website, deine Apps.
Und darauf baust du ganze Workflows auf. Für mich ist das die Basis, um mit KI wirklich effizient zu arbeiten.

🎁 Bonus für alle, die dabei sind: Bis zum 31.12. bekommst du von mir Q&A und technischen Support, während du deine eigenen Ideen umsetzt. Du stehst danach also nicht allein da.

Noch nicht angemeldet? Schreib mir eine Nachricht – dann schick ich dir alle Infos. 👇

#PersonalBrand #KI #ClaudeAI #Codex #FlowMediaAI
```
Grund zum Senden: „Schick das jemandem, dessen Content noch nach ChatGPT klingt.“
Posten: heute (Do 05.11.) 18–19 Uhr; morgen früh als Story mit Countdown-Sticker reposten.

## Neu rendern
`raw/src.mov` → `raw/words.json` (faster-whisper medium) → `python3 cut.py` (Grade inkl. colorbalance) → `overlay.tpl.html` → `overlay.html` → `node render.js` → ffmpeg overlay + Stimme + Musik `talent-in-the-air.mp3 -ss 15.7`, sidechaincompress, loudnorm −14, crf 24.
