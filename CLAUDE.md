# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## Wofür dieses Repo da ist

Grundlage für **FLOW MEDIA AI**, das Business von Maik. Hier entstehen Positionierung, Content (Social-Media-Posts, Texte, Workshops), Angebote und eigene Projekte.

**Für Claude gilt:**
- Alle Texte, Posts und Angebote richten sich nach diesem Profil, insbesondere nach Abschnitt 9 (Tonalität) und 10 (Content-Regel).
- Nichts erfinden: keine Kunden, Umsätze, Ergebnisse, Testimonials oder Erfahrungen, die nicht tatsächlich existieren. Fehlt eine Angabe, nachfragen oder als Platzhalter markieren.
- Sprache für Inhalte: natürliches, modernes Deutsch.
- Für alles rund um Instagram (@flow.media.ai) zuerst den Skill `creative-director` laden (`.claude/skills/creative-director/SKILL.md`).
- Dieses Repo ist nur für Flow Media AI. THE TRIBE, Dating-Fotos und Arbeitgeber-Projekte gehören nicht hierher.

## Aufbau

- `CLAUDE.md` – Brand Identity & Positionierung (maßgeblich)
- `.claude/skills/creative-director/` – Creative Director für @flow.media.ai
- `.claude/skills/flow-design/` – visuelles Design (schwarz-weiß, große Versal-Headlines, ein blauer Akzent) für alles Gestaltete
- `.claude/skills/blindspot-analyse/` – optional, nur wenn Maik ihn einschaltet: Blindspot-Pass vor neuen Projekten
- `auswertungen/` – Auswertungen (z. B. Blindspot-Analysen)
- `.claude/skills/pruefer-agent/` – optional, nur wenn Maik ihn einschaltet: Prüfagent, Interview, Regeln aus Korrekturen, verteilte Recherche
- `content/01_startplan.md` – Startplan der ersten zwei Wochen
- `content/learnings.md` – Ergebnisse und Erkenntnisse je Post

## Google-Drive-Spiegel (Pflicht, Maik 19.10.2026)

Maiks Google Drive `Flow Media AI` (Ordner-ID `1b0BfA5Y56OwA3-RBMhKXakpJ4dKOBRiU`) wird immer auf Stand gehalten – **vor allem `07_KI`**. Das Repo ist die Quelle; Drive ist die Ablage, mit der Maik arbeitet. Dropbox wird nicht mehr genutzt (seit 19.10.2026).

**Nach jeder Änderung an einer dieser Dateien im selben Lauf Drive aktualisieren** (über den Google-Drive-Connector). Markdown wird als Google Doc angelegt (`contentMimeType: text/markdown`, Titel ohne `.md`):

| Repo | Drive (`Flow Media AI/…`) |
|---|---|
| `CLAUDE.md` bis zur Linie `---` (Claude-Kopf; für Abschnitte 1–10 ein Verweis auf die Brand Identity) | `07_KI/CLAUDE` |
| `.claude/skills/<name>/…` (jede Datei, auch neue Skills) | `07_KI/skills/<name>/…` |
| `auswertungen/…` | `07_KI/auswertungen/…` |
| `CLAUDE.md`, Abschnitte 1–10 (ohne Claude-Kopf) | `01_Marketing/Brand_Identity_Flow_Media_AI` |
| `content/01_startplan.md` | `01_Marketing/Startplan_Instagram` |
| `content/learnings.md` | `01_Marketing/Learnings_Instagram` |
| `content/reels/<ID>-<name>/README.md` | `01_Marketing/Reels/<ID>_<Name>_Caption` |
| `marketing/brand/…` | `01_Marketing/Brand/…` |
| `organisatorisch/…`, `finanzen/…` | `06_Organisatorisch/…`, `05_Finanzen/…` |

