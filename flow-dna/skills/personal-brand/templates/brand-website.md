---
name: {{vorname}}-brand-website
description: Baut Websites und Landingpages für {{name}} – One-Pager, Angebots- oder Event-Seiten – als eine HTML-Datei im Look und in der Stimme von {{vorname}}. Laden, wenn für {{vorname}} eine Website, Landingpage oder Link-in-Bio-Seite entstehen soll; nutzt {{vorname}}-brand-dna und {{vorname}}-brand-look.
---

# Website: {{name}}

**Zuerst `{{vorname}}-brand-dna` (Texte, Stimme) und `{{vorname}}-brand-look` (Farben, Schrift, Fotos) lesen.**

## Aufbau One-Pager
1. **Hero:** Kern-Satz als Headline, ein Satz darunter, Foto von {{vorname}}, ein Button ({{haupt_cta}}).
2. **Für wen:** Zielgruppe und ihr Problem in 3 kurzen Punkten.
3. **Was ich mache:** {{angebote}}
4. **Warum ich:** Geschichte in 3–4 Sätzen + Werte.
5. **So läuft's:** 3 Schritte.
6. **Kontakt:** {{kontakt}} – nur echte Daten, sonst `[offen: …]`.
7. **Footer:** Impressum- und Datenschutz-Link (Pflicht in DE; Inhalte nicht erfinden, Platzhalter lassen).

## Technik
- **Eine** `index.html`, CSS im `<style>`, keine Build-Tools; Google Fonts aus `{{vorname}}-brand-look`.
- Mobil zuerst (360 px), dann Desktop; Bilder `loading="lazy"`, Alt-Texte.
- Farben als CSS-Variablen aus dem Look; Akzent sparsam.
- Keine Tracking-Skripte ohne Rückfrage.

## Texte
- In {{vorname}}s Stimme, kurze Absätze, keine Agentur-Floskeln.
- Keine erfundenen Kunden, Logos, Bewertungen oder Zahlen.

## Ausliefern
Datei zum Download geben + 2 Sätze, wie man sie veröffentlicht (z. B. Netlify Drop oder GitHub Pages: Datei hochladen, Link teilen).
