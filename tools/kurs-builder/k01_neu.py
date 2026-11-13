from szenen import *
# KI Basics, Fassung 13.11.2026 (Maik): jede Lektion nach demselben Muster
#   Problem → Bild (Alltagsvergleich) → Lösung an Lisas Beispiel → Merksatz
# Lisa mit ihrer Physio-Praxis ist ein frei erfundenes Beispiel und begleitet alle 20 Lektionen.
# Je Lektion: scenes (Video), satz ("In einem Satz"), check (Mini-Check: Frage, richtige Antwort, zwei falsche, Position, Erklärung).
B = "../../flow-dna/kurse/ki-basics/bilder/"
LB = "Lisa · Physio-Praxis"
def X(nr, h, say): return T(f"Lektion {nr:02d} · Das Problem", h, say, size="m")
def Q(f, ok, w1, w2, pos, e):
    a = [w1, w2]; a.insert(pos, ok); return {"f": f, "a": a, "r": pos, "e": e}

INTRO_LISA = T("Dein Beispiel im Kurs · frei erfunden", "Das ist *Lisa.*", "Durch den Kurs begleitet dich Lisa. Sie hat eine Physio-Praxis und ist ein erfundenes Beispiel. An ihr siehst du jeden Schritt ganz konkret.", size="m")

