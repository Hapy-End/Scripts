import math
x = int(input('Введите x: '))
print('Результат')
print('--Первый: ' + str(2*x)) if (2<x) or (x<-2) else print('--Первый: ' + str(-3 * x))
print('--Второй: ' + str(2*math.sin(x))) if (x>0) else print('--Второй: ' + str(6-x))
if (x<0):
    c = 0
elif x==0 or (x%2)==0:
    c = 1
elif (x%2)==1:
    c = -1
print('--Третий: ' + str(c))
input()