---
name: blindspot-analyse
description: Blindspot-Pass vor einem Projekt – findet die „Unknown Unknowns“ (Recht, Sicherheit, Daten, Betrieb, Fachwissen, Kosten, Menschen), setzt selbst nichts um und schreibt am Ende einen verbesserten Auftrag mit Reihenfolge und Plan-Stopp. Nutzen bei „Blindspot-Analyse“, „was übersehe ich?“, „bevor wir starten“, vor neuen Apps, Websites, Automatisierungen oder Kampagnen.
---

# Blindspot-Analyse

**Erst denken, dann bauen.** Dieser Skill läuft *vor* einem Projekt. Er baut nichts, ändert keine Dateien und veröffentlicht nichts.

## Ablauf

1. **Projekt verstehen.** Was soll entstehen, für wen, wo läuft es, welche Daten fließen (Geld, Personen, Gesundheit, Kundendaten)? Was gibt es schon? Fehlendes nicht erfinden, sondern als offene Frage notieren.
2. **Unknown Unknowns suchen** – nur, was für *dieses* Projekt zutrifft:
   - **Recht & Pflichten:** Impressum, Datenschutz (DSGVO), Bild- und Urheberrechte, Rechnungs- und Steuerregeln, Branchenvorschriften
   - **Sicherheit & Zugriff:** Wer kommt ran? Was passiert bei geteiltem Link, verlorenem Gerät, öffentlichem Code? Wo liegen Passwörter und Schlüssel?
   - **Daten:** Backup, Export, Aufbewahrungsfristen, Abhängigkeit von einem Anbieter, Grenzen von Gratis-Tarifen
   - **Betrieb:** Wer wartet es? Was passiert, wenn KI-gebauter Code bricht? Kann es jemand anderes bedienen?
   - **Fachwissen der Branche:** Begriffe, Standards, typische Anfängerfehler
   - **Geld & Zeit:** versteckte laufende Kosten, Fristen, Entscheidungen mit langer Bindung
   - **Menschen:** Was erwarten Kunden, Nutzer und Partner selbstverständlich?
3. **Zu jedem Punkt drei Zeilen:**
   - **Was ist es?** (ein, zwei Sätze, ohne Fachjargon)
   - **Warum erwischt es dich?** (konkret, mit dem Moment, in dem es wehtut)
   - **Satz für deinen Auftrag:** fertig zum Kopieren in den Prompt
4. **Priorisieren:** oben, was teuer, rechtlich riskant oder schwer rückgängig zu machen ist. Lieber 8 echte Punkte als 25 allgemeine.
5. **Verbesserter Auftrag:** alle Sätze zu einem Prompt mit
   - Ziel und Rahmen
   - den Muss-Sätzen aus Schritt 3
   - **nummerierter Reihenfolge** der Umsetzung
   - **Stopp:** „Zeig mir zuerst den Plan und warte auf mein Okay, bevor du etwas baust.“
   - bei Visuellem: „Zeig mir danach vier deutlich verschiedene Designs zur Auswahl.“

## Ausgabe
Priorisierte Liste · offene Fragen · verbesserter Auftrag. Auf Wunsch als Markdown-Datei `blindspot-<projekt>.md`.

## Regeln
- Nichts erfinden: keine Zahlen, Fristen oder Gesetze, die nicht sicher stimmen. Unsicheres als „prüfen lassen“ markieren und sagen, wer prüft (Steuerberatung, Anwalt, Anbieter-Doku).
- Keine Rechts- oder Steuerberatung vortäuschen.
- Klar, direkt, verständlich – für Menschen ohne Technik-Hintergrund.

## Beispiel
> „Ich will eine Buchungs-App für meine Yogakurse.“
> → u. a.: *Zahlungen & Rückerstattungen* („Warum erwischt es dich? Die erste Absage mit Geld-zurück-Wunsch kommt garantiert.“) · *Gesundheitsdaten im Anmeldeformular* · *Wer pflegt Kurse, wenn du krank bist?* → verbesserter Auftrag mit Plan-Stopp.
