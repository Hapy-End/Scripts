def nod(n,m):
    while n!=m:
        n, m = m, n-m if n>m else m-n
    return n
print(nod(1000,990))