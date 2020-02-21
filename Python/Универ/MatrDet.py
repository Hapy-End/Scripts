import numpy as np
def det(matrix):
	if len(matrix)>2:
		sum = 0
		for i in range(len(matrix)):
			const = matrix[0,i] * (1 if i%2==0 else -1)
			b = np.delete(np.delete(matrix,i,1),0,0)
			sum += const * det(b)
		return sum
	else:
		return matrix[0,0]*matrix[1,1] - matrix[0,1]*matrix[1,0]

a = np.random.randint(-10,10,(5,5))
print(a)
print(det(a))
print(np.linalg.det(a))