# R019 – Talk-to-Brand: Einmal reden. Immer posten. (Workshop Vol. 2)

Stand: 27.10.2026 · Reel 1080×1920, 26,6 s · Status: **fertig (`R019.mp4`)** · Säule `lernen` / `social` · Test-Variable `hook = methoden-name` (Name der Methode als Hook)

Workshop: „Von KI zur Personal Brand – Vol. 2: Talk-to-Brand“ · Mo 02.11.2026 · 18:00 · ca. 60 Min · digital & live · 15 € · Material: `workshops/2026-11-02_personal-brand-vol2/`

## Szenen (Beat-Raster „Talent in the Air“, Mixkit, ab 15,766 s, B = 0,492 s)
1. Hook (0–3 s): Maik im echten Selfie-Video (RAW 24.10., „ziemlich geil“-Moment), „EINMAL REDEN. IMMER POSTEN.“ · Kicker „Talk-to-Brand · Workshop Vol. 2“
2. 01 Red über dich: Handy mit REC + Wellenform, darin Maiks echtes Video („tragt eure Message da draußen“) – „Ein Video. 5 Minuten.“
3. 02 KI hört zu: Transkript-Karte (BEISPIEL-Sätze, sinngemäß aus Maiks Werten) → Tags Werte · Stimme · Zielgruppe · Geschichte
4. 03 Talk-to-Brand: Video zerfällt in 4 Skills (DNA · Look · Content · Website)
5. 04 Content: Maiks echte Posts P002, P005, P004 – „Meine Posts · gebaut mit meinen eigenen Skills“
6. Fakten: Mo 02.11. · 18 Uhr · Digital · 15 €
7. Ende: Maik im Video-Kreis („Ich freue mich auf euch. Ciao!“) – „Dein eigener Skill.“ / „Bring ein Video von dir mit. Du gehst mit deinem eigenen Skill raus. Ein Experiment – mach mit. Schreib mir.“

## Caption
```
Einmal reden. Immer posten. 🎙️

Mein nächster Workshop heißt Talk-to-Brand:
Du nimmst ein 5-Minuten-Video von dir auf – wer du bist, wofür du stehst, für wen.
Daraus baut die KI deine Marke als Skill: deine Werte, deine Stimme, dein Look.

Danach schreibt Claude Posts, Captions und sogar deine Website so, dass sie nach dir klingen. Nicht nach KI.

Genau so entsteht mein eigener Content. Ob es bei dir genauso gut klappt? Finden wir zusammen raus – das Ganze ist ein Experiment, live.

Am Ende gehst du mit deinem eigenen Skill raus.

📅 Montag, 2. November, 18:00 Uhr
⏱ ca. 60 Minuten, digital und live
💶 15 € pro Person

Du willst dabei sein? Schreib mir eine Nachricht, dann schick ich dir die Vorbereitung.

#PersonalBrand #KI #ClaudeAI #ContentCreation #FlowMediaAI
```
Grund zum Senden: „Schick das jemandem, dessen KI-Posts klingen wie von einer Maschine.“
Posten: heute oder morgen 18–20 Uhr; Story-Erinnerung am Mo 02.11. morgens.

## Sprechtext (≈ 26 s, ruhig, auf die Szenen getimt)
| Sek. | Text |
|---|---|
| 0–3 | Einmal reden. Immer posten. |
| 3–7 | Du nimmst ein Video von dir auf: fünf Minuten, wer du bist und wofür du stehst. |
| 7–11 | Die KI hört zu und zieht deine Werte, deine Stimme und deine Zielgruppe raus. |
| 11–15 | Daraus wird deine Marke als Skill: DNA, Look, Content und Website. |
| 15–19 | Und dann klingt jeder Post nach dir. Genau so entsteht mein Content. |
| 19–23 | Ein Experiment, live: Montag, zweiter November, achtzehn Uhr. Fünfzehn Euro. |
| 23–26 | Bring ein Video mit. Du gehst mit deinem eigenen Skill raus. |

Stimme: Maik selbst (Sprachmemo) oder Maiks eigener Stimmklon (ElevenLabs Starter, kommerzielle Lizenz) – keine fremde Computerstimme als Maik. Beim Mischen Musik per sidechaincompress unter die Stimme ducken.

## Checklisten
Teil C §5: Maik im ersten Bild ✓ · Hook ≤ 1 s lesbar ✓ · 26,8 s (Erklärer) ✓ · Wechsel alle 2–4 s ✓ · Grund zum Senden ✓ · Text oben, unten 20 % frei ✓ · nichts erfunden: Transkript-Sätze als BEISPIEL gekennzeichnet, gezeigte Posts sind echte eigene ✓
flow-design §9: s/w + Blau ✓ · Maik im Motiv ✓ · keine fremden Wasserzeichen ✓

## Neu rendern
RAW-Frames (nicht im Repo, `raw/` ist ignoriert): Drive RAW `1pfmBWTy1i32mJBwH2Kuvipl34FMRxHLI` (Selfie 24.10., wie R011) per curl laden, dann mit HLG→SDR-Tonemap + s/w-Grade wie R011 als JPEG-Folgen extrahieren: `hook` ab 38,2 s (2,98 s, 1080×1920), `rec` ab 58,6 s (3,97 s, 600×1068), `end` ab 88,4 s (3,48 s, Crop 480×480 bei y=110 → 440²), je 30 fps.
`node frames.js <ordner>` → `video_only.mp4`, dann
`ffmpeg -i video_only.mp4 -ss 15.766 -i ../../musik/frei/talent-in-the-air.mp3 -t 26.568 -filter_complex "[1:a]afade=t=in:d=0.05,afade=t=out:st=25.17:d=1.4,loudnorm=I=-14:TP=-1:LRA=9[a]" -map 0:v -map "[a]" -c:v libx264 -crf 21 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart R019.mp4`
