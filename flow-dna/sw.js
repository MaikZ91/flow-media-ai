// Flow DNA Service Worker: App-Hülle offline, Inhalte immer frisch (network first)
const C = "flow-dna-v32";
const CORE = ["./", "index.html", "kern.js", "kern.css", "daten.js", "angebote.js", "kurse.js", "kurse-auto.js", "coach.js", "news.js", "manifest.webmanifest", "app/icon-192.png", "app/icon-512.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(C).then(c => c.addAll(CORE)).then(() => self.skipWaiting())) });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(k => Promise.all(k.filter(x => x !== C).map(x => caches.delete(x)))).then(() => self.clients.claim())) });
self.addEventListener("fetch", e => {
  const u = new URL(e.request.url);
  if (e.request.method !== "GET" || u.origin !== location.origin) return; // Lizenz-Server, Fonts, WhatsApp: nie cachen
  e.respondWith(fetch(e.request, { cache: "no-cache" }).then(r => { if (r.ok && !u.pathname.endsWith(".mp4")) { const cp = r.clone(); caches.open(C).then(c => c.put(e.request, cp)) } return r })
    .catch(() => caches.match(e.request).then(r => r || caches.match("index.html"))));
});
