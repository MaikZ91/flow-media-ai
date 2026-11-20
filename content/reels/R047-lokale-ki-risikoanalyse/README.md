# R047 · Lokale KI: Risikoanalyse in Echtzeit (Tool-Reel, 44 s, weiß)

Säule `ki` / `tools` · Problem-Säule `zeit` · Formel Problem → Aha → Lösung.
Aus Maiks Selfie-Video (60 s → 44 s, Ähms und Denkpausen raus) mit dem Video Cutter v2 im neuen **Layout „Kreis + Bühne“**: weißer Hintergrund, Maik als Kreis unten links, darüber eine animierte Tool-Bühne (`buehne.html`), die die Anwendung in Echtzeit zeigt – synchron zum gesprochenen Wort.
Musik: „Digital Clouds“ (Mixkit, Stock Music Free License), leise. Test-Variable: `format = tool-kreis-weiss`.

**Arbeitgeber-Erwähnung von Maik freigegeben (20.11.2026):** Im Video sagt Maik „auf Arbeit“ und „Medical-Bereich“. Die Tool-Demo zeigt trotzdem nur ein frei erfundenes Beispiel (Anleitung „Espressomaschine entkalken“, erfundene Werte, im Bild gekennzeichnet) – keine Daten, Abläufe oder Software aus dem Job.

| Zeit | Gesprochen | Bühne | Einblendung |
|---|---|---|---|
| 0–4,5 s | „Hallo zusammen. Wir haben auf Arbeit einen lokalen KI-Rechner.“ | KI-Rechner fährt hoch, „läuft offline · 0 Byte nach draußen“ | Hook „Lokale KI. Echter Use Case.“ |
| 4,5–11 s | „… Medical-Bereich … Datenschutz sehr wichtig … lokale KI hilft“ | Dokumente prallen an der Cloud ab, landen im Haus | „Datenschutz zuerst.“ |
| 11–15,8 s | „… Prozess-Risiko-Analysen kennt. So PFMEAs.“ | PFMEA kurz erklärt: B × A × E = RPZ | – |
| 15,8–25 s | „aus Anleitungen die Prozessschritte rauslesen und die Risiken bewerten“ | **Tool live:** Anleitung rein → Scan → 5 Schritte → Risikotabelle füllt sich → nach RPZ sortiert | „Anleitung rein.“ · „Risiken bewertet.“ |
| 25–33 s | „… Meeting … drei Stunden … Bewertungsstufen“ | Meeting-Uhr läuft auf 3 Stunden, Sprechblasen „6!“, „Nein, 7!“ | „3 Stunden Meeting“ |
| 33–41,5 s | „super aufwendig … mit KI … ausgefüllten Tabelle reingehen“ | Export Risikoanalyse.xlsx → „Mit fertiger Tabelle ins Meeting“ | „Fertige Tabelle“ |
| 41,5–44 s | „super geiler Use Case, um Zeit zu sparen“ | „Weniger diskutieren. Mehr Zeit.“ | – |

## Caption
```
Lokale KI. Echter Use Case. 👇

Bei mir auf Arbeit steht jetzt ein lokaler KI-Rechner. Im Medical-Bereich ist Datenschutz alles – mit lokaler KI bleiben die Daten im Haus.

Der Use Case: Prozess-Risikoanalysen (PFMEA).
Statt drei Stunden im Meeting über Bewertungsstufen zu diskutieren:
📄 Anleitung rein
🔍 KI liest die einzelnen Prozessschritte raus
📊 und bewertet die Risiken – fertige Tabelle

Dann geht man mit einer ausgefüllten Tabelle ins Meeting und diskutiert nur noch, was wirklich zählt.

Welcher Prozess frisst bei dir am meisten Zeit? 👇

(Die Demo im Video zeigt ein erfundenes Beispiel.)

#LokaleKI #KI #Datenschutz #FMEA #FlowMediaAI
```
Grund zum Senden: „Schick das jemandem, der gerade wieder in einem 3-Stunden-Meeting sitzt.“
Posten: Mo–Mi 18–20 Uhr.

## Checkliste
Mensch im ersten Bild (Kreis) + Bewegung ✓ · Hook ≤ 1 s lesbar ✓ · neue Szene alle 3–8 s, Animation dauernd in Bewegung ✓ · Untertitel ✓ · unten 18 % bis auf den Kreis frei ✓ · Demo frei erfunden und gekennzeichnet ✓ · keine echten Firmendaten ✓ · Frage am Ende (Caption) ✓

## Neu bauen
Video Cutter aus Drive (`07_KI/skills/flow-dna-premium/video-cutting/`, Stand 20.11.2026 mit Layout „Kreis + Bühne“) nach `.videocutter/`, Rohvideo als `raw.mov`, dann `cutter.py analyse raw.mov`, `cuts.json` und `plan.json` aus diesem Ordner nach `raw_schnitt/`, `cutter.py zeiten raw.mov`, `cutter.py bauen raw.mov` (Bühne: `buehne.html` liegt neben `raw.mov`).
