g=9.8
m=float(input('m='))
t1=float(input('t1='))
t2=float(input('t2='))
t3=float(input('t3='))
t4=float(input('t4='))
t5=float(input('t5='))

r=17.5 * (10**(-3))
dr=0.05 * (10**(-3))

br=dr / r
print(br)
br=float(input('бr ='))

h=0.94
dh=0.5 * (10**(-3))

bh=dh/h
print(bh)
bh=float(input('bh ='))

tsr=(t1+t2+t3+t4+t5)/5
print(tsr)
tsr=float(input('tср ='))

i1=1
i2=1
i3=1
i4=1
i5=1
if t1<tsr:
    i1=-1
if t2<tsr:
    i2=-1
if t3<tsr:
    i3=-1
if t4<tsr:
    i4=-1
if t5<tsr:
    i5=-1
dt=((tsr-t1)*i1+(tsr-t2)*i2+(tsr-t3)*i3+(tsr-t4)*i4+(tsr-t5)*i5)/5
print(dt)
dt=float(input('dt ='))

bt=dt/tsr
print(bt)
bt=float(input('bt ='))

a=(2*h)/(tsr**2)
print(a)
a=float(input('a ='))

E=a/r
print(E)
E=float(input('E ='))

M=m*(g-a)*r
print(M)
M=float(input('M ='))

ba=bh+(2*bt)
print(ba)
ba=float(input('ba ='))

bM=((a/(g-a))*ba)+br
print(bM)
bM=float(input('bM ='))

dM=M*bM
print(dM)
dM=float(input('dM ='))

bE=ba+br
print(bE)
bE=float(input('bE ='))

dE=E*bE
print(dE)
dE=float(input('dE ='))

print('!Таблица 2 (по порядку)')
print(m,'|',t1,'|',t2,'|',t3,'|',t4,'|',t5,'|',tsr,'|',dt,'|',bt,'|')
print('!Таблица 3 (по порядку)')
print(a,'|',M,'|',bM,'|',dM,'|',E,'|',bE,'|',dE,'|')
print('M=',M,'+-',dM)
print('E=',E,'+-',dE)
input()