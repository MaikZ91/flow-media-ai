---
name: flow-design
description: Das visuelle Design von Flow Media AI – Plakate, Flyer, Instagram-Posts, Karussells, Story-Grafiken, Reel-Texte, Angebote und Seiten im Flow-Look (schwarz-weiß, minimalistisch, große schmale Versal-Überschriften, ein blauer Akzent). Laden, sobald für Flow Media AI etwas Visuelles gestaltet oder Content mit Layout gebaut wird; zusammen mit `creative-director` (Inhalt) – dieser Skill regelt das Aussehen.
---

# Flow Design (Stand 23.10.2026, aus Maiks Plakaten)

Abgeleitet aus Maiks eigenen Gestaltungen in Google Drive (`Flow Media AI › 01_Marketing › Reels`): **„Flow Business Community“**, **„Zwei Ideen. Eine Vision.“** (App-Flyer), **„AI Masterclass“**, das Wellen-Zeichen und das **Karussell „WOW. ICH HAB'S GESCHAFFT.“** (3 Folien, gepostet 23.10.2026 – aktuell die beste Referenz). Inhalt und Regeln für Posts kommen aus `creative-director` und `CLAUDE.md`; dieser Skill regelt nur das Aussehen.

**Grundidee:** Wie ein gutes Magazin-Cover. Schwarz, weiß, viel Luft, eine laute Überschrift, ein Foto von Maik, sonst nichts.

**Personal Brand (Maik, 23.10.2026):** Auf **jedem** Post, jeder Karussell-Folie 1, jedem Reel-Cover und jedem Plakat ist Maik zu sehen – groß als Hauptmotiv oder klein (Kreis, Ecke, Signatur). Kein Motiv ohne Maik.

## 1. Farben
| Token | Wert | Einsatz |
|---|---|---|
| `--black` | `#0B0B0B` | Hintergrund (Standard bei Plakaten, Posts, Reels-Titeln) |
| `--white` | `#FFFFFF` | Überschriften, Text auf Schwarz |
| `--grey` | `#9A9A9A` | Nebentext, Labels, Linien (`#2A2A2A` als Linie auf Schwarz) |
| `--paper` | `#F4F4F1` | heller Gegenentwurf (Angebote, Dokumente, Folien zum Drucken) |
| `--blue` | `#2F5BFF` | **einziger Akzent**: ein Wort, ein Preis, ein Glow, ein Button – nie Flächen |

- **Warme Variante (Karussell 23.10.2026):** Foto leicht warm getönt (Sepia-Hauch), Text cremeweiß `#F2EDE4`, kurze Trennlinien in Sand `#E8CFA8` (2 px, ca. 40 px lang: unter der Wortmarke, über Info-Blöcken, über „SWIPE“). Sand nur als feine Linie, nie als Fläche oder Schrift, und **nie zusammen mit Blau** in einem Motiv. Offen bei Maik: Ist die warme Variante der neue Standard (dann wird Sand der Akzent statt Blau) oder bleibt Blau? Bis zur Antwort beides erlaubt, pro Post/Serie eines.
- Pro Motiv höchstens **ein** blaues Element. Keine zweite Akzentfarbe, keine Verläufe in Bunt. „Primärfarben“ heißt bei Flow: Schwarz, Weiß, Blau.
- Hell (`--paper` + `--black`) nur für Dokumente/Angebote und wenn ein Motiv bewusst kontrastieren soll.

