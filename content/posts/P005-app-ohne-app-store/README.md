# P005 – Meine App. Ohne App Store.

Stand: 27.10.2026 · Karussell, 5 Folien 1080×1350 (`app_s1.png` … `app_s5.png`) · Säule `tools` · Test-Variable `format = anleitung-karussell` (Schritt-für-Schritt, Ziel: Saves)

Anlass: Maik hat das Flow Board am 26.10. als Web-App auf sein Android-Handy installiert; dabei fiel auf, dass die App den Board-Link immer neu wollte (Fix `ad0fe1d`: dauerhaften Speicher anfordern). Handy-Screens: lokaler Board-Build mit **Beispieldaten** (`shots.js`), keine echten Board-/Finanzdaten. Maik: Porträt frontal (Folie 1 groß, Folie 5 als Kreis).

1. Hook: „Meine App. Ohne App Store.“ – Maik + Handy mit Board
2. Was das ist: Kanban · Kalender · Finanzen, selbst gebaut mit Claude Code
3. So geht's: Web-App (Manifest + Service Worker) → Android: Chrome ⋮ → App installieren → iPhone: Safari Teilen → Zum Home-Bildschirm
4. Warum: keine Freigabe, Updates sofort, ein Code für alle Geräte
5. Build in public: der Link-Bug + Frage „Welches Tool würdest du dir bauen?“

## Caption
```
Meine eigene App – und sie war nie im App Store. 📱

Mein Flow Board (Aufgaben, Kalender, Finanzen) ist eigentlich eine Website. Mit zwei kleinen Dateien wird daraus eine Web-App, die du wie eine normale App installierst:

→ Android: in Chrome öffnen, ⋮ → „App installieren“
→ iPhone: in Safari öffnen, Teilen → „Zum Home-Bildschirm“

Kein Review, kein Upload, und jedes Update ist beim nächsten Öffnen da.

Ehrlicherweise gab's auch einen Bug: Auf meinem Android wollte die App bei jedem Start meinen Link neu. Der Fix ist drin, heute teste ich ihn.

Welches Tool würdest du dir selbst bauen? 👇

#WebApp #KI #ClaudeCode #BuildInPublic #FlowMediaAI
```
Grund zum Senden: „Schick das jemandem, der für jede Kleinigkeit ein neues App-Abo abschließt.“
Posten: Di/Mi 12–13 Uhr oder 18–19 Uhr.

## Checklisten
flow-design §9: s/w + Blau nur in Headline-Zeile/Nummern ✓ · Headline max. 4 Wörter/Zeile ✓ · Wortmarke klein ✓ · Rand 7 % ✓ · Maik im Motiv, Gesicht frei, andere Pose als P004 (Laptop) ✓ · keine erfundenen Zahlen – Finanzwerte nur Beispieldaten, gekennzeichnet ✓ · letzte Folie Frage statt Swipe ✓
creative-director: echtes eigenes Tool ✓ · keine Arbeitgeber-/Kundendaten ✓ · keine Tokens/Links im Bild ✓ (Board-Link nicht sichtbar)

Render: `node shots.js` (Screens), `node shoot.js` (Folien).
