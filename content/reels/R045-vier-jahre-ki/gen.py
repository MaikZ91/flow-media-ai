# Baut time.html aus der 3D-Technik von R044 (space.html) plus den neuen Modellen, Szenen und Texten.
import re
src = open("../R044-ki-im-all/space.html").read()
js = src.split('<script type="module">', 1)[1]
A = js.split("/* ---------- Schwarm ---------- */")[0]
K = js.split("/* ---------- Kamera-Helfer ---------- */")[1].split("/* ---------- Szenen ---------- */")[0]
A = re.sub(r"const W=1080,H=1920,B=60/129\.01, BEATS=\[[^\]]*\], T=BEATS\.map\(b=>b\*B\);\nwindow\.TOTAL=T\[9\]; window\.T=T;",
           "const W=1080,H=1920,B=60/134.02, BEATS=[0,5,11,16,21,27,32,34,38,42,46,50,54,62,68], T=BEATS.map(b=>b*B);\nwindow.TOTAL=T[14]; window.T=T;", A)
assert "134.02" in A
A = A.replace("import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';", "import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';")
K = re.sub(r"const show=\(\.\.\.o\)=>\{[^\n]*\n", "", K)
assert "const show" not in K
head = src.split("<canvas", 1)[0]
head = head.replace("</style></head><body>", open("extra.css").read() + "</style></head><body>")
out = head + open("dom.html").read() + '\n<script type="module">' + A + open("models.js").read() + "\n/* ---------- Kamera-Helfer ---------- */" + K + open("scenes.js").read() + "\n</script></body></html>\n"
open("time.html", "w").write(out)
print(len(out))
