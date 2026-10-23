---
name: flow-design
description: Das visuelle Design von Flow Media AI – Plakate, Flyer, Instagram-Posts, Karussells, Story-Grafiken, Reel-Texte, Angebote und Seiten im Flow-Look (schwarz-weiß, minimalistisch, große schmale Versal-Überschriften, ein blauer Akzent). Laden, sobald für Flow Media AI etwas Visuelles gestaltet oder Content mit Layout gebaut wird; zusammen mit `creative-director` (Inhalt) – dieser Skill regelt das Aussehen.
---

# Flow Design (Stand 23.10.2026, aus Maiks Plakaten)

Abgeleitet aus Maiks eigenen Gestaltungen in Google Drive (`Flow Media AI › 01_Marketing › Reels`): **„Flow Business Community“**, **„Zwei Ideen. Eine Vision.“** (App-Flyer), **„AI Masterclass“** und das Wellen-Zeichen. Inhalt und Regeln für Posts kommen aus `creative-director` und `CLAUDE.md`; dieser Skill regelt nur das Aussehen.

**Grundidee:** Wie ein gutes Magazin-Cover. Schwarz, weiß, viel Luft, eine laute Überschrift, ein echtes Foto, sonst nichts.

## 1. Farben
| Token | Wert | Einsatz |
|---|---|---|
| `--black` | `#0B0B0B` | Hintergrund (Standard bei Plakaten, Posts, Reels-Titeln) |
| `--white` | `#FFFFFF` | Überschriften, Text auf Schwarz |
| `--grey` | `#9A9A9A` | Nebentext, Labels, Linien (`#2A2A2A` als Linie auf Schwarz) |
| `--paper` | `#F4F4F1` | heller Gegenentwurf (Angebote, Dokumente, Folien zum Drucken) |
| `--blue` | `#2F5BFF` | **einziger Akzent**: ein Wort, ein Preis, ein Glow, ein Button – nie Flächen |

- Pro Motiv höchstens **ein** blaues Element. Keine zweite Akzentfarbe, keine Verläufe in Bunt. „Primärfarben“ heißt bei Flow: Schwarz, Weiß, Blau.
- Hell (`--paper` + `--black`) nur für Dokumente/Angebote und wenn ein Motiv bewusst kontrastieren soll.

## 2. Schrift
| Rolle | Schrift (Google Fonts, frei) | Stil |
|---|---|---|
| Headline | **Oswald 700** (Alternative: Bebas Neue) | VERSALIEN, schmal, Zeilenabstand 0.9–0.95, Laufweite 0 bis −1 % |
| Wortmarke „FLOW / MEDIA AI“ | **Montserrat 600** | Versalien, weit gesperrt (+30 bis +40 %), „MEDIA AI“ halb so groß darunter |
| Labels / Rubriken | Montserrat 500 | Versalien, 11–14 px bzw. 2–3 % der Bildbreite, gesperrt +12 % |
| Fließtext | **Inter 400/500** | normal geschrieben, kurze Zeilen, max. 2–3 Zeilen pro Block |
| Handschrift (optional) | Caveat | nur für eine persönliche Notiz/Frage („Welche Idee findet ihr spannender?“) |

- Überschriften sind **groß**: 12–18 % der Bildbreite pro Zeile, 2–4 Wörter pro Zeile, linksbündig (Plakat) oder zentriert (Cover).
- Hierarchie in höchstens drei Stufen: Headline → Unterzeile (gesperrte Versalien, grau oder weiß) → Info.

## 3. Layout
- **Raster:** Rand 6–8 % der Breite rundum; alles auf eine linke Kante ausrichten.
- **Wortmarke** oben (links oder zentriert), klein, mit viel Luft.
- **Headline** im oberen Drittel, Foto daneben oder darunter.
- **Feine Linien** (1 px, `#2A2A2A` bzw. Weiß 20 %) trennen Bereiche; darunter 2–3 Spalten mit Mini-Icon + Label („BUSINESS & MARKETING · KI & DIGITALE TOOLS · AUSTAUSCH & UMSETZUNG“).
- **Icons:** dünne Linien-Icons (1,5 px), weiß, nie gefüllt, nie bunt.
- **Abschluss unten:** Handlungsaufforderung in Versalien („JETZT DABEI SEIN“) + kleine Zeile mit Ort/Bedingung („Kostenlose Community · Bielefeld & Münster“).
- **Preis-Badge** (wenn es einen Preis gibt): große Zahl in Oswald, „PRO PERSON“ als Label darunter, dünner Rahmen; hier darf das Blau sitzen.
- Viel Schwarz stehen lassen. Wenn es voll wirkt: Text streichen, nicht kleiner machen.

