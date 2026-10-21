import json, wave, numpy as np
SR=44100; DUR=21.5; BPM=140; B=60/BPM
N=int(SR*DUR); mus=np.zeros(N); fx=np.zeros(N); rng=np.random.default_rng(11)
def add(buf,sig,t,g=1.0):
    i=int(t*SR); j=min(N,i+len(sig))
    if 0<=i<N: buf[i:j]+=g*sig[:j-i]
def env(n,dec): return np.exp(-np.arange(n)/SR/dec)
def lp(x,a):
    y=np.zeros_like(x); s=0.; a=np.broadcast_to(a,x.shape)
    for k in range(len(x)): s+=a[k]*(x[k]-s); y[k]=s
    return y
def k808(dur=.6,f0=46):
    n=int(dur*SR); tt=np.arange(n)/SR; f=f0+140*np.exp(-tt/.02)
    return np.tanh(2.2*np.sin(2*np.pi*np.cumsum(f)/SR))*env(n,.28)
def snare():
    n=int(.25*SR); tt=np.arange(n)/SR; x=rng.standard_normal(n)
    return (np.diff(np.concatenate([[0],x]))*env(n,.07)*.7+np.sin(2*np.pi*190*tt)*env(n,.05))
def hat(d=.03):
    n=int(.06*SR); x=rng.standard_normal(n); return np.diff(np.concatenate([[0],x]))*env(n,d*.4)*.5
VOICE_END=17.3
nb=int(DUR/B)
for b in range(nb):
    t=b*B
    if t>=21.0: break
    bar_pos=b%4
    if bar_pos==0 or (b%8==6): add(mus,k808(),t,.9)
    if bar_pos==2: add(mus,snare(),t,.6)
    # hats in 8ths, 16th/32nd rolls at the end of every 2 bars
    if b%8==7:
        for r in range(6): add(mus,hat(),t+r*B/6,.35)
    else:
        add(mus,hat(),t,.3); add(mus,hat(),t+B/2,.22)
# dark pad drone (minor) for weight
tt=np.arange(N)/SR
pad=sum(np.sin(2*np.pi*f*tt+np.sin(2*np.pi*.2*tt)) for f in (73.4,110,146.8,174.6))/4
mus+=lp(pad,.05)*.25
# riser into "실력"
r0,r1=12.9,13.88; n=int((r1-r0)*SR); x=rng.standard_normal(n); ramp=np.linspace(0,1,n)**2
add(mus,lp(x,.05+.4*ramp)*ramp*1.2,r0)
mus[int(13.88*SR)-int(.05*SR):int(13.88*SR)]*=0.05  # tiny gap before the drop
# effects from the picture
def impact():
    n=int(.9*SR); t2=np.arange(n)/SR
    return np.tanh(2*np.sin(2*np.pi*np.cumsum(38+120*np.exp(-t2/.03))/SR))*env(n,.35)+rng.standard_normal(n)*env(n,.03)*.6
def whoosh():
    n=int(.18*SR); t2=np.arange(n)/SR; return lp(rng.standard_normal(n),.3)*np.sin(np.pi*t2/.18)*1.4
def tick():
    n=int(.03*SR); t2=np.arange(n)/SR; return np.sin(2*np.pi*1800*t2)*env(n,.006)
ev=json.load(open('events.json'))
for typ,t in ev:
    if typ=='hit': add(fx,impact(),t,.55 if abs(t-13.88)>.01 else .9)
    elif typ=='cut' and t>0: add(fx,whoosh(),t-.09,.35)
    elif typ=='tick': add(fx,tick(),t,.25)
add(fx,impact(),21.0-.0,.6)
# narration
w=wave.open('vo.wav'); sr=w.getframerate(); ch=w.getnchannels()
v=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32).reshape(-1,ch).mean(1)/32768
if sr!=SR: v=np.interp(np.arange(int(len(v)*SR/sr))*sr/SR,np.arange(len(v)),v)
vo=np.zeros(N); vo[:min(N,len(v))]=v[:N]
vo/=np.max(np.abs(vo))/0.9
# duck music under the voice
e=lp(np.abs(vo),.002); e/=e.max(); duck=1-.55*np.clip(e*3,0,1)
mix=vo*1.0+(mus*duck)*.42+fx*.38
mix=np.tanh(mix*1.05); mix/=np.max(np.abs(mix))/0.92
fo=int(.4*SR); mix[-fo:]*=np.linspace(1,0,fo)
pcm=(mix*32767).astype(np.int16)
o=wave.open('mix.wav','wb'); o.setnchannels(2); o.setsampwidth(2); o.setframerate(SR); o.writeframes(np.repeat(pcm[:,None],2,axis=1).tobytes()); o.close()
print('ok')
