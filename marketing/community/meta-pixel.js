/* Meta Pixel for the community landing pages – loads ONLY after consent.
   Reports "Lead" when someone taps a WhatsApp join link, so Meta can optimise ads for real joins.
   Set PIXEL_ID once the pixel exists in Events Manager; empty = nothing loads, no banner. */
(() => {
  const PIXEL_ID = "1548157737344373";
  if (!PIXEL_ID) return;
  const KEY = "flow_meta_consent";
  let ok = null; try { ok = localStorage.getItem(KEY) } catch {}
  const ph = (e, p) => window.posthog?.capture(e, p);

  function load() {
    if (window.fbq) return;
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");
    fbq("init", PIXEL_ID);
    fbq("track", "PageView");
  }
  document.addEventListener("click", e => {
    const a = e.target.closest('a[href*="chat.whatsapp.com"], a[href*="wa.me"]');
    if (a && window.fbq) fbq("track", "Lead", { content_name: location.pathname.includes("stammtisch") ? "stammtisch" : "community" });
  }, true);

  if (ok === "ja") return load();
  if (ok === "nein") return;

  const ask = (b) => {
    try { localStorage.setItem(KEY, b.dataset.c) } catch {}
    ph("meta_consent", { antwort: b.dataset.c });
    document.documentElement.classList.remove("fm-pending");
    if (b.dataset.c === "ja") load();
  };
  const st = document.createElement("style");
  // Seiten mit #consent-slot: kleine Zeile in der Fußzeile, blockiert nichts (ignorieren = keine Messung)
  const slot = document.getElementById("consent-slot");
  if (slot) {
    st.textContent = `.fm-inline{display:inline-flex;align-items:center;gap:6px;white-space:nowrap;font:500 11px Inter,system-ui,sans-serif;color:#bababe}
.fm-inline a{color:#bababe}@media(max-width:360px){.fm-inline{gap:4px}.fm-inline a{font-size:10px}}.fm-inline button{font:600 11px Inter,system-ui,sans-serif;padding:3px 8px;border-radius:999px;border:1px solid #ffffff45;background:transparent;color:#fff;cursor:pointer}
.fm-inline button[data-c=ja]{background:#fff;color:#0B0B0B;border-color:#fff}`;
    slot.className = "fm-inline";
    slot.innerHTML = `<a href="/flow-media-ai/marketing/landing-page/datenschutz.html#meta" title="Darf Meta messen, ob meine Anzeige dich hergebracht hat? (Cookie)">Meta-Messung?</a><button type="button" data-c="ja">Ja</button><button type="button" data-c="nein">Nein</button>`;
    document.documentElement.classList.add("fm-pending");
    slot.addEventListener("click", e => { const b = e.target.closest("[data-c]"); if (!b) return; ask(b); slot.remove(); });
    document.head.appendChild(st);
    return;
  }
  const bar = document.createElement("div");
  bar.setAttribute("role", "dialog"); bar.setAttribute("aria-label", "Einwilligung Meta-Messung");
  bar.innerHTML = `<p>Darf Meta messen, ob meine Anzeige dich hergebracht hat? (Cookie) <a href="/flow-media-ai/marketing/landing-page/datenschutz.html#meta">Mehr dazu</a></p><div><button type="button" data-c="nein">Nein</button><button type="button" data-c="ja">Ja, okay</button></div>`;
  st.textContent = `.fm-consent{position:fixed;left:8px;right:8px;top:8px;z-index:9999;display:flex;gap:8px 10px;align-items:center;justify-content:space-between;flex-wrap:wrap;padding:8px 10px;border:1px solid #ffffff30;border-radius:14px;background:#0B0B0Bf2;color:#fff;font:500 12px/1.35 Inter,system-ui,sans-serif;box-shadow:0 8px 30px #0008}
.fm-consent p{margin:0;flex:1 1 200px}.fm-consent a{color:#bababe}.fm-consent div{display:flex;gap:8px}
.fm-consent button{font:600 13px Inter,system-ui,sans-serif;padding:7px 12px;border-radius:999px;border:1px solid #ffffff55;background:transparent;color:#fff;cursor:pointer}
.fm-consent button[data-c=ja]{background:#fff;color:#0B0B0B;border-color:#fff}`;
  bar.className = "fm-consent";
  bar.addEventListener("click", e => { const b = e.target.closest("[data-c]"); if (!b) return; ask(b); bar.remove(); });
  document.head.appendChild(st); document.body.appendChild(bar);
})();
