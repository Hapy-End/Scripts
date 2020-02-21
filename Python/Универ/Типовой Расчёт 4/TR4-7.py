N = input('Введите числа через пробел: ')
mN = N.split(' ')
n = 0
for i in mN:
	if (int(i)==0):
		break
	if ((int(i)%5)==0):
		n+=1
print('Количество кратных 5 чисел:',n)
input()
	