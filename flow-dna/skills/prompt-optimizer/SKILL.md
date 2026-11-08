---
name: prompt-optimizer
description: Macht aus einem schnellen Prompt einen, der zuverlässig liefert – ergänzt Ziel, Kontext, Format, Beispiele und Prüfkriterien, zeigt vorher/nachher und speichert gute Prompts als Vorlage oder Skill. Nutzen bei „verbessere meinen Prompt“, „warum kommt da Mist raus?“, „mach daraus eine Vorlage“.
---

# Prompt Optimizer

## 1. Diagnose
Lies den Prompt und das (schlechte) Ergebnis, falls vorhanden. Benenne in 2–4 Punkten, was fehlt:
- **Ziel** (Was soll am Ende rauskommen, wofür?)
- **Kontext** (Wer bin ich, für wen ist es, was gibt es schon?)
- **Rahmen** (Länge, Ton, Sprache, No-Gos)
- **Format** (Liste, Tabelle, Code, Datei)
- **Beispiel** (gut / schlecht)
- **Prüfung** (Woran erkenne ich, dass es passt?)

## 2. Verbesserter Prompt
Aufbau:
```
Ziel: …
Kontext: …
Aufgabe: … (in Schritten, wenn es mehrere sind)
Rahmen: …
Format: …
Beispiel: …
Prüfe vor der Antwort: …
Wenn etwas fehlt: frag nach, statt zu raten.
```
Kurz halten – nur, was wirklich hilft.

## 3. Vorher / Nachher
Zeige beide Versionen nebeneinander und erkläre in drei Sätzen, was sich ändert.

## 4. Wiederverwenden
Wird der Prompt öfter gebraucht: Angebot, ihn als **Vorlage mit Platzhaltern** (`{{kunde}}`, `{{thema}}`) oder als **eigenen Skill** (`SKILL.md` mit Name, Beschreibung, Anleitung) zu speichern.

## Regeln
- Absicht der Person nicht verändern, nur klarer machen.
- Keine Tricks, die Sicherheitsregeln von Modellen umgehen sollen.
- Bei vertraulichen Daten im Prompt: Hinweis, sie durch Platzhalter zu ersetzen.
