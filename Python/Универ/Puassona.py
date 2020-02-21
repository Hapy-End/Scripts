import math
def f(c):
	return f(c-1)*c if c>1 else 1
def Puassona(n,k,p):
	lamda = n*p
	return (lamda**k*math.e**(-lamda))/f(k)

print('Ответ: ',Puassona(int(input("n: ")),int(input("k: ")),float(input("p: "))))
