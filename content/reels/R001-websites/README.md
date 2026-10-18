# R001 · „Alle diese Seiten hab ich gebaut.“

Stand: 18.10.2026 · Format: Reel 1080×1920, 15,5 s · Datei: `flow_reel_websites.mp4`

## Konzept
Montage aus Maiks eigenen Websites (THE TRIBE, Event-Seiten, App, MZ.9, Tool-Sammlung), immer schneller geschnitten, dann Raster aller Seiten als Auflösung.

| Zeit | Bild | Text |
|---|---|---|
| 0–2 s | Seiten flackern im 0,25-s-Takt | „Alle diese Seiten hab ich gebaut.“ · „Allein. Mit KI.“ |
| 2–10 s | Scroll durch 13 Seiten, Tempo steigt (1,1 s → 0,3 s) | „Ohne Agentur. Ohne Dev-Team.“ · „Idee rein. Seite raus.“ · Labels je Seitentyp |
| 10–13 s | Raster mit 12 Seiten, Zoom raus | „30+ Seiten. 1 Person.“ · „Apps · Websites · Tools“ |
| 13–15,5 s | Raster unscharf | „Wie das geht? Zeig ich hier.“ · „Folg @flow.media.ai“ → Übergang in Bild 1 (Loop) |

Musik: „Take This Higher“ (Mixkit Stock Music Free License, kommerziell ohne Namensnennung), ab 0:08.

## Fakten-Check
- „30+ Seiten“: in `the-tribe-bot/docs` liegen ~39 eigene Seiten (ohne Impressum/Datenschutz/Hilfsseiten, ohne die Lead-Konzeptseiten). Stimmt.
- Gezeigt werden nur eigene Seiten. Die Lead-Konzeptseiten sind nicht drin (siehe unten).
- Test-Variable: `opener = screen-montage` (kein Gesicht im ersten Frame) – Vergleich mit späteren Reels mit Maik im Bild.

## Caption (Vorschlag)
Alle diese Seiten hab ich selbst gebaut. Mit KI, ohne Agentur, ohne Entwicklerteam.

Eine Ausgeh-App, Event-Seiten mit Ticketverkauf, eine Agentur-Website, eine Sammlung kostenloser Tools für kleine Betriebe.

Nicht alles davon ist perfekt. Aber alles davon ist live.

Ich zeig hier, wie so was entsteht – mit allem, was klappt und was nicht.

Welche Seite soll ich als Nächstes auseinandernehmen?

## Optional besser
Ein 1,5-s-Selfie-Hook von Maik davor („Das hier hab ich alles allein gebaut.“) erfüllt die Regel „Mensch im ersten Frame“ und macht es persönlicher.

## Neu rendern
`shoot.js` (Playwright, Screenshots von `the-tribe-bot/docs` über `python3 -m http.server 8765`) → `render_reel.py <ordner mit shots/>`.
