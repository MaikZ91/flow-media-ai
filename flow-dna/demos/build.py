# Baut die drei Demo-Konzeptseiten für die Flow-DNA-Galerie (erfundene Demo-Betriebe, CC0-Fotos).
# Nach den Premium-Design-Regeln (Branchen-Look, Schriftpaar, Ken Burns, Reveal, Glas-Header, Sheen, Mobile-CTA, Premium-Feature).
# Aufruf: python3 build.py
import json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
CRED = json.load(open(os.path.join(HERE, "credits.json"), encoding="utf-8"))
E = html.escape

DEMOS = {
 "baeckerei": dict(
  name="Bäckerei Musterbrot", ort="Musterstadt", branche="Bäckerei & Café",
  fonts="Cormorant+Garamond:wght@500;600;700&family=Manrope:wght@400;500;600;700", serif="Cormorant Garamond", sans="Manrope",
  c=dict(bg="#FBF6EE", ink="#2B1D14", mute="#7A6656", acc="#B5502E", acc2="#E9B872", card="#FFFFFF", dark="#3A2418"),
  kicker="Handwerksbäckerei seit Generationen", h1="Brot, das nach <em>Zeit</em> schmeckt.",
  lead="Natursauerteig, 24 Stunden Ruhe, jeden Morgen frisch aus dem Steinofen. Vorbestellen und warm abholen.",
  cta="Brot vorbestellen", cta2="Speisekarte ansehen",
  usps=["Natursauerteig", "Steinofen", "Regionales Mehl", "Vorbestellung online"],
  leistungen=[("Brote", "Roggen, Dinkel, Vollkorn – lange geführt, kräftig gebacken."), ("Feingebäck", "Croissants und Plunder aus echter Butter."), ("Café", "Frühstück und Kaffee aus der Röstmanufaktur nebenan.")],
  feature="menu",
  menu=[("Brote", [("Bauernlaib 1 kg", "5,40 €"), ("Dinkel-Vollkorn 750 g", "4,90 €"), ("Roggen-Saaten 750 g", "4,80 €")]), ("Gebäck", [("Butter-Croissant", "1,60 €"), ("Zimtschnecke", "2,20 €"), ("Laugenbrezel", "1,10 €")])],
  hours=[("Mo–Fr", "6:30", "18:00"), ("Sa", "7:00", "13:00"), ("So", "8:00", "11:00")],
  quote=("Für uns zählt Geduld: Ein gutes Brot braucht Zeit – und die geben wir ihm.", "Familie Musterbrot"),
  gal=["g1", "g2", "g3", "g4"]),
 "physio": dict(
  name="Physio Beispiel", ort="Musterstadt", branche="Praxis für Physiotherapie",
  fonts="DM+Serif+Display&family=Inter:wght@400;500;600;700", serif="DM Serif Display", sans="Inter",
  c=dict(bg="#F4F8F8", ink="#12302F", mute="#5E7675", acc="#0F8B8D", acc2="#BDE3E1", card="#FFFFFF", dark="#0E2A2A"),
  kicker="Physiotherapie · Manuelle Therapie · Training", h1="Wieder schmerzfrei <em>bewegen</em>.",
  lead="Persönliche Behandlung, klare Übungen für zu Hause und Termine, die du in zwei Minuten online buchst.",
  cta="Termin online buchen", cta2="Leistungen ansehen",
  usps=["Alle Kassen & privat", "Termine auch abends", "Barrierefrei", "Online-Buchung"],
  leistungen=[("Manuelle Therapie", "Gezielte Mobilisation von Gelenken und Wirbelsäule."), ("Krankengymnastik", "Aktive Übungen, die dich langfristig stark machen."), ("Massage", "Lockert Verspannungen und fördert die Durchblutung.")],
  feature="booking", services=["Erstbefund (45 Min)", "Krankengymnastik", "Manuelle Therapie", "Massage"],
  hours=[("Mo–Do", "7:30", "20:00"), ("Fr", "7:30", "16:00")],
  quote=("Wir behandeln nicht nur Symptome – wir zeigen dir, wie du selbst dranbleibst.", "Praxisteam Physio Beispiel"),
  gal=["g1", "g2"]),
 "friseur": dict(
  name="Friseur Beispiel", ort="Musterstadt", branche="Salon & Barbershop",
  fonts="Playfair+Display:wght@500;600;700&family=Pinyon+Script&family=Manrope:wght@400;500;600;700", serif="Playfair Display", sans="Manrope", script="Pinyon Script",
  c=dict(bg="#F6F1EE", ink="#1E1A19", mute="#6F6461", acc="#9C6B5A", acc2="#D9BFB3", card="#FFFFFF", dark="#1E1A19"),
  kicker="Schnitt · Farbe · Bart", h1="Dein Stil. <em>Präzise</em> geschnitten.",
  lead="Ruhige Atmosphäre, ehrliche Beratung und ein Schnitt, der auch nach drei Wochen noch sitzt.",
  cta="Termin buchen", cta2="Preise ansehen",
  usps=["Online-Termin", "Herren & Damen", "Bartpflege", "Beratung inklusive"],
  leistungen=[("Haarschnitt", "Waschen, Schneiden, Styling – mit Beratung."), ("Farbe", "Natürliche Töne, Strähnen, Balayage."), ("Bart", "Konturen, Rasur mit heißem Tuch.")],
  feature="booking", services=["Herrenschnitt", "Damenschnitt", "Farbe & Strähnen", "Bartpflege"],
  hours=[("Di–Fr", "9:00", "19:00"), ("Sa", "9:00", "15:00")],
  quote=("Ein guter Schnitt fängt mit Zuhören an.", "Team Friseur Beispiel"),
  gal=["g1", "g2", "g3"]),
}

