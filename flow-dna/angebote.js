// Angebote von Flow Media AI für die Flow-DNA-App (Tab „Angebote“). Nur echte Angaben – Stand 12.11.2026.
// Workshop-Termine: vergangene Termine blendet die App automatisch aus. Neue Termine hier eintragen –
// sie erscheinen im Tab „Angebote“ und im Community-Kalender. Weitere Termine (z. B. Stammtisch) in `termine` mit art, titel, datum, ende, ort.
window.FLOW_ANGEBOTE = {
  calendly: "https://calendly.com/flow_media_ai/1-kennenlernen",
  workshopGruppe: "https://chat.whatsapp.com/KZkXQMCsoxrJygPYgfrqB2",
  supportGruppe: "https://chat.whatsapp.com/KnRP9BMgQxZ6V5lcO0KnvQ",
  workshops: [
    { titel: "Von deiner KI-Idee zum digitalen Produkt", tag: "Montag", datum: "2026-11-16T18:00:00+01:00", ende: "19:00", preis: "69 €", format: "Live · 60 Min",
      text: "Egal ob App, Website, Automatisierung oder Buch: In 60 Minuten machst du aus deiner Idee ein erstes digitales Produkt – mit der FLOW-Methode und den Flow-DNA-Skills. Am Ende hast du etwas Echtes, das du selbst weiterentwickelst.",
      extra: "Vorbereitung: vorher Claude Code oder Codex einrichten (Workshop-Start in der App). Danach kostenloser Tech-Support im Tech-Support-Channel." },
    { titel: "Mit KI zur Personal Brand: Deine Website", tag: "Montag", datum: "2026-11-09T18:00:00+01:00", ende: "19:00", preis: "59 €", format: "Live · 60 Min",
      text: "Aus deinen Bildern, Videos, Texten und deinem Stil wird deine eigene Website – mit der FLOW-Methode und dem Website-Skill. Den Skill bekommst du als Teilnehmer kostenlos, danach bearbeitest du deine Seite selbst mit KI weiter.",
      extra: "Bis 31.12.26 kostenloser Tech-Support und Q&A im Tech-Support-Channel." },
    { titel: "Mit KI zur Personal Brand: Deine Website", tag: "Dienstag", datum: "2026-11-10T18:00:00+01:00", ende: "19:00", preis: "59 €", format: "Live · 60 Min",
      text: "Zweiter Termin mit demselben Inhalt – such dir den passenden Abend aus.",
      extra: "Bis 31.12.26 kostenloser Tech-Support und Q&A im Tech-Support-Channel." }
  ],
  termine: [],
  angebote: [
    { id: "erstgespraech", nr: "01", art: "Kostenlos", name: "Erstgespräch", kurz: "Wir sprechen über deine Idee und schauen, wie ich dich am besten unterstützen kann.",
      punkte: ["Kostenlos und unverbindlich", "Termin direkt online wählen"], cta: "Termin wählen", typ: "calendly" },
    { id: "begleitung", nr: "02", art: "Das Herzstück", name: "1:1-Begleitung", kurz: "Dein persönlicher KI-Sparringspartner: Ich begleite dich über Monate, bis aus deiner Idee ein laufendes Business wird – nach der FLOW-Methode.",
      punkte: ["Laufzeit 3 oder 6 Monate", "Jede Woche 1 Stunde Sparring: Strategie, Technik, neue Ideen", "KI-Masterclass: 7 Stunden rund um Claude Code und KI-gestützte Entwicklung", "Ziel: Du setzt deine Ideen wirklich um und arbeitest selbstständiger mit KI"],
      phasen: [["F", "Fokussieren", "Idea2Concept"], ["L", "Losbauen", "Concept2Prototype"], ["O", "Optimieren", "Prototype2Product"], ["W", "Wachsen", "Product2Business"]],
      cta: "Erstgespräch buchen", typ: "calendly", wa: "Hi Maik, ich interessiere mich für die 1:1-Begleitung (3 oder 6 Monate). Kannst du mir mehr erzählen?" },
    { id: "projekt", nr: "03", art: "Build", name: "Dein Projekt", kurz: "Du brauchst eine App, ein eigenes Tool, eine Website oder eine Automatisierung? Ich baue es mit KI – und zeige dir, wie du es selbst weiterführst.",
      punkte: ["Apps & Tools", "Websites", "Automatisierung"], cta: "Erstgespräch buchen", typ: "calendly", wa: "Hi Maik, ich habe eine Projektidee: " },
    { id: "community", nr: "04", art: "Kostenlos", name: "Flow Business Community", kurz: "Austausch, Feedback, erste Schritte mit KI – in Bielefeld, Münster und digital, mit digitalem Stammtisch.",
      punkte: ["Business & Marketing", "KI & digitale Tools", "Digitaler Stammtisch"], cta: "Community beitreten", typ: "community" }
  ],
  support: {
    hinweis: "Kostenloser Tech-Support für Workshop-Teilnehmende bis 31.12.26. Schreib dein Problem kurz – am besten mit Screenshot.",
    themen: ["Skill installieren", "Code einlösen", "Website live stellen", "Claude Code / Codex", "Etwas anderes"],
    faq: [
      ["Wohin kommt ein Skill?", "In deinen Projektordner unter skills/<name>/SKILL.md. Free-Skills lädst du als ZIP, entpackst sie und legst den Ordner dorthin. Im Store gibt es dafür auch den Button „Direkt nutzen“."],
      ["Wie löse ich einen Code ein?", "Skill im Store öffnen, unten „Lizenz-Code einlösen“, Code eintippen, „Laden“. Die Datei SKILL.md landet in deinen Downloads."],
      ["Wie stelle ich meine Website live?", "Der Website-Skill fragt dich am Ende: eigener GitHub-Account (GitHub Pages, kostenlos), ein anderer Account oder nur lokal. Sag ihm einfach, was du willst – er führt dich durch."],
      ["Der Skill reagiert nicht", "Prüfe, ob die Datei wirklich SKILL.md heißt und im Ordner skills liegt. Dann Claude Code im Projektordner neu starten. Hilft das nicht: unten Frage stellen."]
    ]
  }
};
