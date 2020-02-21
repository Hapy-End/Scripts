y=0
for i in range(1, 11):
    y=(2**i + y)**(1/2)
    print('Результат на',i,'шаге =',y)
print('y =',y)
input()