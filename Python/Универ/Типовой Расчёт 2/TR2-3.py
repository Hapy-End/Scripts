print('Введите координату x: ')
x = int(input())
print('Введите координату y: ')
y = int(input())
if x>0:
    if y<0:
        print('''       |
       |
       |
-------+-------
       |
       |  ТУТ
       |''')
    elif y>0:
        print('''       |
       |  ТУТ
       |
-------+-------
       |
       |
       |''')
    else:
        print('''       |
       |
       |
-------+--ТУТ--
       |
       |
       |''')
elif x<0:
    if y<0:
        print('''       |
       |
       |
-------+-------
       |
  ТУТ  |
       |''')
    elif y>0:
        print('''       |
  ТУТ  |
       |
-------+-------
       |
       |
       |''')
    else:
        print('''       |
       |
       |
--ТУТ--+-------
       |
       |
       |''')
else:
    if y<0:
        print('''       |
       |  ТУТ
       |
-------+-------
       |
      ТУТ
       |''')
    elif y>0:
        print('''       |
      ТУТ
       |
-------+-------
       |
       |
       |''')
    else:
        print('''       |
       |
       |
------ТУТ------
       |
       |
       |''')
input()