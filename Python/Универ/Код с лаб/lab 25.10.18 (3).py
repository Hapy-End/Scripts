#-------------------------------------------------------------------------------
import random

def mcr(_n,_m):
    A=[[random.randint(0,9) for i in range(_n)] for j in range(_m)]
    return(A)
#--------------------------------------
n=5
m=5
a=mcr(n,m)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
#--------------------------------------
if len(a)%2==0:
    addl=int(len(a)/2-1)
elif len(a)%2!=0:
    addl=int(len(a)//2)
ln=len(a)-1
_ln=len(a)-1
i=0
j=ln
start=0
#--------------------------------------
print('#' * (2 * m * n + 3))
print('#', end=' ')
for _i in range(m*n+addl):
    if (start==0):
        start+=1
    elif (i==_ln-ln) and (j>_ln-ln):
        j-=1
    elif (i<ln) and (j==_ln-ln):
        i+=1
    elif (i==ln) and (j<ln):
        j+=1
    elif (j==ln) and (i>_ln-ln+1):
        i-=1
    else:
        ln-=1
        continue
    print(a[i][j], end=' ')
print('#')
print('#' * (2 * m * n + 3))