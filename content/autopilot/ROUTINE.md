# Instagram-Autopilot @flow.media.ai

**Auftrag von Maik, 23.11.2026:** „Du sollst halt 3 mal am Tag posten, dabei sowohl die richtige Zeit, Thema, Format etc. auswählen, ohne dass ich was sage – data driven, was am besten geht.“
Damit ist automatisches Posten auf @flow.media.ai freigegeben. Der Autopilot entscheidet selbst und meldet danach kurz, was gepostet wurde.

Ein Lauf = **ein** Post. Es gibt drei Läufe am Tag, die als geplante Aufgabe „Flow Autopilot“ laufen.
- Die Slots stehen unten unter „Slots“.
- Auslöser ist ein Cron-Ausdruck, eingestellt etwa 40 Minuten vor der Zielzeit.
- Den Cron passt der Wochen-Rückblick an (siehe Schritt 8).

## Werkzeuge

- **`tools/ig/ig.py`** ist das Hilfsskript für die Graph-API.
  - Der Token liegt als Network Secret für `graph.facebook.com` in der Cloud-Umgebung „Full“. Nie ausgeben, nie ins Repo.
  - Ohne Secret (Fehler 400/401 „access token“): nichts posten. Im Bericht schreiben „Token fehlt/abgelaufen – bitte neu als Network Secret hinterlegen“.
  - Befehle:
    - `insights` liest alle Posts mit Views, Reach, Saves, Shares und Likes, mit Uhrzeit in Berlin-Zeit. Es schreibt `content/autopilot/insights.json`.
    - `today` zeigt die heutigen Posts.
    - `wait-url` wartet, bis eine Datei auf GitHub Pages online ist.
    - `reel`, `carousel`, `image` und `story` veröffentlichen.
- **Öffentliche URLs:** Medien müssen öffentlich erreichbar sein. Ins Repo committen und pushen, dann:
  - URL: `https://maikz91.github.io/flow-media-ai/<pfad>`
  - vor dem Posten `ig.py wait-url <url>` aufrufen (Pages braucht 1–3 Minuten).
- **Bauen:** HTML + Playwright + ffmpeg, wie bisher (R044, R045, R053 `reel.html`/`render.js`). Chromium unter `/opt/pw-browsers`, ohne `playwright install`.
- **Video Cutter:** nur, wenn neues Rohmaterial von Maik da ist.

## Ablauf je Lauf

1. **Vorbereiten:**
   - `git pull`.
   - `CLAUDE.md` (Brand, Tonalität), die Skills `creative-director`, `content-themen` und `flow-design`, `content/strategie/problem-zu-loesung.md`, `content/learnings.md` und diese Datei lesen.
2. **Doppelte vermeiden:**
   - `ig.py today` aufrufen.
   - Abbruch ohne Post und mit einer Zeile Bericht, wenn eine der Bedingungen zutrifft:
     - Heute sind schon 3 reguläre Posts draußen. Challenge-Posts (Caption beginnt mit „Tag N/31“) zählen nicht mit, insgesamt sind höchstens 4 am Tag erlaubt.
     - Der letzte Post ist weniger als 3 Stunden her.
3. **Daten:**
   - `ig.py insights` aufrufen.
   - In `log.md` bei jedem Post, der 24 Stunden oder älter ist, die Zahlen nachtragen.
   - Dann entscheiden. Grundlage ist der Vergleich nach **Säule, Format, Hook-Art und Uhrzeit**: Views, Reach, Saves und Shares. Die Kennzahlen stehen unten.
4. **Entscheiden** (Begründung mit Zahl in `log.md`):
   - **Säule:**
     - Zwei von drei Posts am Tag gehen an die Säule, die gerade am besten läuft (ausnutzen).
     - Einer testet etwas anderes (erkunden).
     - Dieselbe Säule nie dreimal hintereinander.
   - **Format:**
     - Reels sind Standard: Bisher waren alle Top-Posts Reels.
     - Karussell oder Einzelbild nur gezielt als Test für Saves (z. B. Anleitung, Liste, Prompt-Sammlung), höchstens 1 pro Tag.
     - Stories gehören zu jedem Lauf dazu (siehe Schritt 7b), sie zählen nicht zu den 3 Feed-Posts.
   - **Eine Test-Variable** je Post, z. B. Hook-Art, Länge, Musik, Uhrzeit, mit/ohne Gesicht im ersten Bild. Ins Log `variable` und `variante` schreiben.
