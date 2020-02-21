import random
def m_create(n,m):
    A=[[random.randint(10,20) for i in range(n)] for j in range(m)]
    return(A)
a=m_create(6,6)

def mprint(mn):
    for i in range(len(mn)):
        for j in range(len(mn[i])):
            print(mn[i][j], end=' ')
        print()
    print()
mprint(a)
a1=[]
a2=[]
a3=[]
a4=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        if (i+j<len(a)-1) and (i<j):
            a1.append(a[i][j]) #Верх
        if (i+j>len(a)-1) and (i>j):
            a2.append(a[i][j]) #Низ
        if (i>j) and (i+j<len(a)-1):
            a3.append(a[i][j]) #Лево
        if (i<j) and (i+j>len(a)-1):
            a4.append(a[i][j]) #Право
a1,a2=a1[::-1],a2[::-1]
for i in range(len(a)):
    for j in range(len(a[i])):
        if (i+j<len(a)-1) and (i<j):
            a[i][j]=a2[0]
            a2.remove(a2[0])
        if (i+j>len(a)-1) and (i>j):
            a[i][j]=a1[0]
            a1.remove(a1[0])
        if (i>j) and (i+j<len(a)-1):
            a[i][j]=a4[0]
            a4.remove(a4[0])
        if (i<j) and (i+j>len(a)-1):
            a[i][j]=a3[0]
            a3.remove(a3[0])
mprint(a)