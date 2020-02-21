n = 100
a = True
for i in range(2,n):
    for j in range(2,n):
        if i!=j and i%j==0:
            a = False
            break
    if a:
        print(i, end=' ')
    a = True