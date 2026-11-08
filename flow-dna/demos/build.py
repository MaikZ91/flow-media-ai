# Baut die Demo-Konzeptseiten für die Flow-DNA-Galerie (frei erfundene Demo-Betriebe, CC0-Fotos).
# Aufbau wie die Lead-Agent-Seiten: Vollbild-Foto-Hero zuerst (Header transparent darüber), Icon-Leiste, Story mit Bild-Badge,
# Leistungen mit Bildern, Branchen-Feature im Farbband, Team-Avatare mit Telefon, Galerie, Stimmen-Band, Zeiten + Kontakt,
# CTA-Band, dunkler Footer, Avatar-Kontakt-Assistent, Mobile-CTA.  Aufruf: python3 build.py
import json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
CRED = json.load(open(os.path.join(HERE, "credits.json"), encoding="utf-8"))
E = html.escape

I = {  # Linien-Icons (24px, currentColor)
 "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 "check": '<path d="M5 12l4 4L19 6"/>',
 "fire": '<path d="M12 3s5 4.5 5 9a5 5 0 0 1-10 0c0-2 1-3.5 2-4.5 0 2 1 3 2 3 0-3 1-5.5 1-7.5z"/>',
 "leaf": '<path d="M5 19c0-8 6-14 15-14 0 9-6 15-14 15"/><path d="M5 19l7-7"/>',
 "wheat": '<path d="M12 21V8"/><path d="M12 8c-2-1-3-3-3-5 2 0 3 1.5 3 3 0-1.5 1-3 3-3 0 2-1 4-3 5z"/><path d="M12 13c-2-1-4-1-5-3 2-.5 4 0 5 1.5M12 13c2-1 4-1 5-3-2-.5-4 0-5 1.5"/>',
 "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
 "hand": '<path d="M7 11V6a1.5 1.5 0 0 1 3 0v5M10 10V4.5a1.5 1.5 0 0 1 3 0V10M13 10V5.5a1.5 1.5 0 0 1 3 0V12M16 9.5a1.5 1.5 0 0 1 3 0V14a7 7 0 0 1-7 7h-1a6 6 0 0 1-5-3l-2.5-4a1.5 1.5 0 0 1 2.5-1.6L7 14"/>',
 "access": '<circle cx="12" cy="5" r="2"/><path d="M5 9h14M12 9v12M8 21l4-6 4 6"/>',
 "scissors": '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.5 7.5L20 18M8.5 16.5L20 6"/>',
 "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5L18 18M6 18l2.5-2.5M15.5 8.5L18 6"/>',
 "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
 "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
}
def ic(n, s=22): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[n]}</svg>'

