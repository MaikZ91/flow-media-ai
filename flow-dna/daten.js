// Flow DNA – Skill-Katalog (Stand 08.11.2026). Gemeinsame Daten für alle Varianten.
// Nur echte Skills aus Maiks Projekten; Status ehrlich: "bereit" = Datei existiert und ist teilbar,
// "vorbereitung" = existiert, muss für den Store neutralisiert werden (Maiks Daten raus), "geplant" = Idee, noch nicht gebaut.
// Preise legt Maik fest – bis dahin "Preis folgt".
window.FLOW_DNA = {
  kategorien: [
    { id: "marke", name: "Marke & Content" },
    { id: "web", name: "Websites & Apps" },
    { id: "vertrieb", name: "Vertrieb & Markt" },
    { id: "qualitaet", name: "Strategie & Qualität" },
    { id: "buero", name: "Büro & Abläufe" }
  ],
  stufen: {
    basis: { name: "Basis", hinweis: "kostenlos" },
    premium: { name: "Premium", hinweis: "kaufen oder mieten" },
    community: { name: "Community", hinweis: "von Mitgliedern" }
  },
  status: {
    bereit: "Bereit",
    vorbereitung: "Store-Version in Arbeit",
    geplant: "Geplant"
  },
  skills: [
    {
      id: "brand-dna", name: "Brand-DNA", kat: "marke", stufe: "basis", status: "bereit", icon: "🧬",
      kurz: "Aus einem Video über dich wird deine Marke als Skill.",
      kann: ["Liest dein Video oder Transkript und deine Fotos", "Schreibt dir vier Skills: DNA, Look, Content, Website", "Danach klingt jeder Post nach dir, nicht nach KI"],
      fuer: "Selbstständige, Coaches, Gründer mit eigener Personal Brand",
      herkunft: "Workshop „Mit KI zur Personal Brand“",
      quelle: "https://github.com/MaikZ91/flow-media-ai/tree/main/workshops/2026-11-02_personal-brand-vol2/skills/brand-builder"
    },
    {
      id: "website", name: "Website-Skill", kat: "web", stufe: "basis", status: "vorbereitung", icon: "🌐",
      kurz: "Aus deinem Content wird deine Website – live und selbst weiter bearbeitbar.",
      kann: ["Nimmt Fotos, Videos, Texte und deinen Stil", "Baut eine komplette Website im eigenen Look", "Stellt sie live – danach mit KI weiterpflegen"],
      fuer: "Alle, die eine eigene Website wollen – ohne Baukasten",
      herkunft: "Workshop „Deine Website“ (09.11.)"
    },
    {
      id: "blindspot", name: "Blindspot-Analyse", kat: "qualitaet", stufe: "basis", status: "bereit", icon: "🔦",
      kurz: "Findet, was du vor einem Projekt übersiehst.",
      kann: ["Sucht die „Unknown Unknowns“ in deinem Vorhaben", "Setzt nichts um, sondern fragt und ordnet", "Schreibt dir einen besseren Auftrag mit Reihenfolge"],
      fuer: "Vor jedem größeren Projekt, jeder App, jeder Kampagne",
      herkunft: "Maiks eigener Projektstart",
      quelle: "https://github.com/MaikZ91/flow-media-ai/tree/main/.claude/skills/blindspot-analyse"
    },
    {
      id: "creative-director", name: "Creative Director", kat: "marke", stufe: "premium", status: "vorbereitung", icon: "🎬",
      kurz: "Dein Social-Media-Team als Skill: Idee, Hook, Reel, Caption – jeden Tag.",
      kann: ["Kennt deine Positionierung, Tonalität und Regeln", "Plant Reels, Karussells und Storys mit Hook und Caption", "Tägliche Content-Routine inklusive Learnings"],
      fuer: "Personenmarken und kleine Teams, die regelmäßig posten wollen",
      herkunft: "läuft täglich für @flow.media.ai"
    },
    {
      id: "design-system", name: "Design-System", kat: "marke", stufe: "premium", status: "vorbereitung", icon: "🎨",
      kurz: "Dein Look als Regelwerk – jedes Plakat, jeder Post, jede Seite gleich.",
      kann: ["Farben, Schriften, Bildsprache, Layout-Regeln", "Gilt für Posts, Flyer, Angebote und Websites", "Checkliste, damit nichts aus dem Rahmen fällt"],
      fuer: "Marken, deren KI-Content jedes Mal anders aussieht",
      herkunft: "Flow-Design (Maiks eigener Look)"
    },
    {
      id: "content-planer", name: "Content-Planer", kat: "marke", stufe: "premium", status: "vorbereitung", icon: "🗓️",
      kurz: "Themen-Säulen, Rotation und Verlauf – nie wieder „Was poste ich heute?“.",
      kann: ["Themenpool mit echtem Material je Säule", "Rotationsregeln und Wochenplan", "Verlauf und Learnings nach 48 Stunden"],
      fuer: "Alle, die einen roten Faden im Content wollen",
      herkunft: "Content-Themen von @flow.media.ai"
    },
    {
      id: "autopilot", name: "Instagram-Autopilot", kat: "marke", stufe: "premium", status: "vorbereitung", icon: "🤖",
      kurz: "Beiträge planen, rendern und automatisch posten – ohne bezahlte Tools.",
      kann: ["Warteschlange für Reels und Karussells", "Postet zu festen Zeiten über die Instagram-API", "Holt Kennzahlen und schreibt einen Bericht"],
      fuer: "Kanäle, die zuverlässig laufen sollen, auch wenn du keine Zeit hast",
      herkunft: "Autopilot eines eigenen Kanals"
    },
    {
      id: "app-varianten", name: "App in 5 Varianten", kat: "web", stufe: "premium", status: "bereit", icon: "📱",
      kurz: "Erst fünf Entwürfe, dann die beste – so entsteht jede App.",
      kann: ["Baut fünf echte, klickbare Varianten", "Du wählst aus und mischst", "Neue Version, installierbar als App, veröffentlicht"],
      fuer: "Gründer mit App-Idee, Coaches, Dienstleister",
      herkunft: "AI Masterclass (z. B. Cocktail-App)"
    },
    {
      id: "lead-seiten", name: "Lead-Konzeptseiten", kat: "vertrieb", stufe: "premium", status: "vorbereitung", icon: "🧲",
      kurz: "Für jeden Interessenten eine eigene Konzept-Website als Vorschau.",
      kann: ["Analysiert die bestehende Seite eines Betriebs", "Baut eine branchenpassende Premium-Vorschau", "Fertig zum Zeigen im Erstgespräch"],
      fuer: "Webdesigner, Agenturen, Freelancer in der Akquise",
      herkunft: "MZ.9-Lead-Pipeline"
    },
    {
      id: "wettbewerb", name: "Wettbewerbsanalyse", kat: "vertrieb", stufe: "premium", status: "vorbereitung", icon: "🔍",
      kurz: "Wer bietet was zu welchem Preis – und wo ist deine Lücke?",
      kann: ["Findet Mitbewerber in deiner Region und Nische", "Vergleicht Angebote, Preise und Auftritt", "Leitet Chancen für dein Angebot und deinen Content ab"],
      fuer: "Selbstständige vor dem Start oder vor einer Preisrunde",
      herkunft: "Marktanalyse eines eigenen Projekts"
    },
    {
      id: "agentensystem", name: "Agentensystem", kat: "qualitaet", stufe: "premium", status: "vorbereitung", icon: "🧠",
      kurz: "Ein Prüfagent ohne Vorwissen prüft jedes Ergebnis, bevor du es siehst.",
      kann: ["Interview und Blindspot-Pass vor großen Projekten", "Korrekturen werden zu dauerhaften Regeln", "Recherchen laufen verteilt auf mehrere Modelle"],
      fuer: "Alle, die mit KI viel und verlässlich arbeiten",
      herkunft: "Maiks Arbeitsmodus mit Prüfer-Agent"
    },
    {
      id: "angebot-rechnung", name: "Angebot & Rechnung", kat: "buero", stufe: "basis", status: "geplant", icon: "🧾",
      kurz: "Aus ein paar Stichworten ein sauberes Angebot oder eine Rechnung.",
      kann: ["Vorlage mit deinen Daten", "Kleinbetragsrechnung oder mit Steuer", "Ablage im richtigen Ordner"],
      fuer: "Solo-Selbstständige ohne Buchhaltungs-Software",
      herkunft: "geplanter Basis-Skill"
    },
    {
      id: "post-check", name: "Post-Check", kat: "marke", stufe: "basis", status: "geplant", icon: "✅",
      kurz: "Prüft Hook, Caption und Hashtags, bevor du postest.",
      kann: ["Bewertet den Einstieg in den ersten Sekunden", "Schlägt bessere Hooks und Captions vor", "Checkliste gegen typische KI-Floskeln"],
      fuer: "Alle, die selbst posten",
      herkunft: "geplanter Basis-Skill"
    },
    {
      id: "meeting-aufgaben", name: "Meeting → Aufgaben", kat: "buero", stufe: "basis", status: "geplant", icon: "📝",
      kurz: "Aus Notizen oder Sprachmemo werden Aufgaben mit Termin.",
      kann: ["Fasst Gespräche kurz zusammen", "Zieht Aufgaben, Termine und Verantwortliche heraus", "Fertig für dein Board oder deinen Kalender"],
      fuer: "Alle mit vielen Gesprächen und wenig Zeit",
      herkunft: "geplanter Basis-Skill"
    }
  ],
  pakete: [
    { id: "content-engine", name: "Content-Engine", skills: ["creative-director", "design-system", "content-planer", "autopilot"], kurz: "Das komplette Content-System: planen, gestalten, produzieren, posten." }
  ],
  kontakt: { whatsapp: "4917645961547" }
};
