def f(c):
	return f(c-1)*c if c>1 else 1
def Bernulli(n,k,p):
	C = f(n)/(f(n-k)*f(k))
	print()
	q = 1 - p
	return C*(p**k)*(q**(n-k))
print('Ответ: ',Bernulli(int(input("n: ")),int(input("k: ")),float(input("p: "))))
