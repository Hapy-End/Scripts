pnp = int(input('Порядковый номер пальца (начиная с мизинца): '))
if pnp==1:
    print('Это мизинчик')
elif pnp==2:
    print('Это безымянный палец')
elif pnp==3:
    print('Это средний палец')
elif pnp==4:
    print('Это указательный палец')
elif pnp==5:
    print('Это большой палец')
else:
    print('У человека 5 пальцев на руке!\nОткуда вы взяли ' + str(pnp) + '?')
input()
