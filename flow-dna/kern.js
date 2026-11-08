// Flow DNA – gemeinsame Logik für alle Varianten (Filter, Suche, Aktionen, Detail- und Einreichen-Fenster)
(function () {
  const D = window.FLOW_DNA;
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const wa = text => `https://wa.me/${D.kontakt.whatsapp}?text=${encodeURIComponent(text)}`;
  const katName = id => (D.kategorien.find(k => k.id === id) || {}).name || "";

  function filter({ stufe = "alle", kat = "alle", q = "" } = {}) {
    const n = q.trim().toLowerCase();
    return D.skills.filter(s => (stufe === "alle" || s.stufe === stufe) && (kat === "alle" || s.kat === kat) &&
      (!n || [s.name, s.kurz, s.fuer, ...(s.kann || [])].join(" ").toLowerCase().includes(n)));
  }

  // what the main button does for a skill
  function action(s) {
    if (s.stufe === "basis" && s.status === "bereit" && s.quelle) return { label: "Kostenlos laden", href: s.quelle, typ: "laden" };
    if (s.stufe === "basis" && s.status === "vorbereitung") return { label: "Vormerken", href: wa(`Hi Maik, merk mich für den ${s.name} vor (Flow DNA).`), typ: "vormerken" };
    if (s.status === "geplant") return { label: "Will ich haben", href: wa(`Hi Maik, ich hätte gern den Skill „${s.name}“ im Flow-DNA-Store.`), typ: "wunsch" };
    if (s.stufe === "premium") return { label: "Kaufen oder mieten", href: wa(`Hi Maik, ich interessiere mich für den Premium-Skill „${s.name}“ (Flow DNA). Kaufen oder mieten – was kostet er?`), typ: "anfragen" };
    return { label: "Ansehen", href: s.quelle || "#", typ: "laden" };
  }
  const preis = s => s.stufe === "basis" ? "Kostenlos" : s.stufe === "premium" ? "Preis folgt" : (s.preis || "Kostenlos");

  function badges(s) {
    return `<span class="dna-b dna-b-${s.stufe}">${esc(D.stufen[s.stufe].name)}</span>` +
      (s.status !== "bereit" ? `<span class="dna-b dna-b-st">${esc(D.status[s.status])}</span>` : "");
  }

  function layer() { let l = document.getElementById("dna-layer"); if (!l) { l = document.createElement("div"); l.id = "dna-layer"; document.body.appendChild(l) } return l }
  function close() { layer().innerHTML = ""; document.body.classList.remove("dna-lock") }

  function openDetail(id) {
    const s = D.skills.find(x => x.id === id); if (!s) return;
    const a = action(s), pk = D.pakete.find(p => p.skills.includes(s.id));
    layer().innerHTML = `<div class="dna-scrim" data-dna-close><div class="dna-modal" role="dialog" aria-modal="true" aria-labelledby="dna-h">
      <button class="dna-x" data-dna-close aria-label="Schließen">×</button>
      <div class="dna-ic">${s.icon}</div>
      <div class="dna-badges">${badges(s)}<span class="dna-b">${esc(katName(s.kat))}</span></div>
      <h2 id="dna-h">${esc(s.name)}</h2>
      <p class="dna-kurz">${esc(s.kurz)}</p>
      <h3>Was er kann</h3><ul>${s.kann.map(k => `<li>${esc(k)}</li>`).join("")}</ul>
      <h3>Für wen</h3><p>${esc(s.fuer)}</p>
      <p class="dna-her">Herkunft: ${esc(s.herkunft)} · läuft mit Claude Code und Codex</p>
      ${pk ? `<p class="dna-pk">Teil vom Paket <b>${esc(pk.name)}</b> – ${esc(pk.kurz)}</p>` : ""}
      <div class="dna-foot"><span class="dna-preis">${esc(preis(s))}</span><a class="dna-btn" href="${esc(a.href)}" target="_blank" rel="noopener">${esc(a.label)}</a></div>
    </div></div>`;
    document.body.classList.add("dna-lock");
  }

  function openSubmit() {
    layer().innerHTML = `<div class="dna-scrim" data-dna-close><form class="dna-modal" id="dna-submit" role="dialog" aria-modal="true" aria-labelledby="dna-sh">
      <button type="button" class="dna-x" data-dna-close aria-label="Schließen">×</button>
      <div class="dna-ic">➕</div>
      <h2 id="dna-sh">Skill einreichen</h2>
      <p class="dna-kurz">Du hast einen Skill gebaut, der anderen hilft? Reich ihn ein – ich prüfe ihn und schalte ihn für die Community frei. Zum Start sind Community-Skills kostenlos.</p>
      <label>Name des Skills<input name="name" required maxlength="60" placeholder="z. B. Terminbuchung für Praxen"></label>
      <label>Was macht er? (1–2 Sätze)<textarea name="was" required maxlength="400" rows="3"></textarea></label>
      <label>Kategorie<select name="kat">${D.kategorien.map(k => `<option>${esc(k.name)}</option>`).join("")}</select></label>
      <label>Dein Name<input name="von" required maxlength="60"></label>
      <div class="dna-foot"><span class="dna-preis">Kostenlos teilen</span><button class="dna-btn" type="submit">Per WhatsApp senden</button></div>
    </form></div>`;
    document.body.classList.add("dna-lock");
    document.getElementById("dna-submit").addEventListener("submit", e => {
      e.preventDefault(); const f = new FormData(e.target);
      window.open(wa(`Hi Maik, ich möchte einen Skill für Flow DNA einreichen:\n• Name: ${f.get("name")}\n• Was er macht: ${f.get("was")}\n• Kategorie: ${f.get("kat")}\n• Von: ${f.get("von")}`), "_blank", "noopener");
      close();
    });
  }

  document.addEventListener("click", e => {
    if (e.target.closest("[data-dna-close]") && (e.target.matches("[data-dna-close]"))) { close(); return }
    const d = e.target.closest("[data-skill]"); if (d && !e.target.closest("a[href]")) { openDetail(d.dataset.skill); return }
    if (e.target.closest("[data-submit]")) openSubmit();
  });
  document.addEventListener("keydown", e => { if (e.key === "Escape") close() });

  window.DNA = { ...D, esc, filter, action, preis, badges, katName, openDetail, openSubmit, close, wa };
})();
