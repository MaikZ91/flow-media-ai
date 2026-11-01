# Adil's Cocktail App

Web-App (reines HTML/CSS/JS, kein Build) mit Cocktailrezepten und freihändigem Schritt-für-Schritt-Zubereitungsmodus. Ziel: GitHub Pages, installierbar als PWA auf iPhone und Android; später Smart Glasses. Siehe `Produktanforderungen.md`.

## Aufbau
- `v1-…` bis `v5-….html`: fünf Design-Varianten, jede eigenständig. `v6-geschmack.html` kombiniert die Rückmeldungen (Geschmacks-Finder, Tinder-Zufallsmodus, Bestellungen mit Playlist). **`v7-amber.html` ist der aktuelle Favorit zum Weiterentwickeln**: dieselben Funktionen im Amber-Stil von `v5-bernstein.html` (Stil-Referenz).
- `daten/rezepte.js`: alle Rezepte (`window.REZEPTE`, `window.KATEGORIEN`), inklusive Foto-Credits. Wird für `file://` als Skript geladen, nicht per `fetch`.
- `daten/kern.js` und `daten/kern.css`: gemeinsame Helfer (`window.Bar`) und der Zubereitungsmodus `Bar.kochen(rezept, portionen)`. Design über CSS-Variablen (`--bk-*`) pro Version anpassen.
- `bilder/<id>.jpg`: Fotos, Dateiname = Rezept-ID.
- `daten/iba-roh.json`: unveränderte Quelldaten (IBA, CC BY 4.0).

## Regeln
- Sprache der Oberfläche und der Rezepte: Deutsch.
- Neue Rezepte in `rezepte.js` im bestehenden Format ergänzen: `id`, `kategorie`, `glas`, `technik`, `zutaten` (`m`, `e`, `n`), `schritte` (`t`, `z` = Zutaten-Indizes), `garnitur`, `quelle`, `credit`.
- Für den Geschmacks-Finder braucht jedes Rezept außerdem `profil` (Intensität 0 bis 3 je Richtung: `suess`, `fruchtig`, `sauer`, `cremig`, `bitter`, `herb`, `wuerzig`, `salzig`, `rauchig`, `kaffee`), `basis` (Spirituosen mit mindestens 15 % Anteil am reinen Alkohol: `rum`, `gin`, `wodka`, `tequila`, `whiskey`, `cachaca`, `likoer`, `bitter`, `wermut`, `schaumwein`; leer bei alkoholfreien Drinks) und `stil` (Kategorie, plus `exotisch` für Tiki und lateinamerikanische Drinks). Die Auswertung steht in `Bar.passt` und `Bar.empfehle` (`kern.js`).
- Alkohol: Jede Zutat hat `v` (Vol.-%), nicht-ml-Zutaten zusätzlich `ml`. `Bar.alkohol(r)` schätzt Vol.-% und Gramm, `Bar.FAHRHINWEIS` ist der Pflichttext dazu. `Bar.alkoholStufe(r)` liefert `frei`, `niedrig`, `mittel` oder `hoch` für den Filter `wahl.alkohol`. Alkoholfreie Drinks haben `kategorie: "alkoholfrei"`, `staerke: 0` und Zutaten mit `v: 0`. Alkoholangaben nie als Aussage zur Fahrtauglichkeit darstellen, keine Promille-Rechner oder „darf ich noch fahren“-Anzeigen bauen.
- Bestellungen liegen in `Bar.queue` (`add`, `get`, `set`, `gesamt`, `abspielen`) unter dem Speicherschlüssel `queue`, Dauer über `Bar.dauer(rezept, n)`. `Bar.queue.abspielen(onChange)` startet die Playlist, `Bar.kochen(r, n, fertig, liste)` bekommt dafür den vierten Parameter.
- Auto-Weiter im Zubereitungsmodus ist standardmäßig an (6 Sekunden), Einstellungen liegen in `Bar.store` unter `auto` und `sek`.
- Fotos nur mit freier Lizenz (Wikimedia Commons), Autor und Lizenz immer mit speichern und anzeigen.
- Selbst erfundene Rezepte mit `quelle: "Hausrezept"` und `hinweis` kennzeichnen.
- Nutzereingaben und Rezepttexte immer mit `Bar.esc()` ausgeben.
- `localStorage` nur über `Bar.store` (abgesichert).

## Lokal testen
Dateien lassen sich per Doppelklick öffnen. Mit Server: `python -m http.server 8765` im Projektordner, dann `http://127.0.0.1:8765/v5-bernstein.html`. Schriften kommen von Google Fonts und brauchen beim ersten Laden Internet.

## Hinweise
- Der Ordner `Content/` ist vom Benutzer angelegt (Media, Rezepte), noch leer und nicht eingebunden.
- Das Referenzfoto für Version 5 ist nur Stilvorlage. Keine Namen, Logos oder Marken des Vorbilds übernehmen.
