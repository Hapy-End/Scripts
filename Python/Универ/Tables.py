import numpy as np
from itertools import permutations

s, g, d = 7,7,7 #Столы, Группы, Дни
np.set_printoptions(edgeitems=g) #Настройка вывода массива
groups = list(range(g)) if s<=g else list(range(-s+g,g)) # Список групп

perm = lambda x: np.array(list(permutations(x,r=s))) #Функция получения всех размещений групп

#Функция нахождения не повторяющихся вариантов из всех размещений
def check(A,B): 
	for i in range(len(B)):
		for j in range(len(B[i])-1):
			isRepeat = False #Наличий повторяющихся соседей
			for AA in A:
				for k in range(len(AA)-1):
					if (list(AA[k:k+2]) == list(B[i][j:j+2])
					or list(AA[k:k+2][::-1]) == list(B[i][j:j+2])):
							isRepeat = True
							break
			if isRepeat:
				break
		if not isRepeat:
			A.append(B[i]) #При отсутствии повторяющихся соседей добавить данный вариант в список

vars = perm(groups) #Все варианты размещения групп
print(vars[:d]) #Вывод нужного кол-ва вариантов

vars_wo = [vars[0]] #Список с не повторяющимися варинтами
check(vars_wo,list(vars))
print(np.array(vars_wo))