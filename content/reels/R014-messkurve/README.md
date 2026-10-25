# R014 · „So sieht Zugkraft aus“ – die Messkurve live

Stand: 25.10.2026 · Format: Reel 1080×1920, 18,3 s · Status: **Version 1 fertig (`R014.mp4`)** – Reihe „Robotik aus dem Studium“ (R012–R014), Avatar-Video kann später ergänzt werden

Säule: `engineering` (Maiks eigenes Studienprojekt, kein Arbeitgeber-Material) · **Test-Variable:** `format = screen-cards`

## Idee
Teil 3 der Reihe: die Daten hinter dem Roboter. Bildschirmaufnahme der Messsoftware (LabVIEW, Fenster „Zugversuch 2.0“, 26.06.2017): links die Kraftkurve live, rechts die Kamera auf das Netz, während der Roboter zieht. Brücke zu heute: aus Daten Antworten machen – mit KI.

Material: Video von Maiks Portfolio-Seite (Galerie „Projektarbeit als SHK – robotergesteuerter Teststand zur Zugkraftmessung von chirurgischen Meshes“), 60 s, 1080p. Weil ein Hochformat-Ausschnitt den Bildschirm zu unscharf machen würde, laufen Kurve und Kamera als Querformat-Karten auf weichgezeichnetem Hintergrund.

## Ablauf (4 Szenen à 8 Beats, „Close Up“, 1 Beat = 0,572 s)
| Zeit | Bild | Text |
|---|---|---|
| 0–4,6 s | ganzer Bildschirm (Kurve + Kamera) | Studienprojekt · Messtechnik – SO SIEHT **ZUGKRAFT AUS.** |
| 4,6–9,1 s | Kraftkurve | Die Kurve – KRAFT. **LIVE GEMESSEN.** · Messsoftware · LabVIEW |
| 9,1–13,7 s | Kamera: Netz unter Zug | Die Kamera – DAS NETZ. **UNTER ZUG.** · Roboter zieht, Software zeichnet auf. |
| 13,7–18,3 s | ganzer Bildschirm | Und heute – AUS DATEN WERDEN **ANTWORTEN. MIT KI.** · Flow Media AI · Build. Connect. Enable. |

Maik als Kreis unten links. Musik: **„Close Up“ – Mixkit, Stock Music Free License** (`content/musik/frei/close-up.mp3`), ab 17,27 s.

## Caption (zum Kopieren)
So sieht Zugkraft aus.

Links die Kurve, live gemessen. Rechts die Kamera auf das OP-Netz, während der Roboter zieht. Das ist mein Teststand aus dem Studium – 2017, Messsoftware in LabVIEW.

Damals hab ich gelernt: Spannend wird's erst, wenn aus Daten Antworten werden.

Heute mach ich genau das mit KI – Daten auswerten, Abläufe automatisieren, Tools bauen.

Welche Daten liegen bei dir rum, die eigentlich jemand auswerten müsste? 👇

#Messtechnik #Automatisierung #Daten #KI #FlowMediaAI

**Grund zum Senden:** „Schick das jemandem, der auch schon mal stundenlang Messkurven ausgewertet hat.“
**Posten:** nach R013 (Teil 2), z. B. Sa 31.10., 18–20 Uhr.

## Checkliste
Teil C §5: Bewegung ab Bild 1 (Live-Kurve, Kamera) + Maik als Kreis ✓ · Hook ≤ 1 s ✓ · 18,3 s ✓ · Szenenwechsel alle 4,6 s ✓ · Grund zum Senden ✓ · Text oben, Karten in der Mitte, Kreis links ✓ · nichts erfunden: Software/Datum aus dem Video (Fenstertitel, Achse), keine Messwerte interpretiert ✓ · kein Arbeitgeber-Material ✓
`flow-design` §9: s/w, Oswald/Montserrat/Inter, ein Blau ✓

## Neu bauen
`curl -o src.mp4 https://video.wixstatic.com/video/97c2a9_2297ff977a9d426bb597b156b88d0d1c/1080p/mp4/file.mp4` → `python3 build.py src.mp4`
