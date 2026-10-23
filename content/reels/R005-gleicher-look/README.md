# R005 · „Dein Content sieht jedes Mal anders aus?“

Stand: 23.10.2026 · Format: Reel 1080×1920, 26 s · Status: **fertig (`R005.mp4`), postbereit** – erste Ausgabe der Daily-Content-Routine

Säule: `social` / `design` (Skill `content-themen`) · **Test-Variable:** `look = flow-design` (erstes Reel im neuen Flow-Look, Maik als Foto statt Avatar/Video)

## Konzept
Problem → Lösung: KI-Content sieht ohne System jedes Mal anders aus. Maik zeigt, wie er das gelöst hat: eigene Plakate und Posts als Referenz gesammelt → Claude liest die Regeln raus (Farben, Schrift, Layout) → daraus wird der Skill `flow-design`, der immer wieder angewendet wird. Beweis am Schluss: dieses Reel ist bereits mit dem Skill gebaut (stimmt – Tokens, Schriften und Layout aus `flow-design`).

Alles im Bild ist echt: Plakat „Flow Business Community“, Karussell vom 23.10. (Folie 1 + 2), Profil- und Café-Motiv, die echten Farbwerte und Kapitel aus `.claude/skills/flow-design/SKILL.md`. Nicht verwendet: App-Flyer (Fantasie-Gewinn im Bild), Masterclass-Flyer (CapCut-Wasserzeichen, „x THE TRIBE“), Wellen-Zeichen (Entwurf).

## Ablauf
| Zeit | Szene | Text im Bild | Bild |
|---|---|---|---|
| 0–2,8 s | Hook | DEIN CONTENT SIEHT JEDES MAL **ANDERS** AUS? | Maik frontal, langsamer Zoom (Text ab Bild 1 = Cover) |
| 2,8–5,6 s | Problem | JEDER PROMPT. · Neuer Look. (wechselt Schrift/Farbe) | „So sieht's ohne System aus“, Maik als Kreis oben rechts |
| 5,6–10 s | 01 Referenzen | ICH HAB MEINE BESTEN DESIGNS GESAMMELT. | 5 eigene Motive fliegen ein |
| 10–14,8 s | 02 Analyse | CLAUDE LIEST DIE **REGELN** RAUS. | Scan über die Motive → Farben, Schriften, Regeln |
| 14,8–18,8 s | 03 Skill | DARAUS WIRD EIN **SKILL**. | `SKILL.md`-Kapitel, „Einmal gebaut. Immer wieder anwendbar.“ |
| 18,8–22,4 s | Ergebnis | DIESES REEL? SCHON MIT DEM **SKILL** GEBAUT. | Maik am Laptop |
| 22,4–26 s | CTA | WILLST DU DEINEN EIGENEN **DESIGN-SKILL**? Schreib mir. | Maik frontal → Loop zu Bild 1 |

Musik: „Motivating Mornings“ (Mixkit Stock Music Free License), ab 0:30, leise.

## Caption (zum Kopieren)
Dein KI-Content sieht jedes Mal anders aus? Ging mir genauso.

Jeder Prompt, ein neuer Look. Andere Schrift, andere Farben, anderer Stil. Wiedererkennbar ist da nichts.

Meine Lösung: Ich hab meine besten Plakate und Posts gesammelt und Claude die Regeln rauslesen lassen. Farben, Schriften, Abstände, wie Fotos aussehen. Daraus ist ein Skill geworden – eine Art Design-Handbuch, das die KI jedes Mal mitliest.

Seitdem baut mein Creative Director jeden Post nach denselben Regeln. Dieses Reel ist schon damit entstanden.

Willst du so einen Design-Skill für deine Marke? Schreib mir.

#KI #ContentCreation #Branding #SocialMediaAutomatisierung #FlowMediaAI

**Grund zum Senden:** „Schick das jemandem, dessen Posts jedes Mal anders aussehen.“ (als erster Kommentar)
**Posten:** heute zwischen 18 und 20 Uhr. Cover = erstes Bild (Hook-Text ist drauf).

## Sprechtext (optional, falls Maik einsprechen will, ca. 25 s)
> Dein KI-Content sieht jedes Mal anders aus? Kenn ich.
> Jeder Prompt – ein neuer Look.
> Also hab ich meine besten Designs gesammelt. Plakate, Posts, Fotos.
> Claude hat daraus die Regeln rausgelesen: Farben, Schriften, Layout.
> Und daraus ist ein Skill geworden, den ich immer wieder anwenden kann.
> Dieses Reel? Schon damit gebaut.
> Willst du deinen eigenen Design-Skill? Schreib mir.

Sprachmemo oder HeyGen-Video mit eigener Stimme nach Drive `01_Marketing › Reels` → wird drübergelegt, Musik leiser.

## Checkliste
Creative Director Teil C §5: 1. Mensch im ersten Frame (Maik, Zoom) ✓ 2. Hook ab Bild 1 lesbar ✓ 3. 26 s, Szenen 2,8–4,8 s ✓ 4. Interrupts: Schriftwechsel, einfliegende Motive, Scan, Tippen ✓ 5. Loop: Ende Maik frontal → Anfang Maik frontal ✓ 6. Grund zum Senden ✓ 7. Text über 80 %-Linie ✓ 8. Alles echt, keine Arbeitgeber-/Kundendaten (Karussell-Folien nur verkleinert, Fließtext nicht lesbar) ✓ 9. Klingt nach Maik ✓
`flow-design` §9: Schwarz/Weiß + Blau als einziger Akzent (Ausnahme bewusst: bunte Schriften in der „ohne System“-Szene) ✓ · Maik in jeder Szene (groß oder Kreis) ✓ · keine fremden Wasserzeichen ✓

## Neu rendern
`node frames.js <ordner>` (Playwright, 30 fps, ffmpeg) → `video_only.mp4`, dann:
`ffmpeg -i video_only.mp4 -ss 30 -i motivating-mornings.mp3 -t 26 -filter_complex "[1:a]volume=0.55,afade=t=in:d=0.4,afade=t=out:st=24.6:d=1.4[a]" -map 0:v -map "[a]" -c:v libx264 -crf 23 -pix_fmt yuv420p -c:a aac -movflags +faststart R005.mp4`
