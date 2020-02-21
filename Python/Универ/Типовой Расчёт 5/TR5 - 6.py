m=[0,8,4,-3,10,8,16,9,-2,8]
index=0
s=0
for i in m:
    if (i==8):
        s+=index
    index+=1
print('6. Сумма индексов числа 8 равна',s)