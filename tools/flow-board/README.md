# Flow Board

Trello-ähnliches Task-Board mit Prioritäten-Matrix, Kalender und Dateiablage.

- `index.html` – Arbeitsversion (privat): https://claude.ai/artifact/99KBM42Garnuq9ZtV3MfgN
  Speichert Karten und Dateien im Online-Speicher des Boards, liest Dropbox `/Flow Media AI`.
- `demo.html` – teilbare Demo: https://claude.ai/artifact/NiGiVFXGQKNzzaWTWyEc8u
  Beispielkarten, jede Änderung bleibt im Browser des Besuchers. Keine Dateien, kein Dropbox.

- `web/index.html` – eigenständige Web-Version (GitHub Pages). Login, Daten und Dateien in Supabase
  (Projekt „Liebefeld“, Tabellen `flow_board_tasks/_files/_meta`, Bucket `flow-board`, alles per RLS nur für den eigenen Account).
  Dropbox: nur Links (keine direkte Anbindung ohne eigene Dropbox-App).

`demo.html` und `web/index.html` werden aus `index.html` erzeugt – nie von Hand ändern:

    sed -e 's/const DEMO = false;/const DEMO = true;/' -e 's#<title>Flow Board</title>#<title>Flow Board Demo</title>#' index.html > demo.html

    { printf '<!doctype html>\n<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex"></head><body>\n'; sed 's/const WEB = false;/const WEB = true;/' index.html; printf '\n</body></html>\n'; } > web/index.html

Danach die Artifacts neu veröffentlichen und `web/` deployen.
