// Online-Kurse von Flow Media AI (Tab „Kurse“ in der Flow-DNA-App). Stand 09.11.2026: Kurs 03 live, Rest in Planung („Coming soon“).
// status: "bald" = geplant/in Produktion · "live" = fertig. Mit code: nur nach Eingabe des Kurs-Codes (Merker in localStorage "dna-kurse-frei").
// Themen aus Maiks echtem Content: Workshops, Masterclass, FLOW-Methode, eigene Skills und Systeme.
window.FLOW_KURSE = {
  hinweis: "Die Kurse nehme ich nach und nach auf. Merk dir die vor, die dich interessieren – du bekommst Bescheid, sobald sie starten.",
  kurse: [
    { id: "ki-basics", nr: "01", titel: "KI Basics", untertitel: "KI verstehen und sofort im Alltag nutzen", level: "Einsteiger", dauer: "ca. 90 Min.", status: "bald", bild: "img/maik_front.jpg",
      module: ["Was KI kann – und was nicht", "ChatGPT, Claude, Gemini: Welches Tool wofür?", "Gute Prompts in 5 Minuten", "Deine ersten 10 Alltagsaufgaben mit KI", "Datenschutz und Grenzen"] },
    { id: "personal-brand", nr: "02", titel: "Mit KI zur Personal Brand", untertitel: "Deine Marke, deine Stimme, dein Look – mit KI geschärft", level: "Einsteiger", dauer: "ca. 2 Std.", status: "bald", bild: "img/maik_avatar.jpg",
      module: ["Brand DNA: Wer bist du, für wen, warum?", "Deine Stimme als Skill festhalten", "Look & Design-System ohne Designer", "Fotos und Porträts richtig nutzen", "Dein Brand-Paket für jede KI"] },
    { id: "website", nr: "03", titel: "Bau deine Website mit Skill", untertitel: "Aus deinem Content wird deine eigene Website", level: "Einsteiger", dauer: "ca. 3 Min. Video", status: "live", code: "WEBSITE", bild: "media/r006.jpg",
      intro: { video: "kurse/website-mit-skill/videos/L00.mp4", poster: "kurse/website-mit-skill/videos/L00.jpg", titel: "Hallo – das baust du heute" },
      hinweis: "Videos mit KI-Stimme, teils als Animation.",
      module: ["Content-Ordner anlegen", "Website-Skill einrichten", "5 Varianten bauen und auswählen", "Premium-Look: Hero, Branche, Pflicht-Bausteine", "Live stellen auf GitHub Pages", "Mit KI weiterpflegen"],
      lektionen: [
        { videos: [["kurse/website-mit-skill/videos/L03.mp4", "kurse/website-mit-skill/videos/L03.jpg", "Einrichten: Werkzeug, Ordner, Skill"]],
          text: "Alles, was die KI über dich wissen soll, liegt in einem Ordner. Erst sammeln, dann bauen.",
          punkte: ["Claude Code oder Codex installieren und anmelden", "Projektordner anlegen: <code>Media</code> für Fotos und Videos, <code>Texte</code> für alles über dich", "Was schon da ist, hat Vorrang: eigene Fotos, alte Website, Logo, Farben"],
          links: [["Claude Code", "https://claude.com/download", "Claude App mit Claude Code"], ["Codex", "https://openai.com/codex/", "Codex App von OpenAI"]],
          aufgabe: "Leg deinen Ordner an und pack 5 Fotos und einen Text über dich hinein." },
        { videos: [["kurse/website-mit-skill/videos/L01.mp4", "kurse/website-mit-skill/videos/L01.jpg", "Was ist ein Skill?"], ["kurse/website-mit-skill/videos/L05.mp4", "kurse/website-mit-skill/videos/L05.jpg", "Der Skill von innen"]],
          text: "Ein Skill ist eine Anleitung, die die KI liest und immer wieder nutzt. Du erklärst einmal, sie wendet es jedes Mal an.",
          punkte: ["<b>Name &amp; Beschreibung</b>: wann die KI den Skill nutzt", "<b>Anleitung</b>: Schritte, Regeln, dein Ton", "Website-Skill herunterladen und die ZIP in den Ordner <code>skills</code> legen"],
          links: [["Website-Skill", "?workshop=website", "Workshop-Seite mit Download"]],
          aufgabe: "Leg den Website-Skill in deinen Ordner und öffne den Ordner in Claude Code oder Codex." },
        { videos: [["kurse/website-mit-skill/videos/L02.mp4", "kurse/website-mit-skill/videos/L02.jpg", "Fünf Varianten statt einer"], ["kurse/website-mit-skill/videos/L04.mp4", "kurse/website-mit-skill/videos/L04.jpg", "Live bauen"]],
          text: "Der Skill rät nicht eine Lösung. Er baut fünf deutlich verschiedene Varianten – du wählst und mischst.",
          punkte: ["Start-Prompt: <code>Nutze den Website-Skill. Lies Media und Texte und bau mir fünf Varianten.</code>", "Varianten durchklicken, z. B. Layout von 03 und Farben von 05", "Daraus baut der Skill die finale Version"],
          aufgabe: "Schick den Start-Prompt und wähl deine Lieblingsvariante." },
        { folgt: true, text: "Hero, branchentypische Bausteine und alles, was eine Seite hochwertig wirken lässt. Diese Lektion nehme ich gerade auf." },
        { optional: true, text: "Wenn deine Seite für alle erreichbar sein soll. Du kannst sie auch erst mal nur lokal nutzen.",
          punkte: ["Kostenlosen GitHub-Account anlegen", "Dem Skill sagen: „Stell die Seite auf GitHub Pages online.“ Er fragt nach deinem Account", "Nach ein bis zwei Minuten ist sie erreichbar unter <code>deinname.github.io</code>"],
          links: [["GitHub", "https://github.com/signup", "Kostenlosen Account anlegen"]] },
        { folgt: true, text: "Texte, Bilder und neue Seiten später per Satz an die KI ändern. Diese Lektion nehme ich gerade auf." }
      ] },
    { id: "erste-app", nr: "04", titel: "Deine erste App", untertitel: "In 5 Schritten von der Idee zur App auf dem Handy", level: "Einsteiger", dauer: "ca. 2 Std.", status: "bald", bild: "media/r016.jpg",
      module: ["Die Idee schärfen: Problem, Nutzer, Funktion", "Anforderungen und Content sammeln", "5 Versionen bauen lassen", "Die beste wählen und verbessern", "Als App installierbar machen und teilen"] },
    { id: "claude-code", nr: "05", titel: "Claude Code für Einsteiger", untertitel: "Die KI, die für dich programmiert – Schritt für Schritt", level: "Fortgeschritten", dauer: "ca. 3 Std.", status: "bald", bild: "img/maik_front.jpg",
      module: ["Installation und erste Session", "Projektordner und CLAUDE.md", "Skills: Wissen, das bleibt", "Bauen, testen, verbessern", "GitHub und Veröffentlichen", "Arbeiten mit Agenten"] },
    { id: "content-system", nr: "06", titel: "Content-System mit KI", untertitel: "Reels, Posts und Captions, die nach dir klingen", level: "Einsteiger", dauer: "ca. 2 Std.", status: "bald", bild: "media/r028.jpg",
      module: ["Themenpool und Rotation", "Hooks, die stoppen", "Reels schneiden mit KI", "Captions in deinem Ton", "Zahlen lesen und lernen"] },
    { id: "automation", nr: "07", titel: "Automatisierung & Workflows", untertitel: "Wiederkehrende Arbeit an die KI abgeben", level: "Fortgeschritten", dauer: "ca. 2,5 Std.", status: "bald", bild: "media/r016.jpg",
      module: ["Prozesse finden, die sich lohnen", "Geplante Aufgaben und Routinen", "Daten zwischen Tools bewegen", "Instagram-Autopilot als Beispiel", "Fehler abfangen und überwachen"] },
    { id: "skills", nr: "08", titel: "Skills bauen & verkaufen", untertitel: "Dein Wissen als KI-Skill – für dich und für andere", level: "Fortgeschritten", dauer: "ca. 2 Std.", status: "bald", bild: "img/maik_avatar.jpg",
      module: ["Was ist ein Skill?", "Deinen ersten Skill schreiben", "Testen und verbessern", "Skill-Paket mit Vorlagen und Beispielen", "Im Flow DNA Store anbieten"] },
    { id: "flow-methode", nr: "09", titel: "Die FLOW-Methode", untertitel: "Fokussieren · Losbauen · Optimieren · Wachsen", level: "Alle", dauer: "ca. 2 Std.", status: "bald", bild: "img/maik_front.jpg",
      module: ["F – Fokussieren: Idea2Concept", "L – Losbauen: Concept2Prototype", "O – Optimieren: Prototype2Product", "W – Wachsen: Product2Business", "Dein 90-Tage-Plan"] },
    { id: "kunden-gewinnen", nr: "10", titel: "Kunden gewinnen mit KI", untertitel: "Websites analysieren, Konzepte bauen, ehrlich anschreiben", level: "Fortgeschritten", dauer: "ca. 2 Std.", status: "bald", bild: "media/r017.jpg",
      module: ["Zielgruppe und Region wählen", "Websites automatisch bewerten", "Konzeptseiten im Branchen-Look", "Rechtssicher Kontakt aufnehmen", "Dein Lead-System im Alltag"] }
  ]
};
