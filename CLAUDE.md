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
- `.claude/skills/app-in-varianten/` – Maiks Workflow für jede App: fünf Varianten bauen, Maik fragen, neue Version auf der Grundlage bauen, dann veröffentlichen (zuerst in diesem Repo unter `coaching/<kunde>/`)
- `.claude/skills/content-themen/` – Themenpool, Rotation und Verlauf für den täglichen Content
- **Daily-Content-Routine:** jeden Morgen ein fertiger Post im Chat (Creative Director Teil E); Reels in `content/reels/`, Karussells/Einzelposts in `content/posts/`
- `.claude/skills/blindspot-analyse/` – optional, nur wenn Maik ihn einschaltet: Blindspot-Pass vor neuen Projekten
- `auswertungen/` – Auswertungen (z. B. Blindspot-Analysen)
- `.claude/skills/pruefer-agent/` – optional, nur wenn Maik ihn einschaltet: Prüfagent, Interview, Regeln aus Korrekturen, verteilte Recherche
- `content/01_startplan.md` – Startplan der ersten zwei Wochen
- `content/learnings.md` – Ergebnisse und Erkenntnisse je Post
- `content/musik/` – Musik für Reels: eigene MZ.9-Tracks (`eigene/`) und freie Musik (`frei/`), Katalog im README
- `coaching/<kunde>/` – Apps aus Coachings, die öffentlich laufen dürfen (über GitHub Pages). `coaching/adil/`: Cocktail-App für Adil, live unter https://maikz91.github.io/flow-media-ai/coaching/adil/. Kundenunterlagen (Anforderungen, Angebote) bleiben in Drive.

## Google-Drive-Spiegel (Pflicht, Maik 19.10.2026)

Maiks Google Drive `Flow Media AI` (Ordner-ID `1b0BfA5Y56OwA3-RBMhKXakpJ4dKOBRiU`) wird immer auf Stand gehalten – **vor allem `07_KI`**. Das Repo ist die Quelle; Drive ist die Ablage, mit der Maik arbeitet. Dropbox wird nicht mehr genutzt (seit 19.10.2026).

**Gesammelt spiegeln (Maik, 25.10.2026):** Nicht nach jeder einzelnen Änderung, sondern einmal am Ende eines Arbeitsblocks bzw. auf Maiks Kommando „Drive spiegeln“ – jede geänderte Datei dann genau einmal (über den Google-Drive-Connector), damit nicht ständig Freigabe-Abfragen kommen. Markdown wird als Google Doc angelegt (`contentMimeType: text/markdown`, Titel ohne `.md`):

| Repo | Drive (`Flow Media AI/…`) |
|---|---|
| `CLAUDE.md` bis zur Linie `---` (Claude-Kopf; für Abschnitte 1–10 ein Verweis auf die Brand Identity) | `07_KI/CLAUDE` |
| `.claude/skills/<name>/…` (jede Datei, auch neue Skills) | `07_KI/skills/<name>/…` |
| `auswertungen/…` | `07_KI/auswertungen/…` |
| `CLAUDE.md`, Abschnitte 1–10 (ohne Claude-Kopf) | `01_Marketing/Brand_Identity_Flow_Media_AI` (daneben Maiks eigenes Doc `Persoenlichkeitsprofil_und_Werte_Maik` – nie überschreiben) |
| `content/01_startplan.md` | `01_Marketing/Startplan_Instagram` |
| `content/learnings.md` | `01_Marketing/Learnings_Instagram` |
| `marketing/brand/…` | `01_Marketing/Brand/…` |
| `organisatorisch/…`, `finanzen/…` | `06_Organisatorisch/…`, `05_Finanzen/…` |
| `workshops/<datum>_<thema>/…` (Workshop-Material, Skills) | `04_Coachings/Workshops/<Workshop-Name>/…` (Skill-Dateien als `.md` ohne Umwandlung, README als Google Doc) |
| `coaching/adil/README.md` (Code und Bilder werden nicht gespiegelt, die App läuft über GitHub Pages) | `04_Coachings/2026-11-01_Adil_Trading-App/Cocktail-App/README` (dort auch die Produktanforderungen, nur in Drive) |

