// Flow DNA – gemeinsame Logik für alle Varianten (Filter, Suche, Aktionen, Detail- und Einreichen-Fenster)
(function () {
  const D = window.FLOW_DNA;
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const wa = text => `https://wa.me/${D.kontakt.whatsapp}?text=${encodeURIComponent(text)}`;
  const katName = id => (D.kategorien.find(k => k.id === id) || {}).name || "";

  function filter({ stufe = "alle", kat = "alle", q = "" } = {}) {
    const n = q.trim().toLowerCase();
    return D.skills.filter(s => (stufe === "alle" || s.stufe === stufe) && (kat === "alle" || s.kat === kat) &&
      (!n || [s.name, s.kurz, s.fuer, ...(s.kann || [])].join(" ").toLowerCase().includes(n)))
      .sort((a, b) => ORDER[a.status] - ORDER[b.status] || (b.flagship ? 1 : 0) - (a.flagship ? 1 : 0));
  }
  const ORDER = { bereit: 0, vorbereitung: 1, geplant: 2 };
  // "Meine Skills": gemerkte Skills im Browser (bis es Konten gibt)
  const LS = "flow-dna-merkliste";
  const saved = () => { try { return JSON.parse(localStorage.getItem(LS) || "[]") } catch { return [] } };
  const isSaved = id => saved().includes(id);
  function toggleSave(id) { const l = saved(), i = l.indexOf(id); i < 0 ? l.push(id) : l.splice(i, 1); try { localStorage.setItem(LS, JSON.stringify(l)) } catch {} renderExtras() }

  // Direkt nutzen: Skill-Link als Prompt in Claude oder ChatGPT/Codex öffnen
  const BASE = "https://maikz91.github.io/flow-media-ai/flow-dna/";
  const usePrompt = (url, name) => `Nutze den Skill „${name}“ aus dem Flow DNA Store: ${url}\nLies die Anleitung unter dem Link vollständig und arbeite danach mit mir. Starte mit dem ersten Schritt.`;
  function useBox(url, name) {
    const q = encodeURIComponent(usePrompt(url, name));
    return `<div class="dna-use"><b>Direkt nutzen</b><div><a class="dna-u claude" href="https://claude.ai/new?q=${q}" target="_blank" rel="noopener">In Claude öffnen</a><a class="dna-u gpt" href="https://chatgpt.com/?q=${q}" target="_blank" rel="noopener">In ChatGPT / Codex öffnen</a><button type="button" class="dna-u" data-copy="${esc(usePrompt(url, name))}">Prompt kopieren</button></div><small>Für Claude Code oder Codex: Prompt kopieren und im Projektordner einfügen – oder ZIP laden und in den Ordner skills legen.</small></div>`;
  }
  document.addEventListener("click", e => { const b = e.target.closest("[data-copy]"); if (!b) return; navigator.clipboard && navigator.clipboard.writeText(b.dataset.copy).then(() => { const t = b.textContent; b.textContent = "✓ Kopiert"; setTimeout(() => b.textContent = t, 1600) }) });
  // what the main button does for a skill
  function action(s) {
    if (s.stufe === "basis" && s.status === "bereit" && s.quelle) return { label: s.quelle.endsWith(".zip") ? "⬇ Kostenlos herunterladen" : "Kostenlos laden", href: s.quelle, typ: "laden" };
    if (s.stufe === "basis" && s.status === "vorbereitung") return { label: "Vormerken", href: wa(`Hi Maik, merk mich für den ${s.name} vor (Flow DNA).`), typ: "vormerken" };
    if (s.status === "geplant") return { label: "Will ich haben", href: wa(`Hi Maik, ich hätte gern den Skill „${s.name}“ im Flow-DNA-Store.`), typ: "wunsch" };
    if (s.stufe === "premium") return { label: "Anfragen", href: wa(`Hi Maik, ich interessiere mich für den Premium-Skill „${s.name}“ aus Flow DNA.`), typ: "anfragen" };
    return { label: "Ansehen", href: s.quelle || "#", typ: "laden" };
  }
  // Preis je Anzahl Versionen (Website Builder, App Builder, Website Transformer)
  const vRound = v => v < 30 ? Math.round(v) : Math.round(v / 10) * 10 - 1;
  const vp = (s, oid, n) => s.versionen && D.versionen ? vRound(s.preise[oid] * (D.versionen.faktor[n] || 1)) : s.preise[oid];
  const verOf = {};  // gewählte Versionen je Skill im Detail-Fenster
  const preis = s => s.stufe === "basis" ? "0 €" : s.preise ? `ab ${s.versionen ? vp(s, "miete", 1) : s.preise.miete} €/Mon.` : (s.preis || "auf Anfrage");
  // Warenkorb (nur Anfrage – Bezahlung nach Rückmeldung von Maik)
  const cartGet = () => { try { return JSON.parse(localStorage.getItem("dna-cart") || "[]") } catch (e) { return [] } };
  const cartSet = c => { try { localStorage.setItem("dna-cart", JSON.stringify(c)) } catch (e) { } document.dispatchEvent(new Event("dna-cart")) };
  const PAKET = { id: "paket-alles", icon: "🎓", name: "Alle Kurse + alle Skills", preis: 199, text: "Alle Online-Kurse und alle Skills aus dem Flow DNA Store – einmal zahlen." };
  const cartLine = it => { if (it.sid === PAKET.id) return { s: PAKET, o: { id: "kauf", name: "Komplettpaket", einheit: "einmalig" }, n: 0, p: PAKET.preis }; const s = D.skills.find(x => x.id === it.sid), o = D.optionen.find(x => x.id === it.oid); return s && o ? { s, o, n: it.n, p: vp(s, o.id, it.n) } : null };
  function cartAdd(sid, oid, n) { const c = cartGet().filter(x => x.sid !== sid); c.push({ sid, oid, n: n || 0 }); cartSet(c) }
  function openCart() {
    const L = cartGet().map(cartLine).filter(Boolean);
    const once = L.filter(x => x.o.id !== "miete").reduce((a, x) => a + x.p, 0), month = L.filter(x => x.o.id === "miete").reduce((a, x) => a + x.p, 0);
    const msg = `Hi Maik, ich möchte diese Skills aus Flow DNA:\n` + L.map(x => `• ${x.s.name}${x.n ? ` (${x.n} ${x.n === 1 ? "Version" : "Versionen"})` : ""} – ${x.o.name}: ${x.p} € ${x.o.einheit}`).join("\n") + `\n\nSumme: ${once ? once + " € einmalig" : ""}${once && month ? " + " : ""}${month ? month + " €/Monat" : ""}. Wie geht's weiter?`;
    layer().innerHTML = `<div class="dna-scrim" data-dna-close><div class="dna-modal" role="dialog" aria-modal="true" aria-labelledby="dna-cart-h"><button class="dna-x" data-dna-close aria-label="Schließen">×</button>
      <h2 id="dna-cart-h">Warenkorb</h2>${L.length ? `<div class="dna-cart">${L.map(x => `<div class="dna-ci"><div><b>${esc(x.s.icon || "")} ${esc(x.s.name)}</b><small>${x.n ? `${x.n} ${x.n === 1 ? "Version" : "Versionen"} · ` : ""}${esc(x.o.name)}</small></div><strong>${x.p} €<em>${esc(x.o.einheit)}</em></strong><button type="button" data-cart-del="${esc(x.s.id)}" aria-label="Entfernen">×</button></div>`).join("")}</div>
      <div class="dna-sum">${once ? `<div><span>Einmalig</span><b>${once} €</b></div>` : ""}${month ? `<div><span>Monatlich</span><b>${month} €</b></div>` : ""}</div>
      <button type="button" class="dna-btn" style="width:100%;margin-top:14px" data-checkout>Zur Kasse →</button><p class="dna-her">Bezahlt wird per Rechnung – du bekommst sie zusammen mit deinem Code von Maik. <button type="button" class="dna-clear" data-cart-clear>Warenkorb leeren</button></p>`
      : `<p class="dna-kurz" style="margin-top:10px">Noch leer. Öffne einen Premium-Skill und leg eine Option in den Warenkorb.</p>`}</div></div>`;
    document.body.classList.add("dna-lock");
  }
  // Kommentare zu Kursen und Skills: gehen direkt in die Datenbank (Tabelle flow_dna_feedback, anonym nur Einfügen)
  const SB = "https://ykleosfvtqcmqxqihnod.supabase.co", SBK = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlrbGVvc2Z2dHFjbXF4cWlobm9kIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDA5MzQ0NjIsImV4cCI6MjA1NjUxMDQ2Mn0.70wsZ-c7poYFnbTyXbKrG0b6YPSe-BonMN6kjZ2a2Wo";
  const fbBox = (kind, ref, stelle, titel) => `<form class="dna-fb" data-fb="${esc(kind)}|${esc(ref)}|${esc(stelle || "")}"><b>${esc(titel || "Dein Kommentar")}</b><span>Etwas unklar, falsch oder fehlt etwas? Schreib es hier – Maik liest jeden Kommentar und verbessert damit ${kind === "kurs" ? "den Kurs" : "den Skill"}.</span>
    <textarea name="text" rows="3" maxlength="2000" required minlength="3" placeholder="Was ist dir aufgefallen?"></textarea><input name="name" maxlength="80" placeholder="Name (optional)" autocomplete="name"><input name="web" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0">
    <button type="submit">Kommentar senden</button><p class="dna-fbmsg">Wird gespeichert, damit Maik ihn lesen kann. Bitte keine Passwörter oder Kundendaten.</p></form>`;
  document.addEventListener("submit", async e => {
    const f = e.target.closest("[data-fb]"); if (!f) return; e.preventDefault();
    const [kind, ref, stelle] = f.dataset.fb.split("|"), m = f.querySelector(".dna-fbmsg"), btn = f.querySelector("button"), text = f.text.value.trim();
    if (f.web.value) return; if (text.length < 3) { m.textContent = "Bitte schreib kurz, was dir aufgefallen ist."; return }
    btn.disabled = true; m.textContent = "Sende …";
    try {
      const r = await fetch(SB + "/rest/v1/flow_dna_feedback", { method: "POST", headers: { "content-type": "application/json", apikey: SBK, Authorization: "Bearer " + SBK, Prefer: "return=minimal" }, body: JSON.stringify({ kind, ref, stelle: stelle || null, text, name: f.name.value.trim() || null }) });
      if (!r.ok) throw new Error(r.status);
      f.text.value = ""; m.textContent = "✓ Danke! Dein Kommentar ist bei Maik angekommen."; m.classList.add("ok");
    } catch (err) { m.textContent = "Das hat nicht geklappt – bitte nochmal versuchen."; }
    btn.disabled = false;
  });
  // Kasse: Daten für die Rechnung, Bestellung geht per WhatsApp an Maik (kein Online-Bezahlen, nichts wird gespeichert)
  function openCheckout() {
    const L = cartGet().map(cartLine).filter(Boolean); if (!L.length) return openCart();
    const once = L.filter(x => x.o.id !== "miete").reduce((a, x) => a + x.p, 0), month = L.filter(x => x.o.id === "miete").reduce((a, x) => a + x.p, 0);
    layer().innerHTML = `<div class="dna-scrim" data-dna-close><div class="dna-modal" role="dialog" aria-modal="true" aria-labelledby="dna-co-h"><button class="dna-x" data-dna-close aria-label="Schließen">×</button>
      <h2 id="dna-co-h">Kasse</h2><div class="dna-steps3"><span class="on">1 Warenkorb</span><span class="on">2 Deine Daten</span><span>3 Rechnung &amp; Code</span></div>
      <div class="dna-cart">${L.map(x => `<div class="dna-ci"><div><b>${esc(x.s.icon || "")} ${esc(x.s.name)}</b><small>${esc(x.o.name)}</small></div><strong>${x.p} €<em>${esc(x.o.einheit)}</em></strong></div>`).join("")}</div>
      <div class="dna-sum">${once ? `<div><span>Einmalig</span><b>${once} €</b></div>` : ""}${month ? `<div><span>Monatlich</span><b>${month} €</b></div>` : ""}</div>
      <form class="dna-co" data-checkout-form><label>Name<input name="name" required autocomplete="name"></label><label>E-Mail für Rechnung und Code<input name="mail" type="email" required autocomplete="email"></label><label>Rechnungsadresse <i>(optional)</i><textarea name="adr" rows="2" autocomplete="street-address"></textarea></label>
      <button type="submit" class="dna-btn" style="width:100%">Bestellung an Maik senden →</button></form>
      <p class="dna-her">So geht’s weiter: Deine Bestellung öffnet sich als WhatsApp-Nachricht an Maik. Du bekommst die Rechnung und nach Zahlung deinen Freischalt-Code. Deine Daten werden hier nicht gespeichert. <button type="button" class="dna-clear" data-cart-open>← Zurück zum Warenkorb</button></p></div></div>`;
    document.body.classList.add("dna-lock");
  }
  document.addEventListener("submit", e => {
    const f = e.target.closest("[data-checkout-form]"); if (!f) return; e.preventDefault();
    const L = cartGet().map(cartLine).filter(Boolean);
    const once = L.filter(x => x.o.id !== "miete").reduce((a, x) => a + x.p, 0), month = L.filter(x => x.o.id === "miete").reduce((a, x) => a + x.p, 0);
    const msg = `Hi Maik, ich bestelle aus Flow DNA:\n` + L.map(x => `• ${x.s.name}${x.n ? ` (${x.n} ${x.n === 1 ? "Version" : "Versionen"})` : ""} – ${x.o.name}: ${x.p} € ${x.o.einheit}`).join("\n") + `\n\nSumme: ${once ? once + " € einmalig" : ""}${once && month ? " + " : ""}${month ? month + " €/Monat" : ""}\n\nName: ${f.name.value.trim()}\nE-Mail: ${f.mail.value.trim()}${f.adr.value.trim() ? "\nRechnungsadresse: " + f.adr.value.trim().replace(/\n/g, ", ") : ""}\n\nBitte schick mir Rechnung und Code.`;
    window.open(wa(msg), "_blank", "noopener");
    layer().querySelector(".dna-modal").innerHTML = `<button class="dna-x" data-dna-close aria-label="Schließen">×</button><h2>Fast geschafft</h2><p class="dna-kurz" style="margin-top:10px">WhatsApp hat sich mit deiner Bestellung geöffnet – <b>bitte dort auf Senden tippen</b>. Maik schickt dir die Rechnung und nach Zahlung deinen Code. Den gibst du unter „Kurse“ ein.</p><a class="dna-btn" style="width:100%;margin-top:14px" href="${esc(wa(msg))}" target="_blank" rel="noopener">WhatsApp nochmal öffnen</a>`;
  });
  document.addEventListener("click", e => {
    if (e.target.closest("[data-checkout]")) { openCheckout(); return }
    const v = e.target.closest("[data-ver]"); if (v) { const [sid, n] = v.dataset.ver.split("|"); verOf[sid] = +n; openDetail(sid); return }
    const a = e.target.closest("[data-cart-add]"); if (a) { const [sid, oid, n] = a.dataset.cartAdd.split("|"); cartAdd(sid, oid, +n); openCart(); return }
    const d = e.target.closest("[data-cart-del]"); if (d) { cartSet(cartGet().filter(x => x.sid !== d.dataset.cartDel)); openCart(); return }
    if (e.target.closest("[data-cart-clear]")) { cartSet([]); openCart(); return }
    if (e.target.closest("[data-cart-open]")) openCart();
  });
  const optHref = (s, o) => wa(`Hi Maik, ich möchte den Premium-Skill „${s.name}“ aus Flow DNA – Option „${o.name}“ (${s.preise[o.id]} € ${o.einheit}). Wie geht's weiter?`);

  function badges(s) {
    return (s.highlight ? `<span class="dna-b dna-b-hl">★ Signature</span>` : "") + `<span class="dna-b dna-b-${s.stufe}">${esc(D.stufen[s.stufe].name)}</span>` +
      (s.status !== "bereit" ? `<span class="dna-b dna-b-st">${esc(D.status[s.status])}</span>` : "");
  }

  function layer() { let l = document.getElementById("dna-layer"); if (!l) { l = document.createElement("div"); l.id = "dna-layer"; document.body.appendChild(l) } return l }
  function close() { stopStages(); layer().innerHTML = ""; document.body.classList.remove("dna-lock") }

  function openDetail(id) {
    if (id === "lead-seiten") id = "website-transformer";  // Landingpage Generator ist im Website Transformer aufgegangen
    const s = D.skills.find(x => x.id === id); if (!s) return;
    const a = action(s), pk = D.pakete.find(p => p.skills.includes(s.id));
    layer().innerHTML = `<div class="dna-scrim" data-dna-close><div class="dna-modal" role="dialog" aria-modal="true" aria-labelledby="dna-h">
      <button class="dna-x" data-dna-close aria-label="Schließen">×</button>
      ${s.bild ? `<img class="dna-img" src="${esc(s.bild)}" alt="Vorher / Nachher"><p class="dna-vcap">Vorher / Nachher · echtes Beispiel</p>` : s.video ? `<video class="dna-vid" src="${esc(s.video)}.mp4" poster="${esc(s.video)}.jpg" autoplay muted loop playsinline></video><p class="dna-vcap">So läuft's in echt · aus Maiks Projekt</p>` : `<div class="dna-ic">${s.icon}</div>`}
      <div class="dna-badges">${badges(s)}<span class="dna-b">${esc(katName(s.kat))}</span></div>
      <h2 id="dna-h">${esc(s.name)}</h2>
      <p class="dna-kurz">${esc(s.kurz)}</p>
      ${s.ablauf ? `<h3>So funktioniert's</h3>${stage(s.ablauf, s.highlight)}` : ""}
      ${D.beispiele && D.beispiele.skills.includes(s.id) ? `<h3>Beispielseiten</h3><div class="dna-bsp">${D.beispiele.seiten.map(b => `<a href="${esc(b.url)}" target="_blank" rel="noopener"><img src="${esc(b.bild)}" alt="${esc(b.name)}" loading="lazy"><b>${esc(b.name)}</b><span>${esc(b.art)}</span></a>`).join("")}</div><p class="dna-vcap" style="margin-top:6px!important">Betriebe frei erfunden · Flow Media AI ist echt</p>` : ""}
      <h3>Was er kann</h3><ul>${s.kann.map(k => `<li>${esc(k)}</li>`).join("")}</ul>
      <h3>Für wen</h3><p>${esc(s.fuer)}</p>
      ${s.demo ? `<h3>Beispiel aus der Praxis</h3><p>${esc(s.demo)}</p>` : ""}
      <dl class="dna-facts"><div><dt>Kompatibel</dt><dd>Claude Code · Codex</dd></div><div><dt>Version</dt><dd>${esc(s.version || (s.status === "geplant" ? "–" : "in Arbeit"))}</dd></div><div><dt>Creator</dt><dd>${esc(s.creator || D.standardCreator)}</dd></div><div><dt>Status</dt><dd>${esc(D.status[s.status])}</dd></div></dl>
      ${s.herkunft ? `<p class="dna-her">Herkunft: ${esc(s.herkunft)}</p>` : ""}${s.hinweis ? `<p class="dna-pk">${esc(s.hinweis)}</p>` : ""}
      ${pk ? `<p class="dna-pk">Teil vom Paket <b>${esc(pk.name)}</b> – ${esc(pk.kurz)}</p>` : ""}
      ${s.preise ? (() => { const n = s.versionen ? (verOf[s.id] || 5) : 0;
        return `${s.versionen ? `<h3>Wie viele Versionen?</h3><p class="dna-vtxt">${esc(D.versionen.text)}</p><div class="dna-ver">${D.versionen.optionen.map(k => `<button type="button" data-ver="${esc(s.id)}|${k}" class="${k === n ? "on" : ""}"><b>${k}</b>${k === 1 ? "Version" : "Versionen"}</button>`).join("")}</div>` : ""}
        <h3>Preise${n ? ` · ${n} ${n === 1 ? "Version" : "Versionen"}` : ""}</h3><div class="dna-opts">${D.optionen.map(o => `<button type="button" class="dna-opt${o.id === "kauf" ? " best" : ""}" data-cart-add="${esc(s.id)}|${o.id}|${n}"><b>${esc(o.name)}</b><strong>${vp(s, o.id, n || 5)} €</strong><em>${esc(o.einheit)}</em><span>${esc(o.text)}</span><i>In den Warenkorb +</i></button>`).join("")}</div>
        <p class="dna-her"><a href="${esc(optHref(s, D.optionen[1]))}" target="_blank" rel="noopener" style="color:inherit">Oder direkt per WhatsApp fragen</a></p>` })() : ""}
      ${s.stufe === "basis" && s.quelle && s.quelle.endsWith(".zip") ? useBox(BASE + "skills/" + s.id + "/SKILL.md", s.name) : ""}
      ${s.stufe === "premium" ? `<form class="dna-redeem" data-redeem><label>Schon gekauft? Lizenz-Code einlösen</label><div><input name="code" placeholder="CODE-XXXX-XXXX" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-label="Lizenz-Code"><button type="submit">⬇ Laden</button></div><p class="dna-rmsg"></p></form>` : ""}
      ${fbBox("skill", s.id, "", "Auffälligkeit oder Idee zu diesem Skill?")}
      <div class="dna-foot"><span class="dna-preis">${esc(preis(s))}</span><span class="dna-acts"><button type="button" class="dna-save" data-dna-save="${s.id}">${isSaved(s.id) ? "★ Gemerkt" : "☆ Merken"}</button><a class="dna-btn" href="${esc(a.href)}"${a.href.startsWith("#") ? " data-dna-close" : a.href.endsWith(".zip") ? " download" : ' target="_blank" rel="noopener"'}>${esc(a.label)}</a></span></div>
    </div></div>`;
    document.body.classList.add("dna-lock");
    startStages(layer());
  }

  // Ablauf-Animation: Schritte leuchten nacheinander auf, ein Impuls läuft durch, am Ende "fertig"
  function stage(steps, hl) {
    return `<div class="dna-stage${hl ? " hl" : ""}" data-n="${steps.length}"><div class="dna-track"><i></i></div>${steps.map(([ic, t], i) => `<div class="dna-step" style="--i:${i}"><span class="dna-dot">${ic}</span><span class="dna-lbl">${esc(t)}</span></div>`).join("")}</div>`;
  }
  let timers = [];
  function startStages(root) {
    root.querySelectorAll(".dna-stage").forEach(st => {
      const n = +st.dataset.n, steps = [...st.querySelectorAll(".dna-step")], bar = st.querySelector(".dna-track i"); let k = 0;
      const tick = () => { steps.forEach((el, i) => { el.classList.toggle("on", i <= k); el.classList.toggle("now", i === k) }); bar.style.width = (n > 1 ? (Math.min(k, n - 1) / (n - 1)) * 100 : 100) + "%"; st.classList.toggle("done", k >= n - 1); k = k >= n - 1 + 2 ? 0 : k + 1; if (k > n - 1) { steps.forEach(el => el.classList.remove("now")) } };
      tick(); timers.push(setInterval(tick, 750));
    });
  }
  function stopStages() { timers.forEach(clearInterval); timers = [] }

  function openSubmit() {
    layer().innerHTML = `<div class="dna-scrim" data-dna-close><form class="dna-modal" id="dna-submit" role="dialog" aria-modal="true" aria-labelledby="dna-sh">
      <button type="button" class="dna-x" data-dna-close aria-label="Schließen">×</button>
      <div class="dna-ic">➕</div>
      <h2 id="dna-sh">Skill verkaufen oder teilen</h2>
      <p class="dna-kurz">Verwandle dein Wissen in einen Skill. Reich ihn ein – er wird geprüft und für die Community freigeschaltet. Kostenlos oder mit deinem eigenen Preis.</p>
      <label>Name des Skills<input name="name" required maxlength="60" placeholder="z. B. Terminbuchung für Praxen"></label>
      <label>Was macht er? (1–2 Sätze)<textarea name="was" required maxlength="400" rows="3"></textarea></label>
      <label>Kategorie<select name="kat">${D.kategorien.map(k => `<option>${esc(k.name)}</option>`).join("")}</select></label>
      <label>Preis<select name="preis"><option>Kostenlos</option><option>Festpreis</option></select></label>
      <label>Wunschpreis in € (bei Festpreis)<input name="betrag" inputmode="decimal" maxlength="10" placeholder="z. B. 29"></label>
      <label>Dein Name / Creator-Name<input name="von" required maxlength="60"></label>
      <div class="dna-foot"><span class="dna-preis">Community</span><button class="dna-btn" type="submit">Per WhatsApp senden</button></div>
    </form></div>`;
    document.body.classList.add("dna-lock");
    document.getElementById("dna-submit").addEventListener("submit", e => {
      e.preventDefault(); const f = new FormData(e.target);
      window.open(wa(`Hi Maik, ich möchte einen Skill für Flow DNA einreichen:\n• Name: ${f.get("name")}\n• Was er macht: ${f.get("was")}\n• Kategorie: ${f.get("kat")}\n• Preis: ${f.get("preis")}${f.get("preis") === "Festpreis" && f.get("betrag") ? " " + f.get("betrag") + " €" : ""}\n• Creator: ${f.get("von")}`), "_blank", "noopener");
      close();
    });
  }

  // Zusatz-Bereiche (Meine Skills, Skill-Paket, Roadmap, Creator, Claim) – erscheinen in #dna-extra, wenn die Variante es hat
  function renderExtras() {
    const el = document.getElementById("dna-extra"); if (!el) return;
    const mine = saved().map(id => D.skills.find(s => s.id === id)).filter(Boolean), M = D.marke;
    el.innerHTML = `<section class="dna-x-sec"><h2 class="dna-x-h">Meine Skills</h2>${mine.length ? `<div class="dna-x-mine">${mine.map(s => `<button type="button" data-skill="${s.id}">${s.icon} ${esc(s.name)}</button>`).join("")}</div>` : `<p class="dna-x-p">Noch nichts gemerkt. Tipp einen Skill an und drück „Merken“ – mit Konto später auch deine gekauften Skills.</p>`}</section>
    <section class="dna-x-sec"><h2 class="dna-x-h">Was steckt in einem Skill-Paket?</h2><p class="dna-x-p">Kein loser Prompt, sondern ein Standard-Paket – übertragbar und wiederverwendbar.</p><div class="dna-x-grid">${D.paketAufbau.map(([t, d], i) => `<div class="dna-x-card"><b>${String(i + 1).padStart(2, "0")} · ${esc(t)}</b><span>${esc(d)}</span></div>`).join("")}</div></section>
    <section class="dna-x-sec"><h2 class="dna-x-h">Jeder kann Creator werden</h2><p class="dna-x-p">Coaches, Fotografinnen, Social-Media-Manager, Entwickler, Unternehmer: Verwandle dein Wissen in einen Skill und biete ihn kostenlos oder zu deinem Preis an. Flow Media AI stellt Plattform, Prüfung und Community.</p>
      <div class="dna-x-creator"><img src="img/maik_avatar.jpg" alt=""><div><b>Maik · Flow Media AI</b><span>Erster Creator im Store · baut Skills aus echten Projekten</span></div></div><p style="margin-top:14px"><button class="dna-btn" data-submit>Skill einreichen</button></p></section>
    <section class="dna-x-sec"><h2 class="dna-x-h">Roadmap</h2><div class="dna-x-grid">${D.phasen.map(p => `<div class="dna-x-card${p.jetzt ? " now" : ""}"><b>${esc(p.name)}${p.jetzt ? " · jetzt" : ""}</b>${p.punkte.map(x => `<span>· ${esc(x)}</span>`).join("")}</div>`).join("")}</div></section>
    <section class="dna-x-sec dna-x-end"><div class="dna-x-big">${esc(M.schluss)}</div><p class="dna-x-p">${esc(M.schlussUnter)}</p><p class="dna-x-pw">Powered by Flow Media AI</p></section>`;
  }

  document.addEventListener("click", e => {
    const sv = e.target.closest("[data-dna-save]"); if (sv) { toggleSave(sv.dataset.dnaSave); sv.textContent = isSaved(sv.dataset.dnaSave) ? "★ Gemerkt" : "☆ Merken"; return }
    if (e.target.closest("[data-dna-close]") && (e.target.matches("[data-dna-close]"))) { close(); return }
    const d = e.target.closest("[data-skill]"); if (d && !e.target.closest("a[href]")) { openDetail(d.dataset.skill); return }
    if (e.target.closest("[data-submit]")) openSubmit();
  });
  document.addEventListener("keydown", e => { if (e.key === "Escape") close() });
  // Lizenz-Code einlösen (Supabase Edge Function flow-dna): lädt den persönlichen Lade-Skill als SKILL.md
  const LIC = "https://ykleosfvtqcmqxqihnod.supabase.co/functions/v1/flow-dna";
  document.addEventListener("submit", async e => {
    const f = e.target.closest("[data-redeem]"); if (!f) return; e.preventDefault();
    const msg = f.querySelector(".dna-rmsg"), btn = f.querySelector("button"), code = f.code.value.trim(); if (!code) return;
    btn.disabled = true; msg.className = "dna-rmsg"; msg.textContent = "…";
    try {
      const res = await fetch(LIC + "/claim", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ code }) }); const d = await res.json();
      if (!d.ok) { msg.className = "dna-rmsg err"; msg.textContent = d.error || "Code ungültig."; btn.disabled = false; return }
      const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([d.content], { type: "text/markdown" })); a.download = "SKILL.md"; document.body.appendChild(a); a.click(); a.remove();
      msg.className = "dna-rmsg ok"; msg.innerHTML = `✓ <b>${esc(d.name)}</b> geladen. Leg die Datei als <b>SKILL.md</b> in den Ordner <b>skills/${esc(d.folder)}</b> deines Projekts.` + (d.unbefristet ? "" : ` Gültig bis ${new Date(d.valid_until).toLocaleDateString("de-DE", { timeZone: "Europe/Berlin" })}.`) + useBox(LIC + "/skill?code=" + encodeURIComponent(code), d.name);
      btn.disabled = false;
    } catch (err) { msg.className = "dna-rmsg err"; msg.textContent = "Keine Verbindung – bitte nochmal versuchen."; btn.disabled = false }
  });

  window.DNA = { ...D, esc, filter, action, preis, optHref, stage, startStages, badges, katName, openDetail, openSubmit, close, wa, saved, renderExtras, useBox, BASE, openCart, cartGet, cartAdd, PAKET, vp, fbBox };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", renderExtras); else setTimeout(renderExtras);
})();
