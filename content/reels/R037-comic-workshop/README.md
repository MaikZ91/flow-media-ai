# R037 · Comic „Maik & Bertrand in: Die Website“ (Workshop Mo 09.11. + Di 10.11., 18 Uhr)

Stand: 08.11.2026 · Reel 1080×1920, 36 s · Status: **fertig (`R037.mp4`)** · Säule `web` / `lernen` · Test-Variable `format = cartoon` (gezeichnete Comic-Animation statt Video)
Stil: eigene Gummischlauch-Cartoon-Figuren im Stil alter Zeichentrickfilme (gezeichnet als SVG, keine fremden Figuren), Look nach den echten Vorbildern: Maik mit blondem Haar, runder Brille, Bart, dunklem Pulli; Bertrand als Schimpanse mit Sonnenbrille und schwarzem Hoodie (Aufdruck „KI“). Filmkorn, Vignette, Iris-Blenden. Bertrand verkörpert die KI (siehe creative-director, Nebencharakter).
Musik: „Upbeat Jazz“ (Mixkit, Stock Music Free License) ab 20,271 s; Geräusche (Pop, Boing, Ding, Pfeife) selbst synthetisiert (`sfx/`).

| Zeit | Szene |
|---|---|
| 0–3,2 s | Titelkarte: „Flow Media AI zeigt MAIK & BERTRAND in: ‚Die Website‘“ |
| 3,2–9 s | Maik verzweifelt, Zettel fliegen, Kalender blättert bis November, Laptop „Fehler 404“ – „Meine Website ist seit 3 Monaten ‚fast fertig‘ …“ / „Wo fang ich nur an?!“ |
| 9–14,5 s | Bertrand rutscht rein, Brille runter: „Gib mal her.“ – „Du bist ein AFFE!“ – „Ich bin die KI.“ |
| 14,5–21,5 s | Fotos · Videos · Texte fliegen in den Laptop, „Bau meine Website“, Website-Skill baut 5 Versionen – „Fünf Versionen. Du suchst aus.“ |
| 21,5–26,5 s | Maik nimmt ausgerechnet BANANA.COM – Bertrand: „Ernsthaft? Die Bananen-Version?“ – Seite geht LIVE, Konfetti – „Die ist ja LIVE?!“ |
| 26,5–32,6 s | Schild fällt: Workshop · Deine Website · Morgen 18 Uhr · live · auch Di 10.11. · Website-Skill gratis – „Ich bin dabei!“ – „Ich weiß.“ |
| 32,6–36 s | Endkarte: Bis morgen, 18 Uhr! · Schreib mir „WORKSHOP“ |

Bauen: `node frames.js $PWD` → ffmpeg-Mix (Musik + `sfx/` mit adelay, loudnorm −14 LUFS) → komprimieren (crf 27, tune grain). Higgsfield hatte 0 Credits, darum komplett selbst gezeichnet.

## Caption
```
Maik vs. Bertrand. Rate mal, wer von uns die Website gebaut hat. 🐒

Bertrand ist unsere KI. Er nimmt deinen Content – Fotos, Videos, Texte – und baut daraus mit dem Website-Skill fünf Versionen. Du suchst aus (bitte nicht die Bananen-Version), und am Ende ist deine Seite live.

Genau das machen wir morgen im Workshop „Mit KI zur Personal Brand: Deine Website“:
📅 Montag, 09.11. oder Dienstag, 10.11. · 18–19 Uhr · live
🎁 Den Website-Skill bekommst du als Teilnehmer kostenlos.
🛠️ Bis 31.12.26 Tech-Support im Tech-Support-Channel.

Platz sichern: Schreib mir „WORKSHOP“ per DM.

#PersonalBrand #Website #KI #Comic #FlowMediaAI
```
Grund zum Senden: „Schick das jemandem, der seine Website seit Monaten ‚fast fertig‘ hat.“
Posten: heute (So 08.11.) 19–21 Uhr oder Mo 09.11. morgens; Mo als Story mit Countdown 18:00. Drive-Ordner: `01_Marketing/Content/Workshops`.
