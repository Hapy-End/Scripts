#Задание 1
N=(input('Введите числа через пробел: ')).split(' ')
i_min=int(input('Минимальное значение: '))
i_max=int(input('Максимальное значение: '))
#Переменные 2 задания
a,index = [],0
#Переменные 1 задания
_s_,_n_ = 0,0
#Переменные 3 задания
_s,_n,max = 0,0,0
for i in N:
    #Задание 1
    i=int(i)
    if (i_min<i<i_max):
        if (i>0) and (i%2!=0):
            _s_+=i
            _n_+=1
    #Задание 2
    if (i>5):
        a.append(index)
    index+=1
    #Задание 3
    if (i<0):
        if (_n==0):
            max=i
        _s+=i
        _n+=1

        if(max<i):
            max=i
print('1. Среднее арифметическое положительных нечётных чисел (в интервале ['+str(i_min)+':'+str(i_max)+']):', _s_/_n_)
print('2. Индексы элементов списка, которые больше 5:', a)
sr=_s/_n
print('3. Среднее арифметическое отрицательных чисел:',sr)
sr=max
print('   Максимальное значение из списка:',sr)