**Caption-Docs werden nicht mehr nach Drive gespiegelt** (Maik, 25.10.2026): Reel-/Post-READMEs bleiben nur im Repo, die Caption steht ohnehin im Chat. Fertige Videos/Bilder legt Maik selbst in die Themenordner unter `01_Marketing/Content`.

Ordner-IDs (für `parentId`): 01_Marketing `1dE9gJaTmDR0yIFP6rQBiMXr4m29L4vZh` · RAW (Rohvideos, „Jeder mit dem Link“ freigegeben, Download per `curl https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t`) `1I5Cm2LTCqCB-cJW8cZE4Qwnxti4P5Exi` · Content (früher „Reels“; fertige Videos/Bilder sortiert Maik in die Themenordner: Apps `1xYxUBh0_bKI5YMVJ9ef84vxQhppO0Tg0`, Personal `15ePV3yAwAKMB5kGo6aNOA4C3VqqwiNtU`, Workshops `1fwgeyYybhH_6RnqjtO0tLRxSRVnsCHmJ`, Automation `1taBnBqXqXqmxFpwZbSshQnVchxB7S99c`, Community `1VDt4LXFIaoviYiF_WktsP8cRM3YGLf64`) `1zKIB3-yuIU6WztZSCa0fSOQticuFop8_` · Posts `1km5q-J_uGggM02g9GEGcuxY-0Y4kI_B0` · Brand `1Uo0TsUUVeM7JdP6bd8z1X88SI0nQiRpd` · 02_Sales `1GX1UZHT8ekuAxa092GTfSZpQdXt6kRVj` · 03_Produkt `17FWXK648mnTtJaYaraj9A0q3MygRd441` · 04_Coachings `1fJZyU7NHzPUXTkOpBLtIUdN94CUkcx2o` (Workshops `12s3d8dNBtL_ZDxpN-gm_Fdc9WKYI7eKC`: Von KI zur Personal Brand 1 `1_nd9j-hsFcfvaoTIX2Rw_q4db2cCPzY1`, Von KI zur Personal Brand 2 `1kk3nW66il7Ws2boZIoKWN4-xmk-rmPkB`; Adil `1qyAioTVc-j8zE7TPqFvg47LBLV39cyxa` mit Cocktail-App `1aNBJ_iaaDJdLYHm2_G32c5qHomlxyhx0`) · 05_Finanzen `1q_i8soVlfHsLp4NtEnqBrqXdKaY5lhlB` · Steuern `1r44DkyTilqd6Fm3sRsU7gdatz75P5m9N` (Rechnungen Debitoren `1mknCxYXfBCPY6CQoJcDo5lP8Sz5dMisM`, Rechnungen Kreditoren `1q-qhGmQPtcB0N4b84cfPCi4R8NLgWl-9`, Kontoauszüge `1ND1pSmTKFAIlS0SJpiL6GN599J_LErnV`) · Vorlagen IOF `1nXVwE5-oyOb1ibWbpP5wK0rrb4EcYUDU` · 06_Organisatorisch `1mhm_BW2sqDZZe2XfnbdLJKj257_XxTr7` · 07_KI `1LIw5RIjPsS0pYNPJSKRN9AxYBlvjueDi` · skills `1-iZidnDBICbcPJjf4r3B-Kv8V7IcbpNH` (app-in-varianten `1frL9M5BIC8lNQfxnFZfcbw-VH3QR7oyf`) · auswertungen `1CGUnlkzDWw6C5nOFmWvEHKosDqUMHMwe`. Neue Ordner anlegen und hier nachtragen.

