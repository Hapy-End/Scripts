import math
print('Поиск первого отрицательного члена в последовательности sin(tg(n)), где n изменяется так n=1,2,3,...')
for n in range(1,10):
	a = math.sin(math.tan(n))
	if a < 0:
		print('Первый отрицательный член равен:', a, '\nПри этом n равен:', n)
		break
input()