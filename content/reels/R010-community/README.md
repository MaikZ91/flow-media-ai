# R010 · Community-Reel „Gründer. Selbstständige. Macher.“

Stand: 24.10.2026 (Version 2 – v1 „Der Kreis ist offen“ verworfen: Kreis zu lange im Vordergrund, Community erst spät sichtbar, Tonqualität schlecht) · Format: Reel 1080×1920, 19,7 s (funktioniert auch als Story) · Status: **fertig (`R010.mp4`), postbereit**

Säule: `weg` / `design` (Community-Reihe) · Anlass: Werbung für die kostenlose Flow Business Community (WhatsApp) · **Test-Variable:** `hook = community-bild`, `musik = frei`

## Idee
Die Community steht von Bild 1 an im Vordergrund: Menschen am Tisch aus Maiks Community-Plakat, dazu die Zielgruppe auf den Beat. Danach die drei Themen des Plakats, Maik, der Netzwerk-Effekt der Website (der blaue Kreis ist dort nur noch ein Rahmen, der sich in einem Beat zeichnet), die Orte und zum Schluss das ganze Plakat mit „Jetzt dabei sein“.

## Ablauf (Schnitt auf „Uplifting Bass“, 1 Beat = 0,448 s)
| Beats | Zeit | Bild | Text |
|---|---|---|---|
| 0–6 | 0–2,7 s | Menschen am Tisch (Plakat) | Flow Business Community · kostenlos – GRÜNDER. SELBSTSTÄNDIGE. **MACHER.** |
| 6–14 | 2,7–6,3 s | drei Themen-Karten | Business & Marketing · KI & digitale Tools · Austausch & **Umsetzung** – EIN ORT FÜR **ALLE DREI.** |
| 14–20 | 6,3–9 s | Maik frontal | Ich bin Maik – ICH BRINGE LEUTE ZUSAMMEN, DIE **MACHEN.** |
| 20–30 | 9–13,4 s | Netzwerk: Maik in der Mitte, Menschen kommen dazu | IDEEN TEILEN. FEEDBACK BEKOMMEN. **GEMEINSAM MACHEN.** |
| 30–36 | 13,4–16,1 s | Stadtbild (Plakat) | Treffen & Austausch – BIELEFELD. MÜNSTER. **DIGITAL.** |
| 36–44 | 16,1–19,7 s | das Community-Plakat | JETZT **DABEI SEIN.** Kostenlos · WhatsApp-Community · Link in Bio |

Bilder: `marketing/landing-page/img/community.jpg` (Maiks Plakat, Ausschnitte hochskaliert), `board.jpg` (Flow Board), `portrait_front.jpg`.
Musik: **„Uplifting Bass“ – Mixkit, Stock Music Free License** (`content/musik/frei/uplifting-bass.mp3`, 320 kbps), ab 14,42 s (direkt nach dem Drop).

## Caption (zum Kopieren)
Gründer, Selbstständige, Macher: Ihr müsst das nicht allein machen.

In der Flow Business Community geht's um Business & Marketing, KI & digitale Tools – und vor allem um Austausch und Umsetzung.

→ Ideen teilen
→ Feedback bekommen
→ gemeinsam ins Machen kommen

Kostenlos, in Bielefeld, Münster und digital. Der Link zur WhatsApp-Community ist in meiner Bio – oder schreib mir einfach „Community“.

#Community #Gründer #Selbstständig #KI #FlowMediaAI

**Grund zum Senden:** „Schick das jemandem, der gerade allein an seinem Projekt sitzt.“ (erster Kommentar)
**Posten:** So oder Mo, nicht am selben Tag wie R009. Gut auch als Story mit Link-Sticker zur Community.

## Checkliste
Teil C §5: Menschen im ersten Frame ✓ · Hook ab Bild 1 (Zielgruppe direkt angesprochen) ✓ · ~20 s, Schnitt auf jeden Beat ✓ · Loop (Plakat am Ende enthält das Bild vom Anfang) ✓ · Grund zum Senden ✓ · Text unten, unterer Rand frei ✓ · nichts erfunden (keine Mitgliederzahlen; alle Angaben vom Plakat/der Website) ✓
`flow-design` §9: schwarz-weiß + ein Blau, Oswald/Montserrat/Inter ✓ · Maik in Szene 3, im Netzwerk und auf dem Plakat ✓

## Neu rendern
`node frames.js <ordner>` → `video_only.mp4`, dann
`ffmpeg -i video_only.mp4 -ss 14.42 -i ../../musik/frei/uplifting-bass.mp3 -t 19.70 -filter_complex "[1:a]afade=t=out:st=18.6:d=1.1,aresample=48000[a]" -map 0:v -map "[a]" -c:v libx264 -crf 22 -c:a aac -b:a 256k -movflags +faststart R010.mp4`
