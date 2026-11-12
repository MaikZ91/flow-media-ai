# Kurze Helfer für Szenen (siehe anim.html): jede Szene hat einen Sprechtext `say` (KI-Stimme, spricht nie als Maik).
def T(kicker, h, say, size=None, pic=False): return {"k": "title", "kicker": kicker, "h": h, "say": say, "size": size, "pic": pic}
def C(h, items, say, kicker=""): return {"k": "cards", "h": h, "items": items, "say": say, "kicker": kicker}
def CH(h, items, say, on=(), kicker=""): return {"k": "chips", "h": h, "items": items, "say": say, "on": list(on), "kicker": kicker}
def P(h, text, say, note=None, bar="claude", kicker="Dein Prompt"): return {"k": "prompt", "h": h, "text": text, "say": say, "note": note, "bar": bar, "kicker": kicker}
def TR(h, text, say, note=None, bar="ordner", kicker="So sieht's aus"): return {"k": "tree", "h": h, "text": text, "say": say, "note": note, "bar": bar, "kicker": kicker}
def VS(h, a, b, say, kicker=""): return {"k": "vs", "h": h, "a": a, "b": b, "say": say, "kicker": kicker}
def L(h, items, say, kicker=""): return {"k": "list", "h": h, "items": items, "say": say, "kicker": kicker}
def ST(h, items, say, kicker=""): return {"k": "steps", "h": h, "items": items, "say": say, "kicker": kicker}
def SP(h, stamp, say, kicker=""): return {"k": "stamp", "h": h, "stamp": stamp, "say": say, "kicker": kicker}
def N(num, h, say, kicker=""): return {"k": "num", "num": num, "h": h, "say": say, "kicker": kicker}
def SH(h, img, fx, fy, say, items=(), tag="Hier", src="", bar="", zoom=1.7, ar=1.0, kicker="So sieht's aus"):
    """Original-Bildschirmfoto im App-Fenster: Zoom auf (fx, fy) in Prozent, blauer Kreis + Marke an der Stelle."""
    return {"k": "shot", "h": h, "img": img, "fx": fx, "fy": fy, "say": say, "items": list(items), "tag": tag, "src": src, "bar": bar, "zoom": zoom, "ar": ar, "kicker": kicker}
SUPPORT = ["Ich hänge fest.", "Frag in der Tech-Support-Gruppe (Tab Community) – dort helfen Maik und die Community."]
