print('Поиск максимального из отрицательных чисел')
a=0
mn=0
for i in range(1,11):
	n = int(input('Введите число [' + str(i) + '-10]: '))
	if n>=0:
		continue
	n = n * -1
	if (mn==0) or (n < mn):
		mn=n
print('Максимальное из отрицательных чисел:',mn*-1)
input()