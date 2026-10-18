import subprocess, math, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S=sys.argv[1]; FONT='/home/user/the-tribe-bot/instagram_autopilot/fonts/Geist-Bold.ttf'
FONT_M='/home/user/the-tribe-bot/instagram_autopilot/fonts/Geist-Medium.ttf'
W,H,FPS=1080,1920,30
def load(n):
    im=Image.open(f'{S}/shots/{n}.png').convert('RGB')
    if im.width!=W: im=im.resize((W,int(im.height*W/im.width)))
    if im.height<H:
        bg=Image.new('RGB',(W,H),im.getpixel((5,im.height-5))); bg.paste(im,(0,0)); im=bg
    return im
cache={}
def page(n):
    if n not in cache: cache[n]=load(n)
    return cache[n]
def ease(t): return t*t*(3-2*t)
START={'mz9':300}
def scroll_frame(n,t,depth=1800):
    im=page(n); y0=START.get(n,0); maxy=min(im.height-H-y0,depth); y=y0+(int(maxy*ease(t)) if maxy>0 else 0)
    return im.crop((0,y,W,y+H))
def zoom(im,s):
    if s==1: return im
    w,h=int(W/s),int(H/s); x,y=(W-w)//2,(H-h)//2
    return im.crop((x,y,x+w,y+h)).resize((W,H))
def textbox(fr,lines,y,size=92,sub=None,alpha=1.0):
    d=ImageDraw.Draw(fr,'RGBA'); f=ImageFont.truetype(FONT,size)
    pad=36; lh=int(size*1.12)
    widths=[d.textlength(l,font=f) for l in lines]; bw=max(widths)+2*pad; bh=lh*len(lines)+2*pad-int(size*.12)
    x=(W-bw)//2
    d.rounded_rectangle((x,y,x+bw,y+bh),radius=28,fill=(255,255,255,int(240*alpha)))
    for i,l in enumerate(lines):
        d.text(((W-widths[i])//2,y+pad+i*lh-int(size*.08)),l,font=f,fill=(17,17,17,int(255*alpha)))
    if sub:
        fs=ImageFont.truetype(FONT_M,44); sw=d.textlength(sub,font=fs)
        d.rounded_rectangle(((W-sw)//2-24,y+bh+22,(W+sw)//2+24,y+bh+22+76),radius=38,fill=(47,107,255,int(255*alpha)))
        d.text(((W-sw)//2,y+bh+36),sub,font=fs,fill=(255,255,255,int(255*alpha)))
    return fr
def label(fr,txt):
    d=ImageDraw.Draw(fr,'RGBA'); f=ImageFont.truetype(FONT,54); w=d.textlength(txt,font=f); y=1290
    d.rounded_rectangle((60,y,60+w+60,y+92),radius=46,fill=(47,107,255,255)); d.text((90,y+14),txt,font=f,fill=(255,255,255))
    return fr
def grid(cols,rows,names,t):
    fr=Image.new('RGB',(W,H),(245,244,240)); g=14
    cw=(W-g*(cols+1))//cols; ch=int(cw*16/9)
    total=rows*ch+g*(rows+1); off=(H-total)//2
    for i,n in enumerate(names[:cols*rows]):
        r,c=divmod(i,cols); im=page(n); y=int((im.height-H)*0.15*t) if im.height>H else 0
        tile=im.crop((0,max(0,y),W,max(0,y)+H)).resize((cw,ch))
        fr.paste(tile,(g+c*(cw+g),off+g+r*(ch+g)))
    return fr

HOOK=['index','cinematic','premium','wine-walk','supper-club','germany','techno-paint','app']
SEQ=[('cinematic','Community-Landingpage',1.1),('wine-walk','Event mit Ticket',1.0),('app','Ausgeh-App',1.0),
     ('mz9','Agentur-Website',0.9),('supper-club','Event-Seite',0.8),('germany','Städte-Übersicht',0.75),
     ('tools','Tool-Sammlung',0.7),('techno-paint',None,0.45),('sauna',None,0.4),('pub-crawl',None,0.35),('hosted',None,0.35),('premium',None,0.3),('boulder-beer',None,0.3)]
GRID=['index','cinematic','premium','wine-walk','supper-club','techno-paint','germany','mz9','app','hosted','tools','sauna']
frames=[]
# 1) Hook 0-2.0s: flicker 0.25s per page, text from frame 0
for i in range(int(2.0*FPS)):
    n=HOOK[(i//7)%len(HOOK)]; tt=(i%7)/7
    fr=zoom(scroll_frame(n,0.1*tt),1.06-0.06*tt).copy()
    frames.append(textbox(fr,['Alle diese Seiten','hab ich gebaut.'],620,sub='Allein. Mit KI.'))
# 2) scroll sequence with labels, accelerating
k=0
for n,lab,dur in SEQ:
    N=max(1,int(dur*FPS))
    for i in range(N):
        t=i/max(1,N-1); fr=scroll_frame(n,t).copy()
        if k<2: fr=textbox(fr,['Ohne Agentur.','Ohne Dev-Team.'] if k==0 else ['Idee rein.','Seite raus.'],560,size=84)
        if lab: label(fr,lab)
        frames.append(fr)
    k+=1
# 3) grid reveal 2.6s
N=int(2.6*FPS)
for i in range(N):
    t=i/(N-1); fr=grid(3,4,GRID,t)
    fr=zoom(fr,1.25-0.25*ease(min(1,t*2)))
    if t>0.25: fr=textbox(fr.copy(),['30+ Seiten.','1 Person.'],700,size=100,sub='Apps · Websites · Tools',alpha=min(1,(t-0.25)*5))
    frames.append(fr)
# 4) end card 2.4s over blurred grid
base=grid(3,4,GRID,1).filter(ImageFilter.GaussianBlur(18))
for i in range(int(2.4*FPS)):
    fr=base.copy(); fr=textbox(fr,['Wie das geht?','Zeig ich hier.'],700,size=96,sub='Folg @flow.media.ai')
    frames.append(fr)
# 5) loop bridge: last 6 frames flash into first hook page
for i in range(6):
    frames.append(Image.blend(base,frames[0],(i+1)/6))
dur=len(frames)/FPS; print('frames',len(frames),'dur',round(dur,2))
out=f'{S}/flow_reel_websites.mp4'
p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
  '-ss','8','-i','/home/user/the-tribe-bot/instagram_autopilot/music/take-this-higher.mp3',
  '-map','0:v','-map','1:a','-t',f'{dur:.2f}','-af',f'afade=t=in:d=0.3,afade=t=out:st={dur-0.8:.2f}:d=0.8',
  '-c:v','libx264','-pix_fmt','yuv420p','-preset','medium','-crf','20','-c:a','aac','-b:a','160k','-movflags','+faststart',out],stdin=subprocess.PIPE)
for f in frames: p.stdin.write(f.tobytes())
p.stdin.close(); p.wait(); print(out)
