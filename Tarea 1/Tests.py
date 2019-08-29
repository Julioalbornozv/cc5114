import numpy as np
import random	
import pdb
import Functions as func
import Perceptron as pc
import Network as ntk

def Perceptron_Learning_Test(num, iter):
	Neuron = pc.Perceptron(func.Step(), 2, 0.1)
	data = np.zeros((num,2))
	expected = np.zeros((num))
	for d in range(num):
		data[d][0] = random.uniform(-50.0,50.0)
		data[d][1] = random.uniform(-120.0,120.0)
		if 3*data[d][0]+5 < data[d][1]:	#Generalize this code
			expected[d] = 1
		else:
			expected[d] = 0
		
	start_params = [Neuron.weights, Neuron.bias]
	
	out = np.zeros((num))
	for i in range(iter):
		for j in range(num):
			out[j] = Neuron.feed(data[j])
			Neuron.train(data[j], expected[j])
					
	acc = 0
	for a in range(num):
		if expected[a] == out[a]:
			acc += 1
	
	print((acc/num)*100)
	
def Network_System_Test(n_l, n_h, n_i, n_o, func, lr):
	lay = n_h.copy()
	lay.append(n_o)
	
	Neural = ntk.Network(n_l, n_h, n_i, n_o, func, lr)
	
	### Construction Tests
	
	assert len(Neural.layers) == n_l, "Error: Incorrect number of layers"
	for l in range(len(Neural.layers)):
		assert len(Neural.layers[l].neurons) == lay[l], "Error: Incorrect number of Perceptrons were created"
		
	### Processing Tests
	sample = [0.1, 0.5, 0.8, 0.2, 0.3, 0.2]
	Neural.train(sample, [0.4, 0.3, 0.4, 0.9, 0.2])
	
	out = []
	for layer in Neural.layers:
		out_layer = []
		for neuron in layer.neurons:
			out_layer.append(neuron.out)
		out.append(out_layer)
	
	print(out)
	
	for num in range(len(out[-1])):
		assert out[-1][num] != 0, "Error: Output was not saved properly"
		assert sample[num] != out[-1][num], "Error: Input did not change"
		
def Main_Test():
	#print("Starting Tests...\nRunning Perceptron Test...")
	#Perceptron_Learning_Test(10000,2)
	#Perceptron_Learning_Test(10000,20)
	#Perceptron_Learning_Test(10000,50)
	print("Test Passed\nRunning Network Tests...")
	Network_System_Test(4, [3, 5, 2], 6, 4, func.Sigmoid(), 0.1)
	print("Test Passed")
	
Main_Test()