def calculator(From,To,n):
    if From>10:
        n = list(n)
        for i in range(len(n)):
            if 91>ord(n[i])>64:
                n[i] = str(ord(n[i])-55)
    p = False
    for i in n:
        if '0'<=i<='9' and int(i)>=From:
            p = True
        elif 'A'<=i<='Z':
            if 91>ord(i)>64 and ord(i)-55>=From:
                p = True
    if p:
        return "неверное вводимое число"
    if From == 10:
        n = int(n)
        b = []
        while n>=To:
            b.append(n%To)
            n//=To
        b.append(n)
        b = b[::-1]
    if To == 10 or From != 10:
        b = 0
        for i in range(len(n)):
            b += int(n[-(i+1)])*(From**i)
        if To!=10:
            return calculator(10,To,str(b))
    if To>10:
        for i in range(len(b)):
            if b[i]>=10:
                b[i] = chr(b[i]+54)
    b = ''.join(str(i) for i in b) if type(b) is list else b
    return b

while True:
    n = input("Введите число: ").upper()
    From_ = int(input("Перевести из: "))
    To_ = int(input("В: "))
    print("Результат: ",calculator(From_,To_,n))
    print('-'*60)
    if n == 0:
        break