5. **Bauen:**
   - Flow-Look nach `flow-design`, Maik in jedem Motiv. Dafür vorhandene echte Fotos und Avatare im Repo nutzen, z. B. `flow-dna/img/maik_front.jpg`, `content/posts/*/img/maik_*.jpg`.
   - **Echte Fotos zuerst aus `content/personal/`** (10 Fotos von Maik mit Beschreibung im README: Münster, Strand, Café, Selfie, S/W). Für Reels als Bildfolge mit Bewegung (Zoom/Ken Burns, Schnitt auf den Beat) und Text-Hook, nie als stehendes Porträt mit Text. Ein Foto höchstens einmal pro Woche. Hintergrundpersonen vor dem Posten prüfen.
   - Reel:
     - 1080×1920, H.264 + AAC, 8–30 Sekunden.
     - **Hook-Pflicht** (Maik, 23.11.2026, Details in `creative-director` Teil C §2):
       - Erst **3 Hook-Varianten** schreiben.
       - Jede nach den 4 Wirkungen bewerten, je 0–2 Punkte: Emotion · Versprechen oder Spannung · konkretes Problem · Zielgruppe erkennt sich. Nur ein Hook mit mindestens 6 von 8 Punkten wird genommen.
       - **Immer alle drei** kombinieren, Visual + Text + Audio = maximale Aufmerksamkeit. Fehlt einer, ist das Reel nicht fertig:
         - Text groß ab Frame 0,
         - Bewegung ab Frame 0,
         - Musik-Akzent oder stärkster Satz auf Frame 0.
       - Die 3 Varianten aus **verschiedenen der 6 Text-Hook-Arten** schreiben (`creative-director` Teil C §2): Problem, Myth-Busting, Bold Statement, Story (nur echt), Frage, Benefit (nur einlösbar).
       - Die gewählte Art rotiert als Test-Variable. Im Wochen-Rückblick die Hook-Arten nach Views und Reach vergleichen.
       - Im Log Hook-Text, Hook-Arten und Punktzahl eintragen.
     - Lesbar ohne Ton.
     - **Musik passend zum Reel wählen, nie immer denselben Track:**
       - **Jedes Mal neu entscheiden**, nicht immer aus derselben Liste nehmen:
         1. Stimmung, Tempo und Länge des Reels festlegen (Beispiel: ruhige Persönlichkeit, 15 s, nachdenklich).
         2. Alle Kandidaten prüfen: eigene MZ.9-Tracks in `eigene/` und freie Tracks in `frei/`, dazu neue Tracks aus **Pixabay Music**, **Mixkit** und **Freesound** (Freesound nur Tracks mit Lizenz **CC0**; alle drei kostenlos und kommerziell nutzbar, ohne Namensnennungspflicht). Die Lizenz auf der Quellseite selbst prüfen und festhalten. Keine Tracks mit Namensnennungspflicht oder Nutzungsverbot für Werbung und Social Media; keine Creative-Commons-Tracks mit NC- oder ND-Zusatz.
         3. Den Track wählen, dessen Tempo, Energieverlauf und Stelle für den Einstieg zum Reel passen. Begründung ins Log.
         4. Neue Tracks mit Quelle, Lizenz-Link, Lizenzdatum und Dateiname in `content/musik/README.md` eintragen.
         5. Wenn der Katalog nicht erreichbar ist: aus dem README nehmen, den Track mit der geringsten Nutzung in den letzten 10 Reels, und das im Bericht vermerken.
       - Rotation: Dieselbe Datei höchstens einmal in 5 Reels. Im Log die Musikdatei eintragen, damit das prüfbar ist.
       - Passung prüfen: Schnitt auf den Beat (Musik-Einsatz an der Stelle des Hooks), Lautstärke leise unter Sprache.
       - Ohne Stimme und ohne Sprache: Der Track muss das Reel alleine tragen.
       - Eigene MZ.9-Tracks zuerst, wenn Stimmung passt; sonst freie Musik aus `frei/`.
     - Musik aus `content/musik/`. Bei einem MZ.9-Track kommt die Zeile „🎵 MZ.9 – <Titel> · @mz.9_nyc“ in die Caption.
   - Cover-JPG dazu.
   - Ablage: `content/reels/R<nnn>-<slug>/` bzw. `content/posts/P<nnn>-<slug>/`. Die nächste freie Nummer nehmen. README mit Konzept, Caption, Quellen, Test-Variable.
6. **Prüfen (Pflicht, sonst nicht posten):**
   - Mindestens 4 Frames bzw. alle Folien als PNG ansehen, darunter **Frame 0** (stoppt der Hook allein, ohne Ton?). Prüfen auf:
     - abgeschnittenen Text,
     - Überlappungen,
     - Tippfehler,
     - Lesbarkeit auf dem Handy,
     - die Safe-Zone (oben 250 px und unten 350 px frei für die Instagram-UI).
   - Checklisten `creative-director` Teil C §5 und `flow-design` §9.
   - Jede Zahl und jede News mit Quelle prüfen:
     - Primärquelle oder zwei unabhängige Quellen.
     - News höchstens 7 Tage alt.
     - Quelle steht im Bild oder in der Caption.
   - Im Zweifel nicht posten, sondern im Bericht erklären, was fehlt.
