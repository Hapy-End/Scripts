def LaplasLocal(n,k,p):
	q = 1-p
	a=1/(n*p*q)**.5
	x1=(k-n*p)/(n*p*q)**.5
	fx1 = float(input('f от '+str(x1)+': '))
	return a*fx1
print('Ответ: ',LaplasLocal(int(input("n: ")),int(input("k: ")),float(input("p: "))))