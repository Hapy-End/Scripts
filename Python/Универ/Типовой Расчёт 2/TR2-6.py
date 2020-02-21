print('Введите что-нибудь:')
st = input()
if len(st)>10:
    print(st + ' применена конкатенация')
else:
    print(st * 5)
input()