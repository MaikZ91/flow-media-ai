---
name: pruefer-agent
description: Optionaler Arbeitsmodus für Flow Media AI, NUR laden, wenn Maik ihn ausdrücklich einschaltet (/pruefer-agent, „Prüferagent an“, „mit Prüfagent“, „Prüferagent-Regel“). Nicht von selbst laden. Eingeschaltet: Ein separater Prüfagent ohne Vorwissen prüft jedes Ergebnis vor der Lieferung; größere Projekte starten mit Blindspot-Pass und Interview; Korrekturen werden dauerhafte Regeln; Recherchen laufen verteilt auf Haiku, Sonnet und Opus.
---

# Prüferagent-Regel (optional, Maik 19.10.2026)

**Nur aktiv, wenn Maik den Modus einschaltet** (z. B. `/pruefer-agent` oder „Prüferagent an“). Dann gelten die vier Regeln für den Rest der Session, bis Maik „Prüferagent aus“ sagt. Ohne Einschalten wird nichts davon angewendet.

Beim Einschalten diese Datei und `regeln-aus-korrekturen.md` lesen. Maiks Anweisung im Moment geht vor.

**Gilt nicht für Prüf- und Recherche-Subagenten selbst:** Sie liefern an den Hauptagenten, nicht an Maik, und starten keine weiteren Prüfungen.

## 1. Kein Ergebnis ohne unabhängige Prüfung

Bevor ein fertiges Ergebnis an Maik geht (Code live, Seite veröffentlicht, Text, Analyse, Datei in Dropbox), prüft es ein **separater Prüfagent ohne Vorwissen**.

So geht's:
1. Anforderungen sammeln: Maiks Auftrag **wörtlich**, alle Korrekturen aus dem Gespräch, die passenden Regeln aus `CLAUDE.md`, `regeln-aus-korrekturen.md` und betroffenen Skills.
2. Prüfagent starten (Agent-Tool, `subagent_type: "general-purpose"`, **neuer** Agent, kein Fork, damit er den Verlauf nicht kennt). Er bekommt nur: die Anforderungsliste, die Pfade oder Links zum Ergebnis und den Auftrag:
   > „Prüfe das Ergebnis gegen jede Anforderung einzeln. Für jede: erfüllt / nicht erfüllt / nicht prüfbar, mit Beleg (Datei:Zeile, Screenshot, Testausgabe). Such aktiv nach Fehlern, Widersprüchen, erfundenen Fakten und Dingen, die Maik nicht wollte. Ändere nichts.“
3. Ist etwas **nicht erfüllt**: beheben und erneut prüfen lassen (wieder ein frischer Agent). Erst liefern, wenn alles erfüllt ist.
4. Was **nicht prüfbar** ist (z. B. Live-Verhalten auf Maiks Gerät), Maik offen sagen.
5. In der Antwort an Maik in einem Satz nennen, dass geprüft wurde und was der Prüfer gefunden hat.

Ausnahme: reine Rückfragen und kurze Auskünfte ohne Ergebnis brauchen keine Prüfung.

## 2. Größere Projekte: Blindspot-Pass und Interview

Größer heißt: ein für Maik neuer Bereich, Arbeit über mehrere Tage oder viele Dateien, oder es geht um Geld, Recht oder Kundendaten. Eine einzelne Änderung an etwas Bestehendem ist nicht größer.

1. Skill `blindspot-analyse` ausführen (nichts umsetzen).
2. Danach Maik mit dem **AskUserQuestion-Tool** interviewen: **eine Frage pro Aufruf**, erst nach der Antwort die nächste. Jede Frage enthält deine **Hypothese** als erste Option mit „(Empfohlen)“ und einer kurzen Begründung.
3. Nur fragen, was die Umsetzung wirklich ändert. Was sich aus Repo, Board oder `CLAUDE.md` klären lässt, nicht fragen.
4. Erst danach den verbesserten Auftrag des Blindspot-Skills schreiben (mit den Antworten aus dem Interview), Plan zeigen und einmal am Ende auf Maiks Okay warten.

## 3. Korrekturen werden dauerhafte Regeln

Wenn Maik dich korrigiert („nein, so nicht“, „das soll anders“, „nicht mehr …“):
1. Korrektur umsetzen.
2. Im selben Lauf als Regel in `regeln-aus-korrekturen.md` (dieser Ordner) eintragen: Datum, Regel in einem Satz, Anlass (Maiks Worte, wenn möglich wörtlich). Gilt sie nur für ein Projekt, auch dort festhalten (z. B. README des Projekts).
3. Dropbox-Spiegel aktualisieren (siehe `CLAUDE.md`).
4. Maik in einem Satz sagen, welche Regel du aufgeschrieben hast.

Vor jeder Arbeit `regeln-aus-korrekturen.md` lesen.

## 4. Große Recherchen verteilen

Groß heißt: viele Quellen, mehrere Teilfragen oder Vergleich vieler Optionen.

| Aufgabe | Agent-Tool `model` |
|---|---|
| Fleißarbeit: Quellen suchen, Seiten lesen, Fakten und Zahlen sammeln, Listen bauen | `haiku` |
| Texte: Abschnitte formulieren, zusammenfassen, für Maik umschreiben | `sonnet` |
| Zusammenführen: Ergebnisse abgleichen, Widersprüche klären, Empfehlung, Endfassung | `opus` |

- Recherche-Agenten mit `subagent_type: "general-purpose"` und dem `model` aus der Tabelle starten.
- Teilaufgaben unabhängig schneiden und **parallel** starten (mehrere Agent-Aufrufe in einer Nachricht).
- Jeder Sammel-Agent liefert Quellen (Link) zu jeder Aussage. Nichts ohne Quelle übernehmen.
- Das Ergebnis des Zusammenführens prüft danach ein Prüfagent nach Regel 1.
