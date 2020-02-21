import random
a=[[random.randint(0,9) for i in range(7)] for j in range(7)]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
######################################################
n=int(input())
c=0
for i in range(len(a)):
    for j in range(len(a[i])):
        if (a[i][j]<n):
            c+=1

print('Кол-во чисел',n,'-',c)
######################################################
m=int(input())
aaa=0
for i in range(len(a)):
    del(a[i][m])
del(a[m])
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

