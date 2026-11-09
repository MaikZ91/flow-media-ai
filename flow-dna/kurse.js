// Online-Kurse von Flow Media AI (Tab „Kurse“ in der Flow-DNA-App). Stand 09.11.2026: Kurs 03 live, Rest in Planung („Coming soon“).
// status: "bald" = geplant/in Produktion · "live" = freigeschaltet (dann video/lektionen ergänzen).
// Themen aus Maiks echtem Content: Workshops, Masterclass, FLOW-Methode, eigene Skills und Systeme.
window.FLOW_KURSE = {
  hinweis: "Die Kurse nehme ich nach und nach auf. Merk dir die vor, die dich interessieren – du bekommst Bescheid, sobald sie starten.",
  kurse: [
    { id: "ki-basics", nr: "01", titel: "KI Basics", untertitel: "KI verstehen und sofort im Alltag nutzen", level: "Einsteiger", dauer: "ca. 90 Min.", status: "bald", bild: "img/maik_front.jpg",
      module: ["Was KI kann – und was nicht", "ChatGPT, Claude, Gemini: Welches Tool wofür?", "Gute Prompts in 5 Minuten", "Deine ersten 10 Alltagsaufgaben mit KI", "Datenschutz und Grenzen"] },
    { id: "personal-brand", nr: "02", titel: "Mit KI zur Personal Brand", untertitel: "Deine Marke, deine Stimme, dein Look – mit KI geschärft", level: "Einsteiger", dauer: "ca. 2 Std.", status: "bald", bild: "img/maik_avatar.jpg",
      module: ["Brand DNA: Wer bist du, für wen, warum?", "Deine Stimme als Skill festhalten", "Look & Design-System ohne Designer", "Fotos und Porträts richtig nutzen", "Dein Brand-Paket für jede KI"] },
    { id: "website", nr: "03", titel: "Bau deine Website mit Skill", untertitel: "Aus deinem Content wird deine eigene Website", level: "Einsteiger", dauer: "ca. 3 Min. Video", status: "live", url: "kurse/website-mit-skill/", bild: "media/r006.jpg",
      module: ["Hallo – das baust du heute", "Was ist ein Skill?", "Fünf Varianten statt einer", "Einrichten: Werkzeug, Ordner, Skill", "Live bauen: Prompt, Varianten, Launch", "Der Skill von innen – und dein eigener"] },
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
