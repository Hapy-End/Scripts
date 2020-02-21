a=[1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1]
max0=[]
min1=[]
min_1=0
max_0=0
for i in a:
    if i==1:
        min_1+=1
        if max_0!=0:
            max0.append(max_0)
            max_0=0
    elif i==0:
        max_0+=1
        if min_1!=0:
            min1.append(min_1)
            min_1=0
min1.append(min_1)
max0.append(max_0)
max_0=0
min_1=0
for i in max0:
    if (i>max_0) or (max_0==0):
        max_0=i
for i in min1:
    if (i<min_1) or (min_1==0):
        min_1=i
print(min_1,max_0)
print(min1,max0)
