# Workshop: Von KI zur Personal Brand – Vol. 2 · Die Video-Methode

Mo 02.11.2026 · 18:00 · ca. 60 Min · digital & live · 15 € · Reel-Plan: `content/reels/R019-workshop-vol2/`

**Ein Video rein – deine Marke als Skill raus.** Der Master-Skill `brand-builder` macht aus einem Video-Transkript, Fotos und (optional) der Website in einem Durchlauf vier persönliche Skills.

## Inhalt
```
skills/brand-builder/
├── SKILL.md              Master-Skill (Ultrafast)
├── fragen.md             die 5 Fragen fürs Vorbereitungs-Video
├── scripts/transcribe.py Video → Transkript (nur Claude Code, faster-whisper, lokal)
└── templates/
    ├── brand-dna.md      wer ich bin, Werte, Stimme
    ├── brand-look.md     Farben, Schrift, Bildstil, Fotos
    ├── brand-content.md  Posts, Captions, Reels, Karussells
    └── brand-website.md  One-Pager als eine HTML-Datei
```
Bewusst **nicht** unter `.claude/skills/`, damit die Vorlagen nicht in Maiks eigene Sessions laden.

## Für Teilnehmende
1. Vorher: Video nach `fragen.md` aufnehmen (mit Claude Code reicht das Video – der Skill transkribiert selbst; in der Claude-App Transkript exportieren), 5–10 Fotos bereitlegen, Claude Pro.
2. Im Workshop: `brand-builder.zip` in Claude hochladen (Einstellungen → Fähigkeiten → Skills), Chat starten: „Brand-Builder starten“ + Transkript und Fotos anhängen.
3. Die vier erzeugten Skills als ZIP herunterladen und genauso hochladen.

## ZIP bauen
`bash build_zip.sh` → `dist/brand-builder.zip` (Ordner `brand-builder/` mit `SKILL.md` an der Wurzel).

## Ablauf 60 Min
0–5 Ergebnis vorab zeigen · 5–15 Video → Transkript · 15–30 Brand-Builder, DNA prüfen · 30–40 Look aus Fotos · 40–55 live ein Post + Website-Skizze · 55–60 Wiederverwenden, Fragen

## Vor dem Workshop testen (Maik)
- [ ] Einmal mit eigenem Video komplett durchspielen (Claude-App, Skill hochgeladen)
- [ ] Prüfen, ob die App die vier ZIPs sauber anbietet und der Upload klappt
- [ ] Beispiel-Ergebnis als Einstieg bereitlegen