NEU = [
 # 01 KI als Mitarbeiter
 {"scenes": [
   X(1, "Frage rein. *Antwort raus.*", "Du stellst eine Frage, bekommst eine Antwort – und machst den Rest selbst. So nutzen die meisten KI. Und verschenken fast alles."),
   VS("Neue Kollegin, erster Tag", ("Ohne Einarbeitung", "„Schreib einen Post.“", ["Sie kennt dich nicht", "Sie rät", "Ergebnis: irgendwas"]), ("Mit Einarbeitung", "Rolle, Kontext, Ziel", ["Sie kennt dein Angebot", "Sie fragt nach", "Ergebnis: passt"]), "Stell dir eine neue Kollegin am ersten Tag vor. Ohne Einarbeitung rät sie. Mit Einarbeitung liefert sie, was du brauchst. Bei KI ist es genauso.", kicker="Stell dir vor"),
   P("Lisa arbeitet ihre KI ein", "Du arbeitest ab jetzt als Texterin\nfür meine Physio-Praxis.\nStell mir erst die Fragen, die eine neue\nMitarbeiterin am ersten Tag stellen würde.", "Lisa gibt ihrer KI eine Rolle und lässt sich erst Fragen stellen – wie von einer neuen Mitarbeiterin.", note=("Du bleibst Chef", "Wichtiges prüfst du selbst."), bar=LB, kicker="Lisas Beispiel"),
   M("Nicht fragen. *Einarbeiten.*", "Merk dir: nicht fragen, sondern einarbeiten. Und du bleibst der Chef."),
  ],
  "satz": "Behandle KI wie einen neuen Mitarbeiter: einarbeiten statt nur fragen – und du bleibst der Chef.",
  "check": Q("Was bringt bei KI am meisten?", "Ihr Rolle und Kontext geben, wie einem neuen Mitarbeiter", "Möglichst kurze Fragen stellen", "Für jede Frage einen neuen Chat öffnen", 1, "Wer die KI einarbeitet, bekommt Ergebnisse, die zu ihm passen.")},
 # 02 Context is King
 {"scenes": [
   X(2, "Klingt wie *jeder andere.*", "Du bittest die KI um einen Post – und er klingt wie von jedem anderen. Das liegt nicht am Prompt. Ihr fehlt Kontext."),
   VS("Beim Friseur", ("Ohne Kontext", "„Einmal schneiden, bitte.“", ["Der Friseur rät", "Irgendeine Frisur"]), ("Mit Kontext", "Foto und zwei Sätze", ["Er weiß, was du willst", "Deine Frisur"]), "Es ist wie beim Friseur: Einmal schneiden bitte ergibt irgendeine Frisur. Mit einem Foto und zwei Sätzen bekommst du deine.", kicker="Stell dir vor"),
   TR("Lisas Über-mich", "Wer:     Lisa, Physiotherapeutin, eigene Praxis\nFür wen: Menschen mit Rückenschmerzen im Büro\nTon:     per Du, locker, keine Fachwörter\nBeispiel: ein Post, der mir gefällt", "Lisa schreibt einmal auf, wer sie ist, für wen sie arbeitet und wie sie klingt. Dazu ein Beispiel, das ihr gefällt.", note=("Einmal reicht", "Aufschreiben, immer wieder nutzen."), bar="ueber-mich.md", kicker="Lisas Beispiel"),
   M("Ohne Kontext: *Durchschnitt.*", "Merk dir: Ohne Kontext bekommst du Durchschnitt. Mit Kontext bekommst du deins."),
  ],
  "satz": "Ohne Kontext rät die KI. Sag ihr einmal, wer du bist, für wen du arbeitest und was dir gefällt.",
  "check": Q("Dein KI-Text klingt austauschbar. Was hilft am meisten?", "Mehr Kontext geben: wer du bist, für wen, ein Beispiel", "Ein anderes KI-Tool ausprobieren", "Die Frage in Großbuchstaben schreiben", 0, "Fast immer fehlt Kontext, nicht der perfekte Prompt.")},
 # 03 Sprechen
 {"scenes": [
   X(3, "Der *perfekte* Prompt?", "Du sitzt vor dem leeren Feld und überlegst, wie du es perfekt formulierst. Lass das. Sprich einfach."),
   VS("Wie eine Sprachnachricht", ("Tippen", "Kurz und knapp", ["Wenig Hintergrund", "Du feilst an Sätzen"]), ("Sprechen", "Einfach erzählen", ["Viel Hintergrund", "Unsortiert ist okay"]), "Denk an eine Sprachnachricht an einen guten Freund. Du erzählst einfach, und er versteht dich. Sortieren ist Aufgabe der KI.", kicker="Stell dir vor"),
   P("Lisa spricht ihre Idee ein", "Ich erzähle dir gleich frei von meiner Idee\nfür einen Rückenkurs. Hör erst zu.\nDann ordne: Ziel, offene Fragen,\nnächste drei Schritte.", "Lisa sagt erst, was mit ihren Gedanken passieren soll. Dann spricht sie zwei Minuten frei über ihren Rückenkurs.", note=("Mikrofon", "In der App oder die Diktierfunktion am Handy."), bar="Lisa · Mikrofon", kicker="Lisas Beispiel"),
   M("Erzählen statt *formulieren.*", "Merk dir: erzählen statt formulieren. Schreiben nur, wenn es genau sein muss – bei Namen, Zahlen und Regeln."),
  ],
  "satz": "Sprich deine Gedanken ein wie eine Sprachnachricht – die KI sortiert. Schreiben nur für Genaues.",
  "check": Q("Wann ist Schreiben besser als Sprechen?", "Bei Namen, Zahlen und festen Regeln", "Bei Ideen und Briefings", "Wenn du viel Hintergrund erzählen willst", 2, "Sprechen liefert Kontext, Schreiben liefert Genauigkeit.")},
 # 04 Briefing
 {"scenes": [
   X(4, "Am Ende machst du es *selbst.*", "Die KI liefert etwas, es passt nicht, und am Ende machst du es doch selbst. Meist fehlte ein klares Briefing."),
   VS("Wie beim Handwerker", ("Dirigieren", "Jeder Handgriff", ["„Halt den Hammer so“", "Du denkst alles vor"]), ("Delegieren", "Das Ergebnis", ["„So soll das Bad aussehen“", "Er schlägt den Weg vor"]), "Einem Handwerker sagst du nicht, wie er den Hammer hält. Du sagst, wie das Bad am Ende aussehen soll.", kicker="Stell dir vor"),
   L("Lisas Briefing", ["Ziel: Angebot für einen Rückenkurs in einer Firma", "Für wen: Büro-Team, zwölf Leute", "Rahmen: eine Seite, per Du", "Fertig heißt: Preis und Termine stehen drin"], "Lisas Briefing hat vier Teile: Ziel, für wen, Rahmen – und woran sie ein gutes Ergebnis erkennt. Danach gibt sie Feedback, statt neu anzufangen.", kicker="Lisas Beispiel"),
   M("Ergebnis vorgeben. *Nicht den Weg.*", "Merk dir: Gib das Ergebnis vor, nicht den Weg."),
  ],
  "satz": "Gib das Ergebnis vor, nicht den Weg: Ziel, für wen, Rahmen, „fertig heißt“ – dann Feedback statt Neustart.",
  "check": Q("Was gehört NICHT in ein gutes Briefing?", "Jeder einzelne Arbeitsschritt", "Das Ziel", "Woran du ein gutes Ergebnis erkennst", 2, "Den Weg schlägt die KI vor. Du gibst das Ergebnis vor.")},
 # 05 Wie funktioniert KI
 {"scenes": [
   X(5, "Woher *weiß* sie das?", "Die KI antwortet auf alles, und es klingt immer sicher. Aber woher weiß sie das eigentlich?"),
   VS("Wie deine Handy-Tastatur", ("Handy", "Nächstes Wort", ["Schlägt ein Wort vor", "Aus deinen Nachrichten gelernt"]), ("Sprachmodell", "Ganze Texte", ["Schreibt Wort für Wort", "Aus sehr viel Text gelernt"]), "Du kennst es vom Handy: Die Tastatur schlägt das nächste Wort vor. Ein Sprachmodell macht dasselbe – nur viel besser und über ganze Texte.", kicker="Stell dir vor"),
   L("Was das für Lisa heißt", ["Stark: Texte, Ideen, Erklären, Struktur", "Schwach: schlägt nicht von selbst nach", "Fachliches zu Übungen prüft Lisa selbst"], "Für Lisa heißt das: Texte und Ideen kann die KI sehr gut. Fachliches zu Übungen prüft Lisa selbst, denn die KI kann auch etwas erfinden.", kicker="Lisas Beispiel"),
   M("Klingt sicher heißt nicht *richtig.*", "Merk dir: Klingt sicher heißt nicht richtig."),
  ],
  "satz": "Ein Sprachmodell sagt das wahrscheinlichste nächste Wort voraus – stark bei Sprache, aber es kann sich irren.",
  "check": Q("Warum kann KI falsche Dinge überzeugend behaupten?", "Sie reiht wahrscheinliche Wörter aneinander und schlägt nicht von selbst nach", "Sie lügt absichtlich", "Sie hat zu wenig Text gelesen", 1, "Sie schreibt, was wahrscheinlich passt – nicht, was geprüft ist.")},
 # 06 Modelle
 {"scenes": [
   X(6, "Welche KI ist *die richtige?*", "Claude, ChatGPT, Gemini – und alle paar Wochen ein neues Modell. Welche KI ist die richtige?"),
   VS("Wie beim Auto", ("Kleinwagen", "Schnelles Modell", ["Für den Weg zum Bäcker", "Kleine, schnelle Aufgaben"]), ("Transporter", "Starkes Modell", ["Für den Umzug", "Große, wichtige Aufgaben"]), "Es ist wie beim Auto: Für den Weg zum Bäcker reicht der Kleinwagen. Für den Umzug nimmst du den Transporter.", kicker="Stell dir vor"),
   C("Lisa entscheidet sich", [("01", "Ein Assistent", "Sie bleibt bei einem"), ("02", "Schnelles Modell", "Für kurze Mails"), ("03", "Starkes Modell", "Für Website und Kurs")], "Lisa nimmt einen Assistenten und bleibt dabei. Das schnelle Modell für kurze Mails, das starke für ihre Website.", kicker="Lisas Beispiel"),
   M("Nimm eins. *Lern es richtig.*", "Merk dir: Nimm eins und lern es richtig. Das bringt mehr als fünf, die du nur ausprobiert hast."),
  ],
  "satz": "Alle großen Assistenten können den Alltag. Nimm einen und lern ihn richtig – schnelles Modell für Kleines, starkes für Wichtiges.",
  "check": Q("Du willst mit KI starten. Was ist am klügsten?", "Einen Assistenten wählen und richtig kennenlernen", "Fünf Tools parallel testen", "Auf das nächste, bessere Modell warten", 0, "Ein Assistent, der dich kennt, bringt mehr als fünf ausprobierte.")},
 # 07 Prompting
 {"scenes": [
   X(7, "Zu lang. Zu *steif.*", "Manchmal schreibst du doch. Und die Antwort ist zu lang, zu steif oder am Thema vorbei."),
   VS("Wie eine Bestellung", ("Ungenau", "„Was zu essen, bitte.“", ["Die Küche rät", "Du bekommst irgendwas"]), ("Genau", "„Pizza, ohne Pilze, zum Mitnehmen.“", ["Klar, was und wie", "Du bekommst deins"]), "Wie bei einer Bestellung: Was zu essen bitte ergibt irgendwas. Pizza ohne Pilze zum Mitnehmen ergibt genau deins.", kicker="Stell dir vor"),
   P("Lisas Anweisung", "Ich bin Physiotherapeutin mit eigener Praxis.\nSchreib eine freundliche Absage-Mail\nfür einen Termin, max. 5 Sätze, per Du.\nKeine Floskeln, zwei Ersatztermine anbieten.", "Lisas Anweisung hat vier Teile: wer sie ist, was sie braucht, für wen und in welchem Ton – und was tabu ist.", note=("Vier Teile", "Rolle · Ergebnis · Für wen · Tabu"), bar=LB, kicker="Lisas Beispiel"),
   M("Nicht neu anfangen. *Nachschärfen.*", "Merk dir: nicht neu anfangen, sondern nachschärfen. Kürzer. Lockerer. Drei Varianten."),
  ],
  "satz": "Eine gute Anweisung hat vier Teile: Rolle, Ergebnis, für wen, Tabu. Danach nachschärfen statt neu anfangen.",
  "check": Q("Das Ergebnis ist fast gut. Was tust du?", "Sagen, was anders soll: kürzer, lockerer, drei Varianten", "Neuen Chat öffnen und von vorn beginnen", "Den Prompt doppelt so lang machen", 1, "Nachschärfen im selben Gespräch ist schneller als jeder Neustart.")},
 # 08 Claude Code oder Codex einrichten (Workshop-Start, mit Originalbildern)
 {"scenes": [
   X(8, "Der Chat baut *nichts.*", "Im Browser-Chat bekommst du Antworten – und kopierst alles selbst heraus. Bauen kann der Chat auf deinem Computer nichts."),
   VS("Berater oder Handwerker?", ("Chat im Browser", "Berater am Telefon", ["Sagt dir, was zu tun ist", "Du machst es selbst"]), ("Desktop-App", "Handwerker im Haus", ["Arbeitet in deinem Ordner", "Legt Dateien an, baut Seiten"]), "Der Chat ist wie ein Berater am Telefon. Der Agent in der Desktop-App ist der Handwerker im Haus: Er macht es.", kicker="Stell dir vor"),
   ST("Claude Code in vier Klicks", ["Herunterladen", "Anmelden", "Oben „Code“", "Ordner wählen"], "Für Claude Code: von claude.com laden, anmelden, oben auf Code klicken und einen Ordner auswählen."),
   SH("Bereit zum *Loslegen.*", B + "claude-code-ordner.jpg", 27, 47, "So sieht Claude Code aus: Oben schreibst du deine Aufgabe, darunter wählst du, woran Claude arbeitet – deinen Ordner.", items=["Aufgabe eingeben", "Ordner wählen"], tag="Ordner", src="Anthropic", bar="Claude Code"),
   SH("Jeder Schritt *sichtbar.*", B + "claude-code-desktop.jpg", 20, 86, "Während Claude arbeitet, siehst du jeden Schritt: was es liest und was es schreibt. Unten links stellst du den Modus ein.", items=["Claude liest Dateien", "Claude schreibt Dateien", "Unten links: der Modus"], tag="Modus", src="Anthropic", bar="Claude Code", zoom=1.6),
   SH("Codex: *New chat.*", B + "codex-seitenleiste.jpg", 40, 16, "Bei Codex öffnest du die ChatGPT-App, wechselst oben auf Codex und startest mit New chat.", items=["ChatGPT-App öffnen", "Oben „Codex“", "New chat"], tag="New chat", src="OpenAI", bar="Codex", ar=1.225, zoom=1.6),
   SH("Ordner auf, *loslegen.*", B + "codex-app.jpg", 42, 67, "Dann öffnest du deinen Ordner und schreibst deine Aufgabe ins Eingabefeld – genau wie bei Claude.", items=["Ordner öffnen", "Aufgabe eingeben"], tag="Aufgabe", src="OpenAI", bar="Codex", zoom=1.5),
   L("Lisas Einstellungen", ["Modell: Opus 5.5 auf Medium", "Modus: Auto – fragt nur bei Riskantem", "Nie: Bypass permissions", "Test: eine erste Datei anlegen lassen"], "Lisa nimmt Claude Code. Als Modell Opus auf Medium, als Modus Auto. Zum Test lässt sie eine erste Datei anlegen.", kicker="Lisas Beispiel"),
   M("Der Chat redet. Der Agent *arbeitet.*", "Merk dir: Der Chat redet. Der Agent arbeitet."),
  ],
  "satz": "Der Chat redet, der Agent arbeitet: Desktop-App installieren, auf „Code“ bzw. „Codex“ wechseln, Ordner wählen.",
  "check": Q("Wo arbeitet Claude als Agent auf deinem Computer?", "In der Desktop-App unter „Code“", "Im Browser auf claude.ai", "In jeder beliebigen Chat-App", 0, "Erst unter „Code“ in der Desktop-App arbeitet Claude in deinem Ordner.")},
 # 09 Projekte
 {"scenes": [
   X(9, "Jedes Mal bei *null.*", "Neuer Chat, und du erklärst wieder alles von vorn: wer du bist, was du anbietest. Jedes Mal bei null."),
   VS("Café-Tisch oder Büro?", ("Einzelner Chat", "Tisch im Café", ["Nichts bleibt liegen", "Alles neu mitbringen"]), ("Projekt", "Eigenes Büro", ["Unterlagen liegen bereit", "Anweisungen gelten immer"]), "Ein Chat ist wie ein Tisch im Café: Du bringst jedes Mal alles neu mit. Ein Projekt ist dein eigenes Büro – alles liegt schon da.", kicker="Stell dir vor"),
   TR("Lisas Projekte", "Marketing\n  ueber-mich.md     ← wer Lisa ist\n  beispiel-post.md  ← ihr Ton\nAngebote\n  preisliste.pdf    ← ihre Leistungen\nWebsite", "Lisa legt drei Projekte an: Marketing, Angebote und Website. In jedem liegen eine kurze Anweisung, ihre Unterlagen und ein Beispiel.", bar="Projekte", kicker="Lisas Beispiel"),
   M("Ein Chat vergisst. Ein Projekt *behält.*", "Merk dir: Ein Chat vergisst. Ein Projekt behält."),
  ],
  "satz": "Ein Chat vergisst, ein Projekt behält: ein Projekt pro Arbeitsbereich, mit Anweisung, Unterlagen und Beispiel.",
  "check": Q("Was gehört in ein Projekt?", "Anweisung, Unterlagen und ein Beispiel zu einem Arbeitsbereich", "Alle Themen auf einmal", "Deine Passwörter", 2, "Ein Projekt pro Arbeitsbereich – und Passwörter gehören nie in die KI.")},
 # 10 CLAUDE.md
 {"scenes": [
   X(10, "Schon wieder *erklären?*", "Du sagst deiner KI zum zehnten Mal, wie du klingst und was dir wichtig ist. Das geht einfacher."),
   VS("Das Handbuch für Neue", ("Ohne Handbuch", "Alles mündlich", ["Jeden Tag neu erklären", "Jedes Mal etwas anders"]), ("Mit Handbuch", "Einmal aufgeschrieben", ["Wird zuerst gelesen", "Gilt für jede Aufgabe"]), "In vielen Firmen bekommen Neue ein Handbuch: So arbeiten wir. Deine KI kann das auch bekommen.", kicker="Stell dir vor"),
   TR("Lisas Handbuch", "# Wer ich bin\nLisa, Physio-Praxis, Rücken im Büroalltag\n# Ton\nper Du, locker, kurze Sätze\n# Regeln\nnichts erfinden, keine Heilversprechen", "Lisas Handbuch heißt CLAUDE.md. Claude Code liest die Datei bei jedem Start: wer sie ist, wie sie klingt, welche Regeln gelten.", note=("Ohne Claude Code", "Derselbe Text als Projektanweisung."), bar="CLAUDE.md", kicker="Lisas Beispiel"),
   M("Einmal schreiben. *Nie wieder erklären.*", "Merk dir: einmal schreiben, nie wieder erklären."),
  ],
  "satz": "Die CLAUDE.md ist das Handbuch für deine KI: einmal schreiben lassen, nie wieder erklären.",
  "check": Q("Was ist die CLAUDE.md?", "Eine Textdatei mit deinem Handbuch, die Claude Code bei jedem Start liest", "Ein Programm, das du installieren musst", "Ein gespeicherter Chatverlauf", 1, "Eine einfache Textdatei – dein dauerhafter Kontext.")},
 # 11 Rules
 {"scenes": [
   X(11, "Gestern Du. Heute *Sie.*", "Gestern hast du gesagt: bitte per Du. Heute, im neuen Chat, siezt die KI deine Kunden wieder."),
   VS("Zuruf oder Hausordnung?", ("Im Chat gesagt", "Zuruf", ["Gilt nur in diesem Chat", "Morgen vergessen"]), ("Als Regel abgelegt", "Hausordnung", ["Hängt an der Wand", "Gilt immer"]), "Was du im Chat sagst, ist ein Zuruf. Er gilt nur dort. Eine Regel ist wie die Hausordnung an der Wand: Sie gilt immer.", kicker="Stell dir vor"),
   L("Lisas Regeln", ["Immer per Du, kurze Sätze", "Keine Heilversprechen", "Preise nur aus meiner Preisliste", "Vor dem Versenden immer fragen"], "Lisa legt vier kurze Regeln fest. Und immer, wenn sie etwas zum zweiten Mal korrigiert, wird daraus eine neue Regel.", kicker="Lisas Beispiel"),
   M("Zweimal korrigiert? *Regel.*", "Merk dir: Zweimal korrigiert? Dann wird es eine Regel."),
  ],
  "satz": "Im Chat gesagt gilt einmal, als Regel abgelegt gilt immer – was du zweimal korrigierst, wird zur Regel.",
  "check": Q("Wann machst du aus einer Korrektur eine feste Regel?", "Wenn du dasselbe zum zweiten Mal korrigierst", "Nie, die KI merkt es sich von selbst", "Erst nach zehn Fehlern", 0, "Zweimal dieselbe Korrektur heißt: Das gehört dauerhaft abgelegt.")},
 # 12 Dateien
 {"scenes": [
   X(12, "Dreißig Seiten. *Keine Zeit.*", "Ein Vertrag mit dreißig Seiten, zwei Angebote zum Vergleichen – und du hast keine Zeit, alles zu lesen."),
   C("Eine Assistentin, die alles liest", [("01", "Zusammenfassen", "30 Seiten in 5 Punkten"), ("02", "Fragen", "„Was steht zu den Kosten?“"), ("03", "Vergleichen", "Zwei Angebote nebeneinander"), ("04", "Weiterverarbeiten", "Notizen werden zum Angebot")], "Stell dir eine Assistentin vor, die jedes Dokument in Sekunden liest. Sie fasst zusammen, beantwortet Fragen, vergleicht und macht aus Notizen ein Angebot.", kicker="Stell dir vor"),
   TR("Lisas Unterlagen", "ueber-mich.md       ← wer sie ist\npreisliste.pdf      ← Leistungen und Preise\nbeispiel-posts.md   ← ihr Ton\nhaeufige-fragen.md  ← ihre Antworten", "Lisa legt ins Projekt, was sie oft braucht: Preisliste, Beispiele, häufige Fragen. Und sie hält die Dateien aktuell.", note=("Aktuell halten", "Alte Preisliste, alte Antworten."), bar="Projektwissen", kicker="Lisas Beispiel"),
   M("Die KI kennt nur den *Stand der Datei.*", "Merk dir: Die KI kennt nur den Stand der Datei."),
  ],
  "satz": "Die KI liest deine Dokumente in Sekunden – aber sie kennt nur den Stand der Datei.",
  "check": Q("Deine Preisliste im Projekt ist vom letzten Jahr. Was passiert?", "Die KI antwortet mit den alten Preisen", "Die KI aktualisiert die Preise von selbst", "Die KI verweigert die Antwort", 1, "Sie weiß nur, was in der Datei steht.")},
 # 13 Skills
 {"scenes": [
   X(13, "Letzte Woche *top.* Heute naja.", "Letzte Woche hat die KI ein richtig gutes Angebot geschrieben. Heute ist es deutlich schwächer. Warum?"),
   VS("Wie ein Rezept", ("Ohne Rezept", "Jedes Mal anders", ["Mal gut, mal nicht", "Du erklärst alles neu"]), ("Mit Rezept", "Jedes Mal gleich gut", ["Zutaten und Schritte stehen fest", "Auch andere können es kochen"]), "Ein Skill ist wie ein Rezept: Wer es hat, kocht das Gericht jedes Mal gleich gut.", kicker="Stell dir vor"),
   ST("Lisas erster Skill", ["Angebot einmal sauber schreiben", "„Mach daraus einen Skill“", "Im neuen Chat testen", "Regel ergänzen"], "Lisa schreibt ein Angebot einmal sauber mit der KI. Dann sagt sie: Mach daraus einen Skill. Sie testet ihn und ergänzt, was fehlt.", kicker="Lisas Beispiel"),
   M("Erst machen. Dann *festhalten.*", "Merk dir: erst machen, dann festhalten."),
  ],
  "satz": "Ein Skill ist ein Rezept für eine Aufgabe: einmal sauber lösen, dann festhalten – und es klappt jedes Mal.",
  "check": Q("Was unterscheidet einen Skill von einem Prompt?", "Ein Prompt gilt einmal, ein Skill bleibt und liefert gleichbleibend", "Ein Skill ist nur ein längerer Prompt", "Skills gibt es nur für Programmierer", 2, "Der Skill hält den Weg fest – wie ein Rezept.")},
 # 14 MCPs
 {"scenes": [
   X(14, "Kopieren. Einfügen. *Kopieren.*", "Du kopierst die Mail in den Chat, lädst die Datei hoch, kopierst die Antwort zurück. Die KI kommt selbst nirgends hin."),
   VS("Steckdose und Stecker", ("MCP", "Die Steckdose", ["Ein Standard für alle", "Jedes Gerät passt"]), ("Konnektor", "Der Stecker", ["Verbindet ein Programm", "Per Anmeldung eingerichtet"]), "MCP ist wie die Steckdose: ein einheitlicher Standard. Der Konnektor ist der Stecker zu einem deiner Programme.", kicker="Stell dir vor"),
   L("Lisa verbindet", ["Kalender: darf lesen", "Ablage: darf lesen", "Mails: Entwurf ja, Senden nur nach Rückfrage"], "Lisa verbindet Kalender und Ablage. Lesen darf die KI. Bei Mails schreibt sie nur Entwürfe – gesendet wird erst nach Lisas Okay.", kicker="Lisas Beispiel"),
   M("So wenig Zugriff *wie nötig.*", "Merk dir: so wenig Zugriff wie nötig."),
  ],
  "satz": "Mit Konnektoren arbeitet die KI direkt in deinen Programmen – gib so wenig Zugriff wie nötig.",
  "check": Q("Welche Berechtigung ist am heikelsten?", "Mails senden und Dateien löschen", "Dateien lesen", "Den Kalender ansehen", 2, "Lesen ist harmloser als Schreiben. Bei Senden und Löschen fragt die KI erst.")},
 # 15 Agenten
 {"scenes": [
   X(15, "Und den Rest *machst du.*", "Der Chatbot antwortet. Und den Rest machst du: kopieren, einfügen, prüfen, den nächsten Schritt anstoßen."),
   VS("Auskunft oder Reisebüro?", ("Chatbot", "Auskunft", ["Sagt, wann der Zug fährt", "Buchen musst du selbst"]), ("Agent", "Reisebüro", ["Bucht Zug, Hotel, Mietwagen", "Meldet sich, wenn alles steht"]), "Die Auskunft sagt dir, wann der Zug fährt. Das Reisebüro bucht alles und meldet sich, wenn es steht. So unterscheiden sich Chatbot und Agent.", kicker="Stell dir vor"),
   ST("Lisas Agent baut die Kursseite", ["Ziel verstehen", "Planen", "Bauen", "Prüfen"], "Lisa gibt ein Ziel vor: eine Seite für ihren Rückenkurs. Der Agent plant, baut und prüft. Subagents helfen dabei wie ein kleines Team.", kicker="Lisas Beispiel"),
   M("Chatbot antwortet. Agent *handelt.*", "Merk dir: Ein Chatbot antwortet. Ein Agent handelt."),
  ],
  "satz": "Ein Chatbot antwortet, ein Agent plant und handelt – je selbstständiger er arbeitet, desto klarer dein Briefing.",
  "check": Q("Was macht einen Agenten aus?", "Er verfolgt ein Ziel selbstständig in mehreren Schritten", "Er antwortet schneller als ein Chatbot", "Er braucht kein Briefing", 1, "Ziel verstehen, planen, ausführen, prüfen – in einer Schleife.")},
 # 16 Tools
 {"scenes": [
   X(16, "Sie kann nur *schreiben.*", "Ohne Werkzeuge kann eine KI nur schreiben. Sie sucht nichts nach, legt nichts an, verschickt nichts."),
   C("Tools sind ihre Hände", [("01", "Websuche", "Aktuelles mit Quellen"), ("02", "Dateien", "Erstellen und bearbeiten"), ("03", "Daten", "Tabellen auswerten"), ("04", "Aktionen", "In deinen Programmen")], "Stell dir Tools als Hände vor. Mit ihnen sucht die KI im Web, erstellt Dateien, wertet Tabellen aus und arbeitet in deinen Programmen.", kicker="Stell dir vor"),
   VS("Lisas Regel", ("Unkritisch", "Darf die KI allein", ["Lesen", "Suchen", "Entwerfen"]), ("Kritisch", "Nur mit Lisas Okay", ["Senden", "Löschen", "Bezahlen"]), "Lisa trennt: Lesen, Suchen und Entwerfen darf die KI allein. Senden, Löschen und Bezahlen nur mit ihrem Okay.", kicker="Lisas Beispiel"),
   M("Du gibst *frei.*", "Merk dir: Du gibst frei."),
  ],
  "satz": "Tools sind die Hände der KI: Lesen und Entwerfen darf sie allein, Senden und Löschen gibst du frei.",
  "check": Q("Was sollte die KI nie ohne deine Freigabe tun?", "Eine Mail an Kunden senden", "Einen Entwurf schreiben", "Im Web recherchieren", 0, "Senden, Veröffentlichen, Löschen und Bezahlen gibst du selbst frei.")},
 # 17 Tokens
 {"scenes": [
   X(17, "Plötzlich *vergisst* sie.", "Nach zwei Stunden im selben Chat vergisst die KI, was ihr am Anfang besprochen habt. Die Antworten werden ungenau."),
   VS("Wie ein Schreibtisch", ("Langer Chat", "Voller Tisch", ["Altes rutscht herunter", "Antworten werden ungenau"]), ("Neuer Chat", "Freier Tisch", ["Nur was gerade zählt", "Klare Antworten"]), "Ihr Arbeitsgedächtnis ist wie ein Schreibtisch. Irgendwann ist er voll, und was zuerst darauf lag, rutscht hinten herunter.", kicker="Stell dir vor"),
   L("So macht es Lisa", ["Neues Thema, neuer Chat", "Stand zusammenfassen lassen", "Dauerhaftes liegt im Projekt", "Kleines an das schnelle Modell"], "Lisa lässt sich den Stand zusammenfassen und startet frisch. Was dauerhaft gilt, liegt in ihrem Projekt.", kicker="Lisas Beispiel"),
   M("Neues Thema. *Neuer Chat.*", "Merk dir: neues Thema, neuer Chat."),
  ],
  "satz": "Das Context Window ist der Schreibtisch der KI: Wird er voll, vergisst sie. Neues Thema, neuer Chat.",
  "check": Q("Der Chat ist lang und die KI wird ungenau. Was tust du?", "Stand zusammenfassen lassen und im neuen Chat weitermachen", "Alles noch einmal in denselben Chat schreiben", "Die Frage in Großbuchstaben wiederholen", 1, "Ein frischer Chat mit Zusammenfassung räumt den Schreibtisch auf.")},
 # 18 Multimodal
 {"scenes": [
   X(18, "Wie soll ich das *beschreiben?*", "Eine Fehlermeldung, ein Zettel voller Notizen, ein Design, das dir gefällt. Wie beschreibst du das in Worten? Gar nicht."),
   C("Zeig es einfach", [("01", "Screenshot", "„Was bedeutet das?“"), ("02", "Foto", "Notizen abtippen lassen"), ("03", "Design", "„Bau es in diesem Stil“"), ("04", "Beleg", "Auslesen und einordnen")], "Zeig es einfach – wie einem Kollegen, dem du den Bildschirm hinhältst: ein Screenshot, ein Foto, ein Design, ein Beleg.", kicker="Stell dir vor"),
   L("Lisa zeigt statt zu tippen", ["Foto vom Whiteboard wird zum Kursplan", "Screenshot einer Fehlermeldung wird erklärt", "KI-Bilder kennzeichnet sie"], "Lisa fotografiert ihr Whiteboard, und die KI macht daraus einen Kursplan. KI-Bilder, die echt wirken könnten, kennzeichnet sie.", kicker="Lisas Beispiel"),
   M("Zeigen statt *beschreiben.*", "Merk dir: zeigen statt beschreiben."),
  ],
  "satz": "KI versteht auch Bilder, Ton und Video: zeigen statt beschreiben – und KI-Inhalte kennzeichnen.",
  "check": Q("Du verstehst eine Fehlermeldung nicht. Der schnellste Weg?", "Screenshot machen und der KI zeigen", "Sie Wort für Wort abtippen", "Sie wegklicken und hoffen", 0, "Ein Screenshot erklärt oft mehr als eine lange Beschreibung.")},
 # 19 Halluzinationen
 {"scenes": [
   X(19, "Klingt sicher. Ist *falsch.*", "Die KI nennt eine Zahl, eine Quelle, einen Namen – völlig überzeugend. Und es stimmt nicht."),
   VS("Der belesene Praktikant", ("Seine Stärke", "Schnell und belesen", ["Entwürfe in Sekunden", "Kennt fast jedes Thema"]), ("Seine Schwäche", "Gibt Lücken nicht zu", ["Erfindet lieber etwas", "Darum liest du gegen"]), "Behandle das Ergebnis wie die Arbeit eines sehr schnellen, sehr belesenen Praktikanten. Du liest es, bevor es an den Kunden geht.", kicker="Stell dir vor"),
   ST("Lisas Prüf-Routine", ["Quelle zeigen lassen", "Stichprobe prüfen", "„Wobei bist du unsicher?“", "Selbst entscheiden"], "Lisa prüft Fachliches in vier Schritten: Quelle zeigen lassen, Stichprobe prüfen, nach Unsicherheiten fragen – und selbst entscheiden.", kicker="Lisas Beispiel"),
   M("Die KI bereitet vor. Du *entscheidest.*", "Merk dir: Die KI bereitet vor. Du entscheidest."),
  ],
  "satz": "KI kann überzeugend falschliegen: Quelle zeigen lassen, Stichprobe prüfen – sie bereitet vor, du entscheidest.",
  "check": Q("Wo passieren KI-Fehler besonders oft?", "Bei Zahlen, Quellen, Namen, Recht und Gesundheit", "Bei Begrüßungen", "Bei kurzen Texten", 2, "Genau dort prüfst du immer selbst nach.")},
 # 20 Datenschutz
 {"scenes": [
   X(20, "Darf ich das *eingeben?*", "Du willst der KI von einer Kundin erzählen und zögerst: Darf ich das überhaupt eingeben?"),
   L("Drei Dinge bleiben draußen", ["Passwörter und Zugangsdaten", "Kundendaten mit Namen", "Vertrauliches aus dem Job"], "Stell dir vor, du gibst Unterlagen an ein externes Büro. Manches gibst du nie heraus: Passwörter, Kundendaten mit Namen und Vertrauliches aus dem Job.", kicker="Stell dir vor"),
   VS("Lisa macht Daten neutral", ("Vorher", "Mit Namen", ["„Frau Schneider, Knie-OP im März“"]), ("Nachher", "Neutral", ["„Eine Kundin nach Knie-OP“"]), "Lisa ersetzt Namen durch Platzhalter. Aus Frau Schneider wird: eine Kundin nach Knie-OP. Bei Kundendaten klärt sie den Datenschutz fachlich.", kicker="Lisas Beispiel"),
   M("Namen raus. *Platzhalter rein.*", "Merk dir: Namen raus, Platzhalter rein."),
  ],
  "satz": "Keine Passwörter, keine Kundendaten mit Namen, nichts Vertrauliches – Namen raus, Platzhalter rein.",
  "check": Q("Was gibst du nie in einen KI-Chat ein?", "Passwörter und Kundendaten mit Namen", "Eine Frage zu deinem Angebot", "Einen eigenen Textentwurf", 1, "Mach Daten neutral, bevor du sie einfügst.")},
]

