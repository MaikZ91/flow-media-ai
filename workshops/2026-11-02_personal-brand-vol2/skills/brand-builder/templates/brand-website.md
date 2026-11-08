---
name: {{vorname}}-brand-website
description: Baut Websites und Landingpages für {{name}} – One-Pager, Angebots- oder Event-Seiten – als eine HTML-Datei im Look und in der Stimme von {{vorname}}. Laden, wenn für {{vorname}} eine Website, Landingpage oder Link-in-Bio-Seite entstehen soll; nutzt {{vorname}}-brand-dna und {{vorname}}-brand-look.
---

# Website: {{name}}

**Zuerst `{{vorname}}-brand-dna` (Texte, Stimme) und `{{vorname}}-brand-look` (Farben, Schrift, Fotos) lesen.**

## Aufbau One-Pager (Premium)
1. **Hero = großes Foto von {{vorname}} im Vollbild** (füllt den ersten Bildschirm, langsamer Zoom, dunkler Farbverlauf darüber, Menü transparent oben drauf). Darauf: kleine Begrüßung, Kern-Satz als große Headline mit einem farbigen Wort, ein Satz darunter, Button ({{haupt_cta}}) + zweiter Button, eine Zeile mit Ort und einem echten Vorteil.
2. **Icon-Leiste** direkt darunter (4 Stärken mit Linien-Icons, dunkle Karte, überlappt das Foto).
3. **Für wen:** Zielgruppe und ihr Problem in 3 kurzen Punkten, in ihrer Sprache.
4. **Angebote als 2–3 Pakete:** {{angebote}} – Name, für wen, was drin ist, Ergebnis (Preis nur, wenn {{vorname}} ihn nennen will).
5. **So läuft's:** 3–4 Schritte (eigene Methode mit Namen, falls vorhanden).
6. **Über mich:** Geschichte in 3–4 Sätzen + Werte, zweites Foto mit kleiner Info-Karte.
7. **Farbiges Band mit Hauptaktion:** Erstgespräch buchen (Kalender-Link) oder WhatsApp, daneben Telefon groß.
8. **Stimmen** nur echte mit Freigabe – sonst ein Leitsatz von {{vorname}} im dunklen Band.
9. **Kontakt:** {{kontakt}} mit rundem Avatar-Foto und Anruf-/WhatsApp-Knopf – nur echte Daten, sonst `[offen: …]`.
10. **Footer** dunkel: Impressum- und Datenschutz-Link (Pflicht in DE; Inhalte nicht erfinden). Dazu eine feste Button-Leiste unten auf dem Handy und optional ein kleiner Avatar-Knopf unten rechts.

Wirkung: groß, ruhig, hochwertig – viel Luft, runde Ecken, weiche Schatten, Abschnitte mit wechselndem Hintergrund, sanfte Einblend-Animationen beim Scrollen.

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
