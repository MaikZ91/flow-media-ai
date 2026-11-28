# Oberstes Marketing-Ziel: Reel → Community-Seite → WhatsApp-Community

Festgelegt von Maik am 28.11.2026. Gilt, bis Maik es ändert.

## Das Ziel

Ein beworbenes Reel finden, das genau die Zielgruppe anspricht (Gründer und Selbstständige, siehe CLAUDE.md Abschnitt 3), ihr Problem trifft und Maiks Positionierung zeigt. Wer es sieht, geht auf die Community-Seite (https://maikz91.github.io/flow-media-ai/marketing/community/) und von dort in die WhatsApp-Community.

**Messgröße:** echte Beitritte, also Join-Klicks auf der Community-Seite (PostHog-Event `community_join_click`, ohne Bots). Follower, Views und Seitenaufrufe sind nur Zwischenwerte.

Das Problem wird Schritt für Schritt gelöst: Reel testen → messen → das Bessere behalten → nächste Variante.

## Die zwei Wege (Stand 28.11.2026)

| Weg | Rolle | Warum |
|---|---|---|
| **Reel → Community-Seite → WhatsApp** | **Hauptweg, hier liegt der Fokus** | bringt die richtigen Leute direkt in die Community, ohne Handarbeit |
| Follower-Anzeige → Follower per DM in die Community einladen | Übergang, zweitrangig | mehr Follower geben Vertrauen auf dem Profil (144 → Richtung 1000), bringen aber noch keine Kunden. Maiks Eindruck: oft die falschen Leute (z. B. Profile mit 16 Followern, keine Gründer) |

DMs schreibt Maik selbst, nichts wird automatisch versendet.

## Was bisher bekannt ist

- **Hook:** Das Original R058 („Mitten in der Wüste …“) hat organisch die niedrigste Überspringrate aller Reels (44,7 % bei 893 Reichweite). Die anderen Reels liegen meist bei 65–78 %.
- **Tipp-Aufbau hält länger:** R058-v2 mit Tipp „Fang mit einer Aufgabe an“ hielt in der Anzeige mehr Leute bis 25 % (39 % statt 34 %) und brachte 14 Follower für je 1,44 $.
- **Community-Reel ohne Tipp → Landingpage:** etwa 29 echte Besucher, 0 Beitritte. Danach kam die Stammtisch-Box auf die Seite.
- **Die ersten echten Beitritte** kamen über die Bild-Anzeige B (2 Personen).
- Link-Klick-Anzeigen ziehen viele Klicker mit wenig Interesse an. Darum ist die Landingpage-Kampagne auf Seitenaufrufe optimiert.

## Laufender Test

- Ab 28.11.2026: „Community-Reel mit Tipp · Landingpage“ (`utm_content=reel_tipp`) ersetzt das Community-Reel ohne Tipp (`reel_landingpage`), 30 $/Tag.
- Auswertung nach 2–3 Tagen: Kosten pro Seitenaufruf, Beitritte pro 100 Besucher, wer genau beitritt.

## Stand 28.11.2026 (Abend)

- Follower-Anzeigen sind aus. Es läuft **nur noch eine Anzeige**: R061 (Drehbuch Nr. 2, Variante B mit KI-Hologramm, Stimme Orion) → Community-Seite, `utm_content=reel_r061`, 30 $/Tag (Ad 52567934180765).
- Community-Seite im Look des Reels umgebaut (Wüste/KI-Hologramm-Szene als Hintergrund bzw. Reel rechts, „Gründer & Selbstständige · LOST MIT KI?“, PostHog `layout=reel`).
- R061 organisch gepostet: https://www.instagram.com/reel/DgSLONHg5CM/

## Meta-Messung (Stand 28.11.2026)

- Pixel/Datensatz im Business-Portfolio „Flow Media AI“: **„Flow“, ID 1012935401238191** (der alte Pixel 1135098089124774 hängt nur am Werbekonto und wird nicht mehr genutzt).
- Beitritte über eine Anzeige (fbclid im Link) meldet die Supabase-Funktion `flow-meta-capi` server-seitig als **Lead** (ohne Cookie; Datenschutz Abschnitt 6b). Token: Systemnutzer „Flow“, Supabase-Secret. Test am 28.11.: events_received 1.
- Mit Pixel-Einwilligung (Fußzeile „Ja“) meldet stattdessen der Browser-Pixel.
- Datensatz „Flow“ ist seit 28.11. mit dem Werbekonto 518708974888646 verbunden. Seit 28.11. läuft die neue Kampagne „Community · Leads (Beitritte) · R061“ (52567944032965, Ziel Leads, Optimierung auf das Lead-Event des Datensatzes Flow, 30 $/Tag, gleiche Zielgruppe und gleiches R061-Reel); die alte Landingpage-Aufrufe-Kampagne (52567837237365) ist pausiert. Anfangs wenige Leads → Meta lernt langsam; nach 5–7 Tagen auswerten.

Tägliches Tracking (Follower, Seite, Anzeige, Richtwerte fürs Eingreifen): `ads-tracking.md`.

## Nächste Schritte

Drehbuch mit vier Varianten (5–7 s) und Testplan: `drehbuch-2-community-reel.md`.

1. Tipp-Version auswerten.
2. Neues Reel nach dem stärksten Muster bauen: Hook wie im Original R058 (starkes Bild + Frage, bei der die Zielgruppe nickt), dann ein echtes Problem aus den fünf Säulen (`problem-zu-loesung.md`) und als Lösung die Community, mit klarem Grund zum Beitreten (kostenlos, Stammtisch, Austausch mit Gründern).
3. Pro Runde immer nur eine Sache ändern (Hook, Mitte oder Schluss), damit klar ist, was wirkt.
4. Prüfen, ob die Community-Seite selbst bremst: Besucher ohne Beitritt, Scrolltiefe, Klicks auf den Button.