def page(key, d):
    c = d["c"]; cr = CRED[key]
    script = f"font-family:'{d['script']}',cursive;" if d.get("script") else "font-style:italic;"
    usps = "".join(f'<li class="reveal" style="--d:{i*80}ms">{E(u)}</li>' for i, u in enumerate(d["usps"]))
    lst = "".join(f'<article class="card reveal lift" style="--d:{i*90}ms"><span class="no">0{i+1}</span><h3>{E(t)}</h3><p>{E(x)}</p></article>' for i, (t, x) in enumerate(d["leistungen"]))
    gal = "".join(f'<figure class="reveal" style="--d:{i*80}ms"><img src="img/{g}.jpg" alt="{E(d["branche"])} – Beispielbild" loading="lazy"></figure>' for i, g in enumerate(d["gal"]))
    if d["feature"] == "menu":
        cols = "".join(f'<div class="menu-col reveal"><h3>{E(cat)}</h3>' + "".join(f'<div class="mi"><span>{E(n)}</span><i></i><b>{E(p)}</b></div>' for n, p in items) + "</div>" for cat, items in d["menu"])
        feat = f'<section id="feature" class="sec"><div class="wrap"><p class="kick reveal">Speisekarte · Beispiel</p><h2 class="reveal">Heute frisch <em>aus dem Ofen</em>.</h2><div class="menu">{cols}</div><p class="note">Beispielhafte Karte – im echten Projekt mit den Produkten und Preisen des Betriebs.</p></div></section>'
    else:
        opts = "".join(f'<button type="button" class="opt" data-v="{E(s)}">{E(s)}</button>' for s in d["services"])
        feat = f'''<section id="feature" class="sec"><div class="wrap book reveal"><div><p class="kick">Online-Termin</p><h2>In drei Schritten <em>gebucht</em>.</h2><p class="muted">Leistung wählen, Wunschtermin angeben, Kontakt hinterlassen – wir bestätigen persönlich.</p></div>
<div class="steps" id="steps"><div class="st on" data-s="1"><b>1 · Leistung</b><div class="opts">{opts}</div></div>
<div class="st" data-s="2"><b>2 · Wunschtermin</b><div class="row"><input type="date" id="dt"><select id="tm"><option>Vormittag</option><option>Mittag</option><option>Nachmittag</option><option>Abend</option></select></div><button type="button" class="btn small" id="n2">Weiter</button></div>
<div class="st" data-s="3"><b>3 · Kontakt</b><div class="row"><input id="nm" placeholder="Dein Name"><input id="ph" placeholder="Telefon"></div><button type="button" class="btn small sheen" id="send">Anfrage senden</button><p class="ok" id="ok"></p></div></div></div></section>'''
    hours = "".join(f'<tr data-d="{E(dd)}" data-a="{a}" data-b="{b}"><td>{E(dd)}</td><td>{a}–{b} Uhr</td></tr>' for dd, a, b in d["hours"])
    credits = " · ".join(f'<a href="{E(x["src"])}" target="_blank" rel="noopener">{E(x["file"])}</a> ({E(x["lic"].upper())}{", " + E(x["creator"]) if x["creator"] else ""})' for x in cr)
    return f'''<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>{E(d["name"])} · Demo-Konzeptseite · Flow DNA</title>
<meta name="description" content="Demo-Konzeptseite für einen erfundenen Betrieb ({E(d["branche"])}) – gebaut mit dem Landingpage Generator von Flow DNA.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={d["fonts"]}&display=swap">
<style>
:root{{--bg:{c["bg"]};--ink:{c["ink"]};--mute:{c["mute"]};--acc:{c["acc"]};--acc2:{c["acc2"]};--card:{c["card"]};--dark:{c["dark"]};--serif:'{d["serif"]}',Georgia,serif;--sans:'{d["sans"]}',system-ui,sans-serif;--ease:cubic-bezier(.2,.7,.3,1)}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.65 var(--sans);-webkit-font-smoothing:antialiased}}
img{{display:block;max-width:100%}}a{{color:inherit}}.wrap{{max-width:1160px;margin:0 auto;padding:0 22px}}
.demo{{position:fixed;left:0;right:0;top:0;z-index:60;background:var(--dark);color:#fff;text-align:center;font:600 12px var(--sans);letter-spacing:.08em;padding:6px 10px}}
.demo a{{color:var(--acc2)}}
header{{position:fixed;left:0;right:0;top:28px;z-index:50;transition:all .4s var(--ease)}}
header .wrap{{display:flex;align-items:center;justify-content:space-between;height:74px;transition:height .4s var(--ease)}}
header.scrolled{{background:color-mix(in srgb,var(--bg) 78%,transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);box-shadow:0 8px 30px rgba(0,0,0,.06)}}
header.scrolled .wrap{{height:60px}}
.brand{{font:700 24px/1 var(--serif);letter-spacing:.01em;text-decoration:none}}
nav a{{text-decoration:none;font-weight:600;font-size:15px;margin-left:24px;color:var(--mute)}}nav a:hover{{color:var(--ink)}}
@media(max-width:760px){{nav{{display:none}}}}
.btn{{position:relative;overflow:hidden;display:inline-flex;align-items:center;gap:10px;padding:16px 26px;border-radius:999px;background:var(--acc);color:#fff;font:600 16px var(--sans);text-decoration:none;border:0;cursor:pointer;box-shadow:0 14px 30px color-mix(in srgb,var(--acc) 35%,transparent);transition:transform .3s var(--ease)}}
.btn:hover{{transform:translateY(-2px)}}.btn.ghost{{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--ink) 30%,transparent)}}
.btn.small{{padding:12px 20px;font-size:15px;margin-top:12px}}
.sheen::after{{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.45),transparent);animation:sheen 3.6s 1.2s infinite}}
@keyframes sheen{{0%{{left:-60%}}35%,100%{{left:130%}}}}
.hero{{padding:150px 0 70px;overflow:hidden}}
.hero .wrap{{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center}}
@media(max-width:900px){{.hero .wrap{{grid-template-columns:1fr;gap:34px}}.hero{{padding-top:130px}}}}
.kick{{font:600 13px var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin:0 0 14px}}
h1,h2,h3{{font-family:var(--serif);font-weight:600;line-height:1.05;margin:0}}
h1{{font-size:clamp(46px,6.4vw,84px);letter-spacing:-.01em}}h1 em,h2 em{{{script}color:var(--acc);font-weight:500}}
h2{{font-size:clamp(34px,4.4vw,56px);margin-bottom:22px}}
.lead{{font-size:clamp(18px,1.6vw,20px);color:var(--mute);max-width:36ch;margin:22px 0 30px}}
.ctas{{display:flex;gap:12px;flex-wrap:wrap}}
.stage{{position:relative;border-radius:28px;overflow:hidden;aspect-ratio:4/5;box-shadow:0 40px 80px rgba(0,0,0,.18)}}
.stage img{{width:100%;height:100%;object-fit:cover;animation:kenburns 18s var(--ease) infinite alternate}}
@keyframes kenburns{{from{{transform:scale(1.02)}}to{{transform:scale(1.12) translate(-1.5%,-1%)}}}}
.badge{{position:absolute;left:18px;bottom:18px;background:color-mix(in srgb,var(--card) 88%,transparent);backdrop-filter:blur(10px);border-radius:16px;padding:12px 16px;font:600 14px var(--sans)}}
.badge b{{display:block;font:600 22px var(--serif);color:var(--acc)}}
.usps{{list-style:none;margin:0;padding:22px 0;display:flex;flex-wrap:wrap;gap:12px 34px;justify-content:center;border-block:1px solid color-mix(in srgb,var(--ink) 12%,transparent);font-weight:600;color:var(--mute)}}
.usps li::before{{content:"✦";color:var(--acc);margin-right:10px}}
.sec{{padding:96px 0}}.muted{{color:var(--mute)}}
.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}@media(max-width:860px){{.cards{{grid-template-columns:1fr}}}}
.card{{background:var(--card);border-radius:22px;padding:30px;box-shadow:0 1px 0 rgba(0,0,0,.04)}}
.card .no{{font:600 14px var(--sans);color:var(--acc);letter-spacing:.1em}}.card h3{{font-size:28px;margin:12px 0 10px}}.card p{{margin:0;color:var(--mute)}}
.lift{{transition:transform .5s var(--ease),box-shadow .5s var(--ease)}}.lift:hover{{transform:translateY(-6px);box-shadow:0 24px 50px rgba(0,0,0,.10)}}
.menu{{display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:30px}}@media(max-width:760px){{.menu{{grid-template-columns:1fr}}}}
.menu-col h3{{font-size:30px;margin-bottom:14px}}.mi{{display:flex;align-items:baseline;gap:10px;padding:10px 0;border-bottom:1px dashed color-mix(in srgb,var(--ink) 18%,transparent)}}
.mi i{{flex:1}}.mi b{{font-weight:700;color:var(--acc)}}.note{{font-size:14px;color:var(--mute);margin-top:18px}}
.book{{display:grid;grid-template-columns:.9fr 1.1fr;gap:40px;align-items:start}}@media(max-width:860px){{.book{{grid-template-columns:1fr}}}}
.steps{{background:var(--card);border-radius:24px;padding:22px;box-shadow:0 30px 60px rgba(0,0,0,.08)}}
.st{{padding:14px 6px;border-bottom:1px solid color-mix(in srgb,var(--ink) 10%,transparent);opacity:.45;transition:opacity .4s}}.st:last-child{{border:0}}.st.on{{opacity:1}}
.st b{{font:600 14px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--acc)}}
.opts{{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}}.opt{{border:1.5px solid color-mix(in srgb,var(--ink) 20%,transparent);background:transparent;border-radius:999px;padding:10px 14px;font:500 15px var(--sans);cursor:pointer;color:var(--ink)}}
.opt.sel{{background:var(--acc);border-color:var(--acc);color:#fff}}
.row{{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}}.row input,.row select{{flex:1;min-width:140px;padding:12px 14px;border-radius:12px;border:1.5px solid color-mix(in srgb,var(--ink) 18%,transparent);font:400 16px var(--sans);background:var(--bg);color:var(--ink)}}
.ok{{color:var(--acc);font-weight:600;margin:10px 0 0}}
.gal{{display:grid;grid-template-columns:repeat({min(4,len(d["gal"]))},1fr);gap:14px}}@media(max-width:760px){{.gal{{grid-template-columns:1fr 1fr}}}}
.gal figure{{margin:0;border-radius:20px;overflow:hidden;aspect-ratio:1}}.gal img{{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease)}}.gal figure:hover img{{transform:scale(1.06)}}
.quote{{max-width:820px;margin:0 auto;text-align:center}}.quote p{{font:500 clamp(26px,3.2vw,40px)/1.25 var(--serif);margin:0}}.quote span{{display:block;margin-top:16px;color:var(--mute);font-weight:600}}
.band{{position:relative;border-radius:30px;overflow:hidden;margin:0 22px;min-height:360px;display:grid;place-items:center;text-align:center;color:#fff}}
.band img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}.band::before{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.25),rgba(0,0,0,.6));z-index:1}}
.band div{{position:relative;z-index:2;padding:40px 22px}}.band h2{{color:#fff}}
.contact{{display:grid;grid-template-columns:1fr 1fr;gap:30px}}@media(max-width:760px){{.contact{{grid-template-columns:1fr}}}}
table{{width:100%;border-collapse:collapse}}td{{padding:12px 0;border-bottom:1px solid color-mix(in srgb,var(--ink) 10%,transparent)}}td:last-child{{text-align:right;font-weight:600}}
tr.now td{{color:var(--acc)}}.open{{display:inline-block;margin-top:12px;font-weight:700;color:var(--acc)}}
footer{{padding:40px 0 120px;color:var(--mute);font-size:13px}}footer a{{color:var(--mute)}}
.mcta{{position:fixed;left:14px;right:14px;bottom:14px;z-index:55;display:none}}@media(max-width:760px){{.mcta{{display:block}}}}
.mcta .btn{{width:100%;justify-content:center;animation:pulse 2.6s infinite}}@keyframes pulse{{0%,100%{{box-shadow:0 0 0 0 color-mix(in srgb,var(--acc) 45%,transparent)}}70%{{box-shadow:0 0 0 14px transparent}}}}
.reveal{{opacity:0;transform:translateY(26px);transition:opacity .9s var(--ease) var(--d,0ms),transform .9s var(--ease) var(--d,0ms)}}.reveal.in{{opacity:1;transform:none}}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}.reveal{{opacity:1;transform:none}}}}
</style></head><body>
<div class="demo">DEMO · erfundener Betrieb · Konzeptseite gebaut mit dem <a href="../../#">Flow DNA Landingpage Generator</a></div>
<header id="hd"><div class="wrap"><a class="brand" href="#">{E(d["name"])}</a><nav><a href="#leistungen">Leistungen</a><a href="#feature">{"Speisekarte" if d["feature"]=="menu" else "Termin"}</a><a href="#kontakt">Kontakt</a></nav></div></header>
<section class="hero"><div class="wrap"><div><p class="kick reveal">{E(d["kicker"])}</p><h1 class="reveal" style="--d:80ms">{d["h1"]}</h1><p class="lead reveal" style="--d:160ms">{E(d["lead"])}</p>
<div class="ctas reveal" style="--d:240ms"><a class="btn sheen" href="#feature">{E(d["cta"])} →</a><a class="btn ghost" href="#{"feature" if d["feature"]=="menu" else "leistungen"}">{E(d["cta2"])}</a></div></div>
<div class="stage reveal" style="--d:120ms"><img src="img/hero.jpg" alt="{E(d["branche"])}"><div class="badge"><b>{E(d["ort"])}</b>{E(d["branche"])}</div></div></div></section>
<div class="wrap"><ul class="usps">{usps}</ul></div>
<section id="leistungen" class="sec"><div class="wrap"><p class="kick reveal">Leistungen</p><h2 class="reveal">Was wir <em>besonders</em> gut können.</h2><div class="cards">{lst}</div></div></section>
{feat}
<section class="sec" style="padding-top:0"><div class="wrap"><div class="gal">{gal}</div></div></section>
<section class="sec"><div class="wrap quote reveal"><p>„{E(d["quote"][0])}“</p><span>– {E(d["quote"][1])}</span></div></section>
<div class="band reveal"><img src="img/cta.jpg" alt="" loading="lazy"><div><h2>Wir freuen uns <em>auf dich</em>.</h2><a class="btn sheen" href="#feature">{E(d["cta"])} →</a></div></div>
<section id="kontakt" class="sec"><div class="wrap contact"><div class="reveal"><p class="kick">Kontakt</p><h2>So findest du <em>uns</em>.</h2><p class="muted">Musterstraße 1 · 00000 {E(d["ort"])}<br>Telefon: 0000 000000 (Beispiel)<br>E-Mail: hallo@beispiel.de</p></div>
<div class="reveal" style="--d:100ms"><p class="kick">Öffnungszeiten</p><table id="hours">{hours}</table><span class="open" id="open"></span></div></div></section>
<footer><div class="wrap">Demo-Konzeptseite für einen <b>erfundenen</b> Betrieb – alle Namen, Daten und Preise sind Beispiele. Gebaut mit dem Flow DNA Landingpage Generator · Flow Media AI.<br>Fotos (CC0/frei): {credits}</div></footer>
<div class="mcta"><a class="btn" href="#feature">{E(d["cta"])}</a></div>
<script>
const hd=document.getElementById("hd");addEventListener("scroll",()=>hd.classList.toggle("scrolled",scrollY>30),{{passive:true}});
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add("in");io.unobserve(e.target)}}}}),{{threshold:.14}});document.querySelectorAll(".reveal").forEach(el=>io.observe(el));
// Öffnungszeiten: "jetzt geöffnet" (Beispielzeiten)
(function(){{const map={{"Mo":1,"Di":2,"Mi":3,"Do":4,"Fr":5,"Sa":6,"So":0}},now=new Date(),d=now.getDay(),m=now.getHours()*60+now.getMinutes();let open=false;
document.querySelectorAll("#hours tr").forEach(tr=>{{const p=tr.dataset.d.split("–"),a=map[p[0]],b=map[p[1]||p[0]];const inDay=a<=b?(d>=a&&d<=b):(d>=a||d<=b);
const t=s=>{{const[h,mi]=s.split(":").map(Number);return h*60+mi}};if(inDay){{tr.classList.add("now");if(m>=t(tr.dataset.a)&&m<t(tr.dataset.b))open=true}}}});
document.getElementById("open").textContent=open?"● Jetzt geöffnet":"○ Gerade geschlossen";}})();
// Terminbuchung (Demo)
const steps=document.getElementById("steps");if(steps){{const st=n=>steps.querySelectorAll(".st").forEach(s=>s.classList.toggle("on",+s.dataset.s<=n));
steps.querySelectorAll(".opt").forEach(b=>b.onclick=()=>{{steps.querySelectorAll(".opt").forEach(x=>x.classList.remove("sel"));b.classList.add("sel");st(2)}});
document.getElementById("n2").onclick=()=>st(3);document.getElementById("send").onclick=()=>{{document.getElementById("ok").textContent="✓ Demo: In der echten Seite geht jetzt deine Anfrage raus."}}}}
</script></body></html>'''

for k, d in DEMOS.items():
    open(os.path.join(HERE, k, "index.html"), "w", encoding="utf-8").write(page(k, d))
    print(k, os.path.getsize(os.path.join(HERE, k, "index.html")))