7. **Posten:**
   - Committen und pushen.
   - `ig.py wait-url` aufrufen.
   - `ig.py reel <mp4-url> <caption.txt> <cover-url>` (bzw. `carousel`) aufrufen.
   - Bei einem Fehler einmal beheben und erneut versuchen, dann aufhören und berichten.
   - Danach:
     - Permalink, Uhrzeit, Säule, Format, Hook, Variable und Hypothese in `log.md` eintragen.
     - Den Verlauf in `content-themen` §6 eintragen.
     - Committen und pushen.
7b. **Stories (Maik, 23.11.2026: „in Story auch posten“)**, 1–2 je Lauf:
   - **Immer:** den neuen Feed-Post als Story ankündigen. Bei einem Reel das MP4 direkt als Story (`ig.py story <mp4-url>`). Bei Karussell oder Bild eine eigene Story-Grafik 1080×1920 als JPG mit „Neuer Post“, dem Hook und einem Bild daraus.
   - **Zusätzlich an Termin-Tagen** im Morgen- oder Mittag-Lauf eine Termin-Story im Flow-Look (Vorlage P022: dunkles s/w-Porträt, große Uhrzeit in Blau):
     - Montag: Workshop 18 Uhr, Thema aus `marketing/community/` (THEMEN-Map).
     - Freitag: Stammtisch.
     - Bis 30.11.: täglich höchstens eine Challenge-Story.
     - Termine und Themen nur aus dem Repo, nichts erfinden.
   - Story-Grafiken: Text in der Mitte halten, also oben 250 px und unten 300 px frei. Immer JPG, nicht PNG. Ablage im Ordner des Posts.
   - Sticker (Link, Umfrage, Countdown) kann die API nicht. Darum „Link in Bio“ oder „Schreib mir“ im Bild.
   - Daten: `ig.py stories` bei **jedem** Lauf aufrufen. Stories verschwinden nach 24 Stunden, die Zahlen bleiben nur so in `content/autopilot/stories.json`. Bei neuen Einträgen `inhalt` ergänzen (kurz: was war drauf).
   - Bewertung über Reach und Antworten, außerdem über die Navigation (viele „Verlassen“ = schwache Story). Daraus lernen, welche Story-Art trägt; im Wochen-Rückblick mit auswerten.
8. **Wochen-Rückblick:** Den macht nur der Abendlauf am Sonntag, zusätzlich zum Post.
   - Fazit der Woche oben in `content/learnings.md`: was bestätigt ist, was verworfen ist, was als Nächstes getestet wird.
   - Die Säulen-Reihenfolge unten aktualisieren.
   - Zeigen die Daten klar bessere Uhrzeiten (mindestens 2 Posts je Slot zum Vergleich), die Slots hier ändern. Dann den Cron der geplanten Aufgabe „Flow Autopilot“ per `update_trigger` anpassen (Trigger-ID unten).
9. **Bericht an Maik** in höchstens 3 Zeilen:
   - Link,
   - was und warum (mit Zahl),
   - was getestet wird.
   - „Von dir gebraucht:“ nur, wenn etwas wirklich nur Maik kann (neues Video, Token, Freigabe).

## Slot 4 · 31-Tage-Challenge (24.11.–24.12.2026)

Seit dem 23.11. kommt ein vierter Post pro Tag dazu (Maik: „Mache einen 4. Post pro Tag immer für den 31-Tage-Challenge“).
- Eigene geplante Aufgabe um 15:17, Ziel etwa 16:00.
- Plan, Regeln und Status stehen in `content/autopilot/challenge31.md`.
- Der Lauf geht wie oben (Schritte 1–9), aber das Thema steht fest: der Tag aus `challenge31.md`, der zum heutigen Datum gehört.
- Format, Hook-Art und Umsetzung wählt der Lauf selbst. Caption und erstes Bild beginnen mit „Tag N/31“.
- Nach Tag 31 schaltet sich die Aufgabe ab (`update_trigger` enabled=false, Trigger-ID in `challenge31.md`).

