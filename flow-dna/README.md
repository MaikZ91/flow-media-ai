# Flow DNA – Skill Store (Prototyp)

Stand 08.11.2026 · Idee von Maik: ein „App Store für Skills“ neben der Website. Alle Skills, die ein Business für die Arbeit mit KI braucht – Basis kostenlos, Premium zum Kaufen oder Mieten, dazu Skills aus der Community.

## Produktanforderungen (aus Maiks Briefing)
- Katalog aller vorhandenen Skills aus Maiks Projekten (Creative Director, Design, Website, App, Auto-Post, Agentensystem …).
- Stufen: **Basis** (kostenlos), **Premium** (kaufen oder mieten, eigene Preise – Maik legt sie fest), **Community** (Mitglieder reichen eigene Skills ein; später auch mit eigenem Preis).
- Als Unterseite/App neben der Website (`/flow-dna/`), Skills laden.

## Entscheidungen im Prototyp
- Nur echte Skills. Status ehrlich: *Bereit* (teilbar), *Store-Version in Arbeit* (existiert, Maiks eigene Daten müssen raus), *Geplant* (Idee für Basis-Skills).
- Keine Preise erfunden: Premium zeigt „Preis folgt“, Knopf fragt per WhatsApp an.
- Kostenlos laden = Link auf den Skill-Ordner im öffentlichen Repo (Brand-DNA, Blindspot-Analyse).
- Einreichen = Formular → WhatsApp an Maik (noch kein Backend, keine Auszahlungen an Dritte).
- Nicht im Store: Arbeitgeber-Skills, THE-TRIBE-/Dating-spezifische Skills.

## Aufbau
`daten.js` (Katalog) · `kern.js` / `kern.css` (Filter, Suche, Detail- und Einreichen-Fenster) · `v1-store` · `v2-terminal` · `v3-helix` · `v4-katalog` · `v5-swipe` · `index.html` (Auswahl).

## Offen
- Welche Variante (oder Mischung)?
- Zugang: öffentlich oder nur für Community-Mitglieder (Login)?
- Premium: Einmalkauf, Abo oder beides – und Preise.
- Dürfen Community-Mitglieder gleich verkaufen (dann Marktplatz: Auszahlungen, AGB, Steuern) oder zuerst nur kostenlos teilen?
- Store-Versionen der Premium-Skills neutralisieren (Brand-Daten beim ersten Start abfragen).
