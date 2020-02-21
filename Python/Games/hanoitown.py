import time
def move(_from,_to):
    if _to==[] and _from==[]:
        pass
    elif _to==[]:
        _to.append(_from[-1])
        _from.remove(_from[-1])
    elif _from==[]:
        _from.append(_to[-1])
        _to.remove(_to[-1])
    elif _to[-1]<_from[-1]:
        _from.append(_to[-1])
        _to.remove(_to[-1])
    elif _to[-1]>_from[-1]:
        _to.append(_from[-1])
        _from.remove(_from[-1])

def print_hanoi(a,b,c,nstep,alstep,ae):
    time.sleep(0.3)
    maxls=0
    if (len(a)>=len(b)) and (len(a)>=len(c)):
        maxls=len(a)
    elif (len(c)>=len(a)) and (len(c)>=len(b)):
        maxls=len(c)
    elif (len(b)>=len(a)) and (len(b)>=len(c)):
        maxls=len(b)
    a1=[0 for i in range(maxls-len(a))]
    b1=[0 for i in range(maxls-len(b))]
    c1=[0 for i in range(maxls-len(c))]
    a1.extend(a[::-1])
    b1.extend(b[::-1])
    c1.extend(c[::-1])
    for i in range(maxls,ae+1):
        print()
    for i in range(1,maxls+1):
        print(' '*(ae-a1[i-1]),'##'*a1[i-1], end=' '*(ae-a1[i-1]))
        print(' '*(ae-b1[i-1]),'##'*b1[i-1], end=' '*(ae-b1[i-1]))
        print(' '*(ae-c1[i-1]),'##'*c1[i-1])
    print('Шаг:',nstep,'из',alstep-1)
    print('-'*40)
hsize=int(input())
a=[]
b=[]
c=[]
for i in range(1,hsize+1):
    a.append(i)
a=a[::-1]
n=0
als=2**len(a)
while True:
    move(a,b)
    n+=1
    if n==als:
        break
    print_hanoi(a,b,c,n,als,hsize)
    move(a,c)
    n+=1
    if n==als:
        break
    print_hanoi(a,b,c,n,als,hsize)
    move(b,c)
    n+=1
    if n==als:
        break
    print_hanoi(a,b,c,n,als,hsize)