# Flow Board

Trello-ähnliches Task-Board mit Prioritäten-Matrix, Kalender und Dateiablage.

- `index.html` – Quelle für die Web-Version. Die Claude-Version (https://claude.ai/artifact/99KBM42Garnuq9ZtV3MfgN) ist **eingefroren seit 19.10.2026, nicht mehr veröffentlichen – Maik**. Maßgeblich ist nur noch die Web-Version.
  Speichert Karten und Dateien im Online-Speicher des Boards, liest Dropbox `/Flow Media AI`.
- `demo.html` – teilbare Demo (**eingefroren seit 19.10.2026, nicht mehr aktualisieren – Maik**): https://claude.ai/artifact/NiGiVFXGQKNzzaWTWyEc8u
  Beispielkarten, jede Änderung bleibt im Browser des Besuchers. Keine Dateien, kein Dropbox.

- `web/index.html` – eigenständige Web-Version (GitHub Pages). Login, Daten und Dateien in Supabase
  (Projekt „Liebefeld“, Tabellen `flow_board_tasks/_files/_meta`, Bucket `flow-board`, alles per RLS nur für den eigenen Account).
  Dropbox: nur Links (keine direkte Anbindung ohne eigene Dropbox-App).

`web/index.html` wird aus `index.html` erzeugt – nie von Hand ändern. (`demo.html` nicht mehr neu erzeugen.)


    { printf '<!doctype html>\n<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex"></head><body>\n'; sed 's/const WEB = false;/const WEB = true;/' index.html; printf '\n</body></html>\n'; } > web/index.html

    cp web/index.html ../../board/index.html

Kein Artifact mehr neu veröffentlichen (Claude-Version und Demo sind eingefroren). Live (GitHub Pages, Branch `main`, Ordner `/`): https://maikz91.github.io/flow-media-ai/board/

## Server (Supabase Edge Function `flow-board`)
Quelle: `supabase/flow-board/index.ts` – nach Änderungen per Supabase-MCP (`deploy_edge_function`) neu deployen.
Secrets in Supabase → Edge Functions → Secrets: Calendly-Token (Name beginnt mit `CALENDLY`), optional `GITHUB_TOKEN` (für private Repos) und `GITHUB_REPOS` (z. B. `MaikZ91/flow-media-ai,MaikZ91/flow-media-ai-private`).
