from random import randint as r
import numpy
a = [r(-10,10) for i in range(10)]
print(a)
c = 0
s = 0
for b in a:
	if c==2:
		s+=abs(b)
	elif b<0:
		c+=1
print(s)
print()
a = [[r(-10,10) for i in range(7)] for j in range(7)]
a = numpy.array(a)
print(a)
c = 0
s = 0
for i in a:
	for j in i:
		if c==2:
			s+=abs(j)
		elif j<0:
			c+=1
print(s)
print()
a = numpy.array([[r(0,100) for i in range(5)] for j in range(7)])
print(a)
c = 0
s = 0
for i in a:
	for j in i:
		s+=j
		c+=1
s/=c
print(s)
c=0
for i in a:
	for j in i:
		c += 1 if j<s else 0
print(c)