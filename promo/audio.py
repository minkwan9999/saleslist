import json, wave, numpy as np
SR=44100; DUR=22.0; BPM=120; B=60/BPM
N=int(SR*DUR); mix=np.zeros(N); rng=np.random.default_rng(3)
def add(sig,t,g=1.0):
    i=int(t*SR); j=min(N,i+len(sig))
    if i<N: mix[i:j]+=g*sig[:j-i]
def env(n,dec): return np.exp(-np.arange(n)/SR/dec)
def lp(x,a):  # one-pole lowpass
    y=np.zeros_like(x); s=0.
    for k in range(len(x)): s+=a*(x[k]-s); y[k]=s
    return y
def kick():
    n=int(.35*SR); tt=np.arange(n)/SR; f=45+90*np.exp(-tt/.04)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.12)
def clap():
    n=int(.2*SR); x=rng.standard_normal(n); e=env(n,.05)
    for d in (.0,.012,.024): e[int(d*SR):]+=0  # flams baked in via sum below
    s=sum(np.roll(x*env(n,.008),int(d*SR)) for d in (0,.011,.022))+x*env(n,.06)*.6
    return np.diff(np.concatenate([[0],s]))*.5
def hat():
    n=int(.05*SR); x=rng.standard_normal(n); return np.diff(np.concatenate([[0],x]))*env(n,.012)*.5
def mtof(m): return 440*2**((m-69)/12)
def bassnote(m,dur):
    n=int(dur*SR); tt=np.arange(n)/SR; ph=(tt*mtof(m))%1
    saw=2*ph-1; return lp(saw,.06)*np.minimum(1,tt/.005)*env(n,.25)
def pad(ms,dur):
    n=int(dur*SR); tt=np.arange(n)/SR
    s=sum(np.sin(2*np.pi*mtof(m)*tt)+.4*np.sin(4*np.pi*mtof(m)*tt) for m in ms)
    trem=.75+.25*np.sin(2*np.pi*5.5*tt)
    a=np.minimum(1,tt/.05)*np.minimum(1,(dur-tt)/.1)
    return s*trem*a/len(ms)
K,CL,H=kick(),clap(),hat()
riff=[38,38,41,38,43,41,38,36, 38,38,41,38,45,43,41,43]
chords=[[50,53,57],[50,53,57],[55,58,62],[57,61,64]]  # Dm Dm Gm A
nb=int(DUR/B)
for b in range(nb):
    t=b*B
    if 2.5<=t<4.5 or t>=21.5: continue          # breakdown during "출출하지?" + ending
    add(K,t,.9)
    if t>=4.5 and b%2==1: add(CL,t,.55)
    if t>=4.5:
        add(H,t+B/2,.25); add(H,t,.12)
for e in range(int(DUR/(B/2))):
    t=e*B/2
    if 2.5<=t<4.5 or t>=21.5: continue
    add(bassnote(riff[e%16],B/2*.95),t,.45)
for bar in range(int(DUR/(4*B))):
    t=bar*4*B
    if t<4.5 or t>=21.5: continue
    add(pad(chords[bar%4],4*B),t,.16)
# breakdown drone under the question
add(pad([38,50],2.0),2.5,.25)
# final hit
add(K,21.5,1.0); add(bassnote(38,1.2),21.5,.6); add(pad([50,53,57,62],0.9),21.5,.25)
# sound effects from the animation events
def thump():
    n=int(.25*SR); tt=np.arange(n)/SR
    return np.sin(2*np.pi*np.cumsum(70+60*np.exp(-tt/.03))/SR)*env(n,.08)+rng.standard_normal(n)*env(n,.015)*.5
def click():
    n=int(.03*SR); tt=np.arange(n)/SR
    return (np.sin(2*np.pi*2400*tt)*.5+rng.standard_normal(n)*.6)*env(n,.004)
def whoosh():
    n=int(.5*SR); tt=np.arange(n)/SR; x=lp(rng.standard_normal(n),.12)
    return x*np.sin(np.pi*tt/.5)**2*2.2
def pop():
    n=int(.12*SR); tt=np.arange(n)/SR; f=300+500*tt/.12
    return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.04)
FX={'stamp':(thump(),.7),'click':(click(),.3),'whoosh':(whoosh(),.35),'pop':(pop(),.35)}
for typ,t in json.load(open('events.json')):
    s,g=FX[typ]; add(s,t,g)
mix=np.tanh(mix*1.1); mix/=np.max(np.abs(mix))/0.89
fo=int(.5*SR); mix[-fo:]*=np.linspace(1,0,fo)
pcm=(mix*32767).astype(np.int16); st=np.repeat(pcm[:,None],2,axis=1)
w=wave.open('music.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes()); w.close()
print('ok')
