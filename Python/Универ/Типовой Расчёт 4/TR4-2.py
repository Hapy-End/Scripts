mN = input('Введите цепочку чисел через пробел:\n')
N = mN.split(' ')
a = 0
for i in range(len(N)):
	a= a + int(N[i])
print('Среднее арифметическое этих чисел равно ',a / len(N))
input()