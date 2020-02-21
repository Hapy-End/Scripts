A = int(input('Введите сторону A: '))
B = int(input('Введите сторону B: '))
C = int(input('Введите сторону C: '))
if (A+B>C) and (A+C>B) and (B+C>A):
    print('Треугольник существует!')
else:
    print('Такого треугольника не существует')
input()