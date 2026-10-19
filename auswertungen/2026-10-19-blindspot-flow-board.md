# Blindspot-Analyse: Flow Board mit Finanzen (19.10.2026)

**Projekt:** Dein Flow Board (Aufgaben, Kalender, Dateien) ist mit dem Finanzen-Reiter zu deiner Buchhaltung geworden: Buchungen, Belege, Rechnungen an Kunden, private Finanzen. Es läuft auf GitHub Pages, die Daten liegen in Supabase (Projekt „Liebefeld“), Zugang über deinen geheimen Board-Link.

Kurzfassung: Für Aufgaben ist das Setup gut. Für Geld, Steuern und Kundendaten fehlen ein paar Dinge, die man erst merkt, wenn das Finanzamt fragt oder Daten weg sind.

*Keine Steuer- oder Rechtsberatung. Punkte mit „prüfen lassen“ bitte mit Steuerberater klären.*

---

## 1. Buchungen sind spurlos änderbar (GoBD)
- **Was ist es?** Steuerlich relevante Aufzeichnungen müssen nachvollziehbar und unveränderbar sein (GoBD). Wer eine Buchung ändert oder löscht, muss das später noch sehen können.
- **Warum würde es dich erwischen?** Im Board kannst du jede Buchung löschen, und niemand sieht, dass es sie gab. Bei einer Prüfung zählt das Board dann nicht als ordentliche Aufzeichnung.
- **Satz für deinen Auftrag:** „Buchungen dürfen nie gelöscht oder überschrieben werden; jede Änderung wird als neue Version mit Datum gespeichert und bleibt sichtbar.“

## 2. Rechnungen: Nummern lückenlos, gestellte Rechnungen nicht änderbar
- **Was ist es?** Jede Rechnungsnummer darf nur einmal vorkommen; eine verschickte Rechnung korrigiert man mit einer Storno- oder Korrekturrechnung, nicht durch Überschreiben.
- **Warum würde es dich erwischen?** Im Board kannst du eine verschickte Rechnung „bearbeiten“ oder löschen. Dann stimmt dein PDF beim Kunden nicht mehr mit deinen Daten überein, oder es fehlen Nummern.
- **Satz für deinen Auftrag:** „Eine Rechnung wird beim Verschicken festgeschrieben; Korrekturen nur über eine Stornorechnung mit eigener Nummer.“

## 3. E-Rechnung kommt auf dich zu
- **Was ist es?** Seit 2025 müssen Unternehmen in Deutschland E-Rechnungen (XRechnung/ZUGFeRD) empfangen können; das Ausstellen wird stufenweise bis 2028 Pflicht. Kleinunternehmer sind beim Ausstellen ausgenommen. *Fristen für deinen Fall prüfen lassen.*
- **Warum würde es dich erwischen?** Dein Rechnungsgenerator macht nur PDFs. Sobald du kein Kleinunternehmer mehr bist, reicht das für Geschäftskunden nicht.
- **Satz für deinen Auftrag:** „Rechnungen müssen später auch als E-Rechnung (ZUGFeRD) erzeugt werden können; eingehende E-Rechnungen werden im Original archiviert.“

## 4. Kein Backup, und das Projekt teilt sich die Datenbank mit THE TRIBE
- **Was ist es?** Alle Board-Daten liegen in einem einzigen kostenlosen Supabase-Projekt, zusammen mit THE TRIBE. Ob und wie lange es dort Backups gibt, hängt vom Tarif ab. *In der Supabase-Doku prüfen.*
- **Warum würde es dich erwischen?** Ein Fehler in der Tribe-App, ein pausiertes Projekt oder ein versehentliches Löschen trifft auch deine Buchhaltung. Belege musst du jahrelang aufbewahren.
- **Satz für deinen Auftrag:** „Flow-Daten in einem eigenen Projekt; jede Woche ein automatisches Backup (Buchungen + Belege) an einen zweiten Ort, z. B. Google Drive 05_Finanzen.“

## 5. Der Board-Link ist der einzige Schlüssel
- **Was ist es?** Wer deinen Link mit `#b=…&k=…` hat, kann alles sehen, ändern und löschen, auch Finanzen und Belege. Es gibt keinen zweiten Faktor und kein Protokoll, wer zugegriffen hat.
- **Warum würde es dich erwischen?** Ein Screenshot, ein geteilter Bildschirm oder ein fremder Rechner mit gespeichertem Link reicht.
- **Satz für deinen Auftrag:** „Finanzdaten nur nach Login mit zweitem Faktor; der Link allein öffnet höchstens die Aufgaben.“

## 6. Kleinunternehmer und die Umsatzsteuer, die du nicht zurückbekommst
- **Was ist es?** Als Kleinunternehmer bekommst du die Umsatzsteuer auf Einkäufe nicht zurück. Auf die Kleinunternehmerregelung kannst du verzichten, bist dann aber mehrere Jahre daran gebunden. *Mit Steuerberater rechnen.*
- **Warum würde es dich erwischen?** Allein im Programm CREATION stecken 1.215,81 € Umsatzsteuer. Ob sich der Verzicht für dich lohnt, entscheidet sich vor großen Ausgaben, nicht danach.
- **Satz für deinen Auftrag:** „Vor Ausgaben über 1.000 € erinnert mich das Board: prüfen, ob Kleinunternehmer oder Regelbesteuerung günstiger ist.“

