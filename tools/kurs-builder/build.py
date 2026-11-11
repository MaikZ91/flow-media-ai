#!/usr/bin/env python3
"""Baut die Flow-DNA-Kurse aus inhalte.py: je Lektion ein animiertes Video (1280x800, KI-Stimme, Untertitel)
und die Kursdaten flow-dna/kurse-auto.js (werden in window.FLOW_KURSE gemischt).
Aufruf: python3 build.py [kurs-id ...] [--nur-daten]   Stimme: edge-tts (de-DE-FlorianMultilingualNeural), gekennzeichnet als KI-Stimme."""
import asyncio, hashlib, json, os, ssl, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", ".."); DNA = os.path.join(ROOT, "flow-dna")
CACHE = os.environ.get("KURS_CACHE", os.path.join(HERE, ".cache")); os.makedirs(CACHE, exist_ok=True)
sys.path.insert(0, HERE)
from inhalte import KURSE
VOICE, RATE, FPS = "de-DE-FlorianMultilingualNeural", "+6%", 20

def tts(text):
    f = os.path.join(CACHE, hashlib.sha1((VOICE + RATE + text).encode()).hexdigest()[:16] + ".mp3")
    if not (os.path.exists(f) and os.path.getsize(f) > 500):
        import edge_tts
        from edge_tts import communicate
        ca = os.environ.get("KURS_CA")
        if ca: communicate._SSL_CTX = ssl.create_default_context(cafile=ca)
        for k in range(4):
            try: asyncio.run(edge_tts.Communicate(text, VOICE, rate=RATE).save(f)); break
            except Exception as e:
                if k == 3: raise
    d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode().strip())
    return f, d

def sprech(t):  # Aussprache-Hilfen, der Untertitel zeigt weiter den Originaltext
    for a, b in ((".claude/skills", "Punkt Claude, Skills"), ("CLAUDE.md", "Claude Punkt M D"), ("SKILL.md", "Skill Punkt M D"), ("GitHub Pages", "Git Hab Pages"), ("GitHub", "Git Hab"), ("1:1", "eins zu eins"), ("z. B.", "zum Beispiel"), ("UTM", "U T M"), ("CTA", "Call to Action")):
        t = t.replace(a, b)
    return t

def video(kid, nr, vid, crumb, scenes, force=False):
    out = os.path.join(DNA, "kurse", kid, "videos"); os.makedirs(out, exist_ok=True)
    mp4, jpg = os.path.join(out, vid + ".mp4"), os.path.join(out, vid + ".jpg")
    sig = hashlib.sha1(json.dumps([crumb, scenes], ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    sigf = os.path.join(CACHE, f"{kid}-{vid}.sig")
    if not force and os.path.exists(mp4) and os.path.exists(sigf) and open(sigf).read() == sig: return
    t, sc, aud = 0.0, [], []
    for s in scenes:
        f, d = tts(sprech(s["say"])); dur = round(max(3.0, d + 0.75), 2)
        sc.append({**s, "start": round(t, 2), "dur": dur}); aud.append((f, t + 0.25)); t += dur
    total = round(t + 0.4, 2)
    data = os.path.join(CACHE, f"{kid}-{vid}.json"); json.dump({"crumb": crumb, "scenes": sc, "total": total}, open(data, "w"), ensure_ascii=False)
    wav = os.path.join(CACHE, f"{kid}-{vid}.m4a")
    inp, fc = [], ""
    for i, (f, st) in enumerate(aud): inp += ["-i", f]; fc += f"[{i}:a]adelay={int(st*1000)}|{int(st*1000)}[a{i}];"
    fc += "".join(f"[a{i}]" for i in range(len(aud))) + f"amix=inputs={len(aud)}:normalize=0,highpass=f=80,loudnorm=I=-16:TP=-1.5,apad=whole_dur={total}[a]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", fc, "-map", "[a]", "-t", str(total), "-c:a", "aac", "-b:a", "96k", wav], check=True)
    poster_t = sc[0]["start"] + sc[0]["dur"] - 0.6
    subprocess.run(["node", os.path.join(HERE, "render.js"), data, wav, mp4, jpg, str(FPS), str(poster_t)], check=True)
    open(sigf, "w").write(sig); print("✓", kid, vid, f"{total:.0f}s", flush=True)

def daten():
    res = {}
    for kid, k in KURSE.items():
        base = f"kurse/{kid}/videos/"; secs = 0
        def dur(v):
            p = os.path.join(DNA, base, v + ".mp4")
            return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).decode()) if os.path.exists(p) else 0
        secs += dur("L00"); lek = []
        for i, l in enumerate(k["lektionen"], 1):
            v = f"L{i:02d}"; secs += dur(v)
            e = {"videos": [[base + v + ".mp4", base + v + ".jpg", l["titel"]]], "text": l["text"], "punkte": l["punkte"], "aufgabe": l["aufgabe"]}
            for f in ("prompt", "links", "optional", "bonus", "beispiele"):
                if l.get(f): e[f] = l[f]
            lek.append(e)
        res[kid] = {"status": "live", "code": k["code"], "dauer": f"ca. {max(1, round(secs/60))} Min. Video · {k['umsetzen']} Umsetzen",
                    "hinweis": "Animierte Videos mit KI-Stimme (gekennzeichnet). Jede Lektion endet mit einer Aufgabe.",
                    "intro": {"video": base + "L00.mp4", "poster": base + "L00.jpg", "titel": k["intro"]["titel"]},
                    "module": [l["titel"] for l in k["lektionen"]], "lektionen": lek, "spick": k["spick"], "faq": k["faq"], "ende": k["ende"]}
        if k.get("special"): res[kid]["special"] = k["special"]
    js = ("// Automatisch erzeugt von tools/kurs-builder/build.py – nicht von Hand ändern. Inhalte: tools/kurs-builder/inhalte.py\n"
          "(function(){var A=" + json.dumps(res, ensure_ascii=False) + ";var K=(window.FLOW_KURSE||{}).kurse||[];K.forEach(function(k){if(A[k.id])Object.assign(k,A[k.id])});if(window.FLOW_KURSE)window.FLOW_KURSE.hinweis=\"Zehn Kurse, kurz und zum Mitmachen: Jede Lektion hat ein Video, einen Prompt zum Kopieren und eine Aufgabe. Das Intro kannst du bei jedem Kurs kostenlos ansehen.\"})();\n")
    open(os.path.join(DNA, "kurse-auto.js"), "w", encoding="utf-8").write(js); print("kurse-auto.js", len(js))

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--nur-daten" not in sys.argv:
        for kid, k in KURSE.items():
            if args and kid not in args: continue
            video(kid, k["nr"], "L00", f"Kurs {k['nr']} · Intro", k["intro"]["scenes"])
            for i, l in enumerate(k["lektionen"], 1):
                task = {"k": "title", "kicker": f"Lektion {i:02d} · Deine Aufgabe", "h": "Jetzt *du.*", "say": "Deine Aufgabe: " + l["aufgabe"], "size": None, "pic": False}
                video(kid, k["nr"], f"L{i:02d}", f"Kurs {k['nr']} · Lektion {i:02d} · {l['titel']}", l["scenes"] + [task])
    daten()