Ordner-IDs (für `parentId`): 01_Marketing `1dE9gJaTmDR0yIFP6rQBiMXr4m29L4vZh` · Reels `1zKIB3-yuIU6WztZSCa0fSOQticuFop8_` · Brand `1Uo0TsUUVeM7JdP6bd8z1X88SI0nQiRpd` · 02_Sales `1GX1UZHT8ekuAxa092GTfSZpQdXt6kRVj` · 03_Produkt `17FWXK648mnTtJaYaraj9A0q3MygRd441` · 04_Coachings `1fJZyU7NHzPUXTkOpBLtIUdN94CUkcx2o` · 05_Finanzen `1q_i8soVlfHsLp4NtEnqBrqXdKaY5lhlB` · Steuern `1r44DkyTilqd6Fm3sRsU7gdatz75P5m9N` (Rechnungen Debitoren `1mknCxYXfBCPY6CQoJcDo5lP8Sz5dMisM`, Rechnungen Kreditoren `1q-qhGmQPtcB0N4b84cfPCi4R8NLgWl-9`, Kontoauszüge `1ND1pSmTKFAIlS0SJpiL6GN599J_LErnV`) · Vorlagen IOF `1nXVwE5-oyOb1ibWbpP5wK0rrb4EcYUDU` · 06_Organisatorisch `1mhm_BW2sqDZZe2XfnbdLJKj257_XxTr7` · 07_KI `1LIw5RIjPsS0pYNPJSKRN9AxYBlvjueDi` · skills `1-iZidnDBICbcPJjf4r3B-Kv8V7IcbpNH` · auswertungen `1CGUnlkzDWw6C5nOFmWvEHKosDqUMHMwe`. Neue Ordner anlegen und hier nachtragen.

- **Kundenunterlagen** (Angebote, Briefings, Kundenkarten) und Belege liegen **nur in Drive**, nie im Repo (öffentlich). Pro Kunde ein Ordner unter `04_Coachings/<Datum>_<Name>_<Thema>`.
- **Aktualisieren = ersetzen:** Der Connector kann Inhalte nicht überschreiben. Darum die alte Datei in den Papierkorb (`trash_file`, wiederherstellbar) und neu anlegen. Vorher per `search_files` (`parentId = '<ordner>'`) die Datei-ID suchen.
- **Binärdateien** (PDF, Bilder, Videos, Excel) gehen nur über `base64Content`, und den Inhalt muss Claude dabei Zeichen für Zeichen mitschicken – ab ein paar KB unzuverlässig (Test 19.10.2026: 67-KB-PDF kam kaputt an). Darum: Dokumente wie Angebote und Rechnungen als **Google Doc** anlegen (`contentMimeType: text/html` mit Inline-Styles oder `text/markdown`); Maik exportiert bei Bedarf selbst als PDF (Datei → Herunterladen → PDF). Fertige PDFs, Bilder und Videos legt Maik selbst ab – in der Antwort sagen, welche Datei wohin.
- Gelöschte oder umbenannte Dateien im Repo auch in Drive löschen bzw. umbenennen.
- Ändert Maik etwas direkt in Drive (z. B. im Google Doc), vor der nächsten Änderung dort nachsehen (`read_file_content`) und ins Repo übernehmen, statt es zu überschreiben.
- Ist der Drive-Connector in einer Session nicht verfügbar: Maik am Ende sagen, welche Dateien noch nicht gespiegelt sind.
- In der Antwort an Maik kurz nennen, was in Drive aktualisiert wurde.

---

# FLOW MEDIA AI – Brand Identity & Positionierungsprofil

## 1. Wer ich bin

Ich bin Maik und beschäftige mich mit den Möglichkeiten von künstlicher Intelligenz, digitaler Produktentwicklung, Automatisierung und kreativer Umsetzung.

Mich fasziniert, wie schnell man heute aus einer Idee etwas Reales machen kann. Was früher viel Zeit, verschiedene Dienstleister oder umfangreiche technische Kenntnisse erforderte, lässt sich mit den richtigen KI-Tools oft deutlich schneller umsetzen.

Ich entwickle selbst Apps, Websites, Tools und Automatisierungen und experimentiere damit, wie sich KI sinnvoll in reale Projekte integrieren lässt. Ein Beispiel dafür ist THE TRIBE, meine Community für echte Begegnungen in Bielefeld und Münster, für die ich digitale Lösungen entwickle.

Ich möchte nicht nur über KI reden. Ich möchte Dinge damit bauen, ausprobieren und zeigen, was tatsächlich möglich ist.

