/* Service Worker: macht die App installierbar und offline nutzbar.
   Bei Änderungen an App-Dateien VERSION hochzählen, damit alte Caches verschwinden. */
const VERSION = "adilsbar-2";
const KERN = [
  "./", "./index.html", "./v7-amber.html", "./manifest.webmanifest",
  "./daten/kern.js", "./daten/kern.css", "./daten/rezepte.js",
  "./icons/icon-192.png", "./icons/icon-512.png", "./icons/maskable-512.png", "./icons/apple-touch-icon.png",
];
const BILDER = [   './bilder/aloha-ice-jam.jpg',   './bilder/apfel-holunder-fizz.jpg',   './bilder/bramble.jpg',   './bilder/caipirinha.jpg',   './bilder/caribbean-summer.jpg',   './bilder/cosmopolitan.jpg',   './bilder/cuba-libre.jpg',   './bilder/daiquiri.jpg',   './bilder/dry-martini.jpg',   './bilder/espresso-martini.jpg',   './bilder/long-island.jpg',   './bilder/mai-tai.jpg',   './bilder/maracuja-spritz.jpg',   './bilder/margarita.jpg',   './bilder/mojito.jpg',   './bilder/moscow-mule.jpg',   './bilder/negroni.jpg',   './bilder/old-fashioned.jpg',   './bilder/paloma.jpg',   './bilder/paper-plane.jpg',   './bilder/penicillin.jpg',   './bilder/pina-colada.jpg',   './bilder/sex-on-the-beach.jpg',   './bilder/shirley-temple.jpg',   './bilder/singapore-sling.jpg',   './bilder/spritz.jpg',   './bilder/tequila-sunrise.jpg',   './bilder/virgin-colada.jpg',   './bilder/virgin-margarita.jpg',   './bilder/virgin-mojito.jpg',   './bilder/whiskey-sour.jpg',   './bilder/zombie.jpg',  ];

const SCHRIFT = "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Jost:wght@400;500;600&display=swap";

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(VERSION).then((c) => c.addAll(KERN).then(() => Promise.all([c.addAll(BILDER).catch(() => {}), c.add(SCHRIFT).catch(() => {})]))).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== VERSION).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});

/* Seiten, Skripte und Stile: erst Netz (damit Updates sofort ankommen), sonst Cache.
   Bilder und Schriften: erst Cache, sonst Netz und merken. */
self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  const schrift = url.hostname === "fonts.googleapis.com" || url.hostname === "fonts.gstatic.com";
  if (url.origin !== location.origin && !schrift) return;
  const bild = req.destination === "image" || req.destination === "font" || schrift;
  if (bild) {
    e.respondWith(caches.match(req).then((hit) => hit || fetch(req).then((res) => {
      if (res.ok || res.type === "opaque") { const kopie = res.clone(); caches.open(VERSION).then((c) => c.put(req, kopie)); }
      return res;
    })));
    return;
  }
  e.respondWith(fetch(req).then((res) => {
    if (res.ok) { const kopie = res.clone(); caches.open(VERSION).then((c) => c.put(req, kopie)); }
    return res;
  }).catch(() => caches.match(req, { ignoreSearch: true }).then((hit) => hit || (req.mode === "navigate" ? caches.match("./v7-amber.html") : undefined))));
});
