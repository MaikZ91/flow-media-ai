# Flow Board

Trello-ähnliches Task-Board mit Prioritäten-Matrix, Kalender und Dateiablage.

- `index.html` – Arbeitsversion (privat): https://claude.ai/artifact/99KBM42Garnuq9ZtV3MfgN
  Speichert Karten und Dateien im Online-Speicher des Boards, liest Dropbox `/Flow Media AI`.
- `demo.html` – teilbare Demo: https://claude.ai/artifact/NiGiVFXGQKNzzaWTWyEc8u
  Beispielkarten, jede Änderung bleibt im Browser des Besuchers. Keine Dateien, kein Dropbox.

`demo.html` wird aus `index.html` erzeugt – nie von Hand ändern:

    sed -e 's/const DEMO = false;/const DEMO = true;/' -e 's#<title>Flow Board</title>#<title>Flow Board Demo</title>#' index.html > demo.html

Danach beide Seiten neu veröffentlichen.
