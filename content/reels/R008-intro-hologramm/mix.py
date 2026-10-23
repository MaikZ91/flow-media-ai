"""Audio for the boot intro: MZ.9 track (Dcony8, 69.0-84.0 s, drop at 73.0 s) + AI system voice + impacts."""
import numpy as np, wave, subprocess
from scipy.signal import butter, sosfilt
SR = 48000; T = 15.0; n = int(SR * T); D = 4.0; B = 60 / 143.55
def readwav(p):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-f", "s16le", "-ac", "2", "-ar", str(SR), "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.int16).reshape(-1, 2).astype(np.float32) / 32768
music = readwav("../../musik/eigene/mz9_track_Dcony8.m4a")[int(69.0 * SR):int(69.0 * SR) + n]
music = np.pad(music, ((0, n - len(music)), (0, 0)))
t = np.arange(n) / SR
mix = music * 0.9
fade = np.clip(t / .3, 0, 1) * np.clip((T - t) / 1.2, 0, 1)
voices = [(0.25, "voice/p0.wav"), (2.05, "voice/p1.wav"), (D + 2 * B + .03, "voice/p2.wav"), (D + 6 * B + .03, "voice/p3.wav"), (D + 10 * B + .03, "voice/p4.wav"), (D + 16 * B + .2, "voice/p5.wav")]
duck = np.ones(n)
vtrack = np.zeros((n, 2))
for ts, p in voices:
    v = readwav(p); i0 = int(ts * SR); m = min(len(v), n - i0); vtrack[i0:i0 + m] += v[:m] * 1.15
    duck[i0:i0 + m] = np.minimum(duck[i0:i0 + m], .55)
duck = np.convolve(duck, np.ones(2400) / 2400, mode="same")
mix = mix * duck[:, None] + vtrack
rng = np.random.default_rng(3)
def lp(x, f): return sosfilt(butter(2, f, btype="low", fs=SR, output="sos"), x)
def boom(t0, g):
    m = int(1.4 * SR); tt = np.arange(m) / SR; f = 32 + 90 * np.exp(-tt * 5)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 3) + lp(rng.standard_normal(m), 2500) * np.exp(-tt * 40) * .4
    out = np.zeros(n); i0 = int(t0 * SR); out[i0:i0 + m] = (s * g)[: n - i0]; return out
def zap(t0, g):
    m = int(.3 * SR); tt = np.arange(m) / SR
    gate = (np.sin(2 * np.pi * 140 * tt + rng.random() * 6) > .1).astype(float)
    s = sosfilt(butter(2, 2000, btype="high", fs=SR, output="sos"), rng.standard_normal(m)) * gate * np.exp(-tt * 10)
    out = np.zeros(n); i0 = int(t0 * SR); out[i0:i0 + m] = (s * g)[: n - i0]; return out
fx = boom(D, .9) + boom(D + 16 * B, 1.0) + zap(D, .35) + zap(D + 16 * B, .35) + zap(D + 16 * B + .06, .3)
for k in (2, 6, 10): fx += zap(D + k * B, .25) + boom(D + k * B, .35)
mix += fx[:, None] * .6
# short riser into the drop
rise = np.clip((t - 2.6) / 1.4, 0, 1) * (t < D)
mix += (sosfilt(butter(2, [800, 6000], btype="band", fs=SR, output="sos"), rng.standard_normal(n)) * rise ** 2 * .12)[:, None]
mix *= fade[:, None]
mix = np.tanh(mix * 1.3) / np.tanh(1.3); mix /= np.max(np.abs(mix)) * 1.05
with wave.open("mix.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
print("ok")
