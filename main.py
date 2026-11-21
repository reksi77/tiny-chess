# v6
import json,os,urllib.request as u
U=os.environ['MAKEFUN_ENV_URL']
V=[0,100,320,330,500,900,0]
n=[-21,-19,-12,-8,8,12,19,21]
d=[-11,-9,9,11]
s=[-10,-1,1,10]
g=d+s
O=[0,0,n,d,s,g,g]
PS='<<<<=>>8=;:<<<<@==>A>>@BFFFF<<<<'
NS='246648<=6=>?6<?@6=?@6<>?48<<2466'
H=(0,)*64
def X(v):
 return[(ord(v[r*4+min(f,7-f)])-60)*5 for r in range(8)for f in range(8)]
T=[0,X(PS),X(NS),H,H,H,H]
M=[15]*120
M[91],M[95],M[98],M[21],M[25],M[28]=13,12,14,7,3,11
B=[0]*120;W=1;C=0;E=-1;K=[0,0]
N=0;L=40000;Z=10000
D={};TM=0
class J(Exception):pass
def A(a,w):
 u=2*w-1
 for y in(11,9):
  if B[a+y*u]==u:return 1
 for y,t in((n,2),(g,6)):
  for z in y:
   if B[a+z]==t*u:return 1
 for y,t in((d,(3,5)),(s,(4,5))):
  for z in y:
   x=a+z
   while B[x]==0:x+=z
   if B[x]*u in t:return 1
 return 0
def j(m):
 global B,W,C,E,K
 o=(B,W,C,E,K)
 B=B[:];K=K[:]
 f=m&127;t=(m>>7)&127;p=(m>>14)&7;l=m>>17
 c=B[f];z=p or c
 if l&2:B[t-10+20*W]=0
 B[f]=0;B[t]=z
 if l&4:
  a=f+3-7*(t<f)
  b=f+1-2*(t<f)
  B[b]=B[a];B[a]=0
 E=(f+t)//2 if l&8 else-1
 C=C&M[f]&M[t]
 if abs(c)==6:K[not W]=t
 W=not W
 return o
def w(o):
 global B,W,C,E,K
 B,W,C,E,K=o
def Y(u):
 h=j(u);r=not A(K[W],W);w(h);return r
def G(c):
 v=[]
 for s in range(21,99):
  p=B[s]
  if p==7 or not p or(p>0)!=W:continue
  t=abs(p)
  if t==1:
   e=10-20*W
   for k,x in enumerate((s+e,s+2*e,s+e-1,s+e+1)):
    q=B[x]
    if q==7:continue
    if k<2:
     if q or k and(s//10!=3+5*W or B[s+e]):continue
     f=k<<20
    elif q:
     if(q>0)==W:continue
     f=1<<17
    elif x==E:f=3<<17
    else:continue
    if x//10==2+7*(not W):
     for r in(5,4,3,2):v.append(s|x<<7|r<<14|1<<17)
    else:v.append(s|x<<7|f)
  else:
   for z in O[t]:
    x=s+z
    while B[x]!=7:
     q=B[x]
     if not q:v.append(s|x<<7)
     else:
      if(q>0)!=W:v.append(s|x<<7|1<<17)
      break
     if t%4==2:break
     x+=z
   if t==6:
    for a in(1,-1):
     if not C&1<<(a<0)+2*(not W):continue
     f=s+3-7*(a<0)
     if B[f]!=W*8-4 or B[s+a]or B[s+2*a]or any(A(s+i,not W)for i in(0,a,2*a))or a<0 and B[s-3]:continue
     v.append(s|(s+2*a)<<7|4<<17)
 z=[u for u in v if(not c or(u>>17)&1 or(u>>14)&7)and Y(u)]
 z.sort(key=o)
 return z
def e():
 s=0
 for i in range(64):
  x=91-i//8*10+i%8
  p=B[x]
  if not p:continue
  t=abs(p);v=V[t]+T[t][i^(56*(p<0))]
  s+=v if p>0 else-v
 return s if W else-s
def o(v):
 if v==TM:return-(1<<20)
 f=v&127;t=(v>>7)&127;q=B[t]
 if q:return-10000-V[abs(q)]*16+V[abs(B[f])]
 return 0
def S(d,a,b,p):
 global N,TM,E,W
 N+=1
 if N>L:raise J
 u=A(K[not W],not W)
 if d<=0:
  s=e()
  if s>=b:return b
  if s>a:a=s
  v=G(not u)
  if u and not v:return-Z+p
  for m in v:
   h=j(m);s=-S(0,-b,-a,p+1);w(h)
   if s>=b:return b
   if s>a:a=s
  return a
 k=(tuple(B),W,C,E)
 if u:d+=1
 y=D.get(k);TM=0
 if y:
  TM=y[3]
  if y[0]>=d and(y[2]==0 or y[2]==1 and y[1]>=b or y[2]==2 and y[1]<=a):return y[1]
 v=G(0)
 if not v:return-Z+p if u else 0
 f=-1e9;bm=0;cut=0;al=a
 for m in v:
  h=j(m);s=-S(d-1,-b,-a,p+1);w(h)
  if s>f:f=s;bm=m
  if s>a:a=s
  if a>=b:
   cut=1;break
 if abs(f)<9000 and len(D)<1e5:D[k]=(d,f,cut or(f<=al)*2,bm)
 return f
def c(v):
 f=v&127;t=(v>>7)&127;p=(v>>14)&7
 return'%c%c%c%c%s'%(96+f%10,58-f//10,96+t%10,58-t//10,'qrbn'[5-p]if p else'')
def F(a):
 global B,W,C,E,K
 B=[7*(x%10 in(0,9)or x<21 or x>98)for x in range(120)]
 b=a.split();q=21
 for h in b[0]:
  if h=='/':q+=2
  elif h.isdigit():q+=int(h)
  else:
   t='PNBRQK'.index(h.upper())+1;z=2*h.isupper()-1
   B[q]=t*z
   q+=1
 K=[B.index(6),B.index(-6)]
 W=b[1]=='w'
 C=sum(1<<'KQkq'.index(h)for h in b[2]if h!='-')
 E=-1 if b[3]=='-'else 4-int(b[3][1])*10+ord(b[3][0])
def R(v):
 global N
 f=v[0]
 for d in range(12):
  N=0;g=f;a=-1e9;h=f
  try:
   v.sort(key=o)
   v.remove(g);v.insert(0,g)
   for m in v:
    h2=j(m);s=-S(d,-1e9,-a,1);w(h2)
    if s>a:a=s;h=m
   f=h
  except J:break
 return f
def p(a,b):
 return json.load(u.urlopen(u.Request(U+a,json.dumps(b).encode(),{'content-type':'application/json'})))
while 1:
 y=p('/game',{})
 if y['status']=='done':break
 while y['status']=='your_move':
  F(y['fen']);v=R(G(0))
  y=p('/move',{'game':y['game'],'move':c(v)})
