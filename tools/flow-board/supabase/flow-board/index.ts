// Flow Board gateway: every read/write of the board goes through here.
// Access is granted by a secret board key (sent by the page, compared against a SHA-256 hash in flow_board_boards).
// Secrets (Supabase → Edge Functions → Secrets): CALENDLY_TOKEN, POSTHOG_API_KEY, optional GITHUB_TOKEN and GITHUB_REPOS ("owner/repo,owner/repo2").
import "jsr:@supabase/functions-js/edge-runtime.d.ts";
import { createClient } from "jsr:@supabase/supabase-js@2";

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { ...cors, "Content-Type": "application/json" } });

const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const BUCKET = "flow-board";
const TABLES: Record<string, string> = { tasks: "flow_board_tasks", files: "flow_board_files", finance: "flow_board_finance" };

async function sha256(s: string) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}
function secret(names: string[], pattern: RegExp) {
  const env = Deno.env.toObject();
  const name = names.find((n) => env[n]) ?? Object.keys(env).find((k) => pattern.test(k));
  return name ? env[name].trim() : "";
}

// Booked Calendly meetings (last 30 days, next 90 days).
async function calendlyEvents() {
  const token = secret(["CALENDLY_TOKEN", "CALENDLY_API_TOKEN", "CALENDLY_API_KEY", "CALENDLY_PAT", "CALENDLY"], /calendly/i);
  if (!token) return { status: "no_token", events: [] };
  const h = { Authorization: `Bearer ${token}` };
  const meRes = await fetch("https://api.calendly.com/users/me", { headers: h });
  if (!meRes.ok) return { status: "error", detail: `users/me ${meRes.status}`, events: [] };
  const uri = (await meRes.json())?.resource?.uri;
  const min = new Date(Date.now() - 30 * 864e5).toISOString();
  const max = new Date(Date.now() + 90 * 864e5).toISOString();
  const q = new URLSearchParams({ user: uri, status: "active", min_start_time: min, max_start_time: max, count: "100", sort: "start_time:asc" });
  const evRes = await fetch(`https://api.calendly.com/scheduled_events?${q}`, { headers: h });
  if (!evRes.ok) return { status: "error", detail: `scheduled_events ${evRes.status}`, events: [] };
  const evs = (await evRes.json()).collection ?? [];
  const events = await Promise.all(evs.map(async (e: any) => {
    let invitee = "";
    try {
      const iv = await (await fetch(`${e.uri}/invitees?count=5`, { headers: h })).json();
      invitee = (iv.collection ?? []).map((x: any) => x.name).join(", ");
    } catch { /* names are optional */ }
    const loc = e.location ?? {};
    const location = loc.join_url ? "Video" : loc.type === "inbound_call" || loc.type === "outbound_call" ? "Telefon" : (loc.location ?? "");
    return { start: e.start_time, end: e.end_time, name: e.name, invitee, location };
  }));
  return { status: "ok", events };
}

