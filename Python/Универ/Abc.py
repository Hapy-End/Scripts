import math

#Факториал
def f(c):
	return f(c-1)*c if c>1 else 1
	
#Интегральная формула Лапласа
def LaplasInteg(n,k1,k2,p):
	q = 1-p
	x2=(k2-n*p)/(n*p*q)**.5
	x1=(k1-n*p)/(n*p*q)**.5
	fx1 = float(input('f от '+str(x1)+': '))
	fx2 = float(input('f от '+str(x2)+': '))
	return (fx2-fx1)*.5

#Локальная теорема Лапласа
def LaplasLocal(n,k,p):
	q = 1-p
	a=1/(n*p*q)**.5
	x1=(k-n*p)/(n*p*q)**.5
	fx1 = float(input('f от '+str(x1)+': '))
	return a*fx1

#Формула Бернулли
def Bernulli(n,k,p):
	C = f(n)/(f(n-k)*f(k))
	print()
	q = 1 - p
	return C*(p**k)*(q**(n-k))
	
#Формула Пуассона
def f(c):
	return f(c-1)*c if c>1 else 1
def Puassona(n,k,p):
	lamda = n*p
	return (lamda**k*math.e**(-lamda))/f(k)
def PuassonaWhile(n,k1,k2,p):
	c = 0
	for i in range(k1,k2+1):
		c += i*Puassona(n,i,p)
	return c
	
#Наивероятнейшее число появления событий
def NVC(n,p):
	q = 1 - p
	a = n * p - q
	b = n * p + p
	return int(a) if int(a)>=a else int(b)
while True:
	xx = int(input("""\n\n########################
1.Бернулли
2.Пуассона
21.Распределение Пуассона
3.Лок. Лапласа
4.Интегральная Лапласа
5.Наивероятнейшее число появления событий

0.Выход

Ввод:"""))
	print()
	if not xx:
		print("#"*20)
		break
	elif xx==1:
		print('Ответ: ',Bernulli(int(input("n: ")),int(input("k: ")),float(input("p: "))))
	elif xx==2:
		print('Ответ: ',Puassona(int(input("n: ")),int(input("k: ")),float(input("p: "))))
	elif xx==21:
		print('Ответ: ',PuassonaWhile(int(input("n: ")),int(input("k¹: ")),int(input("k²: ")),float(input("p: "))))
	elif xx==3:
		print('Ответ: ',LaplasLocal(int(input("n: ")),int(input("k: ")),float(input("p: "))))
	elif xx==4:
		print('Ответ: ',LaplasInteg(int(input("n: ")),int(input("k¹: ")),int(input("k²: ")),float(input("p: "))))
	elif xx==5:
		print('Ответ: k='+NVC(int(input("n = ")),float(input("p = "))))
	else:
		print("\n#")





