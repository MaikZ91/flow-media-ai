---
name: meeting-summary
description: Macht aus Gesprächsnotizen, Transkripten oder Sprachmemos eine kurze Zusammenfassung mit Entscheidungen, Aufgaben (wer, was, bis wann) und offenen Fragen – fertig für Board, Kalender oder Follow-up-Mail. Nutzen bei „fass das Meeting zusammen“, „Aufgaben aus dem Call“, „mach aus meinem Sprachmemo To-dos“.
---

# Meeting Summary

## Eingang
Text, Transkript (`.txt`, `.srt`, `.vtt`) oder Notizen. Bei Audio/Video in Claude Code: zuerst transkribieren (z. B. faster-whisper), sonst um ein Transkript bitten.

## Ausgabe (immer in dieser Reihenfolge)
**1. In einem Satz:** Worum ging es, was ist rausgekommen?

**2. Entscheidungen** – nur, was wirklich beschlossen wurde.

**3. Aufgaben**
| Was | Wer | Bis wann |
|---|---|---|
Unklare Verantwortliche oder Fristen als `offen` markieren, nicht erfinden.

**4. Offene Fragen** – was geklärt werden muss, und von wem.

**5. Termine** – genannte Folgetermine mit Datum/Uhrzeit (Zeitzone beachten).

**6. Follow-up-Mail (optional)** – kurz, freundlich, mit Aufgabenliste.

## Regeln
- Nur, was im Material steht. Vermutungen als „(vermutlich)“ kennzeichnen.
- Namen von Teilnehmenden korrekt übernehmen; sensible Inhalte (Gesundheit, Geld, Personal) nicht in geteilte Zusammenfassungen, wenn nicht gewünscht.
- Kurz: die Zusammenfassung soll in 30 Sekunden lesbar sein.
- Auf Wunsch Aufgaben direkt im gewünschten Format (Kanban-Karten, Kalendereinträge, Checkliste).
