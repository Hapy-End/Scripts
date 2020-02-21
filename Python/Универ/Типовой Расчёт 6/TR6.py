import random
a=[[random.randint(1,9) for i in range(5)] for j in range(5)]
######## Сумма элементов выше главной и побочной диагоналей #######
s=0
for i in range(len(a)):
	for j in range(len(a[i])):
		if (i<j) and (i+j<len(a)-1):
			s+=a[i][j]
		print(a[i][j], end=' ')
	print()
print('Сумма',s)
######## Наименьший элемент ниже главной и побочной диагоналей ########
m='пусто'
for i in range(len(a)):
	for j in range(len(a[i])):
		if (i>j) and (i+j>len(a)-1):
			if (m=='пусто') or (int(m)>a[i][j]):
				m=a[i][j]
print('Минимум',m)
######### Максимум на главной и побочной диагонали #########
m='пусто'
for i in range(len(a)):
	for j in range(len(a[i])):
		if (i==j) or (i+j==len(a)-1):
			if (m=='пусто') or (int(m)<a[i][j]):
				m=a[i][j]
print('Максимум',m)
######### Произведение элементов выше главной диагонали ##########
m=1
for i in range(len(a)):
    for j in range(len(a[i])):
        if (i<j):
            m*=a[i][j]
print('Произведение',m)
######### Кол-во каждой цифры ниже побочной диагонали ##########
m=0
for i in range(len(a)):
	for j in range(len(a[i])):
		if (i+j>len(a)-1):
			m+=1
print('Кол-во цифр',m)