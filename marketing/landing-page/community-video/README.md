# Community-Video auf der Landingpage (20.11.2026)

Maiks Selfie-Video (24 s → 19,5 s) mit dem Video Cutter v2 geschnitten: Ähms, Pausen und langgezogene „und…“ raus, Look `klar`, Wort-Untertitel, Namensschild, „Flow Business Community“, Chips Gründer/Selbstständige und KI/Business/Workshops. Am Ende eine **HyperFrames**-Komposition (`flowcard/`, HTML + GSAP, transparent gerendert) als End-Karte „Flow Business Community · Jetzt beitreten“. Musik: „Motivating Mornings“ (Mixkit, frei), leise.

Auf der Seite: `img/community.mp4` (720p) mit `img/community-poster.jpg`, startet stumm beim Hinscrollen, „Ton an“ spielt von vorn mit Ton (PostHog-Event `community_video_sound`).
Neu bauen: Video Cutter aus Drive (`07_KI/skills/flow-dna-premium/video-cutting/`), `cuts.json` und `plan.json` von hier, `flowcard/` neben dem Rohvideo.