## 2. Mein persönliches Why

Ich möchte meine Kreativität und meine Fähigkeiten mit KI nutzen, um Ideen umzusetzen, echte Probleme zu lösen und mir ein unabhängiges, selbstbestimmtes Leben aufzubauen.

Ich möchte selbst entscheiden, mit wem ich arbeite, welche Projekte ich umsetze, wo ich lebe und welchen Wert ich schaffe.

Mich motiviert die Möglichkeit, innerhalb kurzer Zeit etwas zu entwickeln, das Menschen begeistert, Unternehmen weiterbringt oder Arbeit spürbar erleichtert.

Ich möchte meine Fähigkeiten nicht ausschließlich gegen Arbeitszeit eintauschen. Ich möchte Lösungen schaffen, deren Wert sich am Ergebnis orientiert.

Gleichzeitig macht es mir Spaß, andere Menschen für die Möglichkeiten von KI zu begeistern und ihnen zu zeigen, dass sie eigene Ideen umsetzen können, die sie sich vorher vielleicht nicht zugetraut hätten.

Flow Media AI ist für mich deshalb mehr als ein Business. Es ist die Möglichkeit, meine Kreativität, meine Begeisterung für Technologie und meinen Wunsch nach Freiheit miteinander zu verbinden.

## 3. Meine Mission

Ich helfe Menschen und Unternehmen dabei, die Möglichkeiten von KI praktisch zu nutzen, eigene Ideen schneller umzusetzen und unnötigen Aufwand zu reduzieren.

Dabei geht es mir nicht darum, KI um ihrer selbst willen einzusetzen. Entscheidend ist, was am Ende entsteht:

- weniger manuelle Arbeit
- effizientere Prozesse
- schnellere Umsetzung von Ideen
- neue digitale Produkte und Möglichkeiten
- mehr Zeit für die Dinge, die wirklich wichtig sind

Ich verbinde technologische Möglichkeiten mit kreativem Denken und pragmatischer Umsetzung.

## 4. Meine Positionierung

**Flow Media AI – Ideen umsetzen. Arbeit vereinfachen. Möglichkeiten schaffen.**

Ich verbinde KI, Automatisierung und digitale Produktentwicklung, um aus Ideen konkrete Lösungen zu machen.

Mögliche Leistungsbereiche:

- **KI & Automatisierung:** Wiederkehrende Aufgaben vereinfachen und Prozesse effizienter gestalten.
- **Apps & Websites:** Digitale Produkte, Plattformen und individuelle Tools entwickeln.
- **KI-gestützte Content-Produktion:** Inhalte, Bilder, Videos und Werbemittel effizient erstellen.
- **Social-Media-Automatisierung:** Unternehmen dabei unterstützen, regelmäßig sichtbar zu bleiben, ohne dass Social Media unnötig viel Zeit kostet.
- **KI-Workshops & Masterclasses:** Menschen befähigen, selbst Websites, Apps und andere digitale Projekte umzusetzen.

Diese Bereiche sind mögliche Bausteine des Geschäftsmodells. Sie müssen nicht alle gleichzeitig angeboten oder gleich stark kommuniziert werden.

## 5. Meine Zielgruppe

Ich möchte mit Menschen und Unternehmen zusammenarbeiten, die neugierig, offen und bereit sind, neue Wege auszuprobieren.

Wichtiger als eine bestimmte Branche ist zunächst die gemeinsame Haltung.

Meine idealen Kunden:

- interessieren sich für KI oder erkennen, dass sich ihre Arbeitsweise verändern kann
- haben konkrete Probleme, Ideen oder Prozesse, die verbessert werden sollen
- schätzen pragmatische Lösungen statt endloser Konzeptarbeit
- sind offen für neue Möglichkeiten und ehrliche Zusammenarbeit
- wollen Ergebnisse sehen und nicht nur über Innovation sprechen

Besonders interessante Anwendungsfelder können lokale Unternehmen, Gesundheit und Fitness, Gastronomie, Events sowie andere Dienstleister sein.

Ich möchte niemanden davon überzeugen müssen, dass KI grundsätzlich spannend ist. Ich möchte mit Menschen arbeiten, die selbst etwas bewegen wollen.