## 4. Fotos
- **Schwarz-weiß**, kontrastreich, leichtes Korn, natürliche Situationen: Laptop im Café, Hände am Rechner, Gruppe am Tisch, Bielefeld/Münster-Silhouette.
- Menschen echt und nahbar, keine Hochglanz-Stockfotos, keine erkennbar fremden Personen ohne Einverständnis.
- **Maik-Bilder:** Das KI-generierte Profilbild und KI-Porträts nur **klein** einsetzen (Regel vom 19.10.2026 in `marketing/brand/README.md`). Groß nur echte Fotos von Maik. Ob Maik diese Regel für Plakate lockern will, bei ihm nachfragen.
- Bildschirme/Apps im Foto: nur eigene Tools; keine erfundenen Zahlen (z. B. Gewinne) – wenn Beispielwerte, dann im Bild als „Beispiel“ kennzeichnen.

## 5. Formate
| Format | Maße | Aufbau |
|---|---|---|
| Plakat / Flyer | A4/A5 hoch, digital 1024×1536 | Wortmarke · Headline · Foto · Linie + 3 Spalten · CTA |
| Instagram-Post | 1080×1350 | Headline groß, ein Foto, max. 15 Wörter |
| Karussell | 1080×1350 je Folie | Folie 1 = Headline + Foto, Folien 2–n = eine Aussage je Folie, letzte = Frage/CTA |
| Story / Reel-Cover | 1080×1920 | Headline im oberen Drittel, unten 20 % frei (Instagram-UI) |
| Reel-Texte im Bild | 1080×1920 | weiße Oswald-Versalien auf Schwarz oder auf abgedunkeltem Foto, ein Wort in Blau |
| Angebot / Dokument | A4 | hell (`--paper`), Wortmarke oben, Headline Oswald, Text Inter |

## 6. Texte im Design
- Kurz, konkret, Versalien-Headlines mit Punkt am Ende: „ZWEI IDEEN. EINE VISION.“ · „BUILD. MARKET. GROW.“
- Dreiklang funktioniert: „IDEEN VERWIRKLICHEN. MÖGLICHKEITEN SCHAFFEN. MENSCHEN BEFÄHIGEN.“
- Nichts versprechen, was nicht stimmt (kein „PROFITABEL“, keine Fantasie-Renditen, keine erfundenen Teilnehmerzahlen).

## 7. Nicht
- Keine bunten Verläufe, Neon, Glitzer, Emojis als Gestaltungselement.
- Nicht der Kupfer-/Gold-Look von THE TRIBE, nicht der Dating-Look (`shotwAIse`) – eigene Marken.
- Keine zweite Display-Schrift, keine Schrift unter 11 px in Drucksachen.
- Kein Logo-Wasserzeichen fremder Tools (z. B. „CapCut AI“) im fertigen Motiv.

## 8. Umsetzung (wenn Claude baut)
- HTML/CSS mit den Tokens oben, Schriften per Google Fonts (`Oswald:wght@700`, `Montserrat:wght@500;600`, `Inter:wght@400;500`), Rendern mit Playwright als PNG/MP4 (Vorgehen wie bei R002/R004 in `content/reels/`).
- Fotos: eigene Bilder aus Drive; Schwarz-Weiß + Korn per CSS (`filter: grayscale(1) contrast(1.15)`) oder ffmpeg.
- Vor Abgabe: Checkliste unten.

## 9. Checkliste
1. Schwarz/Weiß, höchstens ein blaues Element? 2. Eine Headline, groß, Versalien, max. 4 Wörter pro Zeile? 3. Wortmarke klein und mit Luft? 4. Genug Leerraum, Rand 6–8 %? 5. Foto s/w, echt, KI-Maik nur klein? 6. Keine erfundenen Zahlen/Versprechen? 7. Unten 20 % frei (bei 9:16)? 8. Keine fremden Wasserzeichen, kein Tribe-/Dating-Look?
