print('Определение наименьшей k в выражении: x<2^k')
for i in range(1,6):
	x = int(input('Введите число [' + str(i) + '-5]: '))
	a = 0
	k = 0
	while x>=(2**k):
		k+=1
	print('Наименьшая k:',k)
input()
	