# Flow DNA – Skill Store (live seit 08.11.2026)

Live: https://maikz91.github.io/flow-media-ai/flow-dna/ · Entwürfe: `varianten.html`

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
