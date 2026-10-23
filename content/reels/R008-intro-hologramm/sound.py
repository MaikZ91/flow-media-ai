"""Synthesized sound design for the Flow Media AI hologram intro (no samples, no licences)."""
import numpy as np
from scipy.signal import butter, sosfilt
import wave

SR, T = 48000, 14.0
n = int(SR * T)
t = np.arange(n) / SR
rng = np.random.default_rng(7)
L = np.zeros(n); Rr = np.zeros(n)

def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], btype="band", fs=SR, output="sos"), x)
def lp(x, f, order=2):
    return sosfilt(butter(order, f, btype="low", fs=SR, output="sos"), x)
def hp(x, f, order=2):
    return sosfilt(butter(order, f, btype="high", fs=SR, output="sos"), x)
def env(t0, a, d, length=None):
    e = np.zeros(n); i0 = int(t0 * SR); ia = int(a * SR); idd = int(d * SR)
    seg = np.concatenate([np.linspace(0, 1, max(ia, 1)), np.exp(-np.linspace(0, 6, max(idd, 1)))])
    seg = seg[: n - i0]; e[i0:i0 + len(seg)] = seg; return e
def add(sig, pan=0.0, g=1.0):
    global L, Rr
    L += sig * g * (1 - pan) ** .5 if pan > 0 else sig * g
    Rr += sig * g * (1 + pan) ** .5 if pan < 0 else sig * g

# drone: low fifths with slow movement, swells into the logo
dr_env = np.clip(t / 1.5, 0, 1) * (0.55 + 0.45 * np.clip((t - 1.2) / 9, 0, 1)) * np.clip((T - t) / 1.5, 0, 1)
drone = sum(np.sin(2 * np.pi * f * t + 0.3 * np.sin(2 * np.pi * .1 * t * k)) / k for k, f in enumerate([55, 82.5, 110, 164.8], 1))
saw = lp(2 * ((t * 55.3) % 1) - 1, 220)
add((drone * .35 + saw * .25) * dr_env, g=.5)

# warp whoosh at the start: band noise sweeping upward
noise = rng.standard_normal(n)
sweep = np.zeros(n)
for k, (a, b) in enumerate([(200, 600), (500, 1400), (1200, 3200), (2500, 7000)]):
    seg = bp(noise, a, b) * np.clip(1 - np.abs(t - (0.15 + k * .25)) / .35, 0, 1)
    sweep += seg
add(sweep * np.clip((1.2 - t) / 1.2, 0, 1) * 0.6, g=.6)

# assembly riser 1.2–3.8: rising noise + rising tone
rise = np.clip((t - 1.2) / 2.6, 0, 1) * (t < 3.85)
cut = 300 + 5000 * rise
riser = np.zeros(n)
for lo in [300, 900, 2000, 4000]:
    riser += bp(noise, lo, lo * 2.2) * np.clip(1 - np.abs(cut - lo * 1.5) / (lo * 1.5), 0, 1)
tone_f = 180 + 700 * rise ** 2
tone = np.sin(2 * np.pi * np.cumsum(tone_f) / SR) * rise * (t < 3.85)
add(riser * rise * .5 + tone * .12, g=.7)

def boom(t0, g=1.0, f0=110, f1=34, dur=1.2):
    i0 = int(t0 * SR); m = int(dur * SR); tt = np.arange(m) / SR
    f = f1 + (f0 - f1) * np.exp(-tt * 5)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 3.2)
    click = rng.standard_normal(m) * np.exp(-tt * 90) * .5
    sig = np.zeros(n); seg = (s + lp(click, 3000)) * g; sig[i0:i0 + m] = seg[: n - i0]; return sig

def zap(t0, g=1.0, dur=.35, seed=0):
    r = np.random.default_rng(seed); i0 = int(t0 * SR); m = int(dur * SR); tt = np.arange(m) / SR
    gate = (np.sin(2 * np.pi * (60 + 140 * r.random()) * tt + r.random() * 6) > r.uniform(-.2, .4)).astype(float)
    crack = hp(r.standard_normal(m), 1800) * gate * np.exp(-tt * 9)
    buzz = np.sign(np.sin(2 * np.pi * 95 * tt)) * np.exp(-tt * 12) * .15
    sig = np.zeros(n); seg = (crack + buzz) * g; sig[i0:i0 + m] = seg[: n - i0]; return sig

def thunder(t0, g=1.0, seed=0):
    r = np.random.default_rng(seed + 50); i0 = int(t0 * SR); m = int(2.2 * SR); tt = np.arange(m) / SR
    s = lp(r.standard_normal(m), 180, 4) * (np.exp(-tt * 1.8)) * (1 + .5 * np.sin(2 * np.pi * 3 * tt))
    sig = np.zeros(n); seg = s * g * 3; sig[i0:i0 + m] = seg[: n - i0]; return sig

strikes = [(0.55, .5, -.6), (1.15, 1.0, 0), (4.30, .55, -.4), (5.20, .55, .4), (6.0, .8, 0), (7.2, .8, 0), (8.4, .8, 0), (10.4, 1.0, -.2), (10.48, .9, .2)]
for k, (ts, s, pan) in enumerate(strikes):
    add(zap(ts, s * .55, seed=k), pan=pan)
    add(thunder(ts, s * .5, seed=k), pan=pan * .5)
for ts, s in [(1.15, 1.0), (6.0, .8), (7.2, .8), (8.4, .9), (10.4, 1.3)]:
    add(boom(ts, s), g=.9)

# glitch blips while the hologram glitches
for k in range(26):
    ts = 3.9 + rng.random() * 6.2; i0 = int(ts * SR); m = int(.04 * SR)
    blip = np.sign(np.sin(2 * np.pi * rng.uniform(600, 2400) * np.arange(m) / SR)) * .05
    s = np.zeros(n); s[i0:i0 + m] = blip; add(s, pan=rng.uniform(-.7, .7))

# shimmer on the logo
sh = sum(np.sin(2 * np.pi * f * t) * (1 + .5 * np.sin(2 * np.pi * 6 * t + f)) for f in [1318.5, 1760, 2637]) / 3
add(sh * env(10.4, .05, 3.4) * .16, g=1)
# sub swell before the logo
add(np.sin(2 * np.pi * 41 * t) * np.clip((t - 9.4) / 1.0, 0, 1) * (t < 10.4) * .35)

mix = np.stack([L, Rr], 1)
mix = np.tanh(mix * 1.4) / np.tanh(1.4)
mix /= np.max(np.abs(mix)) * 1.08
fade = np.clip((T - t) / .8, 0, 1)[:, None]
mix *= fade
with wave.open("sound.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype(np.int16).tobytes())
print("ok", mix.shape)
