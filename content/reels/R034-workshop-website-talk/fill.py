import json
c=json.load(open("cuts.json"));caps=json.load(open("captions.json"))
s=open("overlay.tpl.html").read().replace("__CUTS__",json.dumps(c["cuts"])).replace("__CAPS__",json.dumps(caps,ensure_ascii=False)).replace("__TOTAL__",str(c["total"]))
open("overlay.html","w").write(s)