DEMOS = {
 "baeckerei": dict(
  name="Bäckerei Musterbrot", ort="Musterstadt", branche="Bäckerei & Café", art="Handwerksbäckerei",
  fonts="Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Manrope:wght@400;500;600;700&family=Pinyon+Script", serif="Cormorant Garamond", sans="Manrope", script="Pinyon Script",
  c=dict(bg="#FBF6EE", alt="#F3E9DA", ink="#2B1D14", mute="#7A6656", acc="#B5502E", gold="#E9B872", card="#FFFFFF", dark="#2A1A10", band="#7A2E1A"),
  greet="Willkommen in der Backstube", h1="Brot, das nach <em>Zeit</em> schmeckt.",
  lead="Natursauerteig, 24 Stunden Ruhe, jeden Morgen frisch aus dem Steinofen. Vorbestellen und warm abholen.",
  cta="Brot vorbestellen", cta2="Brotkarte ansehen",
  trust=[("pin", "Musterstraße 1 · Musterstadt"), ("clock", "Mo–Sa ab 6:30 Uhr"), ("check", "Natursauerteig")],
  bar=[("fire", "Steinofen", "jeden Morgen frisch"), ("wheat", "Regionales Mehl", "aus der Mühle nebenan"), ("leaf", "Natursauerteig", "24 Std. Teigruhe"), ("cal", "Vorbestellen", "online, warm abholen")],
  story=("Unsere Backstube", "Handwerk, das man <em>schmeckt</em>.", "Bei uns bekommt jeder Teig die Zeit, die er braucht. Wir backen mit Natursauerteig, regionalem Mehl und ohne Fertigmischungen – so wie es in der Familie seit Generationen üblich ist.", "g1", ("Seit", "1962", "in Familienhand")),
  leistungen=[("g2", "wheat", "Brote", "Roggen, Dinkel, Vollkorn – lange geführt, kräftig gebacken."), ("g3", "spark", "Feingebäck", "Croissants und Plunder aus echter Butter."), ("g4", "heart", "Café & Frühstück", "Frühstück, Kuchen und Kaffee in der Backstube.")],
  feature="menu",
  menu=[("Brote", [("Bauernlaib 1 kg", "Roggen-Weizen, Natursauerteig", "5,40 €"), ("Dinkel-Vollkorn 750 g", "mit Saaten", "4,90 €"), ("Roggen-Saaten 750 g", "kräftig, lange frisch", "4,80 €")]),
        ("Gebäck", [("Butter-Croissant", "französische Art", "1,60 €"), ("Zimtschnecke", "mit Ceylon-Zimt", "2,20 €"), ("Laugenbrezel", "handgeschlungen", "1,10 €")]),
        ("Kuchen", [("Apfelkuchen", "Stück, mit Streuseln", "2,90 €"), ("Käsekuchen", "Stück, nach Familienrezept", "3,10 €")])],
  hours=[("Mo–Fr", "6:30", "18:00"), ("Sa", "7:00", "13:00"), ("So", "8:00", "11:00")],
  quote=("Für uns zählt Geduld: Ein gutes Brot braucht Zeit – und die geben wir ihm.", "Familie Musterbrot"),
  host=("FM", "Familie Musterbrot", "Fragen zur Vorbestellung? Ruf uns an oder schreib uns."),
  gal=["g1", "g2", "g3", "g4"]),
 "physio": dict(
  name="Physio Beispiel", ort="Musterstadt", branche="Praxis für Physiotherapie", art="Physiotherapie",
  fonts="DM+Serif+Display:ital@0;1&family=Inter:wght@400;500;600;700", serif="DM Serif Display", sans="Inter",
  c=dict(bg="#F6F9F8", alt="#E8F1EF", ink="#12302F", mute="#5E7675", acc="#0F8B8D", gold="#E3B261", card="#FFFFFF", dark="#0E2A2A", band="#0F6E70"),
  greet="Praxis für Physiotherapie · Musterstadt", h1="Wieder schmerzfrei <em>bewegen</em>.",
  lead="Persönliche Behandlung, klare Übungen für zu Hause und Termine, die du in zwei Minuten anfragst.",
  cta="Termin anfragen", cta2="Unsere Leistungen",
  trust=[("pin", "Musterstraße 1 · Musterstadt"), ("clock", "Mo–Do bis 20 Uhr"), ("check", "Alle Kassen & privat")],
  bar=[("hand", "Manuelle Therapie", "Gelenke & Wirbelsäule"), ("heart", "Krankengymnastik", "aktiv & nachhaltig"), ("spark", "Sportphysio", "zurück ins Training"), ("access", "Barrierefrei", "Aufzug & Parkplätze")],
  story=("Unsere Praxis", "Ein Ort zum <em>Ankommen</em>.", "Helle Räume, ruhige Atmosphäre und ein Team, das sich Zeit nimmt. Wir behandeln nicht nur Symptome, sondern zeigen dir, wie du selbst dranbleibst.", "g1", ("Neu", "2024", "modernisiert")),
  leistungen=[("hero", "hand", "Manuelle Therapie", "Gezielte Mobilisation von Gelenken und Wirbelsäule."), ("g1", "heart", "Krankengymnastik", "Aktive Übungen, die dich langfristig stark machen."), ("g2", "leaf", "Massage", "Lockert Verspannungen und fördert die Durchblutung.")],
  feature="booking", services=["Erstbefund (45 Min)", "Krankengymnastik", "Manuelle Therapie", "Massage"],
  hours=[("Mo–Do", "7:30", "20:00"), ("Fr", "7:30", "16:00")],
  team=[("AM", "Anna Muster", "Physiotherapeutin · Manuelle Therapie"), ("JB", "Jonas Beispiel", "Physiotherapeut · Sportphysio")],
  rezept=[("Verordnung", "Rezept vom Arzt – Kasse oder privat."), ("Anrufen", "Wir finden zusammen deinen Termin."), ("Erstbefund", "45 Minuten Zeit für dich und deinen Plan.")],
  quote=("Wir behandeln nicht nur Symptome – wir zeigen dir, wie du selbst dranbleibst.", "Praxisteam Physio Beispiel"),
  host=("AM", "Anna Muster", "Hallo, ich bin Anna. Ruf mich an oder frag hier deinen Termin an."),
  gal=["g1", "g2", "hero", "cta"]),
 "friseur": dict(
  name="Friseur Beispiel", ort="Musterstadt", branche="Salon & Barbershop", art="Salon",
  fonts="Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Pinyon+Script&family=Manrope:wght@400;500;600;700", serif="Playfair Display", sans="Manrope", script="Pinyon Script",
  c=dict(bg="#F7F2EF", alt="#EDE3DD", ink="#1E1A19", mute="#6F6461", acc="#9C6B5A", gold="#C9A27E", card="#FFFFFF", dark="#171312", band="#2A2220"),
  greet="Willkommen im Salon", h1="Dein Stil. <em>Präzise</em> geschnitten.",
  lead="Ruhige Atmosphäre, ehrliche Beratung und ein Schnitt, der auch nach drei Wochen noch sitzt.",
  cta="Termin buchen", cta2="Preise ansehen",
  trust=[("pin", "Musterstraße 1 · Musterstadt"), ("clock", "Di–Sa geöffnet"), ("check", "Beratung inklusive")],
  bar=[("scissors", "Schnitt", "Damen & Herren"), ("spark", "Farbe", "Strähnen & Balayage"), ("hand", "Bart", "Rasur mit heißem Tuch"), ("cal", "Online-Termin", "in 1 Minute")],
  story=("Unser Salon", "Zeit für <em>dich</em>.", "Bei uns gibt es keinen Schnitt nach Schema. Wir hören zu, beraten ehrlich und arbeiten mit Produkten, hinter denen wir stehen.", "g1", ("Team", "2", "Stylisten")),
  leistungen=[("hero", "scissors", "Haarschnitt", "Waschen, Schneiden, Styling – mit Beratung."), ("g2", "spark", "Farbe", "Natürliche Töne, Strähnen, Balayage."), ("g3", "hand", "Bart", "Konturen, Rasur mit heißem Tuch.")],
  feature="booking", services=["Herrenschnitt", "Damenschnitt", "Farbe & Strähnen", "Bartpflege"],
  prices=[("Damen", [("Waschen, Schneiden, Föhnen", "ab 48 €"), ("Farbe", "ab 55 €"), ("Balayage", "ab 120 €")]), ("Herren", [("Herrenschnitt", "29 €"), ("Bart trimmen", "15 €"), ("Schnitt + Bart", "40 €")])],
  hours=[("Di–Fr", "9:00", "19:00"), ("Sa", "9:00", "15:00")],
  team=[("LM", "Lea Muster", "Inhaberin · Farbe & Balayage"), ("TB", "Tom Beispiel", "Barber · Schnitt & Bart")],
  quote=("Ein guter Schnitt fängt mit Zuhören an.", "Team Friseur Beispiel"),
  host=("LM", "Lea Muster", "Hi, ich bin Lea. Ruf an oder buch direkt deinen Termin."),
  gal=["g1", "g2", "g3", "hero"]),
}