## 2. Schrift
| Rolle | Schrift (Google Fonts, frei) | Stil |
|---|---|---|
| Headline | **Oswald 700** (Alternative: Bebas Neue) | VERSALIEN, schmal, Zeilenabstand 0.9–0.95, Laufweite 0 bis −1 % |
| Wortmarke „FLOW / MEDIA AI“ | **Montserrat 600** (Übergang) | Versalien, weit gesperrt (+30 bis +40 %), „MEDIA AI“ halb so groß darunter. Im Karussell vom 23.10. steht „FLOW“ in einer breiten, technischen Schrift (breit laufend, Querschnitte in den Buchstaben) – das ist die neuere Wortmarke; als Bilddatei nach `marketing/brand/` legen, sobald Maik sie ohne Hintergrund hat, dann ersetzt sie die Montserrat-Variante |
| Labels / Rubriken | Montserrat 500 | Versalien, 11–14 px bzw. 2–3 % der Bildbreite, gesperrt +12 % |
| Fließtext | **Inter 400/500** | normal geschrieben, kurze Zeilen, max. 2–3 Zeilen pro Block |
| Code / Terminal | JetBrains Mono 400 | nur in Vorher/Nachher-Karten und Terminal-Ausschnitten |
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
- **Schwarz-weiß** (auch leicht warm getönt wie im Karussell), kontrastreich, leichtes Korn, natürliche Situationen: Laptop im Café, Hände am Rechner, Gruppe am Tisch, Bielefeld/Münster-Silhouette.
- Menschen echt und nahbar, keine Hochglanz-Stockfotos, keine erkennbar fremden Personen ohne Einverständnis.
- **Maik in jedem Motiv** (siehe Personal Brand oben). Bevorzugt die freigegebenen Porträts unten; sie dürfen **groß** eingesetzt werden (Maik, 23.10.2026). Nur `marketing/brand/profilbild_ki.png` bleibt klein (Profilbild, Kreis, Signatur), weil es Maik aus der Nähe nicht ähnlich genug sieht.
- **Freigegebene Maik-Porträts** (Drive `01_Marketing › Reels`, 1024×1536, s/w-warm, Brille, dunkle Jacke, Laptop/Café-Tisch, Kaffeetasse):

  | Drive-ID | Pose | Gut für |
  |---|---|---|
  | `1cNZuxy8kSNSsybg1KNPBtlgc4eJ2epf7` | frontal, Blick in die Kamera, ruhig-selbstbewusst, Laptop vorn | Hook, Cover, Folie 1, Ergebnis-Posts |
  | `1qLWfXm9pKgY_jiVDqIz6aNLiIdNYZo4U` | Blick auf den Laptop, konzentriert | „So hab ich's gemacht“, Prozess, Anleitung |
  | `1D26WtaT-jlC1C1QZRInOfbedtVhG1Y2S` | leicht schräg, Kopf geneigt, Blick in die Kamera | Vorher/Nachher, Einordnung, CTA-Folie |

  Die Dateien sind fertige Folien mit Text – zum Wiederverwenden das Porträt freistellen bzw. zuschneiden (Personenbereich rechts) oder Maik nach den Originalen ohne Text fragen. Neue Porträts derselben Serie dazunehmen, wenn Maik sie freigibt; hier eintragen.
- **Pose wechseln:** nicht zweimal hintereinander dasselbe Porträt als Hauptmotiv; Blick in die Kamera für Hook/CTA, Blick auf den Laptop für Prozess.
- **Komposition wie im Karussell:** Maik rechts angeschnitten (Kopf im oberen Drittel, Laptop unten), Text links auf dem dunklen Bildteil – so überlappt nichts das Gesicht.
- Bildschirme/Apps im Foto: nur eigene Tools; keine erfundenen Zahlen (z. B. Gewinne) – wenn Beispielwerte, dann im Bild als „Beispiel“ kennzeichnen.

## 5. Formate
| Format | Maße | Aufbau |
|---|---|---|
| Plakat / Flyer | A4/A5 hoch, digital 1024×1536 | Wortmarke · Headline · Foto · Linie + 3 Spalten · CTA |
| Instagram-Post | 1080×1350 | Headline groß, ein Foto, max. 15 Wörter |
| Karussell | 1080×1350 je Folie | Folie 1 = Headline + Foto, Folien 2–n = eine Aussage je Folie, letzte = Frage/CTA. Unten links „SWIPE →“, unten rechts „1 / 3“ (gesperrte Versalien, klein); auf der letzten Folie statt „SWIPE“ die Frage/CTA |
| Story / Reel-Cover | 1080×1920 | Headline im oberen Drittel, unten 20 % frei (Instagram-UI) |
| Reel-Texte im Bild | 1080×1920 | weiße Oswald-Versalien auf Schwarz oder auf abgedunkeltem Foto, ein Wort in Blau |
| Angebot / Dokument | A4 | hell (`--paper`), Wortmarke oben, Headline Oswald, Text Inter |

