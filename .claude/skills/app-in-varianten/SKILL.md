---
name: app-in-varianten
description: Maiks Workflow für jede App, Web-App, Landing-Page oder jedes Tool: erst fünf Design-Varianten bauen, Maik fragen, welche ihm von Design und Features am besten gefällt, dann auf dieser Grundlage eine neue Version bauen und am Ende veröffentlichen (GitHub Pages, installierbar, Drive). Das Design richtet sich nach den Produktanforderungen und mitgelieferten Designs (z. B. Homepages, Fotos, Referenzen). Fehlende Fotos werden beschafft. Nutzen, wenn Maik etwas bauen will, besonders bei "5 Varianten", "Versionen zum Auswählen" oder wenn ein Ordner mit Anforderungen, Videos und Fotos vorliegt.
---

# App in Varianten bauen (Stand 03.11.2026, aus der Cocktail-App für Adil)

Maiks Arbeitsweise: nicht eine Lösung raten, sondern fünf verschiedene zeigen, damit er sieht, was ihm gefällt. Danach wird auf dem Gewählten aufgebaut und veröffentlicht. Gilt für **jede Art von App**, nicht nur für eine bestimmte Branche.

## Der Ablauf

### 1. Input einsammeln (Basis)
Alles, was Maik liefert, ist die Grundlage. Erst nachsehen, was da ist, bevor etwas gebaut oder recherchiert wird:
- **Produktanforderungen** (Markdown, Dokument, Chat): was die App können soll, für wen, welcher Eindruck.
- **Videos und Fotos**, oft in einem Ordner wie `Content/Media`. Die haben Vorrang vor allem Beschafften.
- **Mitgelieferte Designs und Referenzen:** Homepages, Screenshots, Plakate, Fotos von Räumen oder Produkten, Markenfarben. Daraus kommt der Stil (siehe Schritt 3).
- Gibt es zu Maiks eigener Marke einen Skill (`flow-design`) oder zum Kunden eine eigene Marke, daran halten.

Ist die Anforderung zu dünn, kurz nachfragen. Sonst nicht lange fragen, sondern bauen. Die Rückfrage kommt nach den Varianten.

### 2. Fehlendes beschaffen
- **Fotos** nur mit freier Lizenz (Wikimedia Commons, CC0, CC BY, CC BY-SA). Vorher als Kontaktbogen ansehen und das Passende auswählen. Autor, Lizenz und Quelle mit speichern und in der App anzeigen. Mitgelieferte Fotos nie ersetzen.
- **Inhalte** aus guten offenen Quellen holen und sauber aufbereiten. Selbst Erfundenes oder Geschätztes sichtbar kennzeichnen (z. B. "Hausrezept", "Schätzwert"), nie als Fakt ausgeben.
- Gibt es zu einem Begriff keine Standardquelle: nicht raten und verschweigen. Einen Vorschlag bauen, markieren und in der Zusammenfassung ansprechen.
- Nichts erfinden: keine Kunden, Zahlen, Bewertungen oder Testimonials.

### 3. Passendes Design ableiten
Das Design kommt aus den Produktanforderungen und dem Mitgelieferten, nicht aus einem festen Lieblingsstil:
- **Zielgruppe und Ort:** Bar, Praxis, Werkstatt, Onlineshop, Verein, Coaching? Daraus ergeben sich Stimmung, Farbe, Schrift und Bildsprache.
- **Mitgelieferte Seite oder Referenz:** Farben, Schriften, Form der Karten und Knöpfe, Stimmung übernehmen. Aus Fotos Farben ziehen (Hauptfarbe, Akzent). Die Seite ist Stilvorlage, nicht zum Kopieren: keine Namen, Logos, Marken, Texte oder Bilder des Vorbilds übernehmen.
- **Branchen-Logik als Startpunkt**, nicht als Zwang: z. B. Gastronomie dunkel und warm, Gesundheit hell und ruhig, Technik klar und kontrastreich, Kinder bunt und rund, Luxus viel Luft und Serifen.
- Die fünf Varianten bewegen sich **innerhalb dieses Rahmens** und unterscheiden sich in Aufbau, Bedienidee und Ton. Mindestens eine Variante darf mutig daraus ausbrechen.
- Ist nichts geliefert und nichts erkennbar: fünf deutlich verschiedene Richtungen zeigen, dann Maik wählen lassen.

### 4. Fünf Varianten bauen
- **Fünf Dateien** (`v1-….html` bis `v5-….html`), jede **eigenständig lauffähig** und per Doppelklick offen.
- **Gemeinsamer Kern** statt fünfmal derselbe Code: Daten in einer eigenen Datei als `<script>` (nicht per `fetch`, damit `file://` geht), gemeinsame Logik in `kern.js` und `kern.css`. Die Varianten unterscheiden sich in Aufbau und Stimmung, nicht in der Datenlage.
- **Wirklich verschieden:** z. B. Bildkarten-Raster, gedruckte Karte, Vollbild zum Wischen, Profi-Ansicht mit Liste und Detail, eine nach der Referenz. Nicht fünfmal dieselbe Seite mit anderer Farbe.
- Jede Variante hat die Kernfunktionen, sonst lässt sie sich nicht fair vergleichen.
- Handy zuerst (große Tippflächen, kein horizontales Scrollen), auf Desktop darf es sich ausbreiten.
- Jede Variante im Browser öffnen, Hauptwege durchklicken, Konsole auf Fehler und Bilder auf kaputte Links prüfen. Im eingebauten Browser der Claude-App funktionieren keine Service Worker, dafür Playwright nehmen.

