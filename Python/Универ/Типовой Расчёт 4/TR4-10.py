import math
ix = input('Введите 10 значений х через пробел')
X = ix.split(' ')
for x in X:
    x=int(x)
    if (-3<=x<0):
        y=(math.e ** (-2*x))
    elif (0<=x<3):
        y=(x/(x**2-6))
    elif (x>=3):
        y=math.sin(x**2)
    print('y =',y)
input()