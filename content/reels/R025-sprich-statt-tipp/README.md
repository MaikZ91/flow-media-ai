# R025 – Sprich statt tipp (mit Bertrands Stimme)

Stand: 30.10.2026 · Reel 1080×1920, 20 s · Status: **fertig (`R025.mp4`)** · Säule `ki` / `lernen` · Test-Variable `format = tipp-bertrand` · **ohne Stimme** (Maik: TTS klang abgehackt) – Bertrands Sätze nur als Untertitel

## Ablauf
| Zeit | Bild | Text / Ton |
|---|---|---|
| 0–2,4 s | Maik reibt sich auf der Couch die Augen (a.mov, KI) | DU TIPPST DEINE PROMPTS NOCH? |
| 2,4–5 s | Bertrand schiebt die Sonnenbrille hoch (a.mov) | BERTRAND: „Tippen? Ich rede einfach.“ |
| 5–9,6 s | Handy-Mockup: Spracheingabe, Wellenform, Mikrofon pulsiert, Text schreibt sich mit | 01 · Mikrofon statt Tastatur · EINFACH REDEN. · „Bau mir eine Landingpage für meinen Workshop am Montag …“ · „Mikrofon an. Drauflos reden. Fertig.“ |
| 9,6–14,7 s | 3 Tipps oben, Bertrand am Laptop unten (Bertrand.mov) | SPRICH WIE MIT EINEM KOLLEGEN: 1 Mikrofon-Taste in ChatGPT oder Claude · 2 Diktierfunktion der Tastatur (geht überall, sogar im Terminal) · 3 Ziel, Kontext, Beispiel · „Erzähl mir einfach alles. Ziel, Kontext, Beispiel. Ich sortier das.“ |
| 14,7–17,6 s | Maiks Reaktion + Bertrand mit Banane (a.mov, Original-Untertitel abgedeckt) | „Sprich mit mir. Nicht mit deiner Tastatur.“ |
| 17,6–20 s | Endkarte gelb | SPRICH DEINE PROMPTS. · Probier's heute aus – und erzähl mir, was du der KI als Erstes gesagt hast. 🍌 |

Ton: nur Musik „Cat Walk“ (Mixkit, Stock Music Free License) ab 28 s. (Die TTS-Spuren in `voice/` und `stimmproben/` sind verworfen.) Maik spricht nicht. Badge „KI-GENERIERT“.

## Caption
```
Du tippst deine Prompts noch? Bertrand redet einfach. 🎙️🍌

So geht's:
1️⃣ Mikrofon-Taste in ChatGPT oder Claude drücken
2️⃣ Oder die Diktierfunktion deiner Tastatur – geht überall, sogar im Terminal
3️⃣ Erzähl drauflos wie einem Kollegen: Ziel, Kontext, Beispiel

Gesprochen gibst du automatisch mehr Kontext – und genau das macht die Antworten besser.

Probier's heute aus und schreib mir, was du der KI als Erstes gesagt hast 👇

#KI #Prompting #ChatGPT #Claude #FlowMediaAI
```
Grund zum Senden: „Schick das jemandem, der Prompts tippt wie Romane.“
Posten: 18–20 Uhr. Label „Mit KI erstellt“.

## Neu rendern
Clips (Drive `Content/Videos`): hook a.mov 0–1,6 s (0,67×) · bert a.mov 4,5–6,8 s (0,885×) · tips Bertrand.mov 2–7 s · punch a.mov 11–14 s; a.mov mit Crop `452:804:14:50` (Wasserzeichen).
`node frames.js <ordner>` → `video_only.mp4`, dann Stimmen bei 2,6 / 6,2 / 9,9 / 14,9 s + Musik `-ss 28` mit `sidechaincompress`, `loudnorm=I=-14`.
