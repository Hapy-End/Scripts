def calculator(F, T, n, accuracy = 0, m = '', c = ''):
 #F=10 T=4 n='0.025'
    if n.find('.')!=-1: #True
        n, m = n.split('.') #n='0', m='025'
    
    # Преобразование букв в цифры
    if F>10: #False
        n = list(n)
        for i in range(len(n)):
            if 91>ord(n[i])>64:
                n[i] = str(ord(n[i])-55)
        if len(m)>0:
            m = list(m)
            for i in range(len(m)):
                if 91>ord(m[i])>64:
                    m[i] = str(ord(m[i])-55)

    # Проверка целой части
    p = False
    for i in n:
        if '0'<=i<='9' and int(i)>=F: #False
            p = True
            break
        elif 'A'<=i<='Z': #False
            if 91>ord(i)>64 and ord(i)-55>=F:
                p = True
                break

    # Проверка дробной части
    for i in m:
        if '0'<=i<='9' and int(i)>=F: #False
            p = True
            break
        elif 'A'<=i<='Z': #False
            if 91>ord(i)>64 and ord(i)-55>=F:
                p = True
                break
    if p: #False
        return "неверное вводимое число!"
    
    # Из 10-тичной в любую другую
    if F == 10: #True
        n = int(n) # n=0
        b = [] 
        while n>=To: #False
            b.append(n%To)
            n //= To
        b.append(n) #b=[0]
        b = b[::-1] #b=[0]
        if len(m)>0: #True
            lenM = len(m) #3
            m = int(m) / 10 ** lenM #m=0.025
            c = [] 
            for i in range(accuracy if accuracy!=0 else lenM):                                    # i = 0       i=1      i=3
                m *= T                   # m=0.1 m=0.4 m=1.6
                c.append(int(m))# c = [0] c=[0,0] c=[0,0,1]
                m -= int(m)          # m=0.1 m=0.4  m=0.6
    
    # Из любой в 10-тичную
    if T == 10 or F != 10: #False
        b = 0
        for i in range(len(n)):
            b += int(n[-(i+1)])*(F**i)
        if len(m)>0:
            c = 0
            for i in range(len(m)):
                c += int(m[i])*(F**(-1-i))
            b += round(c,accuracy if accuracy!=0 else len(m))
        if T!=10:
            return calculator(10,T,str(b))
    
    # Преобразование чисел в буквы
    if T>10: #False
        for i in range(len(b)):
            if b[i]>=10:
                b[i] = chr(b[i]+55)
        if len(c)>0:
            for i in range(len(c)):
                if c[i]>=10:
                    c[i] = chr(c[i]+55)

    # Преобразовние списка в строку
    b = ''.join(str(i) for i in b) if type(b) is list else b #True, b='0'
    c = ''.join(str(i) for i in c) if type(c) is list else c #True, c='001'
    return (b + '.' + c) if c!='' else b #True, return '0.001'

while True:
    n = input("Введите число: ").upper()
    From = int(input("Перевести из: "))
    To = int(input("В: "))
    print("Результат: ",calculator(From,To,n))
    print('-'*60)
    if n == 0:
        break