- **Kundenunterlagen** (Angebote, Briefings, Kundenkarten) und Belege liegen **nur in Drive**, nie im Repo (öffentlich). Pro Kunde ein Ordner unter `04_Coachings/<Datum>_<Name>_<Thema>`.
- **Aktualisieren = ersetzen:** Der Connector kann Inhalte nicht überschreiben. Darum die alte Datei in den Papierkorb (`trash_file`, wiederherstellbar) und neu anlegen. Vorher per `search_files` (`parentId = '<ordner>'`) die Datei-ID suchen.
- **Binärdateien** (PDF, Bilder, Videos, Excel) gehen nur über `base64Content`, und den Inhalt muss Claude dabei Zeichen für Zeichen mitschicken – ab ein paar KB unzuverlässig (Test 19.10.2026: 67-KB-PDF kam kaputt an). Darum: Dokumente wie Angebote und Rechnungen als **Google Doc** anlegen (`contentMimeType: text/html` mit Inline-Styles oder `text/markdown`); Maik exportiert bei Bedarf selbst als PDF (Datei → Herunterladen → PDF). Fertige PDFs, Bilder und Videos legt Maik selbst ab – in der Antwort sagen, welche Datei wohin.
- Gelöschte oder umbenannte Dateien im Repo auch in Drive löschen bzw. umbenennen.
- Ändert Maik etwas direkt in Drive (z. B. im Google Doc), vor der nächsten Änderung dort nachsehen (`read_file_content`) und ins Repo übernehmen, statt es zu überschreiben.
- Ist der Drive-Connector in einer Session nicht verfügbar: Maik am Ende sagen, welche Dateien noch nicht gespiegelt sind.
- In der Antwort an Maik kurz nennen, was in Drive aktualisiert wurde.

---

# FLOW MEDIA AI – Brand Identity & Positionierungsprofil

**Stand 06.11.2026 – neue Positionierung (Maik).** Markenversprechen: **We build your ideas.**
KI • Kreativität • Automatisierung • Media • Digitale Produkte

**Die Positionierung in einem Satz (strategische Leitlinie für alles, was Flow Media AI anbietet):**
Flow Media AI begleitet Gründer und Selbstständige als persönlicher KI-Sparrings- und Umsetzungspartner dabei, Ideen in konkrete digitale Produkte, smarte Prozesse und neue Geschäftsmöglichkeiten zu verwandeln.

## 1. Wer ich bin

Ich bin Maik, kreativer KI-Sparrings- und Umsetzungspartner für Gründer, Selbstständige und kreative Unternehmer.

Ich unterstütze Menschen dabei, ihre Ideen weiterzuentwickeln, mit KI neue Möglichkeiten zu entdecken und daraus konkrete Projekte, digitale Produkte und funktionierende Lösungen zu erschaffen. Dabei verbinde ich strategisches Denken, Kreativität und technische Umsetzung.

Ich zeige nicht einfach nur, welche KI-Tools es gibt. Ich arbeite gemeinsam mit meinen Kunden an ihren individuellen Vorhaben – von der ersten Idee bis zum fertigen Ergebnis. Ich bin dabei Sparringspartner, Ideengeber, Coach und technischer Umsetzer.

Ich baue selbst Apps, Websites, Tools und Automatisierungen und probiere aus, wie sich KI sinnvoll in reale Projekte integrieren lässt. Ein Beispiel ist THE TRIBE, meine Community für echte Begegnungen in Bielefeld und Münster, für die ich digitale Lösungen entwickle.

KI ist mein Werkzeug und Beschleuniger – nicht der eigentliche Zweck. Mein eigentliches Produkt ist die Verbindung aus:
- kreativem Sparring,
- strategischer Orientierung,
- technischer Umsetzung,
- Wissenstransfer und Befähigung.

## 2. Mein persönliches Why

Ich liebe es, Ideen zu entdecken, Möglichkeiten zu erkennen, Dinge zu erschaffen und andere Menschen dazu zu befähigen.

Ich möchte meine Kreativität und meine Fähigkeiten mit KI nutzen, um Ideen umzusetzen, echte Probleme zu lösen und mir ein unabhängiges, selbstbestimmtes Leben aufzubauen. Ich möchte selbst entscheiden, mit wem ich arbeite, welche Projekte ich umsetze und welchen Wert ich schaffe – und meine Fähigkeiten nicht ausschließlich gegen Arbeitszeit eintauschen, sondern Lösungen schaffen, deren Wert sich am Ergebnis orientiert.

Flow Media AI verbindet meine Kreativität, meine Begeisterung für Technologie und meinen Wunsch nach Freiheit.

## 3. Für wen ich das mache (Zielgruppe)

- Gründer und Business Starter
- Solo-Selbstständige und Solopreneure
- Coaches und Dienstleister
- Kreative Unternehmer
- Kleine Unternehmen und Start-ups

Besonders Menschen, die **viele Ideen haben, aber nicht genau wissen, wie sie diese umsetzen sollen.**

