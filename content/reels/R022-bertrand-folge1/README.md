# R022 – Bertrand · Folge 1: Das Budget (Sitcom)

Stand: 30.10.2026 · Reel 1080×1920, 17,3 s · Status: **fertig (`R022.mp4`)** · Säule `kreativ` / `ki` · Test-Variable `format = sitcom-bertrand` · Nebencharakter Bertrand (creative-director, Teil B)

## Ablauf
| Zeit | Clip | Untertitel |
|---|---|---|
| 0–2,0 s | Büro: Maik stellt vor (b.mov 0–2 s) + Sitcom-Titel „BERTRAND · Folge 1 · Das Budget“ | MAIK: Darf ich vorstellen: unser neuer KI-Mitarbeiter. |
| 2,0–3,6 s | Bertrand am Laptop (b.mov 2–3,6 s) | – |
| 3,6–5,9 s | Couch (a.mov 1,6–3,9 s) | MAIK: Kannst du mir helfen, ein KI-Business aufzubauen? |
| 5,9–8,2 s | Bertrand (a.mov 4,5–6,8 s), **Originalstimme** | BERTRAND: Klar. Erst mal brauch ich ein Budget. |
| 8,2–9,2 s | Maik (a.mov 6,8–7,8 s) | MAIK: Wie viel? |
| 9,2–12,3 s | Bertrand (a.mov 7,8–10,9 s), **Originalstimme** | BERTRAND: Drei Bananen pro Prompt. Premium kostet fünf. |
| 12,3–15,3 s | Reaktion Close-up + Bertrand isst Banane (a.mov 11–14 s), Punch-in, eingebrannter Original-Untertitel abgedeckt | 🍌 |
| 15,3–17,3 s | Endkarte gelb | BERTRAND · Sieht aus wie ein Affe. Rechnet wie eine KI. · Folge 2? Schreib 🍌 in die Kommentare. |

Ton: Maiks Sätze laufen im Original mit KI-Stimme → **stumm**, nur Untertitel (Regel „keine Computerstimme als Maik“). Bertrands Stimme bleibt (er *ist* die KI). Musik: „Sicilian Coffee“ (Mixkit, Stock Music Free License) ab 33 s, unter Bertrands Stimme geduckt. CapCut-Wasserzeichen von a.mov weggeschnitten (Crop oben). Badge „KI-GENERIERT“ durchgehend.

## Caption
```
Mein neuer KI-Mitarbeiter hat Preise. 🍌

Bertrand, Folge 1: Ich wollte nur Hilfe beim KI-Business.
Er wollte erst mal über sein Budget reden.

Drei Bananen pro Prompt. Premium kostet fünf.

(Komplett KI-generiert – Bertrand ist ab jetzt öfter hier.)

Folge 2? Schreib 🍌 in die Kommentare 👇

#KIVideo #Sitcom #KIHumor #Bertrand #FlowMediaAI
```
Grund zum Senden: „Schick das jemandem, der für jeden Prompt bezahlt.“
Posten: abends 19–21 Uhr (Unterhaltung). Label „Mit KI erstellt“ setzen.

## Neu rendern
Clips aus Drive `Content/Videos` (RAW-Kopie + curl): b.mov = Büro (1080×1920), a.mov = Couch-Sitcom (480×854, Crop `452:804:14:50` gegen Wasserzeichen). Segmente siehe Tabelle, je 30 fps nach `raw/s1…s7`.
`node frames.js <ordner>` → `video_only.mp4`, dann Ton: Musik `-ss 33`, Bertrand-Stimme aus a.mov (4,5–6,8 s → 5,9 s; 7,8–10,9 s → 9,2 s), `sidechaincompress`, `loudnorm=I=-14` (Befehl im Chatverlauf/`git log`).
