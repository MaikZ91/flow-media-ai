# R018 · „Cocktails mixen. Hände frei.“ – Produktidee Smart Glasses für die Bar

Stand: 25.10.2026 · Format: Reel 1080×1920, 28,3 s · Status: **fertig (`R018.mp4`)** · als **Konzept** gekennzeichnet

Säule: `kreativ` / `ki` (Produktidee) · **Test-Variable:** `format = produktkonzept-3d`

## Idee (Maik, 25.10.2026)
Smart Glasses, die dich freihändig durch einen Cocktail führen: Anweisung im Display, Ansage im Ohr, die Kamera filmt mit (und erkennt, wie viel schon im Glas ist). Jeder, der die Brille aufhat, mixt wie ein Profi – am Beispiel „Sex on the Beach“.

## Umsetzung
3D-Szene (three.js, wie R015): dunkler Bar-Tresen mit Bokeh-Lichtern, Highball-Glas, Eiswürfel, Flasche mit Ausgießer und Strahl, Flüssigkeit in Schichten (Wodka klar → Pfirsich/Orange → Cranberry sinkt nach unten = Sunset-Effekt), Orangenscheibe; Smart-Glasses-Modell mit Kamera (blauer Ring) und Display-Prisma. In den Schritt-Szenen sieht man durch die Brille: HUD mit Schrittleiste, Anweisung, Mengenring in cl, Sprachansage mit Wellenform, REC.

| Takt (2 Beats) | Zeit | Bild | Text / HUD |
|---|---|---|---|
| 0–5 | 0–3,7 s | Brille vor dem fertigen Cocktail | Produktidee · Smart Glasses – COCKTAILS MIXEN. **HÄNDE FREI.** |
| 5–8 | 3,7–6 s | Brille fliegt auf die Kamera zu (Aufsetzen) | Das Problem – REZEPT AM HANDY? **HÄNDE VOLL.** |
| 8–12 | 6–8,9 s | POV: Eis fällt ins Glas | 1/5 Glas mit Eis · „Fülle das Glas mit Eis.“ |
| 12–16 | 8,9–11,9 s | POV: Wodka läuft ein | 2/5 4 cl Wodka · Ring zählt 0 → 4 cl |
| 16–21 | 11,9–15,6 s | POV: Pfirsichlikör + Orangensaft | 3/5 · 2 cl + 4 cl · Ring bis 6 cl |
| 21–25 | 15,6–18,6 s | POV: Cranberry sinkt nach unten | 4/5 4 cl Cranberry – für den Sunset-Effekt |
| 25–28 | 18,6–20,8 s | Orangenscheibe an den Rand | 5/5 Fertig. · „Perfekt. Video ist gespeichert.“ |
| 28–33 | 20,8–24,6 s | Brille + Cocktail | Die Brille führt dich · Anzeige im Display · Ansage im Ohr · Kamera filmt mit |
| 33–38 | 24,6–28,3 s | Brille + Cocktail | JEDER MIXT **WIE EIN PROFI.** · Würdest du sie aufsetzen? |

Rezept (gängiges Sex-on-the-Beach-Rezept): 4 cl Wodka, 2 cl Pfirsichlikör, 4 cl Orangensaft, 4 cl Cranberrysaft, Eis, Orangenscheibe.
Musik: **„Aruba“ – Mixkit, Stock Music Free License** (`content/musik/frei/aruba.mp3`), ab 11,91 s. Maik als Kreis oben rechts (in den POV-Szenen ausgeblendet). „KONZEPT“-Badge in jedem Bild.

## Caption (zum Kopieren)
Cocktails mixen – mit beiden Händen frei. 🍹

Neue Produktidee: Smart Glasses für die Bar.
Du setzt die Brille auf und sie führt dich Schritt für Schritt:
→ die Anweisung siehst du im Display
→ die Ansage hörst du im Ohr
→ die Kamera filmt mit und erkennt, wie viel schon im Glas ist

Kein Rezept auf dem Handy, keine klebrigen Finger am Display. Am Ende steht ein Sex on the Beach, als hättest du nie was anderes gemacht.

Noch ist das ein Konzept. Würdest du sie aufsetzen – an der Bar oder zu Hause? 👇

Bitte verantwortungsvoll genießen.

#SmartGlasses #Produktidee #Cocktails #KI #FlowMediaAI

**Grund zum Senden:** „Schick das jemandem, der hinter der Bar steht – oder es gern würde.“
**Posten:** Fr/Sa 18–20 Uhr (Bar-Stimmung, Wochenende).

## Checkliste
Teil C §5: Bewegung ab Bild 1 + Maik als Kreis ✓ · Hook ≤ 1 s ✓ · 28,3 s (Schritt-für-Schritt-Demo) ✓ · Wechsel alle 2–4 s ✓ · Grund zum Senden ✓ · Text oben, unten frei ✓ · nichts erfunden: als Konzept gekennzeichnet (Badge + Caption), kein existierendes Produkt behauptet, keine Zahlen ✓
`flow-design` §9: dunkel, ein Blau (HUD, Kamera-Ring, Display), Oswald/Montserrat/Inter/JetBrains Mono ✓ · Cocktail-Farben als Inhalt

## Neu bauen
Ordner per `python3 -m http.server 8772` ausliefern → `node render.js` → Ton: `ffmpeg -i video_only.mp4 -ss 11.91 -i ../../musik/frei/aruba.mp3 -t 28.28 …`
