import random
def m_create(n,m):
    A=[[random.randint(10,20) for i in range(n)] for j in range(m)]
    return(A)

def mprint(mn):
    for i in range(len(mn)):
        for j in range(len(mn[i])):
            print(mn[i][j], end=' ')
        print()
    print()

a=m_create(5,5)
mprint(a)
a1=[]
a2=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        if (i+j>len(a)-1):
            a2.append(a[i][j])
        if (i+j<len(a)-1):
            a1.append(a[i][j])
a1,a2=a1[::-1],a2[::-1]
for i in range(len(a)):
    for j in range(len(a[i])):
        if (i+j<len(a)-1):
            a[i][j]=a2[0]
            a2.remove(a2[0])
        if (i+j>len(a)-1):
            a[i][j]=a1[0]
            a1.remove(a1[0])
mprint(a)