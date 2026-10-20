import json, wave, numpy as np
SR=44100; DUR=29.0; BPM=120; B=60/BPM
N=int(SR*DUR); mix=np.zeros(N); rng=np.random.default_rng(5)
def add(sig,t,g=1.0):
    i=int(t*SR); j=min(N,i+len(sig))
    if i<N: mix[i:j]+=g*sig[:j-i]
def env(n,dec): return np.exp(-np.arange(n)/SR/dec)
def mtof(m): return 440*2**((m-69)/12)
def pluck(m,dur=.6):  # Karplus-Strong
    n=int(dur*SR); p=int(SR/mtof(m)); buf=rng.uniform(-1,1,p); out=np.zeros(n)
    for k in range(n):
        out[k]=buf[k%p]; buf[k%p]=.5*(buf[k%p]+buf[(k+1)%p])*.996
    return out
def kick():
    n=int(.3*SR); tt=np.arange(n)/SR; f=50+110*np.exp(-tt/.03)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.1)
def clap():
    n=int(.2*SR); x=rng.standard_normal(n)
    s=sum(np.roll(x*env(n,.007),int(d*SR)) for d in (0,.01,.02))+x*env(n,.05)*.5
    return np.diff(np.concatenate([[0],s]))*.5
def shaker():
    n=int(.06*SR); x=rng.standard_normal(n); return np.diff(np.concatenate([[0],x]))*np.sin(np.pi*np.arange(n)/n)*.4
def bass(m,dur):
    n=int(dur*SR); tt=np.arange(n)/SR
    return (np.sin(2*np.pi*mtof(m)*tt)+.3*np.sin(4*np.pi*mtof(m)*tt))*np.minimum(1,tt/.01)*env(n,.35)
def bell(m):
    n=int(.8*SR); tt=np.arange(n)/SR
    return (np.sin(2*np.pi*mtof(m)*tt)+.3*np.sin(2*np.pi*mtof(m)*2.76*tt)*env(n,.1))*env(n,.3)
KK,CL,SH=kick(),clap(),shaker()
# C G Am F, one chord per bar
prog=[[60,64,67],[55,59,62],[57,60,64],[53,57,60]]
roots=[36,43,45,41]
cache={}
def pl(m):
    if m not in cache: cache[m]=pluck(m)
    return cache[m]
for e in range(int(DUR/(B/2))):
    t=e*B/2; bar=int(t/(4*B)); ch=prog[bar%4]
    if t>=28.0: break
    arp=[ch[0],ch[1],ch[2]+12,ch[1]+12,ch[2],ch[1]+12,ch[0]+12,ch[1]]
    add(pl(arp[e%8]),t,.33)
for b in range(int(DUR/B)):
    t=b*B; bar=int(t/(4*B))
    if t>=28.0: break
    if t>=4.0:
        add(KK,t,.75 if b%2==0 else .45)
        if b%2==1: add(CL,t,.45)
        add(SH,t+B/2,.5); add(SH,t,.2)
        add(bass(roots[bar%4],B*.9),t,.35)
    elif b%4==0: add(bass(roots[bar%4],B*3.5),t,.25)
# ending chord
for m in (48,60,64,67,72): add(pl(m) if m>50 else bass(m,1.2),28.0,.35)
add(KK,28.0,.8)
def thump():
    n=int(.2*SR); tt=np.arange(n)/SR
    return np.sin(2*np.pi*np.cumsum(90+80*np.exp(-tt/.025))/SR)*env(n,.06)+rng.standard_normal(n)*env(n,.01)*.4
def click():
    n=int(.025*SR); tt=np.arange(n)/SR
    return (np.sin(2*np.pi*2600*tt)*.5+rng.standard_normal(n)*.5)*env(n,.004)
def whoosh():
    n=int(.45*SR); tt=np.arange(n)/SR; x=rng.standard_normal(n); y=np.zeros(n); s=0.
    for k in range(n): s+=.15*(x[k]-s); y[k]=s
    return y*np.sin(np.pi*tt/.45)**2*2
def pop():
    n=int(.12*SR); tt=np.arange(n)/SR
    return np.sin(2*np.pi*np.cumsum(400+700*tt/.12)/SR)*env(n,.04)
FX={'stamp':(thump(),.55),'click':(click(),.25),'whoosh':(whoosh(),.3),'pop':(pop(),.3)}
for typ,t in json.load(open('events.json')):
    s,g=FX[typ]; add(s,t,g)
add(bell(84),25.4,.18)  # sparkle on the free level test badge
mix=np.tanh(mix*1.1); mix/=np.max(np.abs(mix))/0.85
fo=int(.6*SR); mix[-fo:]*=np.linspace(1,0,fo)
pcm=(mix*32767).astype(np.int16)
w=wave.open('music.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(np.repeat(pcm[:,None],2,axis=1).tobytes()); w.close()
print('ok')
