# R002 · „Mein komplettes Firmen-Tool. An einem Tag gebaut.“

Stand: 19.10.2026 · Format: Reel 1080×1920, 28 s · Vorschau (Platzhalter statt Avatar): `flow_reel_board_vorschau.mp4`

## Konzept
Maik (als HeyGen-Avatar mit seiner eigenen Stimme) erzählt, was das Flow Board kann; daneben laufen echte Bildschirmaufnahmen. Avatar groß im Hook und am Ende, dazwischen als runde Blase unten links.

## Vertonungsskript (für HeyGen, ca. 28 s)

| Zeit | Gesprochen | Bild / Text im Bild |
|---|---|---|
| 0–3 s | Mein komplettes Firmen-Tool. An einem Tag gebaut. Mit KI. | Avatar groß, Ansichten flackern · „Mein komplettes Firmen-Tool.“ + „An einem Tag gebaut. Mit KI.“ |
| 3–6 s | Alle Aufgaben auf einem Board, sortiert nach Priorität. | Board → Prioritäten-Matrix · „Alle Aufgaben. Nach Priorität.“ |
| 6–10 s | Mein Kalender: Termine schieb ich einfach mit der Maus rum, wie in Outlook. | Termin wird gezogen · „Termine ziehen wie in Outlook.“ |
| 10–15 s | Buchhaltung ist gleich mit drin: Einnahmen, Ausgaben, Belege und was ich für Steuern zurücklegen muss. | Finanzen · „Buchhaltung gleich mit drin.“ · Beispieldaten |
| 15–17,5 s | Rechnungen? Ein Klick, fertig als PDF. | Rechnung · „Rechnung? Ein Klick. PDF.“ · Beispieldaten |
| 17,5–20,5 s | Dazu meine neue Landingpage … | Landingpage scrollt · „Meine neue Landingpage.“ |
| 20,5–23 s | … und im Board seh ich direkt, wie viele vorbeischauen. | Auswertung · „Besucher live im Board.“ |
| 23–25 s | Ein Tool statt fünf Apps. Genau so, wie ich arbeite. | Raster aller Ansichten · „Ein Tool statt fünf Apps.“ |
| 25–28 s | Schick das jemandem, der seine Rechnungen noch in Word schreibt. | Avatar groß · Text wie gesprochen → Übergang in Bild 1 (Loop) |

**Zum Kopieren in HeyGen (ohne Zeiten):**

> Mein komplettes Firmen-Tool. An einem Tag gebaut. Mit KI.
> Alle Aufgaben auf einem Board, sortiert nach Priorität.
> Mein Kalender: Termine schieb ich einfach mit der Maus rum, wie in Outlook.
> Buchhaltung ist gleich mit drin: Einnahmen, Ausgaben, Belege und was ich für Steuern zurücklegen muss.
> Rechnungen? Ein Klick, fertig als PDF.
> Dazu meine neue Landingpage, und im Board seh ich direkt, wie viele vorbeischauen.
> Ein Tool statt fünf Apps. Genau so, wie ich arbeite.
> Schick das jemandem, der seine Rechnungen noch in Word schreibt.

## HeyGen
- **Stimme:** Regel aus dem Creative Director: keine Computerstimme als Maik. Darum das Skript selbst als Sprachmemo einsprechen und in HeyGen als Audio hochladen („Upload audio“); der Avatar spricht dann lippensynchron mit Maiks echter Stimme.
- **Format:** 9:16 (1080×1920), Avatar mittig, Kopf und Schultern, ruhiger heller Hintergrund. Untertitel in HeyGen aus (die Texte sind schon im Reel).
- **Export:** MP4, dann hier ablegen; neu rendern mit `python3 render_reel.py <arbeitsordner> R002.mp4 <avatar.mp4>`. Die Szenenzeiten in `SCENES` an die echte Länge der Aufnahme anpassen.

## Fakten-Check
- „An einem Tag gebaut“: erste Board-Version am 19.10.2026 um 10:08, Landingpage um 12:04, Stand im Reel um 14:08 (git log). „In einer Stunde“ wäre falsch und steht deshalb nicht drin.
- Finanzen und Rechnung zeigen **Beispieldaten** (Beispiel GmbH, Beispielstraße), im Bild markiert. Keine echten Buchungen, keine Kundendaten.
- Board-Karten sind die Beispielkarten der Demo; Tagesmottos (Ordnung & Klarheit, Health, Social) sind Maiks echte.
- Auswertung: echte Zahlen aus PostHog (Stand 19.10.2026: 4 Besuche). Der Sprechtext nennt keine Zahl.
- Keine Schlüssel, Links mit `#k=` oder Mailadressen im Bild.
- Test-Variable: `opener = avatar` (Mensch im ersten Frame, als KI-Avatar mit eigener Stimme) – Vergleich mit R001 (`screen-montage`).

## Caption (Vorschlag)
Ich hab mir heute mein eigenes Firmen-Tool gebaut. An einem Tag, mit KI.

Aufgaben, Kalender, Buchhaltung, Rechnungen, Landingpage und die Zahlen dazu. Alles an einem Ort, genau so, wie ich arbeite.

Kein Entwicklerteam, kein Abo-Zoo. Nicht perfekt, aber es läuft, und ich nutz es ab jetzt jeden Tag.

Was würdest du in so ein Tool als Erstes einbauen?

## Musik
„Motivating Mornings“ (Mixkit Stock Music Free License, kommerziell ohne Namensnennung), ab 0:11,5; mit Avatar-Stimme leise darunter.

## Neu rendern
1. `node shoot.js <ordner>/shots <board-key-datei>` (Playwright; Board mit Beispielkarten, Landingpage, Auswertung)
2. Schriften (Bricolage Grotesque ExtraBold, IBM Plex Sans SemiBold, WOFF von Google Fonts) nach `<ordner>/fonts/` als `bri800.woff`, `plex600.woff`
3. `python3 render_reel.py <ordner> R002.mp4 [avatar.mp4]`