# Wörterbuch für antippbare Begriffe in der Lektion (wie im Buch).
GLOSSAR = {
 "Agent": "KI, die ein Ziel selbstständig in mehreren Schritten verfolgt und dabei Werkzeuge nutzt.",
 "Briefing": "Einweisung in eine Aufgabe: Ziel, Kontext, Rahmen und woran man ein gutes Ergebnis erkennt.",
 "CLAUDE.md": "Textdatei mit dem „Handbuch“ für die KI. Claude Code liest sie bei jedem Start.",
 "Context Window": "Arbeitsgedächtnis der KI: alles, was sie in einem Gespräch gleichzeitig im Blick hat.",
 "Desktop-App": "Programm auf deinem Computer. Darin arbeiten Claude Code und Codex direkt mit deinen Dateien.",
 "Halluzination": "Erfundene Aussage, die überzeugend klingt.",
 "Konnektor": "Fertige Verbindung zwischen der KI und einem deiner Programme.",
 "Kontext": "Alles, was die KI über dich und die Aufgabe weiß.",
 "LLM": "Large Language Model, auf Deutsch Sprachmodell. Die Technik hinter Claude, ChatGPT und Gemini.",
 "Sprachmodell": "Die Technik hinter Claude, ChatGPT und Gemini: sagt das wahrscheinlichste nächste Wort voraus.",
 "MCP": "Model Context Protocol. Offener Standard, über den KI mit Programmen spricht.",
 "Multimodal": "Die KI arbeitet nicht nur mit Text, sondern auch mit Bild, Ton und Video.",
 "Projekt": "Arbeitsbereich mit dauerhaft hinterlegten Anweisungen und Unterlagen.",
 "Prompt": "Das, was du der KI eingibst.",
 "Rules": "Regeln, die dauerhaft gelten, nicht nur im aktuellen Chat.",
 "Skill": "Anleitung für eine bestimmte Aufgabe, die die KI bei Bedarf selbst lädt.",
 "Subagent": "Helfer, an den ein Agent eine Teilaufgabe abgibt.",
 "Token": "Wortstück. Die Einheit, in der KI Text zählt.",
 "Tool": "Werkzeug, mit dem die KI etwas tun kann, zum Beispiel im Web suchen oder Dateien erstellen.",
 "Voice Prompting": "Der KI etwas einsprechen statt zu tippen.",
}