Ihr Problem:
- Viele Ideen, aber keine klare Richtung.
- Zu viele KI-Tools und Möglichkeiten.
- Keine Lust, sich durch unzählige YouTube-Videos und Tutorials zu kämpfen.
- Fehlendes technisches Know-how.
- Sie brauchen jemanden, der mitdenkt, Feedback gibt und gemeinsam mit ihnen umsetzt.

Wichtiger als eine Branche ist die Haltung: neugierig, offen, bereit, Neues auszuprobieren und selbst etwas zu bewegen.

## 4. Mein Versprechen

**Viele Ideen? Mach sie mit KI real.**

Ich schließe die Lücke zwischen Idee und Umsetzung. Nicht noch mehr Informationen konsumieren, sondern ins Machen kommen:
- Ideen konkretisieren.
- Möglichkeiten erkennen.
- Lösungen entwickeln.
- Prototypen bauen.
- Prozesse automatisieren.
- Selbstständiger mit KI arbeiten.

Das Ziel: **Mehr Freiheit, Kreativität und Unabhängigkeit durch KI.**

## 5. Meine drei Leistungsbereiche

**01 – ENABLE** · Menschen befähigen, KI zu verstehen und selbst einzusetzen.
- Persönliches 1:1-Sparring
- KI-Beratung und Masterclasses
- Ideenentwicklung und Strategie
- Individuelle Begleitung nach der FLOW-Methode (Langzeit-Sparring über 3 oder 6 Monate: wöchentlich 1 Stunde + 7-stündige KI-Masterclass rund um Claude Code)

**02 – BUILD** · Aus Ideen konkrete digitale Lösungen erschaffen.
- Websites und Landingpages
- Apps und Business-Tools
- Digitale Produkte
- KI-Workflows und Automatisierungen
- Content-Systeme

**03 – CONNECT** · Menschen, Ideen und Möglichkeiten zusammenbringen.
- Community und Austausch (Flow Business Community, digitaler Stammtisch)
- Workshops und gemeinsame Projekte
- Wissen teilen
- Gemeinsam wachsen

## 6. Meine Arbeitsweise: die FLOW-Methode

Ich verkaufe nicht einfach Stunden oder einzelne Tools, sondern arbeite individuell und bedarfsorientiert – nach der **FLOW-Methode** (Maik, 06.11.2026). Jeder Buchstabe ist eine Phase:

| | Phase | Was passiert |
|---|---|---|
| **F** | **Fokussieren** | Idea2Concept: Idee schärfen, Ziele, Zielgruppe, Geschäftsmodell – aus einer Idee wird ein konkretes Konzept. |
| **L** | **Losbauen** | Concept2Prototype: erste App, Website oder digitales Produkt – aus dem Konzept entsteht ein Prototyp. |
| **O** | **Optimieren** | Prototype2Product: testen, verbessern, nutzbar machen – aus dem Prototyp wird eine Lösung. |
| **W** | **Wachsen** | Product2Business: Prozesse, Automatisierungen und Geschäftsmodell weiterentwickeln. |

Die FLOW-Methode ist Marke und Methode zugleich: Sie steht im Sparring, in Masterclasses, Workshops, auf der Website und im Content immer gleich (Reihenfolge F · L · O · W, deutsche Phasennamen; die englischen Untertitel immer mit „2“ geschrieben: Idea2Concept · Concept2Prototype · Prototype2Product · Product2Business – Maik, 06.11.2026).

Dabei bin ich Sparringspartner, Ideengeber, Coach und technischer Umsetzer. Ziel ist immer, dass meine Kunden selbstständiger werden – nicht abhängig von mir.

## 7. Kommunikation: Kernbotschaften

| Botschaft | Bedeutung |
|---|---|
| **Viele Ideen? Mach sie mit KI real.** | zentraler Einstieg |
| **Dein persönlicher KI-Partner.** | meine Rolle |
| **Gemeinsam Ideen verwirklichen.** | meine Arbeitsweise |
| **Weniger suchen. Mehr erschaffen.** | der Nutzen |
| **We build your ideas.** | Markenversprechen |
| **Die FLOW-Methode: Fokussieren · Losbauen · Optimieren · Wachsen.** | meine Methode |
| **Komm in den Flow.** | Aufruf am Ende |

