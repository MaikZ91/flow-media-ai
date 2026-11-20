# R050 – Von einer Idee zu etwas Eigenem (animiert)

Bewegte Fassung von Post P020, 13 s, 1080×1920, nur Schwarz-Weiß. Maiks Foto vor der Stab-Skulptur zoomt und fährt langsam nach rechts; das **neuronale Netz** wächst von seinem Kopf aus über die Skulptur (Knoten und Verbindungen aus den echten Stäben per Kantenerkennung, `netz.json`), Lichtimpulse laufen durch die Verbindungen, aus seinem Kopf fließt eine leuchtende Linie ins Netz. Danach Text: „Von einer Idee / zu etwas Eigenem.“ (Outline), Satz darunter, Logo und „Frei denken · Neues erschaffen · Menschen befähigen“.

- Bauen: `node render.js 13` (Playwright, 30 fps, `window.DRAW(t)` in `reel.html`), dann ffmpeg mit Musik (siehe Commit).
- Musik: „Reaching Out“ (Mixkit, frei).
- Look: s/w-Foto + weißes Netz (Abwechslung zu R049 dunkel/blau).
- Caption: wie P020 (Maiks Text).
