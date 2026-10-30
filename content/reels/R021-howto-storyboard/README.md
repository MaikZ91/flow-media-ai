# R021 – How-to: Vom Storyboard-Bild zum KI-Film (mit Bertrand)

Stand: 30.10.2026 · Reel 1080×1920, 22,2 s · Status: **fertig (`R021.mp4`)** · Säule `kreativ` / `lernen` · Test-Variable `format = howto-storyboard` · erster Auftritt von **Bertrand** (Nebencharakter, siehe creative-director)

## Ablauf (Beat-Raster „Sicilian Coffee“, Mixkit, ab 16,115 s, B = 0,6008 s)
1. Hook (0–2,4 s): Maik (KI-Version) fassungslos vor der Bananen-App – „DIESER FILM WAR EIN BILD.“ · Badge „KI-GENERIERT“
2. Schritt 01 · ChatGPT (2,4–6 s): Referenzfoto + der Storyboard-Prompt tippt sich (Maiks Prompt-Vorlage, Idee als [DEINE IDEE])
3. Schritt 02 · Ergebnis (6–9 s): das ganze Storyboard-Bild (6 Szenen) → fliegt in „Seedance 2.5“, Ladebalken
4. Schritt 03 · Seedance 2.5 (9–18 s): 5× passende Videostelle groß im vollen 9:16-Format (nichts abgeschnitten), Storyboard-Szene als Bild-im-Bild daneben („Bild rein. Film raus.“)
5. Ende (18–22 s): Bertrand am Laptop – „Das ist Bertrand. Er macht ab jetzt die KI-Arbeit. Sagt er zumindest.“ · IDEE → STORYBOARD → VIDEO

Material: Drive `Content/Videos` – `Bertrand2.png` (Storyboard aus ChatGPT), `Bertrand.mov` (Seedance-2.5-Ergebnis aus dem kompletten Storyboard-Bild). Originalton des Videos ist nur Musik → ersetzt durch Mixkit „Sicilian Coffee“ (Stock Music Free License).

## Caption
```
Dieses Video war vorher ein einziges Bild. 🍌

So hab ich's gemacht:
1️⃣ Foto von mir + Prompt in ChatGPT → ein Storyboard-Bild mit 6 Szenen
2️⃣ Das komplette Bild in Seedance 2.5 geladen – so wie es ist
3️⃣ Raus kam dieser Film

Mein Prompt:
„Erstelle ein cineastisches Storyboard als EIN Bild mit 4–6 Szenen für ein 15-sekündiges Instagram Reel. Meine Person aus dem Referenzfoto soll die Hauptfigur sein. Idee: [DEINE IDEE]. Fotorealistisch, kreativ, humorvoll und im Hochformat 9:16.“

Merke: Erst die Idee, dann das Storyboard, dann das Video.

Ach ja: Das ist Bertrand. Er macht ab jetzt die KI-Arbeit. Sagt er zumindest. 🐒

Speicher dir den Prompt – und sag mir, welche Idee du damit umsetzt 👇

#KIVideo #Seedance #ChatGPT #HowTo #FlowMediaAI
```
Grund zum Senden: „Schick das jemandem, der immer sagt, KI-Videos kann er nicht.“
Posten: abends 18–20 Uhr. Beim Hochladen das Label „Mit KI erstellt“ setzen.

## Checklisten
Mensch + Bewegung im ersten Bild ✓ · Hook ≤ 1 s ✓ · 22 s (How-to) ✓ · Wechsel alle 1,8–3 s ✓ · Grund zum Senden ✓ (Prompt zum Speichern) · Text oben/Mitte, unten frei ✓ · KI-Kennzeichnung im Bild ✓ · nur Maiks eigene KI-Version, keine fremden Gesichter ✓ · kein fremdes Wasserzeichen im genutzten Material ✓

## Neu rendern
RAW-Frames (nicht im Repo) aus `Bertrand.mov` (curl über RAW-Kopie): hook 6,6 s/2,42 s · p1 0,0/1,82 · p2 2,1/1,82 · p3 4,55/1,0 (0,55×) · p4 5,3/1,3 (0,72×) · p5 6,75/2,2 (1,2×) · end 2,0/2,6 (0,6×), je 30 fps 1080×1920. Panels aus dem Storyboard (img/p1–p6.jpg) per Crop.
`node frames.js <ordner>` → `video_only.mp4`, dann
`ffmpeg -i video_only.mp4 -ss 16.115 -i ../../musik/frei/sicilian-coffee.mp3 -t 22.23 -filter_complex "[1:a]afade=t=in:d=0.05,afade=t=out:st=20.9:d=1.3,loudnorm=I=-14:TP=-1:LRA=9[a]" -map 0:v -map "[a]" -c:v libx264 -crf 21 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart R021.mp4`
