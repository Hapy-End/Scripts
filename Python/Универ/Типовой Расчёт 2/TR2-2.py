size = int(input('Введите значение: '))
ed = input('Введите единицу измерения (Б/B,КБ/KB,МБ/MB):\n')
if ed=='Б' or ed=='B':
    print('Байты: ' + str(size) + '\nКилобайты: ' + str(size / 1024) + '\nМегабайты: ' + str((size / 1024)/1024))
elif ed=='КБ' or ed=='KB':
    print('Байты: ' + str(size * 1024) + '\nКилобайты: ' + str(size)  + '\nМегабайты: ' + str(size/1024))
elif ed=='МБ' or ed=='MB':
    print('Байты: ' + str((size * 1024)*1024) + '\nКилобайты: ' + str(size * 1024) + '\nМегабайты: ' +str(size))
else:
    print('Вы не правильно ввели единицу измерения!!!')
input()