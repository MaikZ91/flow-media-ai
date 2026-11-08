# Transcribes a video or audio file to text for the brand-builder skill (Claude Code only).
# usage: python3 transcribe.py <video-or-audio> [model]   -> writes <name>.transkript.txt next to the input
# Needs: pip install faster-whisper (first run downloads the model, "small" ~ 500 MB); ffmpeg is used if installed.
import os, subprocess, sys, tempfile

import numpy as np
from faster_whisper import WhisperModel

src = sys.argv[1]
model_name = sys.argv[2] if len(sys.argv) > 2 else "small"


def load_audio(path):
    # 16 kHz mono float32; ffmpeg when available, else the decoder bundled with faster-whisper
    try:
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                             check=True, capture_output=True).stdout
        return np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0
    except (FileNotFoundError, subprocess.CalledProcessError):
        from faster_whisper.audio import decode_audio
        return decode_audio(path, sampling_rate=16000)


audio = load_audio(src)
model = WhisperModel(model_name, device="cpu", compute_type="int8")
segments, info = model.transcribe(audio, language=None, vad_filter=True)
text = "\n".join(s.text.strip() for s in segments)

out = os.path.splitext(src)[0] + ".transkript.txt"
with open(out, "w", encoding="utf-8") as f:
    f.write(text + "\n")
print(f"Sprache: {info.language} · Dauer: {info.duration:.0f} s · Transkript: {out}")
