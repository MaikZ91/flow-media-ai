# R007 · „Ich als Hologramm.“

Stand: 23.10.2026 · Format: Reel 1080×1920, 21 s · Status: **fertig (`R007.mp4`), postbereit**

Säule: `foto` / `ki` (Skill `content-themen`) · **Test-Variable:** `format = prozess-reveal` (Ergebnis zuerst, dann der Weg dahin in 4 Schritten)

## Konzept
Aus einem einzigen Porträt (freigegebene Serie, `flow-design` §4) wird ein 3D-Hologramm. Echt gebaut, kein Fake-Effekt:
1. **Foto** – frontales Porträt.
2. **Tiefe** – die KI „Depth Anything V2“ schätzt für jeden Pixel, wie nah er ist (hell = nah).
3. **Punktwolke** – 97.200 Punkte, jeder um seinen Tiefenwert nach vorn geschoben → echtes 3D, das sich drehen lässt.
4. **Hologramm** – blaues Licht, Scanlinien, Glitch, Lichtkegel, Ringe und Wellenlinien (Flow-Motiv) als Plattform.

Ehrlich bleiben: Aus einem Foto entsteht nur die Vorderseite – deshalb dreht sich der Kopf nur etwa ±35°. Eine Rundum-Ansicht (360°) braucht ein echtes 3D-Modell (z. B. Higgsfield „Multi-Image to 3D“ aus 2–4 Fotos aus verschiedenen Winkeln, kostet Credits) – nicht im Reel behaupten.

## Ablauf
| Zeit | Bild | Text im Bild |
|---|---|---|
| 0–3 s | Hologramm dreht sich (Hook) | BUILD IN PUBLIC · ICH ALS **HOLOGRAMM.** Aus einem einzigen Foto. Mit KI. |
| 3–6 s | flaches Foto aus Punkten | 01 · Ein Foto – EIN GANZ NORMALES **BILD.** |
| 6–9 s | Tiefenkarte | 02 · KI schätzt die Tiefe – HELL = NAH. **DUNKEL = FERN.** |
| 9–12 s | Punkte wachsen nach vorn, Kopf dreht sich | 03 · Punktwolke – DARAUS WIRD **3D.** |
| 12–18 s | Hologramm mit Plattform, Glitch, Partikeln | 04 · Hologramm – LICHT, LINIEN, **FLOW.** |
| 18–21 s | Hologramm (Loop zum Anfang) | WILLST DU WISSEN, WIE DAS **GEHT?** Schreib mir. |

Musik: „Motivating Mornings“ (Mixkit Stock Music Free License), ab 0:18, leise.

## Caption (zum Kopieren)
Ich als Hologramm. Aus einem einzigen Foto.

So geht's:
1. Ein ganz normales Porträt.
2. Eine KI schätzt für jeden Pixel, wie weit er weg ist – die Tiefenkarte.
3. Daraus werden fast 100.000 Punkte im Raum. Echtes 3D.
4. Dazu Licht, Scanlinien und mein Flow-Motiv – fertig ist das Hologramm.

Kein teures Programm, kein 3D-Studio. Nur KI, ein bisschen Code und Neugier.

Ehrlich gesagt: Aus einem Foto gibt's nur die Vorderseite. Für 360° bräuchte ich Fotos von allen Seiten – das teste ich als Nächstes.

Willst du wissen, wie das geht? Schreib mir.

#KI #3D #Hologramm #BuildInPublic #FlowMediaAI

**Grund zum Senden:** „Schick das jemandem, der immer sagt, KI kann nur Texte.“ (als erster Kommentar)
**Posten:** 18–20 Uhr, nicht am selben Tag wie R006.

## Checkliste
Teil C §5: 1. Mensch + Bewegung im ersten Frame (drehendes Hologramm von Maik) ✓ 2. Hook ab Bild 1 ✓ 3. 21 s, 6 Szenen à 3 s ✓ 4. Interrupts: jeder Schritt ein neuer Look ✓ 5. Loop ✓ 6. Grund zum Senden ✓ 7. Text im Bereich 1240–1500 px, unten frei ✓ 8. Alles echt (eigenes Foto, echte Tiefenkarte, echte Punktwolke), Grenze offen benannt ✓ 9. Klingt nach Maik ✓
`flow-design` §9: Schwarz + Blau, Oswald-Headlines, Logo, Maik im Motiv ✓

## Neu bauen
1. `python3 depth.py ../R005-gleicher-look/img/portrait_front.jpg` → `photo.png`, `depth.png` (braucht `torch`, `transformers`).
2. Ordner per `python3 -m http.server 8765` ausliefern, `node render.js` (Playwright, WebGL über SwiftShader, three.js 0.160) → `video_only.mp4`.
3. Musik wie bei R006 drunterlegen (`-ss 18 -t 21`, Ausblenden ab 19,6 s).
