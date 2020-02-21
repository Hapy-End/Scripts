#pylint:disable=W0311
#pylint:disable=C0103
#pylint:disable=C0103
#pylint:disable=C0304
#pylint:disable=W0312
import numpy as np
a = np.random.randint(-9,9,(7,7))
print(a)
c = len(a)
for i in a:
      b = []
      for j in i:
           if j in b:
               c-=1
               break
           b.append(j)
print(c)
c = a.shape[1]
for i in range(a.shape[1]):
	s = 0
	for j in range(a.shape[0]):
		if a[j,i]>0:
			s+=1
		elif a[j,i]<0:
			s-=1
	if s>0:
		c-=1
print(c)