## 6. Was mich unterscheidet

Ich denke nicht ausschließlich technisch und nicht ausschließlich kreativ.

Ich verbinde beides: Ich sehe eine Möglichkeit, entwickle eine Idee und versuche, sie möglichst schnell praktisch umzusetzen.

Ich muss nicht erst monatelang über ein Produkt sprechen, bevor ein erster Prototyp entsteht. Ich kann experimentieren, testen, verbessern und konkrete Ergebnisse zeigen.

Meine Stärke liegt darin, Möglichkeiten zu erkennen und daraus etwas Nutzbares zu machen.

Dabei ist KI für mich kein Selbstzweck und kein magisches Versprechen. Sie ist ein Werkzeug, mit dem sich viele Dinge anders, schneller und zugänglicher umsetzen lassen.

## 7. Meine Werte

**Stand 20.10.2026 – meine Werte gerade:**

Macht · Mut · Pragmatismus · Risiko · Entwicklung · Erfolg · Flow · Fokus · Freiheit · Herausforderung · Innovation · Inspiration · Intuition · Kreativität · Selbstvertrauen · Sinnhaftigkeit · Spontaneität · Struktur · Tiefe · Unabhängigkeit · Verlässlichkeit · Visionen · Wachstum · Wahrheit · Weiterentwicklung · Zuverlässigkeit

Bisherige Ausformulierung (18.10.2026):

- **Freiheit:** Ich möchte selbst entscheiden, wie ich arbeite und was ich erschaffe.
- **Kreativität:** Ich möchte Ideen nicht nur sammeln, sondern in die Realität bringen.
- **Pragmatismus:** Lieber etwas Funktionierendes bauen und verbessern als endlos darüber reden.
- **Authentizität:** Ich kommuniziere ehrlich, persönlich und ohne künstliche Erfolgsgeschichten.
- **Partnerschaft:** Ich möchte mit Kunden arbeiten, bei denen die menschliche Ebene stimmt.
- **Wirksamkeit:** Am Ende zählt, ob eine Lösung tatsächlich hilft, Arbeit erleichtert oder neue Möglichkeiten schafft.
- **Befähigung:** Ich möchte Menschen nicht abhängig von mir machen, sondern ihnen zeigen, was sie selbst erreichen können.

## 8. Meine persönliche Geschichte als Content-Grundlage

Ich habe erlebt, wie schnell sich Ideen mit KI umsetzen lassen. Gleichzeitig merke ich in meinem Arbeitsalltag, dass gute Ergebnisse nicht immer bedeuten, dass man seine Zeit optimal einsetzen kann.

Wenn ich eine Aufgabe effizient erledige, möchte ich nicht einfach nur die verbleibende Zeit absitzen. Ich möchte meine Fähigkeiten weiterentwickeln, neue Ideen ausprobieren und mehr aus dem machen, was ich kann.

Mit Flow Media AI möchte ich herausfinden, wie weit ich damit gehen kann.

Ich möchte ein Geschäftsmodell aufbauen, bei dem nicht allein die investierten Stunden zählen, sondern der Wert der Ergebnisse. Ich möchte Projekte auswählen, die mich interessieren, mit Menschen arbeiten, die zu mir passen, und mir langfristig mehr Unabhängigkeit schaffen.

Ich teile auf diesem Weg nicht nur fertige Ergebnisse, sondern auch Experimente, Erkenntnisse, funktionierende Lösungen und Dinge, die nicht auf Anhieb klappen.

THE TRIBE ist ein Beispiel dafür, wie ich KI und digitale Werkzeuge bereits praktisch einsetze. Flow Media AI soll daraus ein eigenständiges Geschäftsmodell entwickeln.

## 9. Wie meine Social-Media-Posts klingen sollen

Schreibe persönlich, direkt, neugierig und praxisnah.

Die Kommunikation soll nach einem kreativen Menschen klingen, der Dinge selbst ausprobiert und seine Erkenntnisse teilt – nicht nach einer klassischen Agentur, einem Unternehmensberater oder einem KI-generierten Werbetext.

### Sprachstil

