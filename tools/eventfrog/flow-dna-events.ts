// Flow DNA – öffentliche Workshop-Termine aus Eventfrog (Supabase Edge Function `flow-dna-events`, verify_jwt=false).
// Liefert nur veröffentlichte, kommende Events, deren Beschreibung „#FlowMediaAI“ enthält (THE-TRIBE-Events bleiben draußen).
// Schlüssel: Secret EVENTFROG_API_KEY (Organizer-Key, nur Lesen). Keine Kundendaten – nur Titel, Datum, Preis, Buchungslink.
const KEY = Deno.env.get("EVENTFROG_API_KEY") ?? "";
const API = "https://api.eventfrog.net/organizer/v1";
const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET, OPTIONS" };
let cache: { at: number; body: string } | null = null;
const strip = (h: string) => h.replace(/<[^>]+>/g, " ").replace(/&nbsp;/g, " ").replace(/\s+/g, " ").trim();
async function load() {
  const h = { Authorization: `Bearer ${KEY}` };
  const r = await fetch(`${API}/events?perPage=100`, { headers: h });
  if (!r.ok) throw new Error("eventfrog " + r.status);
  const all = (await r.json()).data ?? [];
  const now = Date.now();
  const mine = all.filter((e: any) => e.visibility?.published && new Date(e.endDate || e.beginDate).getTime() > now - 36e5
    && /flowmediaai|flow media ai/i.test((e.localizedInfo ?? []).map((l: any) => l.description + " " + l.title).join(" ")));
  const out = await Promise.all(mine.map(async (e: any) => {
    const li = e.localizedInfo?.[0] ?? {};
    let preis = "";
    try {
      const c = (await (await fetch(`${API}/events/${e.id}/ticketcategories`, { headers: h })).json()).data ?? [];
      const ps = c.map((x: any) => x.priceStrategy?.fixed?.price).filter((n: any) => typeof n === "number");
      if (ps.length) preis = (Math.min(...ps) / 100).toLocaleString("de-DE", { maximumFractionDigits: 2 }) + " €";
    } catch { /* Preis optional */ }
    return { id: e.id, titel: li.title ?? "", kurz: li.shortDescription || strip(li.description ?? "").slice(0, 280), datum: e.beginDate, endeISO: e.endDate, preis,
      url: `https://eventfrog.de/de/p/x/x-${e.id}.html` };
  }));
  out.sort((a, b) => a.datum.localeCompare(b.datum));
  return JSON.stringify({ events: out, stand: new Date().toISOString() });
}
Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: cors });
  try {
    if (!cache || Date.now() - cache.at > 5 * 60e3) cache = { at: Date.now(), body: await load() };
    return new Response(cache.body, { headers: { ...cors, "content-type": "application/json; charset=utf-8", "cache-control": "public, max-age=120" } });
  } catch (e) {
    return new Response(JSON.stringify({ events: [], error: String(e) }), { status: 200, headers: { ...cors, "content-type": "application/json" } });
  }
});
