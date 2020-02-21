a=[[2,4,1,-4,-6,5],[6,2,-1,0,8,3],[1,7,4,-3,9,8]]
for i in range(len(a)):
	if i%2==0:
		for j in range(len(a[i])):
			if j%2!=0:
				print('#' + str(a[i][j]),end='#  ')
	print()
input()