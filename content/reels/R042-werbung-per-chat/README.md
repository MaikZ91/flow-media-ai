# R042 · Meine Werbung? Per Chat. (How-to, 24 s)

Säule `agentic` / `tools` · Problem `zeit` · Build in public: echte Schritte vom 15.11.2026 (Meta-Connector in Claude).
Musik: „Deep Urban“ (Mixkit, frei, aus `content/musik/frei/`), ab 8 s, 123 BPM, Schnitte auf dem Beat-Raster.

| Zeit | Szene |
|---|---|
| 0–2,9 s | Maik frontal: „Meine Werbung? Per Chat.“ · „Kein Rumklicken mehr.“ |
| 2,9–7,8 s | Chat: „Wie läuft meine Werbung?“ → echte Zahlen der Community-Anzeige (7 Tage: 311 gesehen, 26 Klicks, 0,14 $ pro Klick, Bielefeld + Münster) |
| 7,8–10,7 s | „Pausier die alte Kampagne von 2021.“ → ✓ Pausiert |
| 10,7–14,6 s | „Neue Kampagne: nur Leute, die in Bielefeld & Münster wohnen. 5 € am Tag.“ → ✓ Angelegt, startet erst nach OK |
| 14,6–20,5 s | So geht's: 01 Meta verbinden · 02 Instagram zulassen · 03 Einfach fragen |
| 20,5–24,4 s | Maik am Laptop: „Werbung per Chat.“ · „Was würdest du als Erstes fragen?“ · Speicher dir das |

Alles echt: Zahlen aus Maiks Werbekonto (Stand 15.11.2026), Kampagne pausiert bzw. angelegt wie gezeigt. Keine Konto-IDs im Bild.
Test-Variable: `format = chat-howto`

## Caption
```
Ich hatte keinen Bock mehr, mich durch den Werbeanzeigenmanager zu klicken. 🙃

Also steuere ich meine Werbung jetzt per Chat:
„Wie läuft meine Werbung?“ → Zahlen in Sekunden.
„Pausier die alte Kampagne.“ → erledigt.
„Nur Leute aus Bielefeld & Münster, 5 € am Tag.“ → angelegt. Live geht's erst nach meinem OK.

So geht's:
1️⃣ Claude → Einstellungen → Connectors → Meta verbinden
2️⃣ Beim Anmelden deinen Instagram-Account zulassen
3️⃣ Einfach fragen

Was würdest du als Erstes fragen? 👇

#Werbung #MetaAds #KI #Selbstständig #FlowMediaAI
```
Grund zum Speichern/Senden: „Schick das jemandem, der jedes Mal im Werbeanzeigenmanager verzweifelt.“
Posten: abends 18–20 Uhr. Label „Mit KI erstellt“ nicht nötig (Grafik/Animation, keine KI-Bilder), Porträts wie bisher.

## Checkliste
Mensch im ersten Frame ✓ · Hook ≤ 1 s lesbar ✓ · 24 s, jede Szene trägt ✓ · Interrupt alle 2–3 s (neue Chat-Nachricht/Schritt) ✓ · Grund zum Senden ✓ · Text in sicherer Zone (unten 20 % frei bis auf Avatar-Zeile) ✓ · nichts erfunden, keine IDs/Tokens im Bild ✓

## Neu rendern
`node frames.js $PWD reel.html` → `video_only.mp4`, dann Musik wie oben mit ffmpeg drunter (`R042.mp4`).
