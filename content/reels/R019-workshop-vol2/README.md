# R019 – Talk-to-Brand: Einmal reden. Immer posten. (Workshop Vol. 2)

Stand: 27.10.2026 · Reel 1080×1920, 26,8 s · Status: **fertig (`R019.mp4`)** · Säule `lernen` / `social` · Test-Variable `hook = methoden-name` (Name der Methode als Hook)

Workshop: „Von KI zur Personal Brand – Vol. 2: Talk-to-Brand“ · Mo 02.11.2026 · 18:00 · ca. 60 Min · digital & live · 15 € · Material: `workshops/2026-11-02_personal-brand-vol2/`

## Szenen (Beat-Raster „Motivating Mornings“, Mixkit, ab 20,271 s, B = 0,4954 s)
1. Hook (0–3 s): Maik groß, „EINMAL REDEN. IMMER POSTEN.“ · Kicker „Talk-to-Brand · Workshop Vol. 2“
2. 01 Red über dich: Handy mit REC + Wellenform – „Ein Video. 5 Minuten.“
3. 02 KI hört zu: Transkript-Karte (BEISPIEL-Sätze, sinngemäß aus Maiks Werten) → Tags Werte · Stimme · Zielgruppe · Geschichte
4. 03 Talk-to-Brand: Video zerfällt in 4 Skills (DNA · Look · Content · Website)
5. 04 Content: Maiks echte Posts P002, P005, P004 – „Meine Posts · gebaut mit meinen eigenen Skills“
6. Fakten: Mo 02.11. · 18 Uhr · Digital · 15 €
7. Ende: Maik (Kreis) – „Bring ein Video von dir mit. Du gehst mit deiner Marke als Skill raus. Schreib mir für einen Platz.“

## Caption
```
Einmal reden. Immer posten. 🎙️

Mein nächster Workshop heißt Talk-to-Brand:
Du nimmst ein 5-Minuten-Video von dir auf – wer du bist, wofür du stehst, für wen.
Daraus baut die KI deine Marke als Skill: deine Werte, deine Stimme, dein Look.

Danach schreibt Claude Posts, Captions und sogar deine Website so, dass sie nach dir klingen. Nicht nach KI.

Genau so entsteht mein eigener Content – live zeigen statt erzählen.

📅 Montag, 2. November, 18:00 Uhr
⏱ ca. 60 Minuten, digital und live
💶 15 € pro Person

Du willst dabei sein? Schreib mir eine Nachricht, dann schick ich dir die Vorbereitung.

#PersonalBrand #KI #ClaudeAI #ContentCreation #FlowMediaAI
```
Grund zum Senden: „Schick das jemandem, dessen KI-Posts klingen wie von einer Maschine.“
Posten: heute oder morgen 18–20 Uhr; Story-Erinnerung am Mo 02.11. morgens.

## Checklisten
Teil C §5: Maik im ersten Bild ✓ · Hook ≤ 1 s lesbar ✓ · 26,8 s (Erklärer) ✓ · Wechsel alle 2–4 s ✓ · Grund zum Senden ✓ · Text oben, unten 20 % frei ✓ · nichts erfunden: Transkript-Sätze als BEISPIEL gekennzeichnet, gezeigte Posts sind echte eigene ✓
flow-design §9: s/w + Blau ✓ · Maik im Motiv ✓ · keine fremden Wasserzeichen ✓

## Neu rendern
`node frames.js <ordner>` → `video_only.mp4`, dann
`ffmpeg -i video_only.mp4 -ss 20.271 -i ../../musik/frei/motivating-mornings.mp3 -t 26.75 -filter_complex "[1:a]afade=t=in:d=0.05,afade=t=out:st=25.3:d=1.4,loudnorm=I=-14:TP=-1:LRA=9[a]" -map 0:v -map "[a]" -c:v libx264 -crf 21 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart R019.mp4`