**Achtung Format:** Die Karussell-Folien vom 23.10. sind 1024×1536 (2:3). Instagram zeigt im Feed höchstens 4:5 (1080×1350) bzw. 3:4 (1080×1440) und schneidet 2:3 oben/unten ab. Darum direkt in 1080×1350 bauen oder bei 2:3 Wortmarke und „SWIPE“ mindestens 8 % vom oberen/unteren Rand einrücken.

## 6. Texte im Design
- Kurz, konkret, Versalien-Headlines mit Punkt am Ende: „ZWEI IDEEN. EINE VISION.“ · „BUILD. MARKET. GROW.“
- Dreiklang funktioniert: „IDEEN VERWIRKLICHEN. MÖGLICHKEITEN SCHAFFEN. MENSCHEN BEFÄHIGEN.“
- **Aufbau aus dem Karussell (bewährt):** Dreiklang als Kicker über der Headline (gesperrte Versalien, dünn, weiß 80 %: „EIN PROJEKT. / EIN SKILL. / GROSSE WIRKUNG.“) → Headline groß („WOW. ICH HAB'S GESCHAFFT.“) → 2–3 Zeilen Fließtext mit dem konkreten Ergebnis → kurze Linie → Info.
- **Info-Liste mit Icons:** dünnes Linien-Icon + Titel in Versalien + Unterzeile klein gesperrt („GITHUB / REVERSE ENGINEER SKILL“). Höchstens drei Einträge.
- **Vorher/Nachher-Karten:** zwei dunkle Fenster mit dünnem Rahmen und drei Punkten oben, „ALT“ → „NEU“, Inhalt in Monospace (z. B. JetBrains Mono), Pfeil dazwischen.
- Nichts versprechen, was nicht stimmt (kein „PROFITABEL“, keine Fantasie-Renditen, keine erfundenen Teilnehmerzahlen).

## 7. Nicht
- Keine bunten Verläufe, Neon, Glitzer, Emojis als Gestaltungselement.
- Nicht der Kupfer-/Gold-Look von THE TRIBE (Gold-Flächen, Kupfer-Verläufe, Glanz – die feinen Sand-Linien der warmen Variante sind davon klar getrennt), nicht der Dating-Look (`shotwAIse`) – eigene Marken.
- Keine zweite Display-Schrift, keine Schrift unter 11 px in Drucksachen.
- Kein Logo-Wasserzeichen fremder Tools (z. B. „CapCut AI“) im fertigen Motiv.

## 8. Umsetzung (wenn Claude baut)
- HTML/CSS mit den Tokens oben, Schriften per Google Fonts (`Oswald:wght@700`, `Montserrat:wght@500;600`, `Inter:wght@400;500`), Rendern mit Playwright als PNG/MP4 (Vorgehen wie bei R002/R004 in `content/reels/`).
- Fotos: eigene Bilder aus Drive; Schwarz-Weiß + Korn per CSS (`filter: grayscale(1) contrast(1.15)`) oder ffmpeg.
- Vor Abgabe: Checkliste unten.

## 9. Checkliste
1. Schwarz/Weiß, höchstens ein blaues Element? 2. Eine Headline, groß, Versalien, max. 4 Wörter pro Zeile? 3. Wortmarke klein und mit Luft? 4. Genug Leerraum, Rand 6–8 %? 5. Ist Maik im Motiv (groß oder klein), mit freigegebenem Porträt, Gesicht frei von Text? Andere Pose als im letzten Post? 6. Keine erfundenen Zahlen/Versprechen? 7. Unten 20 % frei (bei 9:16)? 8. Keine fremden Wasserzeichen, kein Tribe-/Dating-Look? 9. Format 4:5 bzw. bei 2:3 Rand eingerückt; letzte Karussell-Folie mit Frage/CTA statt „SWIPE“?
