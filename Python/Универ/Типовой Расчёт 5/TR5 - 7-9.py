#Данные
m=[[1,4,6,-4,-9,-12,1,9,5,-31,0,-3,-1],[4,-10,9,2,-5,-1,9,3,-18]]
#7 Задание
rm=[]
#8 Задание
max,min = 0,0
#9 Задание
c=0

#Обработка списка
for i in range(len(m)):
    for j in range(len(m[i])):
        #7 Задание
        if (m[i][j]%2!=0):
            rm.append(m[i][j])
        #8 Задание
        if (max<m[i][j]):
            max=m[i][j]
        elif (min>m[i][j]):
            min=m[i][j]
        #9 Задание
        if (m[i][j]==9):
            c+=1
#8 Задание
for i in range(len(m)):
    for j in range(len(m[i])):
        if (m[i][j]==max):
            m[i][j]=min

#Вывод
#7 Задание
print('Нечётные числа в порядке возрастания:')
rm.sort()
print(rm)
#8 Задание
print('Список в котором максимальое значение заменено на минимальное:')
print(m)
#9 Задание
print('Кол-во девяток:',c)