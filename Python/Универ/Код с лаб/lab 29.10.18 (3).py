arr=[1,4,5,3,1,5,5,6,3,5,6,8,3,1]
print(arr)
el=[]
for i in arr:
    a=0
    for j in el:
        if i==j:
            a=1
            break
    if a!=1:
        el.append(i)
for i in el:
    c=0
    for j in arr:
        if i==j:
            c+=1
    print(i,'повторяется',c,'раз(а)')






