import numpy as np
import random	
import pdb
import Functions as func
import Classifier as cl

def Perceptron_Learning_Test(num, iter):
	Neuron = cl.Perceptron(func.Step(), 2)
	data = np.zeros((num,2))
	expected = np.zeros((num))
	for d in range(num):
		data[d][0] = random.uniform(-50.0,50.0)
		data[d][1] = random.uniform(-120.0,120.0)
		if 3*data[d][0]+5 < data[d][1]:	#Should be any curve
			expected[d] = 1
		else:
			expected[d] = 0
		
	start_params = [Neuron.weights, Neuron.bias]
	
	#print(data, end="\n")
	#print(expected)
	out = np.zeros((num))
	for i in range(iter):
		#print(out)
		for j in range(num):
			out[j] = Neuron.feed(data[j])
			Neuron.train(data[j], expected[j])
					
	acc = 0
	for a in range(num):
		if expected[a] == out[a]:
			acc += 1
	
	print((acc/num)*100)
	
Perceptron_Learning_Test(10000,2)
Perceptron_Learning_Test(10000,20)
Perceptron_Learning_Test(10000,50)