// Landing page analytics from PostHog (EU). Needs a personal API key with query:read as secret (name contains "POSTHOG").
async function analytics(daysReq: unknown) {
  const key = secret(["POSTHOG_API_KEY", "POSTHOG_KEY", "POSTHOG_PERSONAL_API_KEY"], /posthog/i);
  if (!key) return { status: "no_token" };
  const days = [7, 30, 90].includes(Number(daysReq)) ? Number(daysReq) : 30;
  const host = Deno.env.get("POSTHOG_HOST") ?? "https://eu.posthog.com";
  const project = Deno.env.get("POSTHOG_PROJECT") ?? "175210";
  const site = "(properties.site = 'flow-media-ai' OR properties.$pathname LIKE '/flow-media-ai/marketing/%')";
  const q = async (sql: string) => {
    const r = await fetch(`${host}/api/projects/${project}/query/`, {
      method: "POST", headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
      body: JSON.stringify({ query: { kind: "HogQLQuery", query: sql } }),
    });
    if (!r.ok) throw new Error(`posthog ${r.status}`);
    return (await r.json()).results as unknown[][];
  };
  const win = (from: number, to: number) => `timestamp > now() - INTERVAL ${from} DAY AND timestamp <= now() - INTERVAL ${to} DAY`;
  const kpiSql = (from: number, to: number) => `SELECT countIf(event = '$pageview'), uniqIf(properties.$session_id, event = '$pageview'),
      countIf(event = 'cta_click'), countIf(event = 'cta_click' AND properties.cta LIKE '%calendly%')
    FROM events WHERE ${site} AND ${win(from, to)}`;
  const [cur, prev, daily, refs, ctas, devices] = await Promise.all([
    q(kpiSql(days, 0)), q(kpiSql(days * 2, days)),
    q(`SELECT toString(toDate(timestamp)) AS d, countIf(event = '$pageview'), uniqIf(properties.$session_id, event = '$pageview'), countIf(event = 'cta_click')
       FROM events WHERE ${site} AND ${win(days, 0)} GROUP BY d ORDER BY d`),
    q(`SELECT coalesce(nullIf(properties.utm_source, ''), nullIf(properties.$referring_domain, ''), '$direct') AS src, count()
       FROM events WHERE event = '$pageview' AND ${site} AND ${win(days, 0)} GROUP BY src ORDER BY count() DESC LIMIT 8`),
    q(`SELECT properties.cta, count() FROM events WHERE event = 'cta_click' AND ${site} AND ${win(days, 0)} GROUP BY properties.cta ORDER BY count() DESC LIMIT 8`),
    q(`SELECT coalesce(properties.$device_type, 'Unbekannt'), count() FROM events WHERE event = '$pageview' AND ${site} AND ${win(days, 0)} GROUP BY 1 ORDER BY 2 DESC LIMIT 5`),
  ]);
  const k = (r: unknown[][]) => { const [pv, visits, cta, cal] = (r[0] ?? [0, 0, 0, 0]) as number[]; return { pv, visits, cta, cal }; };
  return { status: "ok", days, kpi: k(cur), prev: k(prev), daily, refs, ctas, devices, link: `${host}/project/${project}/web` };
}

