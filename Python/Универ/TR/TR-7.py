def fib(n):
    f = (1 + 5**(1/2)) / 2
    u = - 1/f
    return int((f**n-u**n)/5**(1/2))

print(fib(int(input())))