---
name: brand-builder
description: Baut aus einem Video über dich (Transkript), deinen Fotos und optional deiner Website in einem Durchlauf deine persönlichen Marken-Skills – brand-dna (wer du bist und wie du klingst), brand-look (wie du aussiehst), brand-content (Posts, Captions, Reel-Skripte) und brand-website (Landingpage). Nutzen, wenn jemand sagt „Talk-to-Brand“, „Bau meine Marke“, „Brand-Builder starten“, ein Transkript über sich hochlädt oder seine Personal Brand als Skill haben will.
---

# Brand-Builder · Talk-to-Brand – einmal reden, immer posten

Methode **Talk-to-Brand** aus dem Workshop „Von KI zur Personal Brand – Vol. 2“ (Flow Media AI). Ziel: in **einem Durchlauf** vier fertige Skills, die danach jeden Content in der Stimme und im Look der Person erstellen.

## 1. Material einsammeln
Prüfe, was da ist, und frag **einmal gesammelt** nach dem, was fehlt:
- **Video oder Transkript** (Pflicht):
  - **In Claude Code** (Terminal/Shell verfügbar): Das Video selbst transkribieren. Einmalig `pip install faster-whisper` (falls nicht installiert), dann `python3 <skill-ordner>/scripts/transcribe.py "<video>"` – schreibt `<video>.transkript.txt` daneben. Erster Lauf lädt das Sprachmodell (~500 MB), danach ca. 1–2 Min. pro 5 Min. Video. Bei schwachem Rechner `… "<video>" base` (schneller, etwas ungenauer). Das Video bleibt auf dem Rechner.
  - **In der Claude-App** (claude.ai, ohne Shell): Ein Video kann Claude dort nicht anhören. Bitte um ein Transkript als Text (`.txt`/`.srt`, z. B. Auto-Untertitel aus CapCut exportieren, Diktierfunktion, Word „Transkribieren“) oder darum, die fünf Fragen aus `fragen.md` kurz schriftlich zu beantworten.
- **Fotos** (empfohlen, 5–10): Porträts, Arbeit, Umfeld. Ohne Fotos wird `brand-look` neutral angelegt und als „vorläufig“ markiert.
- **Website / Texte** (optional): Link oder eingefügter Text.
- **Vorname** und wie die Person angesprochen werden will (du/Sie).

## 2. Auswerten – nur, was wirklich im Material steht
Lies das Transkript zweimal. Halte fest und belege jeden Punkt mit einem Zitat aus dem Transkript:
1. **Kern:** Was macht die Person, für wen, mit welchem Ergebnis? Ein Satz.
2. **Werte:** 3–5, nur genannte oder klar gezeigte.
3. **Zielgruppe:** wer, welches Problem.
4. **Geschichte:** der Moment/Weg, der sie ausmacht.
5. **Stimme:** du/Sie, Satzlänge, Lieblingswörter, typische Einstiege, Humor ja/nein, Dialekt/Anglizismen, was sie **nie** sagen würde. 5–8 **Originalsätze** als Stimmproben.
6. **Look** (aus Fotos/Website): 2–3 Hauptfarben als Hex, hell/dunkel, Bildstil (Farbe/SW, Licht, Nähe), Schriftcharakter (modern/klassisch/verspielt), welche Fotos als Porträts taugen.

**Nichts erfinden.** Keine Kunden, Zahlen, Auszeichnungen, Erfolge oder Werte, die nicht im Material stehen. Lücken als `[offen: …]` markieren und am Ende als Fragen auflisten.

## 3. Kurz bestätigen lassen
Zeig eine kompakte Zusammenfassung (Kern-Satz, Werte, Zielgruppe, 3 Stimmproben, Farben). Frag: „Passt das so? Was soll anders sein?“ Erst nach OK (oder Korrektur) weiter. Im Ultrafast-Modus („mach einfach“) direkt weiter und Unsicheres als `[prüfen]` markieren.

## 4. Die vier Skills schreiben
Fülle die Vorlagen aus `templates/` vollständig aus (alle `{{…}}` ersetzen, keine Platzhalter stehen lassen außer `[offen: …]`). Der Skill-Name bekommt den Vornamen, klein und ohne Umlaute/Leerzeichen (ä→ae, ö→oe, ü→ue, ß→ss): z. B. `lisa-brand-dna`, `joerg-brand-look`. Im Text bleibt der Name normal geschrieben.
- `templates/brand-dna.md` → `<vorname>-brand-dna/SKILL.md`
- `templates/brand-look.md` → `<vorname>-brand-look/SKILL.md`
- `templates/brand-content.md` → `<vorname>-brand-content/SKILL.md`
- `templates/brand-website.md` → `<vorname>-brand-website/SKILL.md`

Freigegebene Fotos kommen mit in `<vorname>-brand-look/fotos/` (Dateinamen in der Tabelle des Skills eintragen).

## 5. Ausliefern
- **Claude-App (claude.ai):** jeden Skill-Ordner einzeln als ZIP packen und zum Download anbieten. Anleitung dazu ausgeben: Einstellungen → Fähigkeiten → Skills → Skill hochladen, ZIP wählen, aktivieren.
- **Claude Code:** Ordner nach `.claude/skills/` im Projekt (oder `~/.claude/skills/`) schreiben.

## 6. Sofort testen
Direkt nach dem Ausliefern einen Probelauf zeigen: mit `brand-content` **einen** Instagram-Post (Hook + Caption) zum Kern-Thema der Person. Fragen: „Klingt das nach dir?“ Korrekturen fließen zurück in `brand-dna` (Abschnitt „Korrekturen“), damit es beim nächsten Mal sitzt.

## Abschluss
Liste die offenen Fragen (`[offen: …]`, `[prüfen]`) und sag, welcher Skill wofür da ist – in zwei Sätzen, ohne Fachjargon.
