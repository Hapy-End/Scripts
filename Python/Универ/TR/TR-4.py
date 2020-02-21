import numpy as np
A = 20
B = 80
Len = 20
a = np.random.randint(0,100,Len)
a = a[np.where(a>A)]
a = a[np.where(a<B)]
for i in range(Len-len(a)):
    a = np.append(a, 1)
print(a)