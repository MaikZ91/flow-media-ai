# Bertrand's voice: Piper TTS (German "thorsten" high, dataset CC0), pitched down with a little bass, compression and room.
# usage: python3 say.py "Text" out.wav
# Needs: pip install piper-tts; model files de_DE-thorsten-high.onnx(+.json) next to this script
#   (https://huggingface.co/rhasspy/piper-voices/tree/main/de/de_DE/thorsten/high); ffmpeg.
import os, subprocess, sys, tempfile, wave

from piper import PiperVoice

HERE = os.path.dirname(os.path.abspath(__file__))
text, out = sys.argv[1], sys.argv[2]
voice = PiperVoice.load(os.path.join(HERE, "de_DE-thorsten-high.onnx"))
raw = tempfile.mktemp(suffix=".wav")
with wave.open(raw, "wb") as w:
    voice.synthesize_wav(text, w)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-af",
                "asetrate=22050*0.86,aresample=44100,atempo=1.08,bass=g=4:f=120,"
                "acompressor=threshold=0.1:ratio=3,aecho=0.6:0.3:25:0.12,loudnorm=I=-16", out], check=True)
os.remove(raw)
print(out)
