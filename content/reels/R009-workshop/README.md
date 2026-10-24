# R009 · Workshop-Reel „Chaos vs. System“

Stand: 24.10.2026 · Format: Reel 1080×1920, 19,7 s (funktioniert auch als Story) · Status: **fertig (`R009.mp4`), postbereit**

Säule: `lernen` / `design` · Anlass: Digitaler Stammtisch #1 „Mit KI zur Personal Brand – wie dein Content immer gleich aussieht“, **Mo 26.10.2026, 18:00, ca. 60 Min, live, 15 €** · **Test-Variable:** `format = chaos-vs-system`, `musik = eigene`

## Idee
Das Workshop-Thema selbst zeigen: Erst wechselt auf jeden Beat der Look (andere Schrift, andere Farbe, anderer Filter auf Maiks Foto) – so sieht KI-Content ohne System aus. „STOPP.“ Dann rasten Maiks echte Posts im Flow-Look ein (Karussell, R005, Flyer, Community-Plakat, R006) – ein Design-Skill, jeder Post gleich. Danach Titel, Termin und Preis auf den Beat, Maik und „Platz sichern“.

## Ablauf (Schnitt auf „Independence 2.1“, 1 Beat = 0,429 s)
| Beats | Zeit | Bild | Text |
|---|---|---|---|
| 0–5 | 0–2,1 s | Maik frontal | WORKSHOP · MONTAG 18 UHR – DEIN KI-CONTENT SIEHT JEDES MAL **ANDERS** AUS? |
| 5–13 | 2,1–5,6 s | Chaos: 8 Looks, jeder Beat ein neuer | Ohne System: jeder Prompt, ein neuer Look · „Prompt 1 … 8“ |
| 13–15 | 5,6–6,4 s | Schwarz | STOPP. |
| 15–23 | 6,4–9,9 s | 6 echte Flow-Posts rasten nacheinander ins Raster | Mit System: immer derselbe Look · EIN DESIGN-SKILL. **JEDER POST.** |
| 23–27 | 9,9–11,6 s | Maik am Laptop, abgedunkelt | Digitaler Stammtisch #1 – MIT KI ZUR **PERSONAL** BRAND. |
| 27–35 | 11,6–15 s | Infozeilen auf den Beat | MO 26.10. · 18:00 · LIVE · 60 MIN · **15 €** |
| 35–39 | 15–16,7 s | Maik am Laptop | Du gehst raus mit DEINEM EIGENEN **DESIGN-SKILL.** |
| 39–46 | 16,7–19,7 s | Maik frontal (Loop zu Bild 1) | MONTAG · 18 UHR · 15 € – PLATZ **SICHERN.** Schreib mir eine Nachricht. |

Musik: **MZ.9 – Independence 2.1** (`content/musik/eigene/mz9_independence-2-1.m4a`), ab 3,344 s.

## Caption (zum Kopieren)
Dein KI-Content sieht jedes Mal anders aus? Dann komm am Montag vorbei.

Beim ersten digitalen Stammtisch von Flow Media AI bauen wir live:
→ deinen visuellen Stil
→ deinen eigenen KI-Design-Skill
→ einen Workflow, mit dem jeder Post nach dir aussieht

📅 Montag, 26.10., 18:00 Uhr
⏱ ca. 60 Minuten, digital & live
💶 15 € pro Person

Platz sichern: Schreib mir eine Nachricht oder klick den Link in meiner Bio.

🎵 MZ.9 – Independence 2.1 · @mz.9_nyc

#KI #PersonalBrand #ContentCreation #Workshop #FlowMediaAI

**Grund zum Senden:** „Schick das jemandem, dessen Posts jedes Mal anders aussehen.“ (erster Kommentar)
**Posten:** heute (Sa) 18–20 Uhr; als Story Sonntag und Montag früh noch einmal.

## Checkliste
Teil C §5: Mensch im ersten Frame ✓ · Hook ab Bild 1 ✓ · ~20 s, Schnitt auf jeden Beat ✓ · Interrupts im Beat ✓ · Loop (Maik frontal Ende → Anfang) ✓ · Grund zum Senden ✓ · Text oben/Mitte, unten frei ✓ · nichts erfunden (keine Teilnehmerzahlen, kein „ausgebucht“), alle Angaben aus Maiks Workshop-Text ✓
`flow-design` §9: Flow-Look in allen System-Szenen, bunte Farben nur bewusst in der Chaos-Szene ✓ · Maik in jeder Szene außer „Stopp“/Raster (dort in den Posts) ✓

## Neu rendern
`node frames.js <ordner>` → `video_only.mp4`, dann
`ffmpeg -i video_only.mp4 -ss 3.344 -i ../../musik/eigene/mz9_independence-2-1.m4a -t 19.725 -filter_complex "[1:a]afade=t=out:st=18.5:d=1.2[a]" -map 0:v -map "[a]" -c:v libx264 -crf 22 -c:a aac -movflags +faststart R009.mp4`
