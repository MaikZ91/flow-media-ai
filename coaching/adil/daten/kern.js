/* Gemeinsamer Kern für alle App-Versionen: Daten-Helfer, Favoriten, Wach-Modus, Sprache, Geschmacks-Empfehlung und der Zubereitungsmodus (Schritt für Schritt, freihändig, mit Auto-Weiter). */
(function () {
  const R = window.REZEPTE, K = window.KATEGORIEN;
  const Bar = (window.Bar = { rezepte: R, kategorien: K });

  Bar.byId = (id) => R.find((r) => r.id === id);
  Bar.katName = (id) => (K.find((k) => k.id === id) || {}).name || id;
  Bar.esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  const nf = new Intl.NumberFormat("de-DE", { maximumFractionDigits: 1 });
  Bar.menge = (z, p = 1) => (z.m == null ? "" : nf.format(Math.round(z.m * p * 2) / 2) + (z.e ? " " + z.e : ""));
  Bar.suche = (r, q) => {
    q = q.trim().toLowerCase();
    if (!q) return true;
    return [r.name, r.beschreibung, r.glas, r.garnitur, Bar.katName(r.kategorie), ...r.geschmack, ...r.zutaten.map((z) => z.n)].join(" ").toLowerCase().includes(q);
  };
  Bar.credit = (r) => `Foto: ${Bar.esc(r.credit.autor)}, ${Bar.esc(r.credit.lizenz)} (<a href="${Bar.esc(r.credit.quelle)}" target="_blank" rel="noopener">Wikimedia Commons</a>)`;
  Bar.staerkeText = (s) => ["alkoholfrei", "sehr mild", "mild", "mittel", "kräftig", "sehr stark"][s] || "";

  /* Geschmacks-Empfehlung: Jeder wählt, was er mag, die Rezepte werden nach Passung sortiert. */
  Bar.GESCHMACK = [
    { id: "suess", name: "Süß" }, { id: "fruchtig", name: "Fruchtig" }, { id: "sauer", name: "Sauer & frisch" },
    { id: "cremig", name: "Cremig" }, { id: "bitter", name: "Bitter" }, { id: "herb", name: "Herb & trocken" },
    { id: "wuerzig", name: "Würzig & kräuterig" }, { id: "salzig", name: "Salzig" }, { id: "rauchig", name: "Rauchig" }, { id: "kaffee", name: "Kaffee" },
  ];
  /* Spirituosen: "basis" eines Rezepts = jede Sorte mit mindestens 15 % Anteil am reinen Alkohol */
  Bar.BASIS = [
    { id: "rum", name: "Rum" }, { id: "gin", name: "Gin" }, { id: "wodka", name: "Wodka" }, { id: "tequila", name: "Tequila" },
    { id: "whiskey", name: "Whiskey" }, { id: "cachaca", name: "Cachaça" }, { id: "likoer", name: "Likör" },
    { id: "bitter", name: "Bitter & Amaro" }, { id: "wermut", name: "Wermut" }, { id: "schaumwein", name: "Prosecco" },
  ];
  Bar.ALKOHOL = [{ id: "frei", name: "Alkoholfrei" }, { id: "niedrig", name: "Niedrig", text: "bis 10 %" }, { id: "mittel", name: "Mittel", text: "11 bis 17 %" }, { id: "hoch", name: "Hoch", text: "ab 18 %" }];
  Bar.alkoholStufe = (r) => { const v = Bar.alkohol(r).vol; return v < 0.5 ? "frei" : Math.round(v) <= 10 ? "niedrig" : Math.round(v) <= 17 ? "mittel" : "hoch"; };
  Bar.STIL = [{ id: "exotisch", name: "Exotisch & Tiki" }, { id: "klassiker", name: "Klassiker" }, { id: "modern", name: "Modern" }, { id: "longdrink", name: "Longdrink" }];
  Bar.STAERKE = [{ id: "mild", name: "Mild" }, { id: "mittel", name: "Mittel" }, { id: "kraeftig", name: "Kräftig" }];
  const staerkeId = (s) => (s <= 2 ? "mild" : s === 3 ? "mittel" : "kraeftig");
  /* wahl = { geschmack: [ids], stil: [ids], staerke: "", basis: [ids] }. Gibt { punkte 0..1, passt } zurück; "passt" heißt: alle harten Filter erfüllt. */
  Bar.passt = (r, wahl) => {
    const t = wahl.geschmack || [], p = r.profil || {};
    let punkte = 1;
    if (t.length) {
      punkte = t.reduce((a, k) => a + (p[k] || 0) / 3, 0) / t.length;
      if (t.some((k) => !p[k])) punkte *= 0.6;
      const fremd = Object.entries(p).reduce((a, [k, v]) => a + (t.includes(k) ? 0 : v), 0);
      punkte = Math.max(0, punkte - fremd * 0.02);
    }
    const passt = (!(wahl.stil || []).length || wahl.stil.some((s) => (r.stil || [r.kategorie]).includes(s))) &&
      (!wahl.staerke || staerkeId(r.staerke) === wahl.staerke) &&
      (!wahl.alkohol || Bar.alkoholStufe(r) === wahl.alkohol) &&
      (!(wahl.basis || []).length || wahl.basis.some((b) => (r.basis || []).includes(b)));
    return { punkte, passt };
  };
  Bar.empfehle = (wahl) => {
    const alle = R.map((r) => ({ r, ...Bar.passt(r, wahl) }));
    const hatGeschmack = (wahl.geschmack || []).length > 0;
    const sortiert = (l) => l.sort((a, b) => b.punkte - a.punkte || a.r.name.localeCompare(b.r.name, "de"));
    const treffer = sortiert(alle.filter((x) => x.passt && (!hatGeschmack || x.punkte >= 0.25)));
    return { treffer, naheDran: treffer.length ? [] : sortiert(alle.filter((x) => !hatGeschmack || x.punkte >= 0.25)).slice(0, 6) };
  };

  /* Alkoholgehalt (Schätzung aus den Zutaten): Eis verdünnt je nach Zubereitung, Auffüllflüssigkeit zählt mit.
     Das ist nur eine Information. Ob jemand noch fahren darf, lässt sich daraus nicht ableiten. */
  const VERDUENNUNG = { Bauen: 0.1, Rühren: 0.2, Shaken: 0.25, Mixen: 0.5 };
  Bar.alkohol = (r) => {
    let fluessig = 0, rein = 0;
    for (const z of r.zutaten) {
      const ml = z.e === "ml" ? z.m : z.ml || 0;
      fluessig += ml; rein += (ml * (z.v || 0)) / 100;
    }
    const gesamt = fluessig * (1 + (VERDUENNUNG[r.technik] ?? 0.2));
    return { vol: gesamt ? (rein / gesamt) * 100 : 0, gramm: rein * 0.789, ml: gesamt };
  };
  Bar.alkoholText = (r) => { const a = Bar.alkohol(r); return a.vol < 0.5 ? "alkoholfrei" : `ca. ${nf.format(Math.round(a.vol))} % vol.`; };
  Bar.alkoholGramm = (r) => { const g = Bar.alkohol(r).gramm; return g < 0.5 ? "ohne Alkohol" : `ca. ${nf.format(Math.round(g))} g reiner Alkohol`; };
  Bar.FAHRHINWEIS = "Wer fährt, trinkt nicht. Der Alkoholgehalt sagt nichts darüber, ob man noch fahren darf: Das hängt von Körpergewicht, Zeit, Essen und vielem mehr ab, und schon kleine Mengen mindern die Fahrtüchtigkeit. Für Fahranfänger und Berufsfahrer gilt 0,0 Promille.";

  /* Speicher (localStorage kann fehlen, deshalb immer abgesichert) */
  Bar.store = {
    get(k, d) { try { const v = localStorage.getItem("bar." + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem("bar." + k, JSON.stringify(v)); } catch (e) {} },
  };

  /* Bestellungen (Warenkorb): [{ uid, id, n }]. Geschätzte Dauer: erste Portion volle Zeit, jede weitere nur die Hälfte (gemeinsam geshakt). */
  Bar.dauer = (r, n = 1) => r.zeit * (1 + (n - 1) * 0.5);
  Bar.minText = (m) => { m = Math.max(1, Math.round(m)); return m < 60 ? m + " Min." : Math.floor(m / 60) + " Std. " + (m % 60 ? (m % 60) + " Min." : ""); };
  Bar.queue = {
    get() {
      const q = Bar.store.get("queue", []).filter((o) => Bar.byId(o.id));
      q.forEach((o) => { if (!o.uid) o.uid = Date.now().toString(36) + Math.random().toString(36).slice(2, 7); });
      return q;
    },
    set(q) { Bar.store.set("queue", q); },
    add(id, n = 1) {
      const q = Bar.queue.get(), o = q.find((x) => x.id === id);
      o ? (o.n = Math.min(24, o.n + n)) : q.push({ uid: Date.now().toString(36) + Math.random().toString(36).slice(2, 7), id, n });
      Bar.queue.set(q);
    },
    anzahl: () => Bar.queue.get().reduce((a, o) => a + o.n, 0),
    /* Playlist: alle Bestellungen nacheinander ohne Antippen abspielen. Fertige Drinks fallen aus der Liste. onChange: Anzeige neu zeichnen. */
    abspielen(onChange) {
      const gesamt = Bar.queue.get().length;
      let gemacht = 0;
      const los = () => {
        const q = Bar.queue.get();
        if (!q.length) return;
        const o = q[0], rest = q.reduce((a, x) => a + Bar.dauer(Bar.byId(x.id), x.n), 0);
        Bar.kochen(Bar.byId(o.id), o.n, () => {
          const q2 = Bar.queue.get(); q2.shift(); Bar.queue.set(q2); gemacht++;
          if (onChange) onChange();
          if (q2.length) setTimeout(los, 400);
        }, { pos: gemacht + 1, gesamt, rest, naechster: q[1] ? Bar.byId(q[1].id).name : null });
      };
      los();
    },
    gesamt: () => Bar.queue.get().reduce((a, o) => a + Bar.dauer(Bar.byId(o.id), o.n), 0),
  };
  Bar.favs = () => Bar.store.get("favs", []);
  Bar.isFav = (id) => Bar.favs().includes(id);
  Bar.toggleFav = (id) => {
    const f = Bar.favs(), i = f.indexOf(id);
    i < 0 ? f.push(id) : f.splice(i, 1);
    Bar.store.set("favs", f);
    return i < 0;
  };

  /* Display wach halten, solange der Zubereitungsmodus offen ist */
  let lock = null, wantLock = false;
  Bar.wach = async (on) => {
    wantLock = on;
    try {
      if (on && "wakeLock" in navigator) lock = await navigator.wakeLock.request("screen");
      else if (lock) { await lock.release(); lock = null; }
    } catch (e) {}
  };
  document.addEventListener("visibilitychange", () => { if (wantLock && document.visibilityState === "visible") Bar.wach(true); });

  /* Sprache: Vorlesen und Sprachbefehle (Browser-Unterstützung unterschiedlich) */
  Bar.sprich = (t, ende) => {
    try {
      speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(t);
      u.lang = "de-DE"; u.rate = 0.95;
      if (ende) { u.onend = ende; u.onerror = ende; }
      speechSynthesis.speak(u);
    } catch (e) { if (ende) ende(); }
  };
  Bar.schweige = () => { try { speechSynthesis.cancel(); } catch (e) {} };
  Bar.hoerenMoeglich = !!(window.SpeechRecognition || window.webkitSpeechRecognition);
  Bar.hoeren = (cb) => {
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) return null;
    const rec = new SR();
    rec.lang = "de-DE"; rec.continuous = true; rec.interimResults = false;
    let an = true;
    rec.onresult = (e) => cb(e.results[e.results.length - 1][0].transcript.toLowerCase());
    rec.onend = () => { if (an) try { rec.start(); } catch (e) {} };
    rec.onerror = (e) => { if (e.error === "not-allowed" || e.error === "service-not-allowed") an = false; };
    try { rec.start(); } catch (e) { return null; }
    return () => { an = false; try { rec.stop(); } catch (e) {} };
  };

  const ICON = {
    x: '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M5 5l14 14M19 5L5 19"/></svg>',
    left: '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>',
    right: '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>',
    mic: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0014 0M12 18v3"/></svg>',
    speaker: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 9v6h4l5 4V5L8 9H4z"/><path d="M16.5 8.5a5 5 0 010 7M19 6a8.5 8.5 0 010 12"/></svg>',
    pause: '<svg viewBox="0 0 24 24" width="30" height="30" fill="currentColor"><rect x="6" y="4.500" width="4" height="15" rx="1"/><rect x="14" y="4.500" width="4" height="15" rx="1"/></svg>',
    play: '<svg viewBox="0 0 24 24" width="30" height="30" fill="currentColor"><path d="M7 4.500v15l13-7.500z"/></svg>',
    timer: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.500 2M9 2.500h6"/></svg>',
  };
  Bar.icon = ICON;

  /* Zubereitungsmodus: erst Bereitstellen, dann Schritt für Schritt, am Ende Garnitur und Prost.
     Auto-Weiter: Nach einigen Sekunden (Standard 6) geht es von allein zum nächsten Schritt, sodass man das Display nicht anfassen muss. */
  const INTERVALLE = [4, 6, 8, 10, 15];
  /* fertig: wird aufgerufen, wenn der Drink bis zum Ende (Prost) durchgelaufen ist, nicht beim Abbrechen. */
  /* liste (optional, für die Playlist): { pos, gesamt, rest (Minuten), naechster (Name oder null) }. Dann läuft nach dem Prost automatisch der nächste Drink an. */
  Bar.kochen = function (r, portionen, fertig, liste) {
    let p = portionen || 1, i = -1, vorlesen = Bar.store.get("vorlesen", false), stopHoeren = null;
    let auto = liste ? true : Bar.store.get("auto", true), sek = Bar.store.get("sek", 6), pause = false, rest = 0, gesamt = 0, tick = null, spricht = false, sprechId = 0;
    const n = r.schritte.length;
    const ov = document.createElement("div");
    ov.className = "bk"; ov.setAttribute("role", "dialog"); ov.setAttribute("aria-label", "Zubereitung " + r.name);
    ov.innerHTML = `
      <div class="bk-top"><div class="bk-prog">${Array.from({ length: n + 2 }, () => "<i></i>").join("")}</div>
        <button class="bk-x" aria-label="Schließen">${ICON.x}</button></div>
      <div class="bk-head"><span class="bk-name">${Bar.esc(r.name)}</span><span class="bk-glas">${liste ? `Drink ${liste.pos} von ${liste.gesamt} · noch ca. ${Bar.minText(liste.rest)}` : Bar.esc(r.glas)}</span></div>
      <div class="bk-body"></div>
      <div class="bk-auto" hidden><div class="bk-auto-t"><b class="bk-cd"></b><span class="bk-danach"></span></div><div class="bk-bar"><i></i></div></div>
      <div class="bk-tools">
        <div class="bk-port"><button data-a="minus" aria-label="Eine Portion weniger">−</button><span></span><button data-a="plus" aria-label="Eine Portion mehr">+</button></div>
        <button class="bk-tool" data-a="auto" aria-pressed="false">${ICON.timer}<span>Auto-Weiter</span></button>
        <button class="bk-tool" data-a="sek" aria-label="Sekunden pro Schritt"><span></span></button>
        <button class="bk-tool" data-a="vorlesen" aria-pressed="false">${ICON.speaker}<span>Vorlesen</span></button>
        <button class="bk-tool" data-a="mikro" aria-pressed="false" ${Bar.hoerenMoeglich ? "" : "hidden"}>${ICON.mic}<span>Sprache</span></button>
      </div>
      <div class="bk-nav"><button class="bk-back" data-a="zurueck" aria-label="Zurück">${ICON.left}</button>
        <button class="bk-pause" data-a="pause" aria-label="Pausieren"></button>
        <button class="bk-next" data-a="weiter"><span>Weiter</span>${ICON.right}</button></div>`;
    document.body.appendChild(ov);
    document.body.classList.add("bk-offen");
    Bar.wach(true);
    const $ = (s) => ov.querySelector(s);
    const body = $(".bk-body");

    const chips = (idx) => idx.map((k) => { const z = r.zutaten[k]; return `<div class="bk-chip"><b>${Bar.menge(z, p) || " "}</b><span>${Bar.esc(z.n)}</span></div>`; }).join("");
    function text() {
      if (i < 0) return `Zum Bereitstellen: ${r.glas}. ` + r.zutaten.map((z) => Bar.menge(z, p).replace(" ", " ") + " " + z.n).join(", ");
      if (i < n) return r.schritte[i].t;
      return `Fertig. Garnitur: ${r.garnitur}. Prost!`;
    }
    const weiterDrink = () => !!(liste && liste.naechster);
    const danach = () => (i + 1 < n ? r.schritte[i + 1].t : i + 1 === n ? `Fertig mit Garnitur: ${r.garnitur}` : weiterDrink() ? `Nächster Drink: ${liste.naechster}` : "");
    const dauer = () => (i < 0 ? Math.max(15, sek * 3) : i >= n ? Math.max(8, sek) : sek);
    const laeuft = () => auto && (i < n || weiterDrink());

    function anzeigeAuto() {
      const box = $(".bk-auto"), aktiv = laeuft();
      box.hidden = !aktiv;
      $('[data-a="auto"]').setAttribute("aria-pressed", auto);
      $('[data-a="sek"] span').textContent = sek + " s";
      $('[data-a="sek"]').hidden = !auto;
      const pb = $(".bk-pause");
      pb.hidden = !aktiv;
      pb.innerHTML = pause ? ICON.play : ICON.pause;
      pb.setAttribute("aria-label", pause ? "Fortsetzen" : "Pausieren");
      $(".bk-nav").classList.toggle("drei", aktiv);
      if (!aktiv) return;
      $(".bk-danach").textContent = (i >= n ? "" : "Danach: ") + danach();
      const s = Math.ceil(rest / 1000);
      $(".bk-cd").textContent = pause ? "Pause" : spricht ? "Hört zu …" : s + " s";
      $(".bk-bar i").style.width = (gesamt ? Math.max(0, Math.min(100, (rest / gesamt) * 100)) : 0) + "%";
    }
    function planen() {
      clearInterval(tick);
      pause = false;
      gesamt = rest = dauer() * 1000;
      anzeigeAuto();
      if (!laeuft()) return;
      tick = setInterval(() => {
        if (pause || spricht) return;
        rest -= 100;
        anzeigeAuto();
        if (rest <= 0) { clearInterval(tick); weiter(); }
      }, 100);
    }
    function render() {
      ov.querySelectorAll(".bk-prog i").forEach((e, k) => e.classList.toggle("an", k <= i + 1));
      $(".bk-port span").textContent = p + (p === 1 ? " Portion" : " Portionen");
      if (i < 0) {
        body.innerHTML = `<div class="bk-label">Bereitstellen</div><div class="bk-text">${Bar.esc(r.glas)}</div><div class="bk-chips">${chips(r.zutaten.map((_, k) => k))}</div>`;
      } else if (i < n) {
        const s = r.schritte[i];
        body.innerHTML = `<div class="bk-label">Schritt ${i + 1} von ${n}</div><div class="bk-text">${Bar.esc(s.t)}</div><div class="bk-chips">${chips(s.z)}</div>`;
      } else {
        body.innerHTML = `<div class="bk-label">Fertig</div><div class="bk-text">${Bar.esc(r.name)}</div><div class="bk-chips"><div class="bk-chip"><b>Garnitur</b><span>${Bar.esc(r.garnitur)}</span></div></div><div class="bk-prost">Prost!</div>`;
      }
      $(".bk-back").disabled = i < 0;
      $(".bk-next span").textContent = i >= n ? (weiterDrink() ? "Nächster Drink" : "Schließen") : i < 0 ? "Los geht's" : "Weiter";
      spricht = false;
      if (vorlesen) {
        const id = ++sprechId;
        spricht = true;
        Bar.sprich(text(), () => { if (id === sprechId) { spricht = false; anzeigeAuto(); } });
      }
      planen();
    }
    const weiter = () => { if (i >= n) schliessen(true); else { i++; render(); } };
    const zurueck = () => { if (i > -1) { i--; render(); } };
    function schliessen(durchgelaufen) {
      clearInterval(tick);
      if (stopHoeren) stopHoeren();
      sprechId++; Bar.schweige(); Bar.wach(false);
      document.removeEventListener("keydown", taste);
      document.body.classList.remove("bk-offen");
      ov.remove();
      if (durchgelaufen === true && fertig) fertig();
    }
    const umschaltenPause = () => { pause = !pause; anzeigeAuto(); };
    const taste = (e) => {
      if (e.key === "ArrowRight" || e.key === "Enter") { e.preventDefault(); weiter(); }
      else if (e.key === " ") { e.preventDefault(); auto && i < n ? umschaltenPause() : weiter(); }
      else if (e.key === "ArrowLeft") zurueck();
      else if (e.key === "Escape") schliessen();
    };
    document.addEventListener("keydown", taste);
    ov.addEventListener("click", (e) => {
      const b = e.target.closest("[data-a]") || e.target.closest(".bk-x");
      if (!b) return;
      if (b.classList.contains("bk-x")) return schliessen();
      const a = b.dataset.a;
      if (a === "weiter") weiter();
      else if (a === "zurueck") zurueck();
      else if (a === "pause") umschaltenPause();
      else if (a === "plus") { p = Math.min(p + 1, 12); render(); }
      else if (a === "minus") { p = Math.max(p - 1, 1); render(); }
      else if (a === "auto") { auto = !auto; if (!liste) Bar.store.set("auto", auto); planen(); }
      else if (a === "sek") { sek = INTERVALLE[(INTERVALLE.indexOf(sek) + 1) % INTERVALLE.length]; Bar.store.set("sek", sek); planen(); }
      else if (a === "vorlesen") {
        vorlesen = !vorlesen; Bar.store.set("vorlesen", vorlesen);
        b.setAttribute("aria-pressed", vorlesen);
        if (vorlesen) { const id = ++sprechId; spricht = true; Bar.sprich(text(), () => { if (id === sprechId) { spricht = false; anzeigeAuto(); } }); }
        else { sprechId++; spricht = false; Bar.schweige(); anzeigeAuto(); }
      } else if (a === "mikro") {
        if (stopHoeren) { stopHoeren(); stopHoeren = null; b.setAttribute("aria-pressed", "false"); return; }
        stopHoeren = Bar.hoeren((t) => {
          if (/weiter|nächst/.test(t)) weiter();
          else if (/zurück|vorher/.test(t)) zurueck();
          else if (/pause|halt|stopp|moment/.test(t)) { pause = true; anzeigeAuto(); }
          else if (/los|fortsetzen|start|geht's/.test(t)) { pause = false; anzeigeAuto(); }
          else if (/wiederhol|nochmal|noch mal/.test(t)) Bar.sprich(text());
          else if (/ende|schließ|fertig/.test(t)) schliessen();
        });
        b.setAttribute("aria-pressed", stopHoeren ? "true" : "false");
      }
    });
    let x0 = null;
    body.addEventListener("touchstart", (e) => { x0 = e.touches[0].clientX; }, { passive: true });
    body.addEventListener("touchend", (e) => {
      if (x0 == null) return;
      const dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 60) dx < 0 ? weiter() : zurueck();
    });
    $('[data-a="vorlesen"]').setAttribute("aria-pressed", vorlesen);
    render();
    return schliessen;
  };
})();
