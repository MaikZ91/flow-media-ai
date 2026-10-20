# Flow Board

Trello-ähnliches Task-Board mit Prioritäten-Matrix, Kalender und Dateiablage.

- `index.html` – Quelle für die Web-Version. Die Claude-Version (https://claude.ai/artifact/99KBM42Garnuq9ZtV3MfgN) ist **eingefroren seit 19.10.2026, nicht mehr veröffentlichen – Maik**. Maßgeblich ist nur noch die Web-Version.
  Speichert Karten und Dateien im Online-Speicher des Boards. (Die eingefrorene Claude-Version liest noch Dropbox; nicht mehr genutzt.)
- `demo.html` – teilbare Demo (**eingefroren – zuletzt auf Maiks Wunsch einmalig aktualisiert am 19.10.2026 mit neuem Design und Outlook-Kalender, danach nicht mehr aktualisieren**): https://claude.ai/artifact/NiGiVFXGQKNzzaWTWyEc8u
  Beispielkarten, jede Änderung bleibt im Browser des Besuchers. Keine Dateien, kein Dropbox.

- `web/index.html` – eigenständige Web-Version (GitHub Pages). Login, Daten und Dateien in Supabase
  (Projekt „Liebefeld“, Tabellen `flow_board_tasks/_files/_meta`, Bucket `flow-board`, alles per RLS nur für den eigenen Account).
  Ablage: **Google Drive** `Flow Media AI` (seit 19.10.2026, Dropbox nicht mehr). Der Bereich „Google Drive“ unter Dateien zeigt die Ordner aus `meta.drive` (`{root, folders:[{name,id}]}`, im Board-Datensatz, nicht im Code); an Karten hängen Drive-Links (`kind: "link"`, Drive-Symbol).

`web/index.html` wird aus `index.html` erzeugt – nie von Hand ändern. (`demo.html` nicht mehr neu erzeugen. Falls Maik es ausdrücklich will: `sed 's/const DEMO = false;/const DEMO = true;/; 1s#<title>Flow Board</title>#<title>Flow Board Demo</title>#' index.html > demo.html`)


    { printf '<!doctype html>\n<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex"><link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icons/apple-touch-icon.png"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="Flow Board"><meta name="theme-color" content="#f6f6f2"></head><body>\n'; sed 's/const WEB = false;/const WEB = true;/' index.html; printf '\n</body></html>\n'; } > web/index.html

    cp web/index.html ../../board/index.html

App-Installation (iPhone: Safari → Teilen → „Zum Home-Bildschirm“; Android/Chrome: „App installieren“): `board/manifest.webmanifest`, `board/sw.js`, `board/icons/` liegen fest neben der Seite. Die installierte iPhone-App hat einen eigenen Speicher – dort einmal den Board-Link einfügen.

Kein Artifact mehr neu veröffentlichen (Claude-Version und Demo sind eingefroren). Live (GitHub Pages, Branch `main`, Ordner `/`): https://maikz91.github.io/flow-media-ai/board/

## Server (Supabase Edge Function `flow-board`)
Quelle: `supabase/flow-board/index.ts` – nach Änderungen per Supabase-MCP (`deploy_edge_function`) neu deployen.
Secrets in Supabase → Edge Functions → Secrets: Calendly-Token (Name beginnt mit `CALENDLY`), optional `GITHUB_TOKEN` (für private Repos) und `GITHUB_REPOS` (z. B. `MaikZ91/flow-media-ai,MaikZ91/flow-media-ai-private`).
