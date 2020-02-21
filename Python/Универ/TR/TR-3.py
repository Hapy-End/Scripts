from itertools import product
sym = '+ -'
vars = tuple(map(''.join, product(sym, repeat=8)))
number = '1. .2. .3. .4. .5. .6. .7. .8. .9'

z = []
for s in vars:
    numbers = number.split('.')
    for i in range(1,len(numbers),2):
        numbers[i] = s[i//2]
    z.append(''.join('' if x == ' ' else x for x in numbers))
ids = []
for i in z:
    s = 0
    n = ''
    c = 0
    for j in range(-1,-len(i)-1,-1):
        if i[j] == '+':
            s += int(n[::-1])
            n = ''
        elif i[j] == '-':
            s -= int(n[::-1])
            n = ''
        else:
            n += i[j]
    s += int(n)
    if s == 100:
        print(i,'=',s)