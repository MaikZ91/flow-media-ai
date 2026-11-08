// Flow DNA – Skill-Katalog (Stand 08.11.2026, erweitert um Maiks Konzepttext „The Skill Marketplace“).
// Status ehrlich: "bereit" = Skill existiert und ist teilbar · "vorbereitung" = existiert, Store-Version (ohne Maiks eigene Daten) in Arbeit
// · "geplant" = Idee aus dem Konzept, noch nicht gebaut.
// Preise: Rahmen aus Maiks Konzepttext (Vorschlag, vor dem Livegang bestätigen). Ohne Rahmen: "Preis folgt".
window.FLOW_DNA = {
  marke: {
    name: "FLOW DNA",
    claim: "Your Business. Your AI. Your Flow.",
    unter: "The Skill Marketplace by Flow Media AI",
    idee: "Ein zentraler Marktplatz für wiederverwendbare KI-Skills, Agenten und Workflows, mit denen Selbstständige, Coaches und Unternehmen ihre täglichen Geschäftsprozesse vereinfachen, automatisieren und kreativ erweitern.",
    schluss: "Ideas become Skills. Skills become Possibilities.",
    schlussUnter: "An ecosystem of AI skills, workflows and agents. Built by creators, for businesses."
  },
  kategorien: [
    { id: "creative", nr: "01", name: "Creative & Branding" },
    { id: "marketing", nr: "02", name: "Marketing & Content" },
    { id: "automation", nr: "03", name: "Automation & Business" },
    { id: "web", nr: "04", name: "Web & App Development" },
    { id: "agents", nr: "05", name: "AI Agents & Systems" }
  ],
  stufen: {
    basis: { name: "Free", hinweis: "0 € · zum Einstieg" },
    premium: { name: "Premium", hinweis: "19–199 € · spezialisierte Workflows" },
    community: { name: "Community", hinweis: "eigene Preise der Creator" }
  },
  status: { bereit: "Verfügbar", vorbereitung: "Store-Version in Arbeit", geplant: "Geplant" },
  standardCreator: "Maik · Flow Media AI",
  skills: [
    // 01 Creative & Branding
    { id: "personal-brand", name: "Flow DNA Personal Brand", kat: "creative", stufe: "basis", status: "bereit", icon: "🧬", flagship: true,
      kurz: "Dein Stil und deine Marke als Skill – übertragbar auf Content, Websites, Apps und digitale Produkte.",
      kann: ["Liest ein Video oder Transkript über dich und deine Fotos", "Schreibt vier Skills: DNA, Look, Content, Website", "Danach klingt und sieht alles nach dir aus, nicht nach KI"],
      fuer: "Selbstständige, Coaches und Gründer mit eigener Personal Brand",
      demo: "Entsteht live im Workshop „Mit KI zur Personal Brand“; Maiks eigener Content läuft genau so.",
      herkunft: "Workshop „Mit KI zur Personal Brand“", version: "1.0",
      quelle: "https://github.com/MaikZ91/flow-media-ai/tree/main/workshops/2026-11-02_personal-brand-vol2/skills/brand-builder" },
    { id: "creative-director", name: "Creative Director", kat: "creative", stufe: "premium", status: "vorbereitung", icon: "🎬", preis: "49–99 €",
      kurz: "Dein Social-Media-Team als Skill: Idee, Hook, Reel, Caption – jeden Tag.",
      kann: ["Kennt Positionierung, Tonalität und Regeln deiner Marke", "Plant Reels, Karussells und Storys mit Hook und Caption", "Tägliche Content-Routine inklusive Learnings"],
      fuer: "Personenmarken und kleine Teams, die regelmäßig posten wollen",
      demo: "Erstellt den täglichen Content von @flow.media.ai.", herkunft: "läuft täglich für @flow.media.ai" },
    { id: "design-system", name: "Flow DNA Design System", kat: "creative", stufe: "premium", status: "vorbereitung", icon: "🎨", preis: "39–89 €",
      kurz: "Dein Look als Regelwerk – jedes Plakat, jeder Post, jede Seite gleich.",
      kann: ["Farben, Schriften, Bildsprache, Layout-Regeln", "Gilt für Posts, Flyer, Angebote und Websites", "Checkliste, damit nichts aus dem Rahmen fällt"],
      fuer: "Marken, deren KI-Content jedes Mal anders aussieht",
      demo: "Der komplette Flow-Media-AI-Look (Website, Posts, Plakate) folgt diesem System.", herkunft: "Flow-Design (Maiks eigener Look)" },
    { id: "brand-identity", name: "Brand Identity Generator", kat: "creative", stufe: "premium", status: "geplant", icon: "🪪",
      kurz: "Von der Idee zu Name, Werten, Claim und Positionierung.", kann: ["Fragt dein Business ab", "Schlägt Positionierung, Claim und Werte vor", "Gibt dir ein Brand-Dokument zum Weiterarbeiten"], fuer: "Gründer vor dem Start" },
    { id: "style-analyzer", name: "Content Style Analyzer", kat: "creative", stufe: "basis", status: "geplant", icon: "🔬",
      kurz: "Analysiert deinen bisherigen Content und findet deinen Stil.", kann: ["Liest Posts, Texte und Bilder", "Benennt Muster in Ton und Look", "Grundlage für deinen Brand-Skill"], fuer: "Alle, die schon Content haben" },
    // 02 Marketing & Content
    { id: "content-planer", name: "Content Calendar", kat: "marketing", stufe: "premium", status: "vorbereitung", icon: "🗓️",
      kurz: "Themen-Säulen, Rotation und Verlauf – nie wieder „Was poste ich heute?“.",
      kann: ["Themenpool mit echtem Material je Säule", "Rotationsregeln und Wochenplan", "Verlauf und Learnings nach 48 Stunden"],
      fuer: "Alle, die einen roten Faden im Content wollen", demo: "Plant die Woche von @flow.media.ai.", herkunft: "Content-Themen von @flow.media.ai" },
    { id: "post-analyzer", name: "Social Media Post Analyzer", kat: "marketing", stufe: "basis", status: "geplant", icon: "📊",
      kurz: "Prüft Hook, Caption und Zahlen deiner Posts – und sagt, was besser geht.", kann: ["Bewertet den Einstieg in den ersten Sekunden", "Wertet Views, Saves und Sends aus", "Schlägt bessere Hooks und Captions vor"], fuer: "Alle, die selbst posten" },
    { id: "reel-script", name: "Reel Script Generator", kat: "marketing", stufe: "premium", status: "geplant", icon: "🎞️",
      kurz: "Vom Thema zum Drehplan: Hook, Szenen, Sprechtext, Text im Bild.", kann: ["Hook-Varianten zum Testen", "Szenen und Sprechtext in deiner Stimme", "Drehplan zum Abhaken"], fuer: "Creator und Selbstständige mit Reels" },
    { id: "copywriting", name: "Caption & Copywriting", kat: "marketing", stufe: "basis", status: "geplant", icon: "✍️",
      kurz: "Captions, Newsletter und Angebotstexte in deinem Ton.", kann: ["Schreibt in deiner Tonalität", "Ohne typische KI-Floskeln", "Mit passendem Call-to-Action"], fuer: "Alle, die regelmäßig schreiben" },
    // 03 Automation & Business
    { id: "autopilot", name: "Automatisierungspost (Instagram-Autopilot)", kat: "automation", stufe: "premium", status: "vorbereitung", icon: "🤖",
      kurz: "Beiträge planen, rendern und automatisch posten – ohne bezahlte Tools.",
      kann: ["Warteschlange für Reels und Karussells", "Postet zu festen Zeiten über die Instagram-API", "Holt Kennzahlen und schreibt einen Bericht"],
      fuer: "Kanäle, die zuverlässig laufen sollen", demo: "Bespielt einen eigenen Kanal automatisch.", herkunft: "Autopilot eines eigenen Kanals" },
    { id: "wettbewerb", name: "Wettbewerbsanalyse", kat: "automation", stufe: "premium", status: "vorbereitung", icon: "🔍",
      kurz: "Wer bietet was zu welchem Preis – und wo ist deine Lücke?",
      kann: ["Findet Mitbewerber in Region und Nische", "Vergleicht Angebote, Preise und Auftritt", "Leitet Chancen für Angebot und Content ab"],
      fuer: "Selbstständige vor dem Start oder vor einer Preisrunde", herkunft: "Marktanalyse eines eigenen Projekts" },
    { id: "angebot-rechnung", name: "Angebot & Rechnung", kat: "automation", stufe: "basis", status: "geplant", icon: "🧾",
      kurz: "Aus ein paar Stichworten ein sauberes Angebot oder eine Rechnung.", kann: ["Vorlage mit deinen Daten", "Kleinbetragsrechnung oder mit Steuer", "Ablage im richtigen Ordner"], fuer: "Solo-Selbstständige ohne Buchhaltungs-Software" },
    { id: "process-analyzer", name: "Business Process Analyzer", kat: "automation", stufe: "premium", status: "geplant", icon: "🧭",
      kurz: "Findet die Abläufe, die dich am meisten Zeit kosten – und was KI davon übernimmt.", kann: ["Interview zu deinem Arbeitsalltag", "Bewertet Aufwand und Automatisierbarkeit", "Fahrplan mit den ersten drei Automatisierungen"], fuer: "Selbstständige und kleine Teams" },
    { id: "workflow-builder", name: "Workflow Builder", kat: "automation", stufe: "premium", status: "geplant", icon: "🔗",
      kurz: "Verbindet Skills zu einem Ablauf, der von allein läuft.", kann: ["Schritte, Übergaben und Prüfpunkte", "Startet per Zeitplan oder Auslöser", "Protokoll, was wann passiert ist"], fuer: "Alle mit wiederkehrenden Abläufen" },
    { id: "support-agent", name: "Customer Support Agent", kat: "automation", stufe: "premium", status: "geplant", icon: "💬",
      kurz: "Beantwortet Standardfragen deiner Kunden in deinem Ton.", kann: ["Lernt aus FAQ, Website und Angeboten", "Gibt an dich ab, wenn es heikel wird", "Antwortet rund um die Uhr"], fuer: "Dienstleister mit vielen gleichen Fragen" },
    { id: "lead-qualification", name: "Lead Qualification", kat: "automation", stufe: "premium", status: "geplant", icon: "🎯",
      kurz: "Bewertet Anfragen und sagt dir, mit wem sich ein Gespräch lohnt.", kann: ["Fragt Bedarf, Budget und Zeitrahmen ab", "Sortiert nach Passung", "Bereitet das Erstgespräch vor"], fuer: "Coaches und Dienstleister mit Anfragen" },
    // 04 Web & App Development
    { id: "website", name: "Website Builder", kat: "web", stufe: "premium", status: "vorbereitung", icon: "🌐", preis: "49–99 €", hinweis: "Für Workshop-Teilnehmer gratis",
      kurz: "Aus deinem Content wird deine Website – live und selbst weiter bearbeitbar.",
      kann: ["Nimmt Fotos, Videos, Texte und deinen Stil", "Baut eine komplette Website im eigenen Look", "Stellt sie live – danach mit KI weiterpflegen"],
      fuer: "Alle, die eine eigene Website wollen – ohne Baukasten", demo: "Die Website von Flow Media AI ist so entstanden.", herkunft: "Workshop „Deine Website“ (09.11.)" },
    { id: "app-builder", name: "App Builder", kat: "web", stufe: "premium", status: "bereit", icon: "📱", preis: "49–99 €",
      kurz: "Erst fünf klickbare Entwürfe, dann die beste – so entsteht jede App.",
      kann: ["Baut fünf echte, klickbare Varianten", "Du wählst aus und mischst", "Neue Version, installierbar als App, veröffentlicht"],
      fuer: "Gründer mit App-Idee, Coaches, Dienstleister", demo: "Cocktail-App aus der AI Masterclass – und dieser Store.", herkunft: "AI Masterclass", version: "1.0" },
    { id: "lead-seiten", name: "Landingpage Generator", kat: "web", stufe: "premium", status: "vorbereitung", icon: "🧲",
      kurz: "Für jeden Betrieb eine branchenpassende Konzept-Website als Vorschau.",
      kann: ["Analysiert die bestehende Seite", "Baut eine branchenpassende Premium-Vorschau", "Fertig zum Zeigen im Erstgespräch"],
      fuer: "Webdesigner, Agenturen, Freelancer in der Akquise", herkunft: "MZ.9-Lead-Pipeline" },
    { id: "ui-ux", name: "UI/UX Design", kat: "web", stufe: "premium", status: "geplant", icon: "🧩",
      kurz: "Prüft Oberflächen auf Klarheit, Handy-Tauglichkeit und Barrierefreiheit.", kann: ["Checkliste für Layout und Bedienung", "Konkrete Verbesserungen mit Begründung", "Vorher-nachher-Vorschläge"], fuer: "Alle, die Websites oder Apps bauen" },
    // 05 AI Agents & Systems
    { id: "agentensystem", name: "Flow Agentensystem", kat: "agents", stufe: "premium", status: "vorbereitung", icon: "🧠", preis: "99–199 €+",
      kurz: "Ein Prüfagent ohne Vorwissen prüft jedes Ergebnis, bevor du es siehst.",
      kann: ["Interview und Blindspot-Pass vor großen Projekten", "Korrekturen werden zu dauerhaften Regeln", "Recherchen laufen verteilt auf mehrere Modelle"],
      fuer: "Alle, die mit KI viel und verlässlich arbeiten", herkunft: "Maiks Arbeitsmodus mit Prüfer-Agent" },
    { id: "blindspot", name: "Blindspot-Analyse", kat: "agents", stufe: "basis", status: "bereit", icon: "🔦",
      kurz: "Findet, was du vor einem Projekt übersiehst.",
      kann: ["Sucht die „Unknown Unknowns“ in deinem Vorhaben", "Setzt nichts um, sondern fragt und ordnet", "Schreibt dir einen besseren Auftrag mit Reihenfolge"],
      fuer: "Vor jedem größeren Projekt", herkunft: "Maiks eigener Projektstart", version: "1.0",
      quelle: "https://github.com/MaikZ91/flow-media-ai/tree/main/.claude/skills/blindspot-analyse" },
    { id: "research-agent", name: "Research Agent", kat: "agents", stufe: "premium", status: "geplant", icon: "📚",
      kurz: "Recherchiert ein Thema über viele Quellen und fasst es belegt zusammen.", kann: ["Verteilt die Suche auf mehrere Agenten", "Prüft Quellen gegeneinander", "Bericht mit Belegen"], fuer: "Gründer, Berater, Content-Creator" },
    { id: "business-assistant", name: "Business Assistant", kat: "agents", stufe: "premium", status: "geplant", icon: "🗂️",
      kurz: "Dein Assistent für Termine, Aufgaben, Mails und Ablage.", kann: ["Verbindet Kalender, Board und Ablage", "Erinnert und fasst zusammen", "Erledigt Routine per Chat"], fuer: "Solo-Selbstständige" },
    { id: "knowledge", name: "Knowledge Management", kat: "agents", stufe: "premium", status: "geplant", icon: "🏛️",
      kurz: "Dein Firmenwissen an einem Ort – und die KI kennt es.", kann: ["Sammelt Dokumente, Abläufe, Vorlagen", "Hält sie aktuell", "Beantwortet Fragen daraus"], fuer: "Teams und wachsende Unternehmen" },
    // Free-Einstieg
    { id: "meeting-summary", name: "Meeting Summary", kat: "automation", stufe: "basis", status: "geplant", icon: "📝",
      kurz: "Aus Notizen oder Sprachmemo werden Zusammenfassung und Aufgaben.", kann: ["Fasst Gespräche kurz zusammen", "Zieht Aufgaben und Termine heraus", "Fertig für Board oder Kalender"], fuer: "Alle mit vielen Gesprächen" },
    { id: "email-assistant", name: "E-Mail Assistant", kat: "automation", stufe: "basis", status: "geplant", icon: "✉️",
      kurz: "Antwortet auf Mails in deinem Ton – du gibst nur noch frei.", kann: ["Entwürfe für Antworten", "Freundlich, klar, kurz", "Erkennt, was dringend ist"], fuer: "Alle mit vollem Postfach" },
    { id: "brainstorming", name: "Brainstorming", kat: "creative", stufe: "basis", status: "geplant", icon: "💡",
      kurz: "Ein Sparringspartner für Ideen, der nachfragt statt nur aufzulisten.", kann: ["Fragt, worum es wirklich geht", "Entwickelt Ideen in mehreren Richtungen", "Bewertet und sortiert sie"], fuer: "Alle mit vielen Ideen" },
    { id: "idea-validator", name: "Business Idea Validator", kat: "automation", stufe: "basis", status: "geplant", icon: "🧪",
      kurz: "Prüft deine Geschäftsidee, bevor du Zeit und Geld investierst.", kann: ["Zielgruppe, Nutzen, Zahlungsbereitschaft", "Schwachstellen und Risiken", "Nächste kleine Testschritte"], fuer: "Gründer und Ideen-Sammler" },
    { id: "prompt-optimizer", name: "Prompt Optimizer", kat: "agents", stufe: "basis", status: "geplant", icon: "🛠️",
      kurz: "Macht aus einem schnellen Prompt einen, der zuverlässig liefert.", kann: ["Ergänzt Ziel, Kontext und Format", "Zeigt vorher und nachher", "Speichert gute Prompts als Vorlage"], fuer: "Alle, die mit KI arbeiten" }
  ],
  pakete: [
    { id: "content-engine", name: "Content-Engine", skills: ["creative-director", "design-system", "content-planer", "autopilot"], kurz: "Das komplette Content-System: planen, gestalten, produzieren, posten." }
  ],
  paketAufbau: [
    ["SKILL.md", "Name, Beschreibung und die eigentliche Anleitung für die KI"],
    ["Ressourcen", "Vorlagen, Bilder, Schriften, Skripte, die der Skill nutzt"],
    ["Beispiele", "Ein echtes Ergebnis, damit du siehst, was rauskommt"],
    ["Installation", "In wenigen Schritten in Claude Code oder Codex einsatzbereit"]
  ],
  phasen: [
    { name: "Phase 1 · Flow DNA MVP", punkte: ["10–15 eigene Skills", "Kategorien und Suche", "Skill-Detailseiten", "Kostenlose Downloads", "Premium kaufen"], jetzt: true },
    { name: "Phase 2 · Community Marketplace", punkte: ["Skills einreichen", "Creator-Profile", "Freigabeprozess", "Eigene Preise", "Umsatzbeteiligung"] },
    { name: "Phase 3 · Flow DNA Ecosystem", punkte: ["Skill-Abos", "Agenten direkt ausführen", "Skill-Kombinationen", "Persönliche Business-Assistenten", "Teams und Unternehmen"] }
  ],
  kontakt: { whatsapp: "4917645961547" }
};
