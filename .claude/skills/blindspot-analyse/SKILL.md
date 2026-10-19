---
name: blindspot-analyse
description: Optionaler Blindspot-Pass vor Projekten von Maik (Flow Media AI). NUR laden, wenn Maik ihn ausdrücklich einschaltet (/blindspot-analyse, „Blindspot-Analyse“, „Blindspot-Pass“, „Unknown Unknowns“, „was übersehe ich“) oder der eingeschaltete Skill pruefer-agent ihn verlangt. Nicht von selbst vorschlagen oder starten. Findet zuerst die Unknown Unknowns, setzt nichts um, schreibt am Ende einen verbesserten Auftrag mit Reihenfolge und Plan-Stopp; bei visuellen Projekten folgen vier Designs zur Auswahl.
---

# Blindspot-Analyse (Stand 19.10.2026, Vorgabe von Maik)

**Optional:** Nur wenn Maik den Pass ausdrücklich verlangt (oder der eingeschaltete Skill `pruefer-agent` ihn vorsieht). Dann **zuerst** dieser Pass. **Noch nichts umsetzen**, keine Dateien bauen, nichts deployen.

## Ablauf

1. **Projekt kurz verstehen.** Was soll am Ende entstehen, für wen, wo läuft es, welche Daten fließen (Geld, Personen, Gesundheit, Kunden)? Was gibt es schon (Repo, Board, Dropbox)? Fehlende Angaben nicht erfinden, sondern als offene Frage notieren.
2. **Unknown Unknowns suchen.** Dinge, von denen Maik nicht mal weiß, dass er sie nicht weiß. Systematisch durch diese Felder gehen und nur aufnehmen, was für *dieses* Projekt wirklich zutrifft:
   - Recht & Pflichten: Steuern, GoBD, Rechnungsrecht, Impressum, DSGVO, Urheber-/Bildrechte, Branchenregeln
   - Sicherheit & Zugriff: wer kommt ran, was passiert bei geteiltem Link/verlorenem Gerät, Schlüssel, öffentliche Repos
   - Daten: Backup, Aufbewahrungsfristen, Export, Abhängigkeit von einem Anbieter, Kosten- und Free-Tier-Grenzen
   - Betrieb: Wartung, Tests, was passiert, wenn KI-gebauter Code kaputtgeht, wer es außer Maik bedienen kann
   - Fachwissen der Branche: Begriffe, Standards, typische Anfängerfehler, die Profis nie machen würden
   - Geld & Zeit: versteckte laufende Kosten, Fristen, Entscheidungen mit langer Bindung
   - Menschen: Kunden, Nutzer, Partner – was erwarten sie selbstverständlich?
3. **Zu jedem Punkt drei Zeilen:**
   - **Was ist es?** (ein, zwei Sätze, ohne Fachjargon)
   - **Warum würde es dich erwischen?** (konkret für dieses Projekt, mit dem Moment, in dem es wehtut)
   - **Satz für deinen Auftrag:** ein fertiger Satz, den Maik in seinen Prompt kopieren kann
4. **Priorisieren.** Oben, was teuer, rechtlich riskant oder schwer rückgängig zu machen ist. Kurz bleiben: lieber 8 echte Punkte als 25 allgemeine.
5. **Verbesserten Auftrag bauen.** Bei größeren Projekten erst nach dem Interview aus dem Skill `pruefer-agent` (Regel 2). Alle Sätze zu einem Prompt zusammenführen:
   - Ziel und Rahmen
   - die Muss-Sätze aus Schritt 3
   - **Reihenfolge** der Umsetzung (nummeriert, weil die Reihenfolge zählt)
   - **Stopp:** „Zeig mir zuerst den Plan und warte auf mein Okay, bevor du etwas baust.“
   - bei Visuellem: „Mach mir dann vier deutlich verschiedene Designs, aus denen ich eins auswähle.“
6. **Visuelles Projekt?** Erst nach Maiks Okay zum Plan vier wirklich unterschiedliche Designs zeigen (Richtung, Farbe, Schrift, Layout), nicht vier Varianten derselben Idee. Maik wählt eins, erst dann bauen.

## Ausgabe

- Antwort an Maik: die priorisierte Liste, offene Fragen, der verbesserte Auftrag.
- Auswertung als Markdown ablegen: im Repo unter `auswertungen/<datum>-blindspot-<projekt>.md`, gespiegelt in die Dropbox `/Flow Media AI/07_KI/auswertungen/` (siehe Dropbox-Spiegel in `CLAUDE.md`).

## Regeln

- Nichts erfinden: keine Zahlen, Fristen oder Gesetze, die nicht sicher stimmen. Unsicheres als „prüfen lassen“ markieren und sagen, wer das prüft (Steuerberater, Anwalt, Anbieter-Doku).
- Keine Steuer- oder Rechtsberatung vortäuschen: Hinweise geben, Entscheidung beim Fachmann lassen.
- Deutsch, direkt, verständlich (Tonalität aus `CLAUDE.md`, Abschnitt 9).
