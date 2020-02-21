wh=0
res=0
while wh<10:
	n = int(input('Введите число ['+str(wh+1)+'-10]: '))
	if (-5<n<5):
		res+=n
	wh+=1
print('Результат: ',res)
input()