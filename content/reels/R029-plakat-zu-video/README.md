# R029 – Dieses Video war ein Plakat. (How-to Seedance 2.5)

Stand: 04.11.2026 · Reel 1080×1920, 21,5 s · Status: **fertig (`R029.mp4`)** · Säule `kreativ` / `lernen` · Test-Variable `format = howto-pipeline-bild-video`

Ablauf: Hook mit Maiks fertigem Seedance-Video („Dieses Video war ein Plakat.“) → 1 Zwei Inputs (Selfie mit Tasse + Plakat aus der Stadt als Stil-Referenz) → 2 Stil-Bild (Prompt tippt, Ergebnis 1) → 3 Mein Charakter (Ergebnis 2, Maik mit verschränkten Armen) → 4 Seedance 2.5 (Bild fliegt ins Tool, Ladebalken) → Flash, Video läuft → „Foto + Plakat + Prompt = Film.“

**Bewusst nicht gezeigt:** das Plakat nur stark weichgezeichnet (echter Künstler, fremde Gestaltung), das erste generierte Bild/Video mit der Figur vom Plakat (Ähnlichkeit zu einer realen Person) und alle CapCut-Wasserzeichen (in Ergebnis 2 abgedeckt). Die Prompts sind **sinngemäß rekonstruiert** (Maik hatte sie nicht mehr) – in der Caption so markiert.
Musik: „Uplifting Bass“ (Mixkit, Stock Music Free License), Drop beim Video-Reveal (15,6 s). Badge „KI-GENERIERT“ durchgehend.

## Caption
```
Dieses Video war vorher ein Plakat an der Wand. 🎬

So bin ich vorgegangen:
1️⃣ Zwei Inputs: ein Selfie von mir + ein Foto von einem Plakat, dessen Look ich mochte
2️⃣ Daraus ein Poster im gleichen Stil erzeugt
3️⃣ Dann mich selbst als Hauptfigur reingesetzt
4️⃣ Das Bild in Seedance 2.5 – raus kam das Video

Die Prompts (sinngemäß):

🖼 Bild 1:
„Erstelle ein Kampagnen-Poster im Hochformat 9:16 im Stil dieses Plakats: dunkles Studio, Person im weißen Overall, Lichtstative, schwebende KI-Interfaces. Titel ‚FLOW MEDIA AI‘, Untertitel ‚Bring Your Creativity to the Next Level‘, Akzentfarbe Lila.“

🧑 Bild 2:
„Ersetze die Person durch mich aus dem Referenzfoto – gleiches Gesicht, gleiche Brille. Arme verschränkt, selbstbewusstes Lächeln, beiger Pullover. Stil und Licht bleiben gleich.“

🎬 Video (Seedance 2.5):
„Kamera fährt langsam auf mich zu. Lila Lichtringe kreisen um mich und steigen nach oben, Interface-Fenster leuchten auf. Ich tippe in ein Hologramm und schaue nach oben in einen hellen Lichtring. Cineastisch, 9:16, 10 Sekunden.“

Speicher dir die Prompts – welches Plakat machst du zu deinem Film? 👇

#KIVideo #Seedance #ChatGPT #HowTo #FlowMediaAI
```
Grund zum Speichern/Senden: „Schick das jemandem, der an jedem Plakat stehen bleibt.“
Posten: abends 18–20 Uhr. Label „Mit KI erstellt“ setzen.

## Neu rendern
`raw/seedance.mov` (Maiks Seedance-Video) → `raw/vid/%03d.jpg` (30 fps); Bilder in `img/` (Plakat mit `gblur=sigma=22`, Wasserzeichen per `drawbox` abgedeckt). `node frames.js $PWD reel.html` → `video_only.mp4`, Musik `adelay=1200`, loudnorm −14.