Instagram-Bio (@flow.media.ai):
```
Viele Ideen? Mach sie mit KI real.
Dein persönlicher KI-Partner
Sparring für Gründer & Selbstständige
Apps • Automatisierung • digitale Produkte
↓ Jetzt starten
```

**Was Flow Media AI ausdrücklich nicht ist:**
- keine klassische IT-Agentur,
- kein reiner KI-Schulungsanbieter,
- kein austauschbarer Automatisierungsdienstleister,
- keine reine Cloud- oder Softwareberatung,
- kein Verkäufer von möglichst vielen KI-Tools.

## 8. Meine Werte

**Stand 20.10.2026 – meine Werte gerade:**

Macht · Mut · Pragmatismus · Risiko · Entwicklung · Erfolg · Flow · Fokus · Freiheit · Herausforderung · Innovation · Inspiration · Intuition · Kreativität · Selbstvertrauen · Sinnhaftigkeit · Spontaneität · Struktur · Tiefe · Unabhängigkeit · Verlässlichkeit · Visionen · Wachstum · Wahrheit · Weiterentwicklung · Zuverlässigkeit

Kurzform (aus Maiks eigener Fassung in Drive, 21.10.2026): **Frei sein. Ideen verwirklichen. Einfach machen. Echt bleiben. Wachsen. Etwas bewegen.** Seine ausführlichen Werte (Freiheit & Selbstbestimmung · Kreativität, Vision & Schaffenskraft · Einfachheit, Pragmatismus & Fokus · Authentizität, Ehrlichkeit & echte Verbindung · Wachstum, Mut & Selbstvertrauen · Sinnhaftigkeit & Wirksamkeit) und sein Persönlichkeitsprofil (strategischer Visionär, kreativer Erfinder, pragmatischer Umsetzer) stehen **nur in Drive** (`01_Marketing/Persoenlichkeitsprofil_und_Werte_Maik`) – dort nachlesen, nicht ins öffentliche Repo kopieren.

Ausformulierung:
- **Freiheit:** Ich möchte selbst entscheiden, wie ich arbeite und was ich erschaffe – und anderen mit KI mehr Freiheit ermöglichen.
- **Kreativität:** Ideen nicht nur sammeln, sondern in die Realität bringen.
- **Pragmatismus:** Lieber etwas Funktionierendes bauen und verbessern als endlos darüber reden.
- **Authentizität:** ehrlich, persönlich, ohne künstliche Erfolgsgeschichten.
- **Partnerschaft:** Zusammenarbeit, bei der die menschliche Ebene stimmt – auf Augenhöhe, als Sparringspartner.
- **Wirksamkeit:** Am Ende zählt, ob eine Lösung tatsächlich hilft.
- **Befähigung:** Menschen nicht abhängig machen, sondern zeigen, was sie selbst erreichen können.

### Persönliche Geschichte als Content-Grundlage

Ich habe erlebt, wie schnell sich Ideen mit KI umsetzen lassen. Wenn ich eine Aufgabe effizient erledige, möchte ich nicht die verbleibende Zeit absitzen, sondern mich weiterentwickeln und mehr aus dem machen, was ich kann. Mit Flow Media AI finde ich heraus, wie weit ich damit gehen kann – und nehme andere mit. Ich teile nicht nur fertige Ergebnisse, sondern auch Experimente, Erkenntnisse und Dinge, die nicht auf Anhieb klappen.

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

**Nicht nur erzählen, was KI kann. Zeigen, was du damit machst – und wie andere ihre eigenen Ideen damit real machen.**

Jeder Inhalt zahlt auf die Positionierung ein: Maik als persönlicher KI-Sparrings- und Umsetzungspartner (Enable · Build · Connect) mit der FLOW-Methode. Der Content dokumentiert meine Entwicklung, vermittelt praktische Möglichkeiten und baut Vertrauen auf. Daraus entstehen Sparring-Begleitungen, Masterclasses, Workshops, Kundenprojekte und digitale Produkte.

Das langfristige Ziel ist ein Geschäft, das zu meinen Fähigkeiten und Werten passt: kreativ, wirksam, wirtschaftlich tragfähig und unabhängig.
