import json, wave, numpy as np
SR=44100; DUR=34.8; BPM=120; B=60/BPM
N=int(SR*DUR); mix=np.zeros(N); rng=np.random.default_rng(21)
def add(sig,t,g=1.0):
    i=int(t*SR); j=min(N,i+len(sig))
    if 0<=i<N: mix[i:j]+=g*sig[:j-i]
def env(n,dec): return np.exp(-np.arange(n)/SR/dec)
def lp(x,a):
    a=np.broadcast_to(a,x.shape); y=np.zeros_like(x); s=0.
    for k in range(len(x)): s+=a[k]*(x[k]-s); y[k]=s
    return y
def mtof(m): return 440*2**((m-69)/12)
def kick():
    n=int(.35*SR); tt=np.arange(n)/SR; return np.tanh(1.8*np.sin(2*np.pi*np.cumsum(48+130*np.exp(-tt/.025))/SR))*env(n,.13)
def clap():
    n=int(.2*SR); x=rng.standard_normal(n)
    return np.diff(np.concatenate([[0],sum(np.roll(x*env(n,.007),int(d*SR)) for d in (0,.01,.02))+x*env(n,.05)*.5]))*.5
def hat():
    n=int(.05*SR); x=rng.standard_normal(n); return np.diff(np.concatenate([[0],x]))*env(n,.01)*.5
def saw(m,dur,cut=.08):
    n=int(dur*SR); tt=np.arange(n)/SR; s=sum(((tt*mtof(m)*d)%1)*2-1 for d in (1,1.006,.994))/3
    return lp(s,cut)*np.minimum(1,tt/.005)*np.minimum(1,(dur-tt)/.02)
def pluck(m,dur=.25): n=int(dur*SR); return saw(m,dur,.25)*env(n,.08)
def boom():
    n=int(1.6*SR); tt=np.arange(n)/SR
    return np.tanh(2.5*np.sin(2*np.pi*np.cumsum(32+150*np.exp(-tt/.05))/SR))*env(n,.5)+lp(rng.standard_normal(n),.2)*env(n,.25)*.8
K,CL,H=kick(),clap(),hat()
prog=[(57,[57,60,64]),(53,[53,57,60]),(48,[55,60,64]),(55,[55,59,62])]  # Am F C G
def bar_of(t): return prog[int(t/(4*B))%4]
def section(t):
    if t<3: return 'hook'
    if t<6: return 'fuse'
    if t<7: return 'boom'
    if t<13: return 'story'
    if t<16.2: return 'build'
    if t<21: return 'drop'
    if t<26.5: return 'logo'
    if t<28: return 'slogan'
    if t<31: return 'drop'
    if t<34.3: return 'end'
    return 'off'
for e in range(int(DUR/(B/4))):
    t=e*B/4; sec=section(t); root,ch=bar_of(t); q=e%16
    full=sec in('hook','drop')
    if sec in('hook','drop','build') and q%4==0: add(K,t,.85)
    if sec=='story' and q in(0,10): add(K,t,.6)
    if sec in('hook','drop','story') and q in(4,12): add(CL,t,.45)
    if sec in('hook','drop','story','build','end') and q%2==0: add(H,t+(B/8 if q%4==2 else 0),.18 if q%4 else .1)
    if sec=='build' and t>14.5: add(CL,t,.15+.35*(t-14.5)/1.7)
    if sec in('hook','drop','build') and q%2==0: add(saw(root-12,B/2*.9,.05),t,.33)
    if sec in('story','drop','end','logo') and q%2==0:
        arp=[ch[0]+12,ch[1]+12,ch[2]+12,ch[1]+24]; add(pluck(arp[(e//2)%4]),t,.16 if sec!='logo' else .1)
# pads for logo and end
for t0,t1,g in ((21,26.5,.14),(31,34.3,.12)):
    for bar in np.arange(t0,t1,4*B):
        _,ch=bar_of(bar); d=min(4*B,t1-bar)
        add(sum(saw(m,d,.03) for m in ch)/3,bar,g)
# fuse: hiss + riser into the boom
n=int(3*SR); x=rng.standard_normal(n); r=np.linspace(0,1,n)**2
add(lp(x,.03+.5*r)*(.15+.85*r)*.7,3.0)
tt=np.arange(n)/SR; add(np.sin(2*np.pi*np.cumsum(80+600*r)/SR)*r*.25,3.0)
# build riser
n=int(3.2*SR); r=np.linspace(0,1,n)**2; add(lp(rng.standard_normal(n),.02+.5*r)*r*.6,13.0)
for typ,t in json.load(open('events.json')):
    if typ=='boom': add(boom(),t,.9)
    elif typ=='whoosh':
        n=int(.35*SR); w=lp(rng.standard_normal(n),.2)*np.sin(np.pi*np.arange(n)/n)**2; add(w,t-.1,.35)
    elif typ=='pop':
        n=int(.1*SR); tt=np.arange(n)/SR; add(np.sin(2*np.pi*np.cumsum(500+900*tt/.1)/SR)*env(n,.03),t,.22)
    elif typ=='tick':
        n=int(.04*SR); tt=np.arange(n)/SR; add(np.sin(2*np.pi*2200*tt)*env(n,.008),t,.3)
    elif typ=='glitch':
        n=int(.4*SR); g=np.sign(np.sin(2*np.pi*np.cumsum(rng.choice([200,900,3000],n))/SR))*env(n,.15); add(g,t,.25)
mix=np.tanh(mix*1.2); mix/=np.max(np.abs(mix))/0.9
fo=int(.5*SR); mix[-fo:]*=np.linspace(1,0,fo)
pcm=(mix*32767).astype(np.int16)
o=wave.open('music.wav','wb'); o.setnchannels(2); o.setsampwidth(2); o.setframerate(SR); o.writeframes(np.repeat(pcm[:,None],2,axis=1).tobytes()); o.close(); print('ok')
