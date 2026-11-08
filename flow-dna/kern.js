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

  // what the main button does for a skill
  function action(s) {
    if (s.stufe === "basis" && s.status === "bereit" && s.quelle) return { label: "Kostenlos laden", href: s.quelle, typ: "laden" };
    if (s.stufe === "basis" && s.status === "vorbereitung") return { label: "Vormerken", href: wa(`Hi Maik, merk mich für den ${s.name} vor (Flow DNA).`), typ: "vormerken" };
    if (s.status === "geplant") return { label: "Will ich haben", href: wa(`Hi Maik, ich hätte gern den Skill „${s.name}“ im Flow-DNA-Store.`), typ: "wunsch" };
    if (s.stufe === "premium") return { label: "Anfragen", href: wa(`Hi Maik, ich interessiere mich für den Premium-Skill „${s.name}“ aus Flow DNA.`), typ: "anfragen" };
    return { label: "Ansehen", href: s.quelle || "#", typ: "laden" };
  }
  const preis = s => s.stufe === "basis" ? "0 €" : s.preise ? `ab ${s.preise.miete} €/Mon.` : (s.preis || "auf Anfrage");
  const optHref = (s, o) => wa(`Hi Maik, ich möchte den Premium-Skill „${s.name}“ aus Flow DNA – Option „${o.name}“ (${s.preise[o.id]} € ${o.einheit}). Wie geht's weiter?`);

  function badges(s) {
    return (s.highlight ? `<span class="dna-b dna-b-hl">★ Signature</span>` : "") + `<span class="dna-b dna-b-${s.stufe}">${esc(D.stufen[s.stufe].name)}</span>` +
      (s.status !== "bereit" ? `<span class="dna-b dna-b-st">${esc(D.status[s.status])}</span>` : "");
  }

  function layer() { let l = document.getElementById("dna-layer"); if (!l) { l = document.createElement("div"); l.id = "dna-layer"; document.body.appendChild(l) } return l }
  function close() { stopStages(); layer().innerHTML = ""; document.body.classList.remove("dna-lock") }

  function openDetail(id) {
    const s = D.skills.find(x => x.id === id); if (!s) return;
    const a = action(s), pk = D.pakete.find(p => p.skills.includes(s.id));
    layer().innerHTML = `<div class="dna-scrim" data-dna-close><div class="dna-modal" role="dialog" aria-modal="true" aria-labelledby="dna-h">
      <button class="dna-x" data-dna-close aria-label="Schließen">×</button>
      ${s.bild ? `<img class="dna-img" src="${esc(s.bild)}" alt="Vorher / Nachher"><p class="dna-vcap">Vorher / Nachher · echtes Beispiel</p>` : s.video ? `<video class="dna-vid" src="${esc(s.video)}.mp4" poster="${esc(s.video)}.jpg" autoplay muted loop playsinline></video><p class="dna-vcap">So läuft's in echt · aus Maiks Projekt</p>` : `<div class="dna-ic">${s.icon}</div>`}
      <div class="dna-badges">${badges(s)}<span class="dna-b">${esc(katName(s.kat))}</span></div>
      <h2 id="dna-h">${esc(s.name)}</h2>
      <p class="dna-kurz">${esc(s.kurz)}</p>
      ${s.ablauf ? `<h3>So funktioniert's</h3>${stage(s.ablauf, s.highlight)}` : ""}
      <h3>Was er kann</h3><ul>${s.kann.map(k => `<li>${esc(k)}</li>`).join("")}</ul>
      <h3>Für wen</h3><p>${esc(s.fuer)}</p>
      ${s.demo ? `<h3>Beispiel aus der Praxis</h3><p>${esc(s.demo)}</p>` : ""}
      <dl class="dna-facts"><div><dt>Kompatibel</dt><dd>Claude Code · Codex</dd></div><div><dt>Version</dt><dd>${esc(s.version || (s.status === "geplant" ? "–" : "in Arbeit"))}</dd></div><div><dt>Creator</dt><dd>${esc(s.creator || D.standardCreator)}</dd></div><div><dt>Status</dt><dd>${esc(D.status[s.status])}</dd></div></dl>
      ${s.herkunft ? `<p class="dna-her">Herkunft: ${esc(s.herkunft)}</p>` : ""}${s.hinweis ? `<p class="dna-pk">${esc(s.hinweis)}</p>` : ""}
      ${pk ? `<p class="dna-pk">Teil vom Paket <b>${esc(pk.name)}</b> – ${esc(pk.kurz)}</p>` : ""}
      ${s.preise ? `<h3>Preise · auf Anfrage</h3><div class="dna-opts">${D.optionen.map(o => `<a class="dna-opt${o.id === "kauf" ? " best" : ""}" href="${esc(optHref(s, o))}" target="_blank" rel="noopener"><b>${esc(o.name)}</b><strong>${s.preise[o.id]} €</strong><em>${esc(o.einheit)}</em><span>${esc(o.text)}</span><i>Anfragen →</i></a>`).join("")}</div>` : ""}
      <div class="dna-foot"><span class="dna-preis">${esc(preis(s))}</span><span class="dna-acts"><button type="button" class="dna-save" data-dna-save="${s.id}">${isSaved(s.id) ? "★ Gemerkt" : "☆ Merken"}</button><a class="dna-btn" href="${esc(a.href)}" target="_blank" rel="noopener">${esc(a.label)}</a></span></div>
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

  window.DNA = { ...D, esc, filter, action, preis, optHref, stage, startStages, badges, katName, openDetail, openSubmit, close, wa, saved, renderExtras };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", renderExtras); else setTimeout(renderExtras);
})();