def head_(t, cap, sub=""):
    return f'<div class="sh reveal"><span class="cap">{E(cap)}</span><h2>{t}</h2>{f"<p>{E(sub)}</p>" if sub else ""}</div>'

def page(key, d):
    c = d["c"]; cr = CRED[key]; scr = d.get("script")
    em = f"font-family:'{scr}',cursive;font-weight:400;font-size:1.15em;" if scr else "font-style:italic;"
    trust = "".join(f'<span>{ic(i, 16)}{E(t)}</span>' for i, t in d["trust"])
    bar = "".join(f'<div class="bi reveal" style="--d:{i*80}ms"><i>{ic(n)}</i><b>{E(t)}</b><small>{E(s)}</small></div>' for i, (n, t, s) in enumerate(d["bar"]))
    st = d["story"]
    story = f'''<section class="sec"><div class="wrap story"><div class="sp reveal"><img src="img/{st[3]}.jpg" alt="{E(d["branche"])}" loading="lazy"><div class="badge"><small>{E(st[4][0])}</small><b>{E(st[4][1])}</b><small>{E(st[4][2])}</small></div></div>
<div class="reveal" style="--d:120ms"><span class="cap">{E(st[0])}</span><h2>{st[1]}</h2><p class="muted">{E(st[2])}</p>{f'<p class="sig">{E(d["quote"][1])}</p>' if scr else ""}</div></div></section>'''
    lst = "".join(f'<article class="svc reveal lift" style="--d:{i*90}ms"><div class="si"><img src="img/{im}.jpg" alt="{E(t)}" loading="lazy"><i>{ic(n, 20)}</i></div><div class="sb"><h3>{E(t)}</h3><p>{E(x)}</p></div></article>' for i, (im, n, t, x) in enumerate(d["leistungen"]))
    rez = ""
    if d.get("rezept"):
        rez = '<section class="sec alt"><div class="wrap">' + head_("So einfach <em>geht’s</em>.", "Mit Rezept zu uns") + '<div class="steps3">' + "".join(f'<div class="s3 reveal" style="--d:{i*100}ms"><span>{i+1}</span><b>{E(t)}</b><small>{E(x)}</small></div>' for i, (t, x) in enumerate(d["rezept"])) + '</div></div></section>'
    if d["feature"] == "menu":
        tabs = "".join(f'<button type="button" class="tab{" on" if i==0 else ""}" data-t="{i}">{E(cat)}</button>' for i, (cat, _) in enumerate(d["menu"]))
        panes = "".join(f'<div class="pane{" on" if i==0 else ""}" data-p="{i}">' + "".join(f'<div class="mi"><div><b>{E(n)}</b><small>{E(s)}</small></div><i></i><em>{E(p)}</em></div>' for n, s, p in items) + "</div>" for i, (cat, items) in enumerate(d["menu"]))
        feat = f'<section id="feature" class="sec">' + '<div class="wrap">' + head_("Heute frisch <em>aus dem Ofen</em>.", "Brotkarte · Beispiel", "Unser Sortiment – im echten Projekt mit den Produkten und Preisen des Betriebs.") + f'<div class="menu reveal"><div class="tabs">{tabs}</div>{panes}</div><p class="note">✦ Beispielhafte Karte · Vorbestellung bis 18 Uhr für den nächsten Morgen</p></div></section>'
    else:
        opts = "".join(f'<button type="button" class="opt" data-v="{E(s)}">{E(s)}</button>' for s in d["services"])
        feat = f'''<section id="feature" class="sec band"><div class="wrap book"><div class="reveal"><span class="cap light">Online-Termin</span><h2>In wenigen Schritten zu <em>deinem Termin</em>.</h2><p>Leistung wählen, Wunschtermin angeben, Kontakt hinterlassen – wir bestätigen persönlich. Lieber telefonieren?</p><a class="telbig" href="tel:+490000000000">{ic("phone", 18)} 0000 000000</a></div>
<div class="steps reveal" id="steps" style="--d:120ms"><b class="ft">Terminanfrage</b><div class="st on" data-s="1"><b>1 · Leistung</b><div class="opts">{opts}</div></div>
<div class="st" data-s="2"><b>2 · Wunschtermin</b><div class="row"><input type="date" id="dt" aria-label="Datum"><select id="tm" aria-label="Tageszeit"><option>Vormittag</option><option>Mittag</option><option>Nachmittag</option><option>Abend</option></select></div><button type="button" class="btn small" id="n2">Weiter</button></div>
<div class="st" data-s="3"><b>3 · Kontakt</b><div class="row"><input id="nm" placeholder="Dein Name" aria-label="Name"><input id="ph" placeholder="Telefon" aria-label="Telefon"></div><button type="button" class="btn small sheen" id="send">Anfrage senden</button><p class="ok" id="ok"></p></div></div></div></section>'''
    prices = ""
    if d.get("prices"):
        prices = '<section id="preise" class="sec"><div class="wrap">' + head_("Klare <em>Preise</em>.", "Preisliste · Beispiel") + '<div class="pl">' + "".join(f'<div class="plc reveal" style="--d:{i*100}ms"><h3>{E(cat)}</h3>' + "".join(f'<div class="mi"><div><b>{E(n)}</b></div><i></i><em>{E(p)}</em></div>' for n, p in items) + '</div>' for i, (cat, items) in enumerate(d["prices"])) + '</div></div></section>'
    team = ""
    if d.get("team"):
        team = '<section class="sec alt"><div class="wrap">' + head_("Menschen, die sich <em>Zeit nehmen</em>.", "Unser Team", "Direkt erreichbar – ein Anruf genügt.") + '<div class="team">' + "".join(f'<div class="av reveal lift" style="--d:{i*90}ms"><span class="ini">{E(a)}</span><b>{E(n)}</b><small>{E(r)}</small><a class="btn small ghost" href="tel:+490000000000">{ic("phone", 16)} Anrufen</a></div>' for i, (a, n, r) in enumerate(d["team"])) + '</div><p class="note center">Ohne Foto zeigen wir Initialen – nie erfundene Gesichter.</p></div></section>'
    gal = "".join(f'<figure class="reveal g{i}" style="--d:{i*80}ms"><img src="img/{g}.jpg" alt="{E(d["branche"])} – Einblick" loading="lazy"></figure>' for i, g in enumerate(d["gal"]))
    hours = "".join(f'<tr data-d="{E(dd)}" data-a="{a}" data-b="{b}"><td>{E(dd)}</td><td>{a}–{b} Uhr</td></tr>' for dd, a, b in d["hours"])
    credits = " · ".join(f'<a href="{E(x["src"])}" target="_blank" rel="noopener">{E(x["file"])}</a> ({E(x["lic"].upper())}{", " + E(x["creator"]) if x["creator"] else ""})' for x in cr)
    h = d["host"]
    nav2 = "Brotkarte" if d["feature"] == "menu" else "Termin"
    greet_css = f"font-family:'{scr}',cursive;font-size:clamp(30px,3.4vw,44px);" if scr else "font-family:var(--sans);font-size:13px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;"
    sig_font = f"'{scr}',cursive" if scr else "var(--serif)"
    return f'''<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>{E(d["name"])} · Demo-Konzeptseite · Flow DNA</title>
<meta name="description" content="Demo-Konzeptseite für einen erfundenen Betrieb ({E(d["branche"])}) – gebaut mit dem Landingpage Generator von Flow DNA.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={d["fonts"]}&display=swap">
<link rel="preload" as="image" href="img/hero.jpg">
<style>
:root{{--bg:{c["bg"]};--alt:{c["alt"]};--ink:{c["ink"]};--mute:{c["mute"]};--acc:{c["acc"]};--gold:{c["gold"]};--card:{c["card"]};--dark:{c["dark"]};--band:{c["band"]};--serif:'{d["serif"]}',Georgia,serif;--sans:'{d["sans"]}',system-ui,sans-serif;--ease:cubic-bezier(.2,.7,.3,1)}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.65 var(--sans);-webkit-font-smoothing:antialiased;overflow-x:hidden}}
img{{display:block;max-width:100%}}a{{color:inherit}}.wrap{{max-width:1180px;margin:0 auto;padding:0 22px}}
h1,h2,h3{{font-family:var(--serif);font-weight:600;line-height:1.08;margin:0}}h1 em,h2 em{{{em}color:var(--acc)}}
.demo{{position:fixed;left:0;right:0;top:0;z-index:70;background:#000;color:#fff;text-align:center;font:600 11px/1.3 var(--sans);letter-spacing:.06em;padding:6px 10px}}.demo a{{color:var(--gold)}}
header{{position:fixed;left:0;right:0;top:26px;z-index:60;color:#fff;transition:background .4s var(--ease),color .4s,box-shadow .4s}}
header .wrap{{display:flex;align-items:center;gap:18px;height:78px;transition:height .4s var(--ease)}}
header.scrolled{{background:color-mix(in srgb,var(--bg) 82%,transparent);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);color:var(--ink);box-shadow:0 8px 30px rgba(0,0,0,.08)}}header.scrolled .wrap{{height:62px}}
.brand{{font:700 24px/1 var(--serif);text-decoration:none;margin-right:auto}}
nav{{display:flex;gap:22px}}nav a{{text-decoration:none;font-weight:600;font-size:15px;opacity:.85}}nav a:hover{{opacity:1}}
.hp{{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:600;font-size:14px;padding:9px 14px;border-radius:999px;border:1px solid color-mix(in srgb,currentColor 35%,transparent)}}
@media(max-width:900px){{nav,.hp{{display:none}}}}@media(max-width:520px){{header .hb{{display:none}}}}
.btn{{position:relative;overflow:hidden;display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:16px 26px;border-radius:999px;background:var(--acc);color:#fff;font:600 16px var(--sans);text-decoration:none;border:0;cursor:pointer;box-shadow:0 14px 30px color-mix(in srgb,var(--acc) 35%,transparent);transition:transform .3s var(--ease),box-shadow .3s}}
.btn:hover{{transform:translateY(-2px)}}.btn.ghost{{background:transparent;color:inherit;box-shadow:inset 0 0 0 1.5px color-mix(in srgb,currentColor 45%,transparent)}}.btn.small{{padding:11px 18px;font-size:15px}}.btn.hb{{padding:12px 20px;font-size:15px}}
.sheen::after{{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.45),transparent);animation:sheen 3.6s 1.2s infinite}}@keyframes sheen{{0%{{left:-60%}}35%,100%{{left:130%}}}}
.hero{{position:relative;isolation:isolate;min-height:100svh;display:flex;align-items:center;color:#fff;overflow:hidden;padding:140px 0 150px}}
.hero .bg{{position:absolute;inset:0;z-index:-2}}.hero .bg img{{width:100%;height:100%;object-fit:cover;animation:kb 22s var(--ease) infinite alternate}}
@keyframes kb{{from{{transform:scale(1.04)}}to{{transform:scale(1.16) translate(-1.5%,-1%)}}}}
.hero::before{{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,color-mix(in srgb,var(--dark) 88%,transparent) 0%,color-mix(in srgb,var(--dark) 62%,transparent) 48%,color-mix(in srgb,var(--dark) 18%,transparent) 100%),linear-gradient(0deg,color-mix(in srgb,var(--dark) 70%,transparent),transparent 40%)}}
.hero .in{{max-width:660px}}.greet{{{greet_css}color:var(--gold);margin:0 0 6px}}
.hero h1{{font-size:clamp(46px,6.6vw,92px);letter-spacing:-.01em}}.hero h1 em{{color:var(--gold)}}
.hero .lead{{font-size:clamp(17px,1.5vw,20px);opacity:.9;max-width:44ch;margin:22px 0 30px}}.ctas{{display:flex;gap:12px;flex-wrap:wrap}}
.trust{{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:30px;font-size:14px;opacity:.9}}.trust span{{display:inline-flex;align-items:center;gap:8px}}.trust svg{{color:var(--gold)}}
.scroll{{position:absolute;left:50%;bottom:110px;transform:translateX(-50%);font:600 11px var(--sans);letter-spacing:.3em;opacity:.7}}.scroll::after{{content:"";display:block;width:1px;height:34px;margin:8px auto 0;background:#fff;animation:sc 2s infinite}}@keyframes sc{{0%{{transform:scaleY(0);transform-origin:top}}50%{{transform:scaleY(1);transform-origin:top}}51%{{transform-origin:bottom}}100%{{transform:scaleY(0);transform-origin:bottom}}}}
@media(max-height:940px){{.scroll{{display:none}}}}@media(max-width:760px){{.scroll{{display:none}}.hero{{padding:130px 0 120px;align-items:flex-end}}.hero::before{{background:linear-gradient(0deg,color-mix(in srgb,var(--dark) 92%,transparent) 0%,color-mix(in srgb,var(--dark) 55%,transparent) 60%,color-mix(in srgb,var(--dark) 30%,transparent) 100%)}}}}
.bar{{position:relative;z-index:5;margin-top:-86px}}.bar .wrap{{display:grid;grid-template-columns:repeat(4,1fr);background:var(--dark);color:#fff;border-radius:22px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.25);padding:0}}
.bi{{padding:26px 20px;text-align:center;border-left:1px solid rgba(255,255,255,.08)}}.bi:first-child{{border-left:0}}.bi i{{display:inline-grid;place-items:center;width:46px;height:46px;border-radius:50%;background:rgba(255,255,255,.08);color:var(--gold);margin-bottom:10px}}.bi b{{display:block;font-size:16px}}.bi small{{opacity:.65;font-size:13px}}
@media(max-width:1220px){{.bar .wrap{{margin:0 22px}}}}@media(max-width:760px){{.bar{{margin-top:-60px}}.bar .wrap{{grid-template-columns:1fr 1fr;margin:0 16px}}.bi:nth-child(3){{border-left:0}}.bi:nth-child(n+3){{border-top:1px solid rgba(255,255,255,.08)}}.bi{{padding:20px 12px}}}}
.sec{{padding:110px 0}}.alt{{background:var(--alt)}}.muted{{color:var(--mute)}}.center{{text-align:center}}@media(max-width:760px){{.sec{{padding:80px 0}}}}
.cap{{display:inline-flex;align-items:center;gap:10px;font:600 12px var(--sans);letter-spacing:.24em;text-transform:uppercase;color:var(--acc);margin-bottom:14px}}.cap::before,.sh .cap::after{{content:"";width:26px;height:1px;background:currentColor}}.cap.light{{color:var(--gold)}}
.sh{{text-align:center;max-width:720px;margin:0 auto 48px}}.sh h2,.story h2,.book h2{{font-size:clamp(34px,4.4vw,58px)}}.sh p{{color:var(--mute);margin:14px 0 0}}
.story{{display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:center}}@media(max-width:860px){{.story{{grid-template-columns:1fr;gap:40px}}}}
.story h2{{margin-bottom:20px}}.sp{{position:relative}}.sp img{{border-radius:26px;aspect-ratio:4/5;object-fit:cover;width:100%;box-shadow:0 40px 80px rgba(0,0,0,.18)}}
.badge{{position:absolute;right:-18px;bottom:28px;background:var(--card);border-radius:18px;padding:16px 20px;text-align:center;box-shadow:0 20px 40px rgba(0,0,0,.15)}}.badge b{{display:block;font:600 40px/1 var(--serif);color:var(--acc)}}.badge small{{display:block;font-size:12px;color:var(--mute);letter-spacing:.05em}}
@media(max-width:860px){{.badge{{right:14px}}}}.sig{{font-family:{sig_font};font-size:34px;color:var(--acc);margin:22px 0 0}}
.svcs{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}@media(max-width:860px){{.svcs{{grid-template-columns:1fr}}}}
.svc{{background:var(--card);border-radius:22px;overflow:hidden;box-shadow:0 1px 0 rgba(0,0,0,.04)}}.si{{position:relative}}.si img{{aspect-ratio:16/10;object-fit:cover;width:100%;transition:transform .8s var(--ease)}}.svc:hover .si img{{transform:scale(1.05)}}
.si i{{position:absolute;left:20px;bottom:-22px;width:46px;height:46px;border-radius:14px;display:grid;place-items:center;background:var(--acc);color:#fff;box-shadow:0 10px 20px color-mix(in srgb,var(--acc) 40%,transparent)}}.sb{{padding:34px 24px 26px}}.sb h3{{font-size:26px;margin-bottom:8px}}.sb p{{margin:0;color:var(--mute)}}
.lift{{transition:transform .5s var(--ease),box-shadow .5s var(--ease)}}.lift:hover{{transform:translateY(-6px);box-shadow:0 24px 50px rgba(0,0,0,.10)}}
.steps3{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}@media(max-width:760px){{.steps3{{grid-template-columns:1fr}}}}.s3{{background:var(--card);border-radius:22px;padding:28px;text-align:center}}.s3 span{{display:inline-grid;place-items:center;width:52px;height:52px;border-radius:50%;background:var(--acc);color:#fff;font:600 22px var(--serif);margin-bottom:12px}}.s3 b{{display:block;font:600 24px var(--serif)}}.s3 small{{color:var(--mute);font-size:15px}}
.menu{{max-width:860px;margin:0 auto;background:var(--card);border-radius:26px;padding:30px;box-shadow:0 30px 60px rgba(0,0,0,.07)}}.tabs{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-bottom:18px}}
.tab{{border:1.5px solid color-mix(in srgb,var(--ink) 15%,transparent);background:transparent;color:var(--ink);border-radius:999px;padding:10px 18px;font:600 15px var(--sans);cursor:pointer}}.tab.on{{background:var(--acc);border-color:var(--acc);color:#fff}}
.pane{{display:none}}.pane.on{{display:block;animation:fi .5s var(--ease)}}@keyframes fi{{from{{opacity:0;transform:translateY(8px)}}}}
.mi{{display:flex;align-items:baseline;gap:12px;padding:14px 0;border-bottom:1px dashed color-mix(in srgb,var(--ink) 16%,transparent)}}.mi b{{font:600 21px var(--serif)}}.mi small{{display:block;color:var(--mute);font-size:14px}}.mi i{{flex:1}}.mi em{{font-style:normal;font-weight:700;color:var(--acc);white-space:nowrap}}
.note{{font-size:14px;color:var(--mute);margin-top:18px;text-align:center}}
.band{{background:var(--band);color:#fff;position:relative;overflow:hidden}}.band::before{{content:"";position:absolute;width:420px;height:420px;border-radius:50%;background:rgba(255,255,255,.06);left:-140px;top:-140px}}
.book{{position:relative;display:grid;grid-template-columns:.95fr 1.05fr;gap:56px;align-items:center}}@media(max-width:860px){{.book{{grid-template-columns:1fr}}}}.book h2 em{{color:var(--gold)}}.book p{{opacity:.85;margin:18px 0 22px}}
.telbig{{display:inline-flex;align-items:center;gap:10px;font:600 22px var(--serif);text-decoration:none;color:#fff;border-bottom:1px solid rgba(255,255,255,.4);padding-bottom:4px}}
.steps{{background:var(--card);color:var(--ink);border-radius:24px;padding:26px;box-shadow:0 40px 80px rgba(0,0,0,.25)}}.ft{{display:block;font:600 24px var(--serif);margin-bottom:6px}}
.st{{padding:14px 0;border-bottom:1px solid color-mix(in srgb,var(--ink) 10%,transparent);opacity:.4;transition:opacity .4s}}.st:last-child{{border:0}}.st.on{{opacity:1}}.st>b{{font:600 12px var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--acc)}}
.opts{{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}}.opt{{border:1.5px solid color-mix(in srgb,var(--ink) 18%,transparent);background:transparent;border-radius:999px;padding:10px 14px;font:500 15px var(--sans);cursor:pointer;color:var(--ink)}}.opt.sel{{background:var(--acc);border-color:var(--acc);color:#fff}}
.row{{display:flex;gap:8px;margin:10px 0;flex-wrap:wrap}}.row input,.row select{{flex:1;min-width:130px;padding:12px 14px;border-radius:12px;border:1.5px solid color-mix(in srgb,var(--ink) 16%,transparent);font:400 16px var(--sans);background:var(--bg);color:var(--ink)}}.ok{{color:var(--acc);font-weight:600;margin:10px 0 0}}
.pl{{display:grid;grid-template-columns:1fr 1fr;gap:22px}}@media(max-width:760px){{.pl{{grid-template-columns:1fr}}}}.plc{{background:var(--card);border-radius:22px;padding:28px}}.plc h3{{font-size:28px;margin-bottom:6px}}
.team{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,300px));gap:22px;justify-content:center}}.av{{background:var(--card);border-radius:24px;padding:30px 24px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:4px}}
.ini{{width:108px;height:108px;border-radius:50%;display:grid;place-items:center;background:linear-gradient(135deg,var(--acc),color-mix(in srgb,var(--acc) 60%,var(--dark)));color:#fff;font:600 38px var(--serif);margin-bottom:12px;box-shadow:0 0 0 6px var(--card),0 0 0 8px color-mix(in srgb,var(--acc) 30%,transparent)}}
.av b{{font:600 22px var(--serif)}}.av small{{color:var(--mute);margin-bottom:14px}}.av .btn{{color:var(--acc)}}
.gal{{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:220px;gap:14px}}.gal figure{{margin:0;border-radius:20px;overflow:hidden}}.gal .g0{{grid-column:span 2;grid-row:span 2}}.gal img{{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease)}}.gal figure:hover img{{transform:scale(1.06)}}
@media(max-width:760px){{.gal{{grid-template-columns:1fr 1fr;grid-auto-rows:150px}}}}
.qb{{background:var(--dark);color:#fff;text-align:center}}.qb .stars{{color:var(--gold);display:flex;gap:4px;justify-content:center;margin-bottom:18px}}.qb p{{font:500 clamp(26px,3.4vw,44px)/1.25 var(--serif);max-width:860px;margin:0 auto}}.qb span{{display:block;margin-top:18px;opacity:.6;font-weight:600}}
.contact{{display:grid;grid-template-columns:1fr 1fr;gap:28px}}@media(max-width:760px){{.contact{{grid-template-columns:1fr}}}}.cc{{background:var(--card);border-radius:24px;padding:30px}}
.cl{{display:flex;gap:14px;align-items:flex-start;padding:12px 0}}.cl i{{flex:none;width:42px;height:42px;border-radius:12px;display:grid;place-items:center;background:color-mix(in srgb,var(--acc) 12%,transparent);color:var(--acc)}}.cl small{{display:block;color:var(--mute);font-size:13px;letter-spacing:.08em;text-transform:uppercase}}
table{{width:100%;border-collapse:collapse}}td{{padding:13px 0;border-bottom:1px solid color-mix(in srgb,var(--ink) 10%,transparent)}}td:last-child{{text-align:right;font-weight:600}}tr.now td{{color:var(--acc)}}.open{{display:inline-flex;align-items:center;gap:8px;margin-top:14px;font-weight:700;color:var(--acc)}}
.ctab{{position:relative;margin:0 22px;border-radius:30px;overflow:hidden;min-height:420px;display:grid;place-items:center;text-align:center;color:#fff}}.ctab img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}.ctab::before{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,color-mix(in srgb,var(--dark) 40%,transparent),color-mix(in srgb,var(--dark) 85%,transparent));z-index:1}}
.ctab div{{position:relative;z-index:2;padding:50px 22px}}.ctab h2{{font-size:clamp(36px,5vw,64px);margin-bottom:24px}}.ctab h2 em{{color:var(--gold)}}
footer{{background:var(--dark);color:rgba(255,255,255,.7);margin-top:110px;padding:70px 0 120px;font-size:14px}}.fg{{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:40px}}@media(max-width:760px){{.fg{{grid-template-columns:1fr}}}}footer b{{display:block;color:#fff;font:600 13px var(--sans);letter-spacing:.18em;text-transform:uppercase;margin-bottom:12px}}footer .brand{{display:block;color:#fff;font-size:28px;margin-bottom:12px}}footer a{{color:rgba(255,255,255,.7);text-decoration:none;display:block;padding:3px 0}}.fine{{border-top:1px solid rgba(255,255,255,.1);margin-top:40px;padding-top:20px;font-size:12px}}.fine a{{display:inline;text-decoration:underline}}
.mcta{{position:fixed;left:12px;right:84px;bottom:14px;z-index:55;display:none}}@media(max-width:760px){{.mcta{{display:block}}}}.mcta .btn{{width:100%;animation:pulse 2.6s infinite}}@keyframes pulse{{0%,100%{{box-shadow:0 0 0 0 color-mix(in srgb,var(--acc) 45%,transparent)}}70%{{box-shadow:0 0 0 14px transparent}}}}
.ask{{position:fixed;right:16px;bottom:14px;z-index:58}}.ask>button{{width:60px;height:60px;border-radius:50%;border:3px solid #fff;background:linear-gradient(135deg,var(--acc),color-mix(in srgb,var(--acc) 60%,var(--dark)));color:#fff;font:600 20px var(--serif);cursor:pointer;box-shadow:0 12px 30px rgba(0,0,0,.25);position:relative}}.ask>button::after{{content:"";position:absolute;right:0;top:2px;width:13px;height:13px;border-radius:50%;background:#2ecc71;border:2px solid #fff}}
.askp{{position:absolute;right:0;bottom:74px;width:min(320px,86vw);background:var(--card);color:var(--ink);border-radius:20px;box-shadow:0 30px 60px rgba(0,0,0,.25);padding:18px;display:none}}.ask.open .askp{{display:block;animation:fi .35s var(--ease)}}
.askh{{display:flex;gap:12px;align-items:center;margin-bottom:12px}}.askh span{{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:var(--acc);color:#fff;font:600 16px var(--serif)}}.askh b{{display:block}}.askh small{{color:#1e9e57;font-weight:600}}.bub{{background:var(--alt);border-radius:4px 16px 16px 16px;padding:12px 14px;font-size:15px;margin-bottom:12px}}.askp .btn{{width:100%;margin-top:6px}}
.reveal{{opacity:0;transform:translateY(28px);transition:opacity .9s var(--ease) var(--d,0ms),transform .9s var(--ease) var(--d,0ms)}}.reveal.in{{opacity:1;transform:none}}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}.reveal{{opacity:1;transform:none}}}}
</style></head><body>
<div class="demo">DEMO · frei erfundener Betrieb · Konzeptseite gebaut mit dem <a href="../../">Flow DNA Landingpage Generator</a></div>
<header id="hd"><div class="wrap"><a class="brand" href="#">{E(d["name"])}</a><nav><a href="#leistungen">Leistungen</a><a href="#feature">{nav2}</a><a href="#kontakt">Kontakt</a></nav><a class="hp" href="tel:+490000000000">{ic("phone", 16)} 0000 000000</a><a class="btn hb sheen" href="#feature">{E(d["cta"])}</a></div></header>
<section class="hero"><div class="bg"><img src="img/hero.jpg" alt="{E(d["branche"])} in {E(d["ort"])}"></div><div class="wrap"><div class="in">
<p class="greet reveal">{E(d["greet"])}</p><h1 class="reveal" style="--d:80ms">{d["h1"]}</h1><p class="lead reveal" style="--d:160ms">{E(d["lead"])}</p>
<div class="ctas reveal" style="--d:240ms"><a class="btn sheen" href="#feature">{E(d["cta"])} →</a><a class="btn ghost" href="#{"feature" if d["feature"]=="menu" else "leistungen"}">{E(d["cta2"])}</a></div>
<div class="trust reveal" style="--d:320ms">{trust}</div></div></div><span class="scroll">SCROLL</span></section>
<div class="bar"><div class="wrap">{bar}</div></div>
{story}
<section id="leistungen" class="sec alt"><div class="wrap">{head_("Was wir <em>besonders</em> gut können.", "Leistungen")}<div class="svcs">{lst}</div></div></section>
{rez}{feat}{prices}{team}
<section class="sec"><div class="wrap">{head_("Ein <em>Einblick</em>.", "Galerie")}<div class="gal">{gal}</div></div></section>
<section class="sec qb"><div class="wrap reveal"><div class="stars">{ic("star",20)*5}</div><p>„{E(d["quote"][0])}“</p><span>– {E(d["quote"][1])} · Leitsatz des Betriebs (Beispiel)</span></div></section>
<section id="kontakt" class="sec"><div class="wrap">{head_("So findest du <em>uns</em>.", "Kontakt & Öffnungszeiten")}<div class="contact">
<div class="cc reveal"><div class="cl"><i>{ic("pin",20)}</i><div><small>Adresse</small>Musterstraße 1 · 00000 {E(d["ort"])}</div></div><div class="cl"><i>{ic("phone",20)}</i><div><small>Telefon</small><a href="tel:+490000000000">0000 000000 (Beispiel)</a></div></div><div class="cl"><i>{ic("chat",20)}</i><div><small>E-Mail</small>hallo@beispiel.de</div></div><a class="btn sheen" style="margin-top:12px" href="#feature">{E(d["cta"])} →</a></div>
<div class="cc reveal" style="--d:100ms"><div class="cl" style="padding-top:0"><i>{ic("clock",20)}</i><div><small>Öffnungszeiten</small>aktuelle Woche</div></div><table id="hours">{hours}</table><span class="open" id="open"></span></div></div></div></section>
<div class="ctab reveal"><img src="img/cta.jpg" alt="" loading="lazy"><div><h2>Wir freuen uns <em>auf dich</em>.</h2><a class="btn sheen" href="#feature">{E(d["cta"])} →</a></div></div>
<footer><div class="wrap"><div class="fg"><div><span class="brand">{E(d["name"])}</span>{E(d["art"])} in {E(d["ort"])}. Demo-Konzeptseite für einen frei erfundenen Betrieb.</div><div><b>Seite</b><a href="#leistungen">Leistungen</a><a href="#feature">{nav2}</a><a href="#kontakt">Kontakt</a></div><div><b>Kontakt</b><a href="tel:+490000000000">0000 000000</a><a href="#">hallo@beispiel.de</a><a href="#">Impressum · Datenschutz</a></div></div>
<div class="fine">Alle Namen, Daten und Preise sind Beispiele. Gebaut mit dem Flow DNA Landingpage Generator · Flow Media AI. Fotos (CC0/frei): {credits}</div></div></footer>
<div class="mcta"><a class="btn" href="#feature">{E(d["cta"])}</a></div>
<div class="ask" id="ask"><div class="askp"><div class="askh"><span>{E(h[0])}</span><div><b>{E(h[1])}</b><small>● jetzt erreichbar</small></div></div><div class="bub">{E(h[2])}</div><a class="btn small" href="tel:+490000000000">{ic("phone",16)} Anrufen</a><a class="btn small ghost" style="color:var(--acc)" href="#feature">{E(d["cta"])}</a></div><button type="button" aria-label="Kontakt öffnen" onclick="this.parentNode.classList.toggle('open')">{E(h[0])}</button></div>
<script>
const hd=document.getElementById("hd");const sc=()=>hd.classList.toggle("scrolled",scrollY>40);addEventListener("scroll",sc,{{passive:true}});sc();
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add("in");io.unobserve(e.target)}}}}),{{threshold:.12}});document.querySelectorAll(".reveal").forEach(el=>io.observe(el));
(function(){{const map={{"Mo":1,"Di":2,"Mi":3,"Do":4,"Fr":5,"Sa":6,"So":0}},now=new Date(),d=now.getDay(),m=now.getHours()*60+now.getMinutes();let open=false;
document.querySelectorAll("#hours tr").forEach(tr=>{{const p=tr.dataset.d.split("–"),a=map[p[0]],b=map[p[1]||p[0]];const inDay=a<=b?(d>=a&&d<=b):(d>=a||d<=b);
const t=s=>{{const[h,mi]=s.split(":").map(Number);return h*60+mi}};if(inDay){{tr.classList.add("now");if(m>=t(tr.dataset.a)&&m<t(tr.dataset.b))open=true}}}});
document.getElementById("open").textContent=open?"● Jetzt geöffnet":"○ Gerade geschlossen";}})();
document.querySelectorAll(".tab").forEach(b=>b.onclick=()=>{{document.querySelectorAll(".tab").forEach(x=>x.classList.toggle("on",x===b));document.querySelectorAll(".pane").forEach(p=>p.classList.toggle("on",p.dataset.p===b.dataset.t))}});
const steps=document.getElementById("steps");if(steps){{const st=n=>steps.querySelectorAll(".st").forEach(s=>s.classList.toggle("on",+s.dataset.s<=n));
steps.querySelectorAll(".opt").forEach(b=>b.onclick=()=>{{steps.querySelectorAll(".opt").forEach(x=>x.classList.remove("sel"));b.classList.add("sel");st(2)}});
document.getElementById("n2").onclick=()=>st(3);document.getElementById("send").onclick=()=>{{document.getElementById("ok").textContent="✓ Demo: In der echten Seite geht jetzt deine Anfrage raus."}}}}
</script></body></html>'''

for k, d in DEMOS.items():
    open(os.path.join(HERE, k, "index.html"), "w", encoding="utf-8").write(page(k, d))
    print(k, os.path.getsize(os.path.join(HERE, k, "index.html")))