## 7. Privates und Geschäftliches vermischt
- **Was ist es?** In die Einnahmen-Überschuss-Rechnung gehört nur, was geschäftlich ist. Private Ausgaben sind nicht absetzbar.
- **Warum würde es dich erwischen?** Im Board steht z. B. „Dating Fotoshooting“ zwischen deinen Geschäftsbuchungen und landet so auch im EÜR-Export. Laut deinem `CLAUDE.md` gehört Dating gar nicht zu Flow Media AI.
- **Satz für deinen Auftrag:** „Jede Buchung ist als geschäftlich oder privat markiert; nur geschäftliche gehen in den Export für die Steuer.“

## 8. Kategorien passen nicht zur Steuererklärung
- **Was ist es?** Beim Finanzamt gibst du den Gewinn über die Anlage EÜR in ELSTER ab, mit festen Zeilen (z. B. Fremdleistungen, Fortbildung, Werbung).
- **Warum würde es dich erwischen?** Deine Board-Kategorien sind frei gewählt. Am Jahresende sortierst du alles von Hand um.
- **Satz für deinen Auftrag:** „Kategorien entsprechen den Zeilen der Anlage EÜR, damit der Jahresexport direkt übernommen werden kann.“

## 9. Kundendaten und Tracking brauchen Datenschutz-Papierkram
- **Was ist es?** Sobald du Namen und Adressen von Kunden speicherst oder Besucher deiner Landing Page mit PostHog misst, brauchst du eine passende Datenschutzerklärung und mit Anbietern wie Supabase und PostHog einen Vertrag zur Auftragsverarbeitung.
- **Warum würde es dich erwischen?** Das fällt erst auf, wenn ein Kunde fragt, welche Daten du über ihn hast, oder eine Abmahnung kommt.
- **Satz für deinen Auftrag:** „Liste alle Dienste, die Personendaten verarbeiten, und sorge für Datenschutzerklärung und Auftragsverarbeitungsverträge.“

## 10. KI-gebauter Code ohne Netz
- **Was ist es?** Das Board wird ständig per KI erweitert, aber es gibt keine automatischen Tests.
- **Warum würde es dich erwischen?** Heute hätte eine kleine Änderung fast jeden Klick ins Formular kaputt gemacht. Bei Finanzdaten merkst du so etwas vielleicht erst, wenn Buchungen fehlen.
- **Satz für deinen Auftrag:** „Vor jedem Live-Gang laufen automatische Tests für Buchen, Rechnung, Beleg und Kalender; schlägt einer fehl, geht nichts live.“

---

## Offene Fragen an dich
- Hast du dein Gewerbe schon angemeldet, und ab wann? Davon hängt ab, wie die Ausgaben vor der Anmeldung behandelt werden.
- Soll das Board deine echte Buchhaltung sein oder nur die Übersicht neben einem Buchhaltungstool (z. B. sevDesk, Lexware)?
- Arbeitest du mit einem Steuerberater, der die Daten später bekommt?

---

## Verbesserter Auftrag

> Ich will mein Flow Board zur Finanzzentrale von Flow Media AI ausbauen: Buchungen, Belege, Rechnungen an Kunden und private Finanzplanung, nutzbar auf allen Geräten.
>
> **Muss gelten:**
> - Buchungen dürfen nie gelöscht oder überschrieben werden; jede Änderung wird als neue Version mit Datum gespeichert und bleibt sichtbar.
> - Eine Rechnung wird beim Verschicken festgeschrieben; Korrekturen nur über eine Stornorechnung mit eigener Nummer. Rechnungen können später auch als E-Rechnung (ZUGFeRD) erzeugt werden.
> - Jede Buchung ist geschäftlich oder privat; nur geschäftliche gehen in den Steuer-Export. Kategorien entsprechen den Zeilen der Anlage EÜR.
> - Finanzdaten nur nach Login mit zweitem Faktor; der Board-Link allein öffnet höchstens die Aufgaben.
> - Flow-Daten in einem eigenen Supabase-Projekt, getrennt von THE TRIBE; jede Woche ein automatisches Backup von Buchungen und Belegen nach Google Drive 05_Finanzen.
> - Liste alle Dienste, die Personendaten verarbeiten, für Datenschutzerklärung und Auftragsverarbeitungsverträge.
> - Vor Ausgaben über 1.000 € erinnert mich das Board an die Frage Kleinunternehmer oder Regelbesteuerung.
> - Vor jedem Live-Gang laufen automatische Tests für Buchen, Rechnung, Beleg und Kalender.
>
> **Reihenfolge:**
> 1. Backup der heutigen Daten und Umzug in ein eigenes Supabase-Projekt
> 2. Login mit zweitem Faktor für den Finanzbereich
> 3. Buchungen unveränderbar machen (Versionen statt Überschreiben), geschäftlich/privat trennen
> 4. Rechnungen festschreiben, Storno, lückenlose Nummern
> 5. Kategorien nach Anlage EÜR, Jahresexport
> 6. Wöchentliches Backup nach Google Drive
> 7. Automatische Tests
> 8. Später: E-Rechnung (ZUGFeRD)
>
> **Stopp:** Zeig mir zuerst den Plan mit den offenen Entscheidungen und warte auf mein Okay, bevor du etwas baust. Fragen zu Steuern markierst du für meinen Steuerberater.
>
> Für alles Sichtbare (z. B. Login-Seite, Rechnungslayout): Zeig mir vier deutlich verschiedene Designs, ich wähle eins aus.
