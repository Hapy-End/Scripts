A = int(input('A: '))
B = int(input('B: '))
C = int(input('C: '))
if abs(A-B)==abs(A-C):
    print('B и C на одинаковом расстоянии от А!\n Расстояние: ' + str(abs(B-A)))
elif B-A<C-A:
    print('Точка C ближе к A!\nИ расстояние между ними: ' + str(abs(C-A)))
elif B-A>C-A:
    print('Точка B ближе к A!\nИ расстояние между ними: ' + str(abs(B-A)))
input()