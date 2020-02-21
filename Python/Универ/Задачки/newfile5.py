#pylint:disable=C0103
#pylint:disable=C0304
#pylint:disable=W0312
import numpy as np
a = np.random.random((5,5))
a-=0.5
a*=100
for i in range(len(a)):
	for j in range(len(a)):
		a[i,j] = round(a[i,j],2)
print(a)
s1,s2=0,0
for i in range(a.shape[0]):
	for j in range(a.shape[1]):
		if (i<j) and (i+j<a.shape[0]-1) and (a[i,j]<0):
			s1 += a[i,j]
		elif (i>j) and (i+j>a.shape[0]-1) and (a[i,j]>0):
			s2 += a[i,j]
print(s1 if abs(s1)>abs(s2) else s2)