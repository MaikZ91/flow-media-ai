#!/usr/bin/env python3
"""Kurz-Tutorial „So benutzt du den Video Cutter“ für die Skill-Seite im Flow DNA Store (mit Lisa, erfundenes Beispiel).
Aufruf: KURS_CA=… KURS_CACHE=… python3 howto_video_cutter.py  -> flow-dna/media/howto-video-cutting.mp4/.jpg"""
import os, shutil
from szenen import *
from build import video, DNA
S = [
 T("Flow DNA Skill · So geht's", "Du filmst. Die KI *schneidet.*", "Du filmst dich selbst – und der Video Cutter macht daraus ein fertiges Reel. So benutzt du ihn.", size="m"),
 LI("Lisa lädt den Skill", "Lisa gibt beim Skill ihren Code ein und lädt die Datei. Sie legt sie in ihrem Projekt in den Ordner Skills, Video Cutting.", act="type", items=["Code beim Skill eingeben", "Datei SKILL.md laden", "In den Ordner skills/video-cutting legen"], kicker="Schritt 1"),
 LI("Lisa filmt sich", "Dann filmt sie sich mit dem Handy und redet einfach drauflos. Versprecher sind egal. Das Video legt sie in ihren Projektordner.", act="photo", items=["Selfie-Video, einfach drauflos reden", "Versprecher sind egal", "Video in den Projektordner legen"], kicker="Schritt 2"),
 LI("Ein Satz genügt", "In Claude Code oder Codex schreibt sie einen Satz: Schneide mein Video zu einem Reel.", act="type", text="Schneide mein Video rueckenkurs.mov\nzu einem Reel. Untertitel in meiner Farbe,\nMusik leise darunter.", bar="Claude Code", note=("Tipp", "Farbe und Musik sind freiwillig."), kicker="Schritt 3"),
 ST("Das passiert von selbst", ["Transkript", "Ähms raus", "Hochformat", "Untertitel", "Musik & Ton"], "Der Rest passiert von selbst: Die KI schreibt mit, schneidet Ähms und Pausen heraus, bringt das Video ins Hochformat, setzt Untertitel und legt Musik unter deine Stimme."),
 LI("Lisa sagt, was anders soll", "Am Ende schaut Lisa das Ergebnis an und sagt, was anders soll. Dann ist ihr Reel fertig.", act="check", items=["Ergebnis ansehen", "„Schnitt drei raus“", "„Untertitel tiefer“", "Fertig: reel.mp4"], kicker="Schritt 4"),
 M("Einfach reden. Den Rest macht der *Skill.*", "Merk dir: Du redest einfach drauflos. Den Rest macht der Skill."),
]
if __name__ == "__main__":
    video("_howto", "", "video-cutting", "Flow DNA · Video Cutter · So geht's", S)
    src = os.path.join(DNA, "kurse", "_howto", "videos"); dst = os.path.join(DNA, "media")
    for e in ("mp4", "jpg"): shutil.move(os.path.join(src, "video-cutting." + e), os.path.join(dst, "howto-video-cutting." + e))
    shutil.rmtree(os.path.join(DNA, "kurse", "_howto")); print("ok")
