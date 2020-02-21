n1 = int(input('Первое число: '))
n2 = int(input('Второе число: '))
n3 = int(input('Третье число: '))
n = 0
if n1>0 and (n1%2)==0:
    n = n + 1
if n2>0 and (n2%2)==0:
    n = n + 1
if n3>0 and (n3%2)==0:
    n = n + 1
print('Положительных и чётных чисел: ' + str(n))
input()

