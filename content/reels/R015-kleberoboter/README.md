# R015 · „Build your own Kleberoboter für 420 €“

Stand: 25.10.2026 · Format: Reel 1080×1920, 27,5 s · Status: **fertig (`R015.mp4`)**

Säule: `engineering` / `ki` · **Test-Variable:** `format = 3d-animation` (erstes Reel als reine 3D-/CAD-Animation)

## Idee (Maik, 25.10.2026)
Low-Budget-Kleberoboter zum Nachbauen: Ein normaler Maker-3D-Drucker (z. B. Anycubic) druckt sich die Halterung für einen Dosierkopf selbst, dann kommen Mechanik und Spritze mit Kleber drauf, und Claude Code schreibt den Fahrweg (G-Code). Kosten laut Maik: ~400 € Hardware + ~20 €/Monat Claude Code.
**Bewusst ohne Bezug zu Maiks Arbeit:** keine Firma, keine Küvetten, keine Messtechnik aus dem Job – als Anwendung eine typische Maker-Aufgabe: eine Dichtraupe um einen 3D-gedruckten Gehäusedeckel (z. B. für ein ESP32-Projekt).

## Umsetzung
Komplett in 3D gebaut und gerendert (three.js, physikalisch basiertes Licht, Schatten): kartesischer Bed-Slinger mit 2040-Alu-Profilen, Z-Spindeln, X-Portal, Schlitten mit Lüfter, Filament-Spule; gedruckte Halterung in Flow-Blau (einziger Akzent), Spritze transparent mit bernsteinfarbenem Kleber, Edelstahl-Nadel. Kein Markenlogo am Drucker.

| Beats | Zeit | Bild | Text |
|---|---|---|---|
| 0–6 | 0–3,3 s | fertiger Roboter zieht die Raupe | Build your own – KLEBEROBOTER FÜR **420 €?** |
| 6–14 | 3,3–7,7 s | Drucker setzt sich aus Einzelteilen zusammen | 01 · Die Basis – EIN 3D-DRUCKER. |
| 14–21 | 7,7–11,6 s | Drucker druckt die blaue Halterung Schicht für Schicht | 02 · Drucken – ER DRUCKT SEIN **EIGENES TEIL.** |
| 21–27 | 11,6–14,9 s | Hotend raus, Halterung + Spritze rein | 03 · Umbauen – DOSIERKOPF DRAUF. |
| 27–35 | 14,9–19,3 s | Draufsicht, blauer Pfad entsteht, Terminal mit Claude-Code-Prompt und G-Code | 04 · Steuern – CLAUDE CODE **SCHREIBT DEN PFAD.** |
| 35–42 | 19,3–23,1 s | Nadel fährt, Klebe-Raupe wächst um den Deckel | 05 · Kleben – EINE RAUPE. **AUF DEN MILLIMETER.** |
| 42–50 | 23,1–27,5 s | Totale + Kostenkarte | DEIN **KLEBEROBOTER.** · 3D-Drucker + Teile ~400 € · Claude Code ~20 €/Monat |

Maik als Kreis unten links (in der Terminal-Szene ausgeblendet). Musik: **„Pop Track 03“ – Mixkit, Stock Music Free License** (`content/musik/frei/pop-track-03.mp3`), ab 8,89 s.

## Caption (zum Kopieren)
Kleberoboter für 420 €? Geht.

Du brauchst:
1️⃣ einen 3D-Drucker (ein ganz normaler Maker-Drucker reicht)
2️⃣ der druckt dir die Halterung für den Dosierkopf
3️⃣ Mechanik + Spritze mit Kleber drauf
4️⃣ Claude Code schreibt dir den Fahrweg – du beschreibst nur, was geklebt werden soll
5️⃣ los geht's: eine saubere Raupe, auf den Millimeter

Hardware ca. 400 €, Claude Code ca. 20 € im Monat. Die Animation zeigt das Prinzip – ich hab so einen schon gebaut und es funktioniert erstaunlich gut.

Was würdest du damit kleben? 👇

#3DDruck #Maker #Automatisierung #ClaudeCode #FlowMediaAI

**Grund zum Senden:** „Schick das jemandem, der einen 3D-Drucker hat und ihn nur für Figuren benutzt.“
**Posten:** Mi 28.10. oder Fr 30.10., 18–20 Uhr (zwischen den Robotik-Teilen R012–R014 passt es gut).

## Checkliste
Teil C §5: Bewegung ab Bild 1 + Maik als Kreis ab 0,6 s ✓ · Hook als Frage mit Preis ✓ · 27,5 s (Demo ≤ 30 s, jede Szene ein Schritt) ✓ · Szenenwechsel alle 3–4 s ✓ · Grund zum Senden ✓ · Text oben, Kreis links ✓ · nichts erfunden: Kosten von Maik, als „ca.“ markiert; Animation als Prinzip gekennzeichnet ✓ · **kein Arbeitgeber-Bezug** (keine Firma, kein Produkt, keine Abläufe aus dem Job) ✓
`flow-design` §9: dunkel/neutral, ein Blau (gedruckte Teile + Pfad), Oswald/Montserrat/Inter ✓

## Neu bauen
Ordner per `python3 -m http.server 8771` ausliefern → `node render.js` (Playwright, WebGL/SwiftShader, ~15 Min.) → Ton: `ffmpeg -i video_only.mp4 -ss 8.89 -i ../../musik/frei/pop-track-03.mp3 -t 27.52 …` (siehe Verlauf). three.js 0.160 liegt lokal in `three/`.