- Schreibe in natürlichem, modernem Deutsch.
- Verwende kurze bis mittellange Sätze.
- Sei selbstbewusst, aber nicht arrogant.
- Zeige Begeisterung, ohne künstlich zu übertreiben.
- Erkläre technische Möglichkeiten verständlich.
- Sprich über konkrete Ergebnisse und reale Anwendungsfälle.
- Nutze persönliche Beobachtungen, eigene Projekte und Erfahrungen als Ausgangspunkt.
- Verwende Humor, wenn er natürlich passt.
- Sei kritisch gegenüber übertriebenen KI-Versprechen.
- Vermeide unnötigen Fachjargon und Marketingfloskeln.

### Inhaltliche Schwerpunkte

1. **Build in public:** Zeige, was du mit KI baust – Apps, Websites, Tools, Automatisierungen und digitale Produkte.
2. **Aha-Momente:** Zeige Möglichkeiten, die viele Menschen noch nicht kennen.
3. **Praktischer Nutzen:** Erkläre, wie KI Zeit spart, Abläufe vereinfacht oder neue Ideen ermöglicht.
4. **Experimente:** Teile Tests, Learnings, Fehler und Verbesserungen.
5. **Persönlicher Weg:** Erzähle ehrlich vom Aufbau von Flow Media AI, deinen Zielen und deinen Herausforderungen.
6. **Kreativität mit KI:** Zeige, wie aus einem Gedanken ein konkretes Ergebnis wird.
7. **Wissen weitergeben:** Gib praktische Impulse und zeige, wie andere selbst ins Umsetzen kommen.
8. **Geschäftlicher Mehrwert:** Erkläre, wie Unternehmen KI sinnvoll nutzen können, ohne jedem neuen Trend hinterherzulaufen.

### Regeln für gute Posts

- Beginne mit einer konkreten Beobachtung, einer überraschenden Erkenntnis, einer Frage oder einem greifbaren Ergebnis.
- Liefere echten Mehrwert, statt nur Aufmerksamkeit zu erzeugen.
- Zeige nach Möglichkeit das Ergebnis oder den tatsächlichen Anwendungsfall.
- Verbinde technische Möglichkeiten mit einem menschlichen oder geschäftlichen Nutzen.
- Schreibe nicht jeden Post wie eine Verkaufsanzeige.
- Verkaufe dort, wo es sinnvoll ist, aber dränge nicht in jeden Beitrag einen Call-to-Action.
- Stelle keine Ergebnisse, Kunden, Umsätze oder Erfahrungen als real dar, wenn sie nicht tatsächlich existieren.
- Erfinde keine Erfolgsgeschichten und verspreche keine unrealistischen Einsparungen.
- Nutze Emojis sparsam und nur, wenn sie wirklich passen.
- Vermeide generische Einstiege wie „In der heutigen digitalen Welt“, „KI revolutioniert alles“ oder „Die Zukunft ist jetzt“.
- Vermeide künstliche Kontraste, übertriebene Superlative und typische KI-Floskeln.
- Verwende keine künstliche Motivation oder leere Hustle-Phrasen.

### Die gewünschte Wirkung

Menschen sollen nach einem Beitrag denken:

- „Krass, das wusste ich noch gar nicht.“
- „Das könnte ich für mein eigenes Projekt nutzen.“
- „Der setzt die Dinge wirklich selbst um.“
- „Das könnte meinem Unternehmen konkret helfen.“
- „Ich würde gerne lernen, wie das funktioniert.“
- „Mit dem könnte ich mir eine Zusammenarbeit vorstellen.“

## 10. Übergeordnete Content-Regel

**Nicht nur erzählen, was KI kann. Zeigen, was du damit machst und was dadurch möglich wird.**

Der Content soll meine Entwicklung dokumentieren, praktische Möglichkeiten vermitteln und Vertrauen aufbauen. Aus dieser Grundlage sollen sich sowohl Kundenprojekte als auch Workshops, Masterclasses und digitale Produkte entwickeln können.

Das langfristige Ziel ist ein Geschäft, das zu meinen Fähigkeiten und Werten passt: kreativ, wirksam, wirtschaftlich tragfähig und unabhängig.
