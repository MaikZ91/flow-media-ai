---
name: angebot-rechnung
description: Erstellt aus Stichworten ein sauberes Angebot oder eine Rechnung (Deutschland) mit den eigenen Absenderdaten – inklusive Pflichtangaben-Check, Kleinbetragsrechnung bis 250 € brutto und Kleinunternehmer-Hinweis – als Dokument zum Exportieren. Nutzen bei „schreib eine Rechnung für …“, „Angebot für Kunde X“, „Rechnung über 2 Stunden Coaching“.
---

# Angebot & Rechnung

## 0. Einmalig: Absenderprofil
Beim ersten Mal abfragen und als `absender.md` neben diesem Skill speichern (nie in öffentliche Repos!):
Name/Firma · Anschrift · E-Mail/Telefon · Steuernummer **oder** USt-IdNr. · Kleinunternehmer ja/nein · Bankverbindung (IBAN, BIC, Bank) · Zahlungsziel (z. B. 14 Tage) · Nummernkreis (z. B. `2026-001`).

## 1. Stichworte aufnehmen
Kunde (Name, Anschrift), Leistung(en), Menge/Stunden, Einzelpreis, Leistungsdatum oder -zeitraum, ggf. Rabatt. Fehlt etwas Pflichtiges, **nachfragen statt raten**.

## 2. Angebot
Titel · Angebotsnummer · Datum · gültig bis · Ausgangslage in einem Satz · Leistungen als Positionen · Preis (netto/brutto bzw. Kleinunternehmer-Hinweis) · Ablauf und Termine · was nicht enthalten ist · nächster Schritt („Zusage per Mail genügt“).

## 3. Rechnung
Prüfe die Pflichtangaben einer Rechnung (Deutschland, § 14 UStG):
- vollständiger Name und Anschrift von Leistendem und Empfänger
- Steuernummer oder USt-IdNr. des Leistenden
- Ausstellungsdatum und **fortlaufende Rechnungsnummer**
- Menge und Art der Leistung, Zeitpunkt/Zeitraum der Leistung
- Entgelt, Steuersatz und Steuerbetrag – **oder** bei Kleinunternehmern der Hinweis auf die Steuerbefreiung (§ 19 UStG)

**Kleinbetragsrechnung** (Gesamtbetrag bis 250 € brutto): vereinfachte Angaben genügen – Name und Anschrift des Leistenden, Ausstellungsdatum, Menge und Art der Leistung, Bruttobetrag und Steuersatz (bzw. Hinweis auf Steuerbefreiung). Empfängeranschrift und Steuernummer dürfen dann fehlen.

## 4. Ausgabe
- Als sauberes Dokument (HTML/Markdown oder Google Doc), das als PDF exportiert werden kann. Layout: Absender oben, Empfänger, Meta-Tabelle (Nr., Datum), Positionstabelle, Summe, Zahlungshinweis, Fußzeile mit Bankdaten.
- Dateiname: `Rechnung_<Nummer>_<Kunde>.pdf` bzw. `Angebot_<Nummer>_<Kunde>.pdf`.
- Nächste freie Nummer im Profil hochzählen.

## Regeln
- **Keine Steuerberatung.** Bei Sonderfällen (Ausland, Reverse Charge, Anzahlungen, Gutschriften) Hinweis: „Bitte mit deiner Steuerberatung prüfen.“
- Nie Bankdaten, Steuernummern oder Kundendaten in öffentliche Ordner oder Repos schreiben.
- Beträge nachrechnen und die Rechnung am Ende einmal gegen die Pflichtliste abhaken.
