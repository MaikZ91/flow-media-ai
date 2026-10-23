# R006 · „Meine neue Website. Komplett mit KI.“

Stand: 23.10.2026 · Format: Reel 1080×1920, 28,6 s · Status: **fertig (`R006.mp4`), postbereit**

Säule: `web` / `design` (Skill `content-themen`) · **Test-Variable:** `format = website-tour` (echte Bildschirmaufnahme der eigenen Seite im Handy-Rahmen, Maik als Rahmen vorn und hinten)

## Konzept
Build in public: Maik zeigt seine neue Website – live aufgenommen von maikz91.github.io/flow-media-ai, so wie sie jeder am Handy sieht. Gebaut heute mit KI (Claude) nach seinen Vorgaben und seinem Design-Skill. Alles im Bild ist echt: fließende Linien, das Manifest, die Werte-Szene Build · Connect · Enable, die Community-Karte, das Flow Board als Live-Demo und der „Frag Maik“-Kontakt. Keine Zeitangabe zur Bauzeit im Reel (nicht behaupten, was nicht gemessen ist).

## Ablauf
| Zeit | Szene | Text im Bild |
|---|---|---|
| 0–2,6 s | Hook: Maik frontal, langsamer Zoom | BUILD IN PUBLIC · MEINE NEUE WEBSITE. **KOMPLETT MIT KI.** |
| 2,6–6,5 s | Handy: Startseite mit fließenden Linien | 01 · Der Einstieg – ALLES IST **IM FLOW.** |
| 6,5–10,4 s | Manifest leuchtet Wort für Wort | 02 · Meine Haltung – WORT FÜR WORT **BEIM SCROLLEN.** |
| 10,4–18,4 s | Werte-Szene: Handy baut sich, Netzwerk um Maik, Lernkurve | 03 · Meine Werte – BUILD. CONNECT. **ENABLE.** |
| 18,4–21,2 s | Community-Karte | 04 · Angebote – COMMUNITY **ALS EINSTIEG.** |
| 21,2–23,5 s | Flow Board mit „Live ausprobieren“ | 05 · Mein Tool – LIVE ZUM **AUSPROBIEREN.** |
| 23,5–25 s | „Frag Maik“ öffnet sich | 06 · Kontakt – FRAG MAIK – **PER WHATSAPP.** |
| 25–28,6 s | CTA: Maik frontal (Loop zu Bild 1) | WILLST DU AUCH SO EINE **SEITE?** Schreib mir. |

Maik ist in jeder Szene (groß vorn/hinten, Kreis oben rechts während der Tour, dazu auf der Website selbst). Musik: „Motivating Mornings“ (Mixkit Stock Music Free License), ab 0:38, leise.

## Caption (zum Kopieren)
Meine neue Website. Komplett mit KI gebaut.

Ich wollte keine Seite, die aussieht wie jede andere. Sondern eine, die sich anfühlt wie mein Name: im Flow.

Drin steckt alles, was mir wichtig ist:
→ Build. Connect. Enable. – meine Werte, animiert beim Scrollen
→ die kostenlose Flow Business Community als Einstieg
→ der Workshop am Montag mit Countdown
→ mein Flow Board zum direkt Ausprobieren
→ und ein Klick, um mich per WhatsApp zu erreichen

Gebaut mit Claude und meinem eigenen Design-Skill – damit alles genauso aussieht wie meine Posts.

Willst du auch so eine Seite? Schreib mir.

#KI #Webdesign #Website #BuildInPublic #FlowMediaAI

**Grund zum Senden:** „Schick das jemandem, dessen Website noch von 2015 ist.“ (als erster Kommentar)
**Posten:** heute oder morgen, 18–20 Uhr. Cover = erstes Bild. Website-Link in die Bio bzw. als Link-Sticker in die Story.

## Sprechtext (optional, ca. 25 s)
> Meine neue Website – komplett mit KI gebaut.
> Alles ist im Flow: Linien, die sich bewegen, meine Haltung Wort für Wort.
> Meine Werte – Build, Connect, Enable – laufen beim Scrollen ab.
> Die Community ist der Einstieg, mein Tool kann man direkt ausprobieren.
> Und mit einem Klick schreibst du mir auf WhatsApp.
> Willst du auch so eine Seite? Schreib mir.

## Checkliste
Teil C §5: 1. Mensch im ersten Frame (Maik, Zoom) ✓ 2. Hook ab Bild 1 lesbar ✓ 3. 28,6 s – Demo, jede Szene zeigt etwas Neues ✓ 4. Interrupts: neue Überschrift alle 2–4 s, Animationen im Handy ✓ 5. Loop: Ende Maik frontal → Anfang ✓ 6. Grund zum Senden ✓ 7. Texte oben bzw. über 80 %-Linie ✓ 8. Echte Aufnahme der eigenen Seite, keine fremden Daten ✓ 9. Klingt nach Maik ✓
`flow-design` §9: Schwarz/Weiß + Blau ✓ · Maik in jeder Szene ✓ · neue Wortmarke (Logo) ✓

## Neu rendern
1. `node rec.js site.webm` – nimmt die Live-Website Bild für Bild auf (Playwright-Clock, 390×844 @2x, 22,4 s). `site.webm` liegt wegen der Größe nicht im Repo.
2. `node frames.js <ordner>` → `video_only.mp4`
3. `ffmpeg -i video_only.mp4 -ss 38 -i motivating-mornings.mp3 -t 28.6 -filter_complex "[1:a]volume=0.55,afade=t=in:d=0.4,afade=t=out:st=27.2:d=1.4[a]" -map 0:v -map "[a]" -c:v libx264 -crf 23 -pix_fmt yuv420p -c:a aac -movflags +faststart R006.mp4`
