#pylint:disable=E1101
#pylint:disable=C0301
#pylint:disable=C0304
#pylint:disable=W0312
#pylint:disable=W0312
#pylint:disable=C0103
import numpy as np

N = 100
a = np.random.randint(0,N,(5,7))
print(a)

sn,ac = [],True
for x in range(2,N):
    for y in range(2,N):
        if x != y and x%y==0:
            ac = False
            break
    if ac == True:
        sn.append(x)
    ac = True

b = []
for i in range(a.shape[0]):
	s = 0
	for j in range(a.shape[1]):
		if j%2==0:
			s+=a[i,j] if a[i,j] in sn else 0
	b.append(s)
print(b)