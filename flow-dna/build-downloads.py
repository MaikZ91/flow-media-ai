# Baut für jeden Free-Skill eine ZIP zum direkten Download: downloads/<id>.zip mit Ordner <skill-name>/…
# Aufruf: python3 build-downloads.py   (nach jeder Änderung an skills/)
import os, re, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
SRC, OUT = os.path.join(HERE, "skills"), os.path.join(HERE, "downloads")
os.makedirs(OUT, exist_ok=True)
for d in sorted(os.listdir(SRC)):
    p = os.path.join(SRC, d)
    if not os.path.isdir(p): continue
    md = open(os.path.join(p, "SKILL.md"), encoding="utf-8").read()
    name = re.search(r"^name:\s*(\S+)", md, re.M).group(1)
    z = os.path.join(OUT, d + ".zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(p):
            for f in sorted(files):
                fp = os.path.join(root, f)
                zf.write(fp, os.path.join(name, os.path.relpath(fp, p)))
        zf.write(os.path.join(SRC, "INSTALLATION.md"), os.path.join(name, "INSTALLATION.md"))
    print(d, "→", name, os.path.getsize(z), "B")