### 5. Maik fragen
Nach dem Bauen **nicht weitermachen**. Kurze Übersicht (Datei, Konzept, Besonderheit) und offen fragen, welche von Design und Features am besten gefällt und was er jeweils mag oder stört. Maik mischt gern: "Aufbau von 1, Filter von 2, Farben von 4".

### 6. Neue Version bauen
- Rückmeldung wörtlich in die Anforderungen übernehmen (was gefiel, was nicht, welche Features).
- **Neue Datei** (`v6-…`) aus den gelobten Teilen, nicht eine Variante umbauen. Frühere Versionen bleiben unverändert.
- Kommt eine Stilreferenz dazu, die nächste Version in deren Stil bauen (`v7`).
- Spätere Wünsche in die neueste Version einarbeiten und Gemeinsames im Kern ablegen.

### 7. Dokumentieren
- `Produktanforderungen.md`: Vision, Zielgruppe, Funktionen, Rückmeldungen und Entscheidungen, offene Fragen. Bei jedem Schritt aktualisieren.
- `CLAUDE.md` im Projekt: Aufbau, Regeln, wie man testet.
- Am Ende kurz sagen, was gebaut ist, was getestet wurde und was nicht (z. B. nicht auf echtem Handy).

## Veröffentlichen
Auf Maiks Wunsch ("live schalten", "auf GitHub"). **Zuerst immer in Maiks eigenes Repo**, ein Kunden-Repo erst danach und nur auf ausdrücklichen Wunsch.

1. **Ablageort im Repo:** `flow-media-ai` (`https://github.com/MaikZ91/flow-media-ai`), App unter `coaching/<kunde>/`. GitHub Pages ist dort an, Adresse: `https://maikz91.github.io/flow-media-ai/coaching/<kunde>/`. Mitnehmen: HTML, `daten/`, `bilder/`, `README.md`. Eine `index.html` leitet auf die aktuelle Version weiter. Im Repo-`CLAUDE.md` unter "Aufbau" den Ordner eintragen.
2. **Kundenunterlagen nicht ins Repo** (es ist öffentlich): Produktanforderungen, Angebote, Briefings nur in Google Drive unter `04_Coachings/<Datum>_<Name>_<Thema>/…`. Ins Repo kommt nur ein README. Drive-Spiegel nach der Regel im Repo-`CLAUDE.md` (Markdown als Google Doc, aktualisieren = alte Datei in den Papierkorb und neu anlegen).
3. **Commit-Autor vorher prüfen:** `git config user.email` zeigt oft Maiks Arbeits-E-Mail. Die darf nicht öffentlich erscheinen. Mit `-c user.name="Claude" -c user.email="noreply@anthropic.com"` committen, passend zu den bisherigen Commits im Repo. Vor dem Pushen `git pull --rebase`.
4. **Als Web-App installierbar machen** (auf Wunsch oder wenn das Ziel "App aufs Handy" ist):
   - `manifest.webmanifest` (Name, Start, `display: standalone`, Farben), Symbole 192, 512 und maskable 512 plus `apple-touch-icon.png` 180 in `icons/`.
   - `sw.js` mit Offline-Speicher für App, Daten, Bilder und Schriften. Netz zuerst für Seiten (Updates kommen sofort), Cache zuerst für Bilder. **Nach jeder Änderung `VERSION` hochzählen.**
   - Apple-Meta-Tags und Manifest-Link in der Haupt-HTML, `.nojekyll` im Repo.
   - Knopf "App installieren", der **immer** sichtbar ist (Chrome-Android bietet nicht immer von selbst an) und je Gerät die richtige Anleitung zeigt: Android über ⋮ oder Dialog, iPhone nur Safari über Teilen und "Zum Home-Bildschirm", Instagram, WhatsApp und andere In-App-Browser erst im Browser öffnen lassen.
   - Test mit Playwright: Service Worker aktiv, Dateien im Cache, offline geladen, Knopf auf simuliertem iPhone, Android und In-App-Browser.
5. **Prüfen, dass es live ist:** nach dem Push auf Pages warten (`curl` auf `sw.js` und `manifest.webmanifest`), die Live-Adresse im Browser öffnen, Konsole prüfen.
6. **Kunden-Repo:** Gehört die App dem Kunden, ins Kunden-Repo erst nach ausdrücklicher Ansage und Adresse des Repos. Schreibrechte klären (Einladung muss angenommen sein, sonst 403). Pages im Kunden-Repo schaltet dessen Besitzer ein (Settings, Pages, Branch `main`, `/ (root)`).
7. In der Antwort nennen: Live-Adresse, was im Repo und in Drive liegt, was nicht getestet wurde.
