def LaplasInteg(n,k1,k2,p):
	q = 1-p
	x2=(k2-n*p)/(n*p*q)**.5
	x1=(k1-n*p)/(n*p*q)**.5
	fx1 = float(input('f от '+str(x1)+': '))
	fx2 = float(input('f от '+str(x2)+': '))
	return (fx2-fx1)*.5
print('Ответ: ',LaplasInteg(int(input("n: ")),int(input("k¹: ")),int(input("k²: ")),float(input("p: "))))