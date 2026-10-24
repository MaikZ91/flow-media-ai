# R011 · „Erste Aufträge – vor dem ersten Coaching-Tag“

Stand: 24.10.2026 · Format: Reel 1080×1920, 38 s · Status: **fertig (`R011.mp4`), postbereit** · Quelle: Maiks Selfie-Rohvideo (Drive `01_Marketing/RAW`, 95 s, 480×854 HLG)

Säule: `weg` (Build in public) · **Test-Variable:** `format = selfie-schnitt` (erstes Reel aus echtem Rohvideo von Maik)

## Idee
Maik erzählt ehrlich, dass er schon die ersten Aufträge hat, bevor sein Business-Coaching am 2. November überhaupt anfängt – nur weil er mit vielen Leuten über sein Vorhaben gesprochen hat. Botschaft an alle, die sich selbstständig machen wollen: „Tragt eure Message nach draußen.“ Am Ende Einladung zum Workshop am Montag.

## Schnitt
- Der stärkste Satz („habe ich jetzt auch schon die ersten Aufträge, bevor überhaupt das Coaching angefangen hat“) ist als Cold Open nach vorn gezogen; danach chronologisch.
- 95 s → 38 s: Begrüßung, Versprecher, Pausen und Wiederholungen raus; 18 Schnitte, Jump-Cuts mit wechselndem Punch-in (100–122 %), damit es alle 2–3 s einen Bildwechsel gibt.
- HLG-HDR des iPhones auf SDR gemappt, s/w nach `flow-design`, weiche Abdunklung oben/unten für die Lesbarkeit.
- Untertitel Wort für Wort (Oswald, Versalien, Schlüsselwörter blau) per Spracherkennung, von Hand korrigiert.
- Hook-Text oben (0–3,9 s): ERSTE AUFTRÄGE – VOR DEM ERSTEN **COACHING-TAG.** · Workshop-Karte ab 30 s: Digitaler Stammtisch #1 · Mo 26.10. · 18 Uhr – MIT KI ZUR **PERSONAL BRAND.** 15 € · live · Link in Bio
- Ton: Stimme gesäubert (Hochpass, Entrauschen, EQ, Kompressor, −15 LUFS), Musikbett leise darunter und unter der Stimme abgesenkt: „Uplifting Bass“ (Mixkit, Stock Music Free License).

## Caption (zum Kopieren)
Ehrlich gesagt: Damit hab ich nicht gerechnet.

Am 2. November startet mein Business-Coaching. Und ich hab jetzt schon die ersten Aufträge – einfach, weil ich mit vielen Leuten darüber gesprochen habe, was ich vorhabe.

Monatelang war es schwierig, an Kunden zu kommen. Was sich geändert hat: Ich rede darüber.

Wenn du dich selbstständig machen willst: Erzähl Leuten, was du kannst und was du anbietest. Nicht erst, wenn alles perfekt ist.

Und wenn du lernen willst, wie du dafür mit KI eine Personal Brand aufbaust: Montag, 18 Uhr, digitaler Stammtisch. Link in Bio.

#Selbstständig #Gründer #BuildInPublic #PersonalBrand #FlowMediaAI

**Grund zum Senden:** „Schick das jemandem, der sich selbstständig machen will, aber noch keinem davon erzählt hat.“ (erster Kommentar)
**Posten:** So 25.10., 18–20 Uhr (letzter Abend vor dem Workshop). R010 dann am Mo früh oder als Story.

## Checkliste
Teil C §5: Maik im ersten Frame, Bewegung ✓ · Hook-Text ≤ 1 s lesbar ✓ · 38 s – länger als 30 s, aber reiner Selfie-Talk mit Story-Bogen ✓ · Schnitt alle 2–3 s ✓ · Grund zum Senden ✓ · Text oben/unten in sicherer Zone ✓ · nichts erfunden: alle Aussagen von Maik selbst im Video ✓
`flow-design` §9: s/w, Oswald/Montserrat/Inter, ein Blau ✓
Hinweis: Das Rohvideo kam nur in 480×854 an – mit der Originaldatei in voller Auflösung wird das Bild deutlich schärfer (`build.py` einfach neu laufen lassen).

## Neu bauen
Rohvideo laden (Drive `RAW`, per Link freigegeben) → Abschrift mit Wortzeiten (`faster-whisper small`, `words.json`) → `python3 build.py <raw.mov> <words.json>`. Schnittliste `SEG` in `build.py`.
