# R017 · „Alte Website? Meine KI baut die neue.“ – die Lead-Pipeline

Stand: 25.10.2026 · Format: Reel 1080×1920, 28,7 s · Status: **fertig (`R017.mp4`)** · Reihe: Agentic Marketing, Teil 2 (Teil 1 = R016)

Säule: `agentic` / `web` · **Test-Variable:** `format = pipeline-erklaerer` (Serie)

## Idee (Maik, 25.10.2026)
Maiks Lead-Agent als Pipeline: findet Betriebe mit veralteten Websites, analysiert sie, Claude baut eine neue, branchenspezifische Seite, die Konzeptvorschau geht online – und **wenn der Betrieb fragt**, antwortet Agent Mail automatisch mit der Vorschau und einem Link zum Erstgespräch.
**Entscheidungen (Maik):** Versand nur auf Anfrage (kein Kaltmail-Versand im Reel, Regel „Kaltmail nicht zeigen“ bleibt) · ausschließlich erfundene Demo-Betriebe („Bäckerei Musterbrot“, „Friseur Beispiel“ …), als DEMO gekennzeichnet · keine echten Lead-Seiten, kein MZ.9-Name.

## Ablauf (Schnitt auf „Reaching Out“, 1 Beat = 0,522 s)
| Beats | Zeit | Station | Text | Animation |
|---|---|---|---|---|
| 0–7 | 0–3,7 s | Hook | Agentic Marketing · Teil 2 – ALTE WEBSITE? MEINE KI BAUT **DIE NEUE.** | Maik am Laptop |
| 7–15 | 3,7–7,8 s | 01 Finden | SIE SUCHT BETRIEBE MIT **ALTEN WEBSITES.** | Demo-Betriebe mit Score-Balken, „Bäckerei Musterbrot – Website von 2011“ wird markiert |
| 15–23 | 7,8–12 s | 02 Analysieren | SIE FINDET, **WAS NICHT PASST.** | Alte Seite im Handy, rote Hinweise: nicht fürs Handy, kein Bestell-Button, seit 2011 nicht aktualisiert, kaum lesbar |
| 23–32 | 12–16,7 s | 03 Neu bauen | SIE BAUT **DIE NEUE SEITE.** | blaue Wischkante, alte Seite wird zur Premium-Bäckerei-Seite |
| 32–38 | 16,7–19,8 s | 04 Vorschau | DIE KONZEPTSEITE **STEHT ONLINE.** | Konzept-URL, Seite scrollt |
| 38–47 | 19,8–24,5 s | 05 Antworten | BETRIEB FRAGT. **KI ANTWORTET.** | Anfrage „Was würde so eine Seite kosten?“ → Agent-Mail-Antwort mit Vorschau + „Kostenloses Erstgespräch“ · „Versand nur, wenn der Betrieb fragt“ |
| 47–55 | 24,5–28,7 s | Überblick | DIE KI BAUT VOR. **ICH REDE MIT DIR.** | 6 Stationen + „Neugierig, wie deine neue Website aussehen könnte? Schreib mir.“ |

Maik: Foto im Hook, danach als Kreis oben rechts. Musik: **„Reaching Out“ – Mixkit, Stock Music Free License** (`content/musik/frei/reaching-out.mp3`), ab 8,38 s.

## Caption (zum Kopieren)
Alte Website? Meine KI baut die neue – bevor jemand fragt.

So läuft meine Lead-Pipeline:
1. Ein Agent sucht lokale Betriebe mit veralteten Websites
2. Er prüft, was nicht passt: Handy, Buchen, Aktualität
3. Claude baut eine neue Seite – passend zur Branche
4. Die Konzeptvorschau steht online
5. Meldet sich der Betrieb, antwortet Agent Mail sofort mit der Vorschau
6. Und dann reden wir – Mensch zu Mensch

Die KI macht die Vorarbeit. Das Gespräch führe ich.

Neugierig, wie deine neue Website aussehen könnte? Schreib mir. 👇

#AgenticMarketing #Webdesign #KI #Automatisierung #FlowMediaAI

**Grund zum Senden:** „Schick das jemandem, dessen Website noch aus 2011 ist.“
**Posten:** nach R016 (Teil 1), z. B. Do 29.10. oder So 1.11., 18–20 Uhr.

## Checkliste
Teil C §5: Maik im ersten Bild ✓ · Hook ≤ 1 s ✓ · 28,7 s (Erklärer) ✓ · Wechsel alle 2–4 s ✓ · Grund zum Senden ✓ · Text oben, unten frei ✓ · nichts erfunden: nur Demo-Betriebe (gekennzeichnet), keine echten Zahlen/Kunden; kein Kaltmail-Versand gezeigt (nur Antwort auf Anfrage) ✓
`flow-design` §9: schwarz/weiß + ein Blau (Demo-Bäckerei-Seite in ihren eigenen Branchenfarben als Inhalt) ✓

## Neu rendern
`node frames.js <ordner>` → `video_only.mp4`, dann `ffmpeg -i video_only.mp4 -ss 8.38 -i ../../musik/frei/reaching-out.mp3 -t 28.70 …`
