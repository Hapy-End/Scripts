Ax = int(input('Введите A[x]: '))
Ay = int(input('Введите A[y]: '))
Bx = int(input('Введите B[x]: '))
By = int(input('Введите B[y]: '))
Cx = int(input('Введите C[x]: '))
Cy = int(input('Введите C[y]: '))
if (Ax==Bx):
    print('4 вершина имеет координаты [' + str(Ax) + ':' + str(Cy) + ']')
elif (Ax==Cx):
    print('4 вершина имеет координаты [' + str(Ax) + ':' + str(By) + ']')
elif (Cx==Bx):
    print('4 вершина имеет координаты [' + str(Ax) + ':' + str(Ay) + ']')
else:
    print('С такими вершинами прямоугольника не может быть!!!')
input()
