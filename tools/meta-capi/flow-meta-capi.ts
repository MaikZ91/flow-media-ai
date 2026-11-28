// Supabase Edge Function "flow-meta-capi" – meldet einen Community-Beitritt server-seitig an Meta (Conversions API).
// Datensparsam: nur die Klick-Kennung aus dem Anzeigen-Link (fbclid → fbc) und der Browser-Typ (User-Agent).
// Keine Cookies, keine IP-Adresse, keine Namen oder Telefonnummern. Ohne fbclid wird nichts gesendet.
// Secret META_CAPI_TOKEN (Meta Events Manager → Pixel → Einstellungen → Conversions API → Zugriffsschlüssel generieren).
const PIXEL_ID = "1012935401238191";
const ALLOWED = ["https://maikz91.github.io"];
const cors = (o: string | null) => ({
  "Access-Control-Allow-Origin": o && ALLOWED.includes(o) ? o : ALLOWED[0],
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "content-type",
});

Deno.serve(async (req) => {
  const origin = req.headers.get("origin");
  if (req.method === "OPTIONS") return new Response(null, { headers: cors(origin) });
  if (req.method !== "POST") return new Response("method", { status: 405, headers: cors(origin) });
  const token = Deno.env.get("META_CAPI_TOKEN") || Deno.env.get("Pixel") || Deno.env.get("PIXEL") || Deno.env.get("pixel") || Deno.env.get("Pexel") || Deno.env.get("PEXEL");
  let body: Record<string, unknown> = {};
  try { body = JSON.parse(await req.text() || "{}"); } catch { /* leer */ }
  const fbclid = String(body.fbclid || "").slice(0, 500);
  const url = String(body.url || "").slice(0, 500);
  if (!fbclid || !/^https:\/\/maikz91\.github\.io\//.test(url)) return new Response(null, { status: 204, headers: cors(origin) });
  if (!token) return new Response(null, { status: 204, headers: cors(origin) });
  const now = Math.floor(Date.now() / 1000);
  const landed = Number(body.landed) || now * 1000;
  const event = {
    event_name: "Lead",
    event_time: now,
    event_id: String(body.event_id || crypto.randomUUID()).slice(0, 100),
    action_source: "website",
    event_source_url: url.split("?")[0],
    user_data: { fbc: `fb.1.${landed}.${fbclid}`, client_user_agent: (req.headers.get("user-agent") || "").slice(0, 400) },
    custom_data: { content_name: "community", content_category: String(body.role || "").slice(0, 40) },
  };
  const test = String(body.test_event_code || "");
  const r = await fetch(`https://graph.facebook.com/v21.0/${PIXEL_ID}/events?access_token=${encodeURIComponent(token)}`, {
    method: "POST", headers: { "content-type": "application/json" },
    body: JSON.stringify({ data: [event], ...(test ? { test_event_code: test } : {}) }),
  });
  const out = await r.text();
  return new Response(out, { status: r.ok ? 200 : 502, headers: { ...cors(origin), "content-type": "application/json" } });
});
