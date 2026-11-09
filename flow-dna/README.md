# Flow DNA – Skill Store (live seit 08.11.2026)

Live: https://maikz91.github.io/flow-media-ai/flow-dna/ · Entwürfe: `varianten.html`

## Workshop-Edition (Maik, 08.11.2026)
`/flow-dna/workshop/` → `/flow-dna/?workshop=website`: Website Builder oben angepinnt, für Teilnehmende kostenlos **mit persönlichem Code** (Lizenz-System unten), Ablauf-Animation, 3-Schritte-Anleitung, Personal-Brand-Skill, Bonus Tech-Support bis 31.12.26. Im normalen Store bleibt der Website Builder Premium.

## Lizenz-System (Supabase, 08.11.2026)
Projekt `ykleosfvtqcmqxqihnod`, Edge Function **`flow-dna`** (verify_jwt aus, prüft selbst den Code), Tabellen `flow_dna_skills` (geheime Anleitung), `flow_dna_licenses` (Code, Skill, gültig bis, max. Einlösungen/Nutzungen), `flow_dna_license_log`; RLS ohne Policies, Zugriff nur über die Funktion `flow_dna_license_take` (atomar, zählt hoch).
- `POST /functions/v1/flow-dna/claim {code}` → persönlicher **Lade-Skill** `SKILL.md` (Code einmal einlösbar).
- `GET /functions/v1/flow-dna/skill?code=…` → eigentliche Anleitung, nur solange gültig und Nutzungen übrig; sonst 403 mit Hinweis auf den Store.
- Die Anleitung liegt nie beim Teilnehmer als Datei; nach Ablauf (Workshop: Mi 11.11.2026 23:59) ist der Skill nutzlos. Grenze: Was während der Laufzeit geladen wurde, könnte jemand mitkopieren.
- **Workshop 09.–11.11.2026: ein gemeinsamer Code `WEBSITE`** (bis Mi 11.11. 23:59, 200 Einlösungen, 1000 Abrufe; Maik: „Code ist nur für den Workshop und Code ist dann Website“). Die 20 Einzelcodes `WEB-XXXX-XXXX` sind deaktiviert. Workshop-Seite auf Code-Feld + Download reduziert (Maik: „so easy wie möglich“). Neue Codes, Verlängern, Sperren: per SQL – auf Zuruf erledigt Claude das.

## Free-Download & Premium-Lizenzen (Maik, 08.11.2026)
- **Free:** Knopf „⬇ Kostenlos herunterladen“ lädt direkt `downloads/<id>.zip` (Ordner mit SKILL.md + Dateien + INSTALLATION.md). Neu bauen nach Änderungen: `python3 build-downloads.py`.
- **Premium:** alle 25 Anleitungen liegen in Supabase `flow_dna_skills` (IDs = Store-IDs, Website = `website-builder`). Verkauf: Anfrage per WhatsApp → Claude stellt einen Code aus (`select flow_dna_issue('<skill>','<Kunde>','kauf'|'setup'|'miete', <Tage>)`; Kauf/Einrichtung unbefristet, Miete standardmäßig 31 Tage) → Kunde gibt den Code im Detailfenster unter „Schon gekauft? Lizenz-Code einlösen“ ein und bekommt den Lade-Skill. Miete verlängern: `valid_until` hochsetzen; sperren: `active = false`.
- Premium-Dateien in Drive (`07_KI/flow-dna-premium`) bleiben die Arbeitsfassung; Änderungen dort auch in `flow_dna_skills` übernehmen.

