def calculator(F, T, n, accuracy = 0, m = '', c = ''):

    if n.find('.')!=-1:
        n, m = n.split('.')
    
    # Преобразование букв в цифры
    if F>10:
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
        if '0'<=i<='9' and int(i)>=F:
            p = True
            break
        elif 'A'<=i<='Z':
            if 91>ord(i)>64 and ord(i)-55>=F:
                p = True
                break

    # Проверка дробной части
    for i in m:
        if '0'<=i<='9' and int(i)>=F:
            p = True
            break
        elif 'A'<=i<='Z':
            if 91>ord(i)>64 and ord(i)-55>=F:
                p = True
                break
    if p:
        return "неверное вводимое число!"
    
    # Из 10-тичной в любую другую
    if F == 10:
        n = int(n)
        b = []
        while n>=To:
            b.append(n%To)
            n //= To
        b.append(n)
        b = b[::-1]
        if len(m)>0:
            lenM = len(m)
            m = int(m) / 10 ** lenM
            c = []
            for i in range(accuracy if accuracy!=0 else lenM):
                m *= T
                c.append(int(m))
                m -= int(m)
    
    # Из любой в 10-тичную
    if T == 10 or F != 10:
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
    if T>10:
        for i in range(len(b)):
            if b[i]>=10:
                b[i] = chr(b[i]+55)
        if len(c)>0:
            for i in range(len(c)):
                if c[i]>=10:
                    c[i] = chr(c[i]+55)

    # Преобразовние списка в строку
    b = ''.join(str(i) for i in b) if type(b) is list else b
    c = ''.join(str(i) for i in c) if type(c) is list else c
    return (b + '.' + c) if c!='' else b

while True:
    n = input("Введите число: ").upper()
    From = int(input("Перевести из: "))
    To = int(input("В: "))
    print("Результат: ",calculator(From,To,n))
    print('-'*60)
    if n == 0:
        break