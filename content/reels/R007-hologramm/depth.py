"""Depth map for the hologram: Depth Anything V2 (small) on Maik's portrait, contrast stretched on the person."""
import sys
import numpy as np
from PIL import Image, ImageFilter
from transformers import pipeline

src = sys.argv[1]  # e.g. ../R005-gleicher-look/img/portrait_front.jpg (1080x1920)
d = pipeline("depth-estimation", model="depth-anything/Depth-Anything-V2-Small-hf")(Image.open(src))["depth"]
d = np.asarray(d.convert("L").crop((0, 0, 1080, 1440)).resize((600, 800), Image.LANCZOS), dtype=np.float32) / 255
fg = d > 0.38
lo, hi = np.percentile(d[fg], [2, 99.5])
out = np.where(fg, .45 + .55 * np.clip((d - lo) / (hi - lo), 0, 1) ** 1.2, d * .75)
Image.fromarray((out * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2)).save("depth.png")
Image.open(src).convert("L").crop((0, 0, 1080, 1440)).resize((600, 800), Image.LANCZOS).save("photo.png")
