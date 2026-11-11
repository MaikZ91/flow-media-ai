# Inhalte aller automatisch gebauten Kurse (Kurs 03 ist von Hand gebaut und steht in flow-dna/kurse.js).
import importlib
KURSE = {}
for kid, mod in [("ki-basics", "k01"), ("personal-brand", "k02"), ("erste-app", "k04"), ("claude-code", "k05"), ("content-system", "k06"), ("automation", "k07"), ("skills", "k08"), ("flow-methode", "k09"), ("kunden-gewinnen", "k10")]:
    try: KURSE[kid] = importlib.import_module(mod).KURS
    except ModuleNotFoundError: pass
