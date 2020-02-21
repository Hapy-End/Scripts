import math
y = 3,2,2,1,5,1,2,2,3

mean = lambda x: sum(x)/len(x)

def disp(x,t=0):
	s = 0
	m = mean(x)
	for i in x:
		s += (i - m)**2
	return s/len(x) if t==0 else s/(len(x)-1)

def sk(x):
	return disp(x)**0.5

def asim(x):
	s = 0
	m = mean(x)
	for i in x:
		s += (i - m)**3
	return s/(len(x)*sk(x)**3)

def eks(x):
	s = 0
	m = mean(x)
	for i in x:
		s += (i - m)**4
	return s/(len(x)*sk(x)**4) - 3

kcount = lambda x: int(round(1 + 1.4 * math.log(len(x)),0))

raz = lambda x: max(x) - min(x)

step = lambda x: raz(x)/kcount(x)

median = lambda x: x[len(x)//2-1]/2+x[len(x)//2]/2 if len(x)%2==0 else x[(len(x)-1)//2]

def stat(X):
	STAT = {}
	STAT['Объём'] = len(X)
	STAT['Среднее'] = mean(X)
	STAT['Медиана'] = median(X)
	STAT['Смещ. дисперсия'] = disp(X)
	STAT['Несмещ. дисперсия'] = disp(X,1)
	STAT['Ср. квадр.'] = sk(X)
	STAT['Асимметрия'] = asim(X)
	STAT['Эксцесс'] = eks(X)
	STAT['Кол-во интервалов']= kcount(X)
	STAT['Размах']= raz(X)
	STAT['Длина интервала']= step(X)
	return STAT
print(stat(y))