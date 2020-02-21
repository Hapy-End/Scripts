 #pylint:disable=W0312
from math import factorial as f
import random as r
import itertools as it

#Вывод вариантов
def _print(lst,col=2):
	for i in range(1,len(lst)+1):
		print('[',end="")
		for j in range(len(lst[i-1])):
			print(lst[i-1][j], end=' ' if j+1!=len(lst[i-1]) else '')
		print(']',end='\n' if i%col==0 else '  ')
	print('\n\nВариантов:',len(lst))
	print()

#Сочетания без повторения
def CombWoR(_list,m):
	n = len(_list)
	if m<=n:
		a = []
		while len(a)!=(f(n)/f(n-m)/f(m)):
			b = r.sample(_list,m)
			b = sorted(b)
			if b not in a:
				a.append(b)
		a = sorted(a)
		return(a)
	else:
		return(-1)

#Сочетания с повторениями
def CombWR(_list,m):
	n = len(_list)
	a = []
	while len(a)!=(f(n+m-1)/f(n-1)/f(m)):
		b = [r.choice(_list) for i in range(m)]
		b = sorted(b)
		if b not in a:
			a.append(b)
	return(sorted(a))

#Размещения с повторениями
def RazWR(_list,m):
	n = len(_list)
	a = []
	while len(a)!=(n**m):
		b = [r.choice(_list) for i in range(m)]
		if b not in a:
			a.append(b)
	return(sorted(a))
		
#Размещения без повторений
def RazWoR(_list,m):
	n = len(_list)
	if m<=n:
		a = []
		while len(a)!=(f(n)/f(n-m)):
			b = r.sample(_list,m)
			if b not in a:
				a.append(b)
		a = sorted(a)
		return(a)
	else:
		return(-1)

#Перемещения без повторений
def PerWoR(_list):
	return(RazWoR(_list,len(_list)))

#Перемещения с повторениями
def PerWR(_list):
	n = len(_list)
	pF = f(n)
	pV, pC = [],[]
	for i in _list:
		if i not in pV:
			pV.append(i)
			pC.append(1)
		else:
			pC[pV.index(i)]+=1
	for i in pC:
		pF/=f(i)
	pF = int(pF)
	a = []
	while len(a)!=pF:
		b = r.sample(_list,n)
		if b not in a:
			a.append(b)
	return(sorted(a))
	
while True:
	try:
		x = int(input('1.Сочетания без повторений\n2.Размещение без повторений\n3.Перемещения без повторений\n4.Сочетания с повторениями\n5.Размещение с повторениями\n6.Перемещения с повторениями\n\tВведите: '))
		l = input('Введите элементы через пробел:\n')
		if l == 'Выход' or l =='Exit' or l=='0':
			break
		elif l[0:5]=='range':
			_list = list(range(int(l[5:])))
		elif l[0:7]=='letters':
			_list = list(l[7:])
		else:
			_list = l.split(' ')
		m=len(_list)
		if x!=3 and x!=6:
			m = int(input('Введите m:\n'))
		if x==1:
			_print(list(it.combinations(_list,m)),3)
			#_print(CombWoR(_list,m),3)
		elif x==2:
			_print(list(it.permutations(_list,m)),3)
			#_print(RazWoR(_list,m),3)
		elif x==3:
			_print(list(it.permutations(_list, len(_list))),3)
			#_print(PerWoR(_list),3)
		elif x == 4:
			_print(CombWR(_list,m),3)
		elif x == 5:
			_print(RazWR(_list,m),3)
		elif x == 6:
			_print(PerWR(_list),3)
	except:
		print('\nПроизошла ошибка\n')