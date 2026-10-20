// Flow Board service worker: makes the board installable and keeps the last loaded page for offline viewing.
// Network first, so every deploy shows up immediately; board data itself always comes live from Supabase.
const CACHE = "flow-board-shell-v1";
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => e.waitUntil(self.clients.claim()));
self.addEventListener("fetch", e => {
  const r = e.request;
  if (r.method !== "GET" || new URL(r.url).origin !== location.origin) return;
  e.respondWith(fetch(r).then(res => {
    if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(r, copy)) }
    return res;
  }).catch(() => caches.match(r, { ignoreSearch: true }).then(m => m || Response.error())));
});