// Folder listing of an allowed GitHub repo (token optional for public repos, required for private ones).
async function githubList(repoReq: unknown, pathReq: unknown) {
  const repos = (Deno.env.get("GITHUB_REPOS") ?? "MaikZ91/flow-media-ai").split(",").map((r) => r.trim()).filter(Boolean);
  const repo = typeof repoReq === "string" && repos.includes(repoReq) ? repoReq : repos[0];
  const path = typeof pathReq === "string" ? pathReq.replace(/^\/+|\/+$/g, "") : "";
  if (path.split("/").some((p) => p === ".." || p === ".")) return { error: "bad_request", status: 400 };
  const token = secret(["GITHUB_TOKEN", "GH_TOKEN", "GITHUB_PAT"], /^(github|gh)_/i);
  const headers: Record<string, string> = { Accept: "application/vnd.github+json", "User-Agent": "flow-board" };
  if (token) headers.Authorization = `Bearer ${token}`;
  const url = `https://api.github.com/repos/${repo}/contents/${path.split("/").map(encodeURIComponent).join("/")}`;
  const r = await fetch(url, { headers });
  if (r.status === 404) return { error: "not_found", status: 404 };
  if (r.status === 403 || r.status === 429) return { error: "rate_limited", status: 429 };
  if (!r.ok) return { error: "github", status: 502 };
  const data = await r.json();
  const list = Array.isArray(data) ? data : [data];
  return { repo, repos, path, entries: list.map((e: any) => ({ name: e.name, path: e.path, type: e.type, size: e.size, html_url: e.html_url })) };
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return json({ error: "method" }, 405);
  let body: any;
  try { body = await req.json(); } catch { return json({ error: "bad_json" }, 400); }
  const { board, key, action } = body ?? {};
  if (typeof board !== "string" || typeof key !== "string" || key.length < 16) return json({ error: "denied" }, 403);

  const { data: b } = await db.from("flow_board_boards").select("key_hash").eq("id", board).maybeSingle();
  if (!b || b.key_hash !== await sha256(key)) return json({ error: "denied" }, 403);
  const prefix = `boards/${board}/`;

  try {
    switch (action) {
      case "load": {
        const [t, f, m, fin] = await Promise.all([
          db.from("flow_board_tasks").select("id,data").eq("board_id", board),
          db.from("flow_board_files").select("id,data").eq("board_id", board),
          db.from("flow_board_meta").select("data").eq("board_id", board).maybeSingle(),
          db.from("flow_board_finance").select("id,data").eq("board_id", board),
        ]);
        if (t.error || f.error || fin.error) throw t.error || f.error || fin.error;
        return json({ tasks: t.data, files: f.data, meta: m.data?.data ?? null, finance: fin.data });
      }
      case "upsert": {
        const table = TABLES[body.table];
        if (!table || typeof body.id !== "string" || typeof body.data !== "object") return json({ error: "bad_request" }, 400);
        const { data: existing } = await db.from(table).select("board_id").eq("id", body.id).maybeSingle();
        if (existing && existing.board_id !== board) return json({ error: "denied" }, 403);
        const r = await db.from(table).upsert({ id: body.id, board_id: board, data: body.data, updated_at: new Date().toISOString() });
        if (r.error) throw r.error;
        return json({ ok: true });
      }
      case "delete": {
        const table = TABLES[body.table];
        if (!table || typeof body.id !== "string") return json({ error: "bad_request" }, 400);
        const r = await db.from(table).delete().eq("id", body.id).eq("board_id", board);
        if (r.error) throw r.error;
        return json({ ok: true });
      }
      case "meta": {
        if (typeof body.data !== "object") return json({ error: "bad_request" }, 400);
        const r = await db.from("flow_board_meta").upsert({ board_id: board, data: body.data, updated_at: new Date().toISOString() }, { onConflict: "board_id" });
        if (r.error) throw r.error;
        return json({ ok: true });
      }
      case "upload": {
        const name = String(body.name || "datei").replace(/[^\w.\-]+/g, "_").slice(-80);
        const path = `${prefix}${crypto.randomUUID()}-${name}`;
        const r = await db.storage.from(BUCKET).createSignedUploadUrl(path);
        if (r.error) throw r.error;
        return json({ path, token: r.data.token });
      }
      case "sign": {
        const paths = (Array.isArray(body.paths) ? body.paths : []).filter((p: unknown) => typeof p === "string" && p.startsWith(prefix)).slice(0, 200);
        if (!paths.length) return json({ urls: [] });
        const r = await db.storage.from(BUCKET).createSignedUrls(paths, 60 * 60 * 12);
        if (r.error) throw r.error;
        return json({ urls: r.data.map((x) => ({ path: x.path, url: x.signedUrl })) });
      }
      case "remove": {
        if (typeof body.path !== "string" || !body.path.startsWith(prefix)) return json({ error: "denied" }, 403);
        const r = await db.storage.from(BUCKET).remove([body.path]);
        if (r.error) throw r.error;
        return json({ ok: true });
      }
      case "calendly":
        return json(await calendlyEvents());
      case "analytics": {
        try { return json(await analytics(body.days)); } catch (e) { return json({ status: "error", message: String((e as any)?.message ?? e) }); }
      }
      case "gh_list": {
        const r = await githubList(body.repo, body.path);
        return "error" in r ? json({ error: r.error }, r.status as number) : json(r);
      }
      default:
        return json({ error: "unknown_action" }, 400);
    }
  } catch (e) {
    return json({ error: "server", message: String((e as any)?.message ?? e) }, 500);
  }
});