## Signature-Skills, Animationen, Videos (Maik, 08.11.2026)
- **Signature** (★, Verlauf-Badge, blaue Leiste, schwarze Leiste ganz oben in der Liste): Lead Agent · Website (39 €/Mon. · 399 € · 799 €), Lead Agent · Business (49 · 499 · 999), Social Content System (49 · 449 · 899), Creative Director, Agentensystem. Landingpage Generator dafür auf 19 · 149 · 349 (Baustein des Lead Agents).
- Neue Premium-Skills in Drive: `lead-agent-website`, `lead-agent-business`, `social-content-system` (aus `the-tribe-bot/lead_agent_deepseek` und `instagram_autopilot`, neutralisiert; Versand nur rechtssicher: Entwurf / auf Anfrage / mit Einwilligung).
- Jeder Skill hat `ablauf` (Schritte) → animierter Ablauf im Detail („So funktioniert's“), Signature-Karten mit Mini-Animation.
- Videos (`media/`, ohne Ton, 540×960): R017 Lead-Pipeline (Lead Agent · Website), R016 Content-Pipeline (Social Content System, Autopilot), R006 Website-Tour (Website Builder).

## Preise Premium (Maik, 08.11.2026)
Drei Optionen je Premium-Skill, Bezug **auf Anfrage** (WhatsApp mit vorausgefüllter Option): **Mieten** (€/Monat, inkl. Updates & Support, monatlich kündbar) · **Kaufen** (allgemeine Version) · **Mit Einrichtung** (angepasst, von Maik eingerichtet). Preise in `daten.js` (`preise: { miete, kauf, setup }`); Landingpage Generator 399 € Kauf (Maiks Vorgabe), der Rest von Claude vorgeschlagen.
Miete technisch: vorerst per Absprache (Zugang zu Updates/Support); echtes Abo später z. B. über Stripe.

Stand 08.11.2026 · Idee von Maik: ein „App Store für Skills“ neben der Website. Alle Skills, die ein Business für die Arbeit mit KI braucht – Basis kostenlos, Premium zum Kaufen oder Mieten, dazu Skills aus der Community.

## Produktanforderungen (aus Maiks Briefing)
- Katalog aller vorhandenen Skills aus Maiks Projekten (Creative Director, Design, Website, App, Auto-Post, Agentensystem …).
- Stufen: **Basis** (kostenlos), **Premium** (kaufen oder mieten, eigene Preise – Maik legt sie fest), **Community** (Mitglieder reichen eigene Skills ein; später auch mit eigenem Preis).
- Als Unterseite/App neben der Website (`/flow-dna/`), Skills laden.

## Erweiterung 08.11.2026 (Maiks Konzepttext „The Skill Marketplace“)
- Marke: **FLOW DNA** · „Your Business. Your AI. Your Flow.“ · „The Skill Marketplace by Flow Media AI“ · Schluss „Ideas become Skills. Skills become Possibilities.“
- 5 Kategorien: Creative & Branding · Marketing & Content · Automation & Business · Web & App Development · AI Agents & Systems.
- Stufen Free (0 €) · Premium (19–199 €) · Community (eigene Preise). **Keine Miete** – nur Kauf bzw. kostenloser Download.
- Richtpreise aus dem Konzept: Creative Director 49–99 €, Design System 39–89 €, Website Builder 49–99 € (für Workshop-Teilnehmer gratis), App Builder 49–99 €, Agentensystem 99–199 €+. **Vor dem Livegang bestätigen.**
- Flaggschiff: Flow DNA Personal Brand (kostenlos).
- Konzept-Skills, die es noch nicht gibt, stehen als „Geplant“ (z. B. Reel Script Generator, Research Agent, Meeting Summary).
- Detailseite: Was er kann, für wen, Beispiel aus der Praxis, Kompatibilität, Version, Creator, Preis, Merken.
- Neu: Meine Skills (gemerkt, im Browser), Skill-Paket-Standard (SKILL.md · Ressourcen · Beispiele · Installation), „Jeder kann Creator werden“ mit Einreichen inkl. Preis, Roadmap Phase 1–3.

## Entscheidungen im Prototyp
- Nur echte Skills. Status ehrlich: *Bereit* (teilbar), *Store-Version in Arbeit* (existiert, Maiks eigene Daten müssen raus), *Geplant* (Idee für Basis-Skills).
- Premium ohne Richtpreis zeigt „Preis folgt“; Kaufen/Vorbestellen läuft per WhatsApp (noch kein Bezahlsystem).
- Kostenlos laden = Link auf den Skill-Ordner im öffentlichen Repo (Brand-DNA, Blindspot-Analyse).
- Einreichen = Formular → WhatsApp an Maik (noch kein Backend, keine Auszahlungen an Dritte).
- Nicht im Store: Arbeitgeber-Skills, THE-TRIBE-/Dating-spezifische Skills.

## Aufbau
`daten.js` (Katalog) · `kern.js` / `kern.css` (Filter, Suche, Detail- und Einreichen-Fenster) · `v1-store` · `v2-terminal` · `v3-helix` · `v4-katalog` · `v5-swipe` · `index.html` (Auswahl).

## Rückmeldung Maik (08.11.2026) → v6
„Design vom Katalog (weiß, minimalistische Kacheln), Übersicht vom Terminal (kompakt, nicht ewig scrollen), Animation vom DNA-Strang (schlicht, klein), das Ganze in der App.“
→ `v6-app.html`: helles Katalog-Design, kompakte Liste (eine Zeile pro Skill, Kategorie-Köpfe bleiben stehen), kleiner animierter DNA-Strang neben dem Namen, App mit Tab-Leiste (Entdecken · Meine · Verkaufen · Mehr).

## Stand 08.11.2026 – alle Skills mit Inhalt
- **Free (11, öffentlich):** `skills/<id>/SKILL.md` – Personal Brand (= Brand-Builder aus dem Workshop), Blindspot-Analyse, Content Style Analyzer, Brainstorming, Social Media Post Analyzer, Caption & Copywriting, Angebot & Rechnung, Meeting Summary, E-Mail Assistant, Business Idea Validator, Prompt Optimizer. Installation: `skills/INSTALLATION.md`. Download-Knopf im Store verlinkt den Ordner.
- **Premium (19, privat):** nur in Drive `07_KI/flow-dna-premium/<id>.SKILL.md` (das Repo ist öffentlich!). Neutralisiert aus Maiks Skills: Creative Director, Design System, Content Calendar, Instagram-Autopilot, Wettbewerbsanalyse, App Builder, Landingpage Generator, Flow Agentensystem; neu: Website Builder, Brand Identity Generator, Reel Script Generator, Business Process Analyzer, Workflow Builder, Customer Support Agent, Lead Qualification, UI/UX Design, Research Agent, Business Assistant, Knowledge Management. Auslieferung nach Kauf: Datei als `SKILL.md` in einen Ordner mit dem Skill-Namen legen.
- v6: Auswahlleiste kompakter (Suche + Stufe in einer Zeile, Bereiche klappen beim Scrollen weg).

## Offen
- Welche Variante (oder Mischung)?
- Zugang: öffentlich oder nur für Community-Mitglieder (Login)?
- Premium: Einmalkauf, Abo oder beides – und Preise.
- Dürfen Community-Mitglieder gleich verkaufen (dann Marktplatz: Auszahlungen, AGB, Steuern) oder zuerst nur kostenlos teilen?
- Store-Versionen der Premium-Skills neutralisieren (Brand-Daten beim ersten Start abfragen).

## Beispielseiten (Demo-Galerie)

`demos/<betrieb>/` – drei Konzeptseiten für **frei erfundene** Demo-Betriebe (Bäckerei Musterbrot, Physio Beispiel, Friseur Beispiel), gebaut nach den Premium-Design-Regeln. Jede Seite trägt oben ein Demo-Banner, `noindex` und die Bildnachweise (CC0, `demos/credits.json`). Neu bauen: `python3 demos/build.py`. Im Store erscheinen sie im Detail von Lead Agent · Website, Landingpage Generator und Website Builder (`beispiele` in `daten.js`). Echte Betriebe kommen hier nur mit Einwilligung rein.

**Branchen-Regeln (Stand 08.11.2026):** Website Builder, Landingpage Generator und Lead Agent · Website haben den Abschnitt „Branche erkennen“: Branche genau bestimmen, Branchen-Steckbrief, Pflicht-Module je Branche (Restaurant → Speisekarte + Reservierung, Praxis/Therapie → Avatar mit Telefon + Termin + „Mit Rezept zu uns“, Friseur → Preisliste + Termin + Galerie, Handwerk → Referenzen + Anfrage …). Gepflegt in Supabase (`flow_dna_skills.body`), Kopie in Drive `flow-dna-premium/_branchen-playbook.md`. Die Workshop-Karte (`?workshop=website`) zeigt die Demo-Galerie ebenfalls.

**Stand 08.11.2026 (Nachmittag):** Demo-Seiten neu im Aufbau der Lead-Agent-Seiten (Vollbild-Foto-Hero, Icon-Leiste, Story mit Badge, Bildkarten, Farbband mit Terminanfrage/Speisekarte-Tabs, Team-Avatare, Mosaik-Galerie, dunkles Zitat-Band, Kontakt-Karten, Avatar-Assistent, dunkler Footer). Die Skills haben dazu „Seitenaufbau Premium“ (Pflicht) und „Selbstständige, Coaches, Berater, Kreative“. Galerie zeigt zusätzlich die echte Flow-Media-AI-Seite als Personal-Brand-Beispiel und steht auch in der Workshop-Karte der Hauptwebsite. Neuer Premium-Skill **Website-Performance (PostHog)** (`website-performance`, 19/149/349 €).

**App & Direkt nutzen (08.11.2026):** Flow DNA ist eine installierbare Web-App (`manifest.webmanifest`, `sw.js`, Icons in `app/`): Android über den Installieren-Button bzw. Chrome-Menü, iPhone über Safari → Teilen → „Zum Home-Bildschirm“ (Anleitung im Store). Free-Skills und eingelöste Premium-/Workshop-Codes haben „Direkt nutzen“: **In Claude öffnen** (`claude.ai/new?q=`), **In ChatGPT / Codex öffnen** (`chatgpt.com/?q=`) und **Prompt kopieren** für Claude Code/Codex – der Prompt verweist auf die SKILL.md bzw. den Lizenz-Loader (`/skill?code=`).

**App-Tabs (09.11.2026):** Entdecken · KI-News (Artikel + YouTube-Videos, Top-Themen, Sortierung nach Relevanz = Zahl der Quellen zum selben Thema + Themen-Gewicht + Frische) · Aktien (KI- & Robotik-Kurse: SpaceX, UBTech, Tesla, Nvidia, Alphabet, Microsoft; Anthropic/OpenAI nicht börsennotiert; Yahoo Finance, verzögert, mit Rückfall auf den letzten Stand) · Kurse (10 Online-Kurse „Coming soon“, Daten `kurse.js`, Vormerken + Code-Feld) · Community (mit Kalender + Tech-Support) · Mehr (Angebote & Buchen, Meine Skills, Verkaufen). *Angebote* (Daten `angebote.js`): Workshop-Termine mit Countdown und „Platz sichern“ per WhatsApp (vergangene Termine verschwinden automatisch), Erstgespräch über Calendly, 1:1-Begleitung, Projekt, Community. *KI-News* (`news.js`/`news.json`): automatisch aus offenen RSS-Feeds (The Decoder, t3n, heise, OpenAI) über `tools/ki-news/fetch.py`, alle 3 Std. per GitHub Action `.github/workflows/ki-news.yml`. *Community* enthält den Tech-Support (FAQ + Frage per WhatsApp). „Meine Skills“ und „Verkaufen“ liegen unter *Mehr*.

**Frag Maik – KI-Coach (Beta, 09.11.2026):** Mittlerer Tab unten (Avatar). Chat mit Vorschlagsfragen, Spracheingabe (Mikrofon, Browser-Spracherkennung), Antworten aus `coach.js` (Wissensbasis in Maiks Stimme, Stichwort-Abgleich, noch **ohne** Sprachmodell) mit passenden Buttons (Kurs, Skill, Kalender, Erstgespräch, Tech-Support-Gruppe). Unbekannte Fragen → Tech-Support-Gruppe/WhatsApp. Keine Computerstimme als Maik (nur Text). „Mehr“ sitzt jetzt oben rechts im Kopf. Ausbau zum echten KI-Coach: Supabase Edge Function + Claude API mit Maiks Wissen als Kontext (kein Training nötig).
