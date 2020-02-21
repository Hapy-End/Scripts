print('Приветик :)')
#Начало цикла
while True:
  print('''\nВот то что я могу:\n
1.Найти среднее арифметическое/геометрическое чисел
2.Найти значение переменной y (по форм. y=x³+x²-¾)
3.Найти значения переменной y (по 3 разным форм.)
4.Найти периметр треугольника (Исп. его стороны)
5.Найти объем куба и площадь его поверхности (Исп. ребро)
6.Найти объем шара (Исп. радиус)
7.Найти площадь равностороннего треугольника (Исп. его сторону)
8.Посчитать кол-во букв в слове\n''')
  try:
    nfun = float(input('Введите номер нужной вам функции: '))
    
    #Первая задача
    if nfun == 1:
      a1 = input('Введите a¹: ')
      a2 = input('Введите a²: ')
      a3 = input('Введите a³: ')
      try:
        ma1 = float(a1)
        ma2 = float(a2)
        ma3 = float(a3)
        sAn = (ma1 + ma2 + ma3) / 3
        print('\nСреднее арифметическое этих чисел равно: ' + str(sAn))
        sGn = (ma1 * ma2 * ma3) ** (1/3)
        print('А среднее геометрическое = ' + str(sGn))
      except ValueError:
        print('!!!Что-то пошло не так!!!\nВозможно вы ввели не число\nПопробуйте ещё разок')
        
    #Вторая задача
    elif nfun == 2:
      try:
        x = float(input('x = '))
        y = (x ** 3) + (x ** 2) - (3 / 4)
        print('Получаем: ' + str(y))
      except ValueError:
        print('Походу вы не правильно ввели число или вовсе не ввели')
    #Третья задачка
    elif nfun == 3:
      try:
        e = 2.718
        x = float(input('\nx = '))
        A = float(input('A = '))
        B = float(input('B = '))
        C = float(input('C = '))
        if B!=0:
            y1 = ((x * A) / B) * (((x ** C) + 1) ** .5) *(1 / ((A ** x) + 1))
            print('По 1 форм. =  ' + str(round(y1,3))[0:5])
        else:
            print('1.В знаменатели получился 0, а на 0 делить нельзя')
        if (A**2+B-C)!=0:
            y2 = -2 * (((A ** x) + ((4 * (x ** 2)) / ((A ** 2) + B - C))) ** .5)
            print('По 2 форм. = ' + str(round(y2,3))[0:6])
        else:
            print('2.В знаменатели получился 0, а на 0 делить нельзя')
        if e>0:
            y3 = (x ** (A * C)) + (e ** -B) + (((A * x) + B) ** .5)
            print('По 3 форм. =  ' + str(round(y3,3))[0:5])
        else:
            print('3.В знаменатели получился 0, а на 0 делить нельзя')
      except ValueError:
        print('Походу вы не правильно ввели числа или вовсе не ввели')
    #Четвёртая
    elif nfun == 4:
      A = input('Введите сторону A: ')
      B = input('Введите сторону B: ')
      C = input('Введите сторону C: ')
      try:
        mA = float(A)
        mB = float(B)
        mC = float(C)
        pT = mA + mB + mC
        print('\nПериметр равен: ' + str(pT))
      except ValueError:
        print('!!!Что-то пошло не так!!!\nВозможно вы ввели не число\nПопробуйте ещё разок')
    #Пятая
    elif nfun == 5:
      hr = input('Введите длину ребра: ')
      try:
        mhr = float(hr)
        vK = mhr ** 3
        sPK = 6 * (mhr ** 2)
        print('\nОбъем куба: ' + str(vK) + '\nА площадь поверхности = ' + str(sPK))
      except ValueError:
        print('!!!Что-то пошло не так!!!\nВозможно вы ввели не число\nПопробуйте ещё разок')
    #Шестая
    elif nfun == 6:
      nPi = 3.14
      R = input('Введите радиус шара: ')
      try:
        mR = float(R)
        oSH = 4/3 * nPi * (mR ** 3)
        print('\nЕсли π взять равным 3.14,')
        print('Объем шара равен ' + str(oSH))
      except ValueError:
        print('!!!Что-то пошло не так!!!\nВозможно вы ввели не число\nПопробуйте ещё разок')
    #Седьмая
    elif nfun == 7:
      a = input('Введите a: ')
      try:
        ma = float(a)
        sRT = (3 * .5)/4 * (ma * 2)
        print('\nПлощадь равна ' + str(sRT))
      except ValueError:
        print('!!!Что-то пошло не так!!!\nВозможно вы ввели не число\nПопробуйте ещё разок')
    elif nfun == 8:
      a = input('Введите слово: ')
      print('\nВ вашем слове: ' + str(len(a)) + ' букв')
    else:
      print('   -----------------------------\n   :Выберите из доступных [1-8]:\n   -----------------------------')
  except ValueError:
    print('   -----------------------------\n   :Выберите из доступных [1-8]:\n   -----------------------------')