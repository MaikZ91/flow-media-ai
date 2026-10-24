# R010 · Community-Reel „Der Kreis ist offen“

Stand: 24.10.2026 · Format: Reel 1080×1920, 20 s (funktioniert auch als Story) · Status: **fertig (`R010.mp4`), postbereit**

Säule: `weg` / `design` (Community-Reihe) · Anlass: Werbung für die kostenlose Flow Business Community (WhatsApp) · **Test-Variable:** `format = linien-animation`, `musik = eigene`

## Idee (Maik, 24.10.2026)
Die Community als minimalistischer blauer Linienkreis: Er zeichnet sich, dreht sich ein und öffnet sich oben. In der Öffnung steht Maik, danach entsteht um ihn herum der Netzwerk-Effekt der Website (Connect-Szene): Menschen tauchen auf dem Beat auf, Linien verbinden sie, Impulse laufen. Zum Schluss kommt durch die Öffnung ein neuer Punkt „DU“ dazu. Austausch steht im Vordergrund.

## Ablauf (Schnitt auf „Loneliness v.1.3“, 1 Beat = 0,608 s)
| Beats | Zeit | Bild | Text |
|---|---|---|---|
| 0–6 | 0–3,6 s | Blauer Kreis zeichnet sich als Linie | Flow Business Community – DU BAUST MIT KI – ABER **ALLEIN?** |
| 6–12 | 3,6–7,3 s | Ringe drehen sich ein, der Kreis öffnet sich oben | DER KREIS IST **OFFEN.** |
| 12–19 | 7,3–11,6 s | Maik erscheint im Kreis (Scanlinie) | Ich bin Maik – UND ICH WILL DAS **NICHT ALLEIN** MACHEN. |
| 19–28 | 11,6–17 s | Höhepunkt des Tracks: Maik wird zum Mittelpunkt, Netzwerk wächst | Connect – AUSTAUSCH STATT **EINZELKAMPF.** · Ideen teilen · Feedback · gemeinsam umsetzen |
| 28–33 | 17–20 s | „DU“ kommt durch die Öffnung dazu, Logo | Bielefeld · Münster · digital – KOSTENLOS **BEITRETEN.** WhatsApp-Community · Link in Bio |

Musik: **MZ.9 – Loneliness v.1.3** (`content/musik/eigene/mz9_loneliness-v1-3.m4a`), ab 65,37 s (Anstieg bis zum Höhepunkt). Passt zur Geschichte: von „allein“ zu „gemeinsam“.

## Caption (zum Kopieren)
Mit KI kannst du heute fast alles alleine bauen. Musst du aber nicht.

Darum gibt es die Flow Business Community: ein offener Kreis für Gründer, Selbstständige und Macher, die mit KI und digitalen Tools ins Machen kommen wollen.

→ Ideen teilen
→ Feedback bekommen
→ gemeinsam umsetzen

Kostenlos, in Bielefeld, Münster und digital. Der Link zur WhatsApp-Community ist in meiner Bio – oder schreib mir einfach „Community“.

🎵 MZ.9 – Loneliness v.1.3 · @mz.9_nyc

#Community #KI #Gründer #Selbstständig #FlowMediaAI

**Grund zum Senden:** „Schick das jemandem, der gerade allein an seinem Projekt sitzt.“ (erster Kommentar)
**Posten:** So oder Mo, nicht am selben Tag wie R009 (Workshop-Reel heute). Gut auch als Story mit Link-Sticker zur Community.

## Checkliste
Teil C §5: Hook ab Bild 1 (Text + Kreis) ✓ · ~20 s, Schnitt auf den Beat ✓ · Loop (Kreis am Ende → Kreis am Anfang) ✓ · Grund zum Senden ✓ · Text unten-mittig, unterer Rand frei ✓ · nichts erfunden (keine Mitgliederzahlen; Angaben von der Website: kostenlos, WhatsApp, Bielefeld/Münster/digital) ✓
`flow-design` §9: schwarz-weiß + ein Blau, Oswald/Montserrat/Inter ✓ · Maik ab Sekunde 7 und als Mittelpunkt des Netzwerks ✓ – **Ausnahme:** erstes Bild ohne Mensch, weil Maik den Kreis ausdrücklich als Einstieg wollte.

## Neu rendern
`node frames.js <ordner>` → `video_only.mp4`, dann
`ffmpeg -i video_only.mp4 -ss 65.37 -i ../../musik/eigene/mz9_loneliness-v1-3.m4a -t 20.06 -filter_complex "[1:a]afade=t=in:d=0.3,afade=t=out:st=18.9:d=1.15[a]" -map 0:v -map "[a]" -c:v libx264 -crf 22 -c:a aac -b:a 192k -movflags +faststart R010.mp4`