## Harte Regeln (zusätzlich zu `creative-director` Teil A §6)
- **Kein Reel nur mit Technik (Maik, 23.11.2026):** Terminal, Screens oder Ablaufgrafiken allein tragen kein Reel (R055 war so ein Test). Ein Reel braucht immer einen Menschen oder Moment, eine kleine Geschichte oder Überraschung und einen emotionalen Hook (Neugier, Identifikation, Staunen). Technik darf als Beleg dienen, nie als Hauptinhalt. Reichweite kommt bei Maik von persönlichen Geschichten (Wüste 957 Aufrufe), nicht von Prozessen.
- **Nicht jedes Mal Porträt (Maik, 23.11.2026):** Posts mit Maiks Gesicht und Text sehen sonst alle gleich aus und wirken billig. Pro Tag höchstens ein Porträt-Post. Sonst echtes Material: Screenshots, Bildschirmaufnahmen, Terminal-Looks, Karussells, Clips. Das Format wechselt, nie zweimal hintereinander dieselbe Gestaltung. Gestaltung des vorigen Posts im Log ansehen.

- **Nichts erfinden.**
  - Keine Kunden, Ergebnisse, Testimonials, Zahlen ohne Quelle.
  - Keine Erlebnisse, die Maik nicht wirklich hatte. Ich-Form nur für Dinge, die im Repo belegt sind (eigene Projekte, Learnings, Verlauf).
- **Keine KI-Stimme und kein KI-Avatar als Maik.** Text im Bild und Musik reichen.
- Echte Aufnahmen von Maik dürfen neu geschnitten werden (frühere Reels, RAW), wenn das Konzept neu ist.
- Kein Arbeitgeber-Content, niemanden markieren, keine The-Tribe- oder Dating-Werbung.
- **Angebote:**
  - Höchstens 1 Angebots- oder Community-Post pro Tag. Die Daten zeigen: Werbe-Posts laufen am schwächsten.
  - Bis zum Challenge-Start (30.11.) darf es täglich einer sein, ab dann jeden zweiten Tag.
  - Preise, Termine und Links nur aus dem Repo (`marketing/challenge/config.js`, `marketing/community/`).
- Keine Kommentare beantworten, keine DMs, kein Folgen, nichts löschen. Gepostete Beiträge nicht ändern.
- Keine Werbeanzeigen anlegen oder ändern.

## Kennzahlen

- Hauptziel ist **Reichweite bei Nicht-Followern** (Views und Reach). Bei 120 Followern zeigt alles über ~150 Views, dass der Post über die Follower hinausgeht.
- Zweitziel sind **Saves und Shares**. Bis zum 23.11. lagen beide bei 0, also ist jeder Save oder Share ein Signal.
- Ein Post wird erst nach 24 Stunden bewertet, endgültig nach 72 Stunden.

## Säulen (Reihenfolge nach Daten; Stand 23.11.2026, n = 26 Posts)

| # | Säule | Belege (Views) |
|---|---|---|
| 1 | Persönliche Story / Abenteuer mit echtem Material | Wüste 957 · „Hier hat es angefangen“ 138 |
| 2 | KI-News und neue Tools, verständlich erklärt, mit Quelle | Seedance 2.5 228 · KI im All 173 · Claude 5.2 152 |
| 3 | Selbst gebaut / Maker-Projekte (Build in public) | Roboterarm OP-Netz 174 · Plakat→Video 154 · Kleberoboter 147 · 3 Dinge 112 |
| 4 | Problem → Lösung / Anleitung (Ziel: Saves) | Website mit KI 71 · erste App 59 · Problem-Hook „Viele Ideen…“ 87 |
| 5 | Angebot / Community / Workshop / Challenge | 21–68, am schwächsten |

## Slots (Berlin-Zeit)

| Slot | Zielzeit | Cron-Start | Warum |
|---|---|---|---|
| Morgen | ~07:30 | 06:47 | morgens gute Werte (Plakat→Video 07:20 → 154; Community 07:34 → 87) |
| Mittag | ~12:30 | 11:47 | Test-Slot, noch wenig Daten |
| Abend | ~19:30 | 18:47 | stärkster Bereich (Wüste 19:27 → 957; Seedance 20:49 → 228; KI im All 22:20 → 173) |

`online_followers` liefert noch keine Daten (Stand 23.11.). Den Wert bei jedem Wochen-Rückblick neu abfragen: `GET /{ig}/insights?metric=online_followers&period=lifetime`.

Geplante Aufgabe: „Flow Autopilot: Instagram 3× täglich“ · Trigger-ID `trig_01PPnYqYZ1wt2HoaprdKai4H` (läuft in Maiks Hauptsession `session_013fteYFceKiG7Uk7Z2ie8Jy`, die ins Repo pushen darf; frische Sessions hatten keinen Push-Zugriff). Die alte Daily-Content-Routine (`trig_01FBws1P68soP9NQAu1MhsSv`) ist seit 23.11. ausgeschaltet.
