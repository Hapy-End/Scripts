#pylint:disable=C0304
#pylint:disable=C0200
#pylint:disable=R0902
#pylint:disable=W0622
#pylint:disable=W0612
#pylint:disable=C0111
#pylint:disable=W0201
#pylint:disable=C0103
#pylint:disable=W0312

import numpy as np

class NeuralNetwork:
	def __init__(self, input, output, c=1):
		self.input = input
		self.output = output
		self.w1 = 2*np.random.random((self.input.shape[1],self.input.shape[0])) - 1
		self.w2 = 2*np.random.random((self.input.shape[0],c)) - 1
	def train(self,n):
		for i in range(n):
			self.l1 = 1/(1+np.exp(-(np.dot(self.input,self.w1))))
			self.l2 = 1/(1+np.exp(-(np.dot(self.l1,self.w2))))
			self.l2_h = (self.output - self.l2)*(self.l2*(1-self.l2))
			self.l1_h = self.l2_h.dot(self.w2.T) * (self.l1 * (1-self.l1))
			self.w2 += self.l1.T.dot(self.l2_h)
			self.w1 += self.input.T.dot(self.l1_h)
	def run(self):
		for i in range(len(self.input)):
			print(self.input[i],'-',self.l2[i])
	def get_result(self, input):
		self.l1 = 1/(1+np.exp(-(np.dot(input,self.w1))))
		self.l2 = 1/(1+np.exp(-(np.dot(self.l1,self.w2))))
		for i in range(len(input)):
			print(input[i],'-',self.l2[i])

X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
y = np.array([[0,1,1,0]]).T

NN = NeuralNetwork(X, y, 1)
NN.train(60000)
NN.run()
while True:
	x = np.array([list(map(int,
	input().split(' ')))])
	NN.get_result(x)