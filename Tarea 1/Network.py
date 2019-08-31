import numpy as np
import Perceptron as pc
import Functions as fc
import pdb

class Layer(object):
	def __init__(self, n_p , n_i , act, lr):
		"""
		n_p: Integer, number of neurons contained in this layer
		n_i: Integer, number of inputs recieved by each Perceptron
		act: Activation function
		lr: Learning rate
		
		self.prev: Previous Layer Object
		self.next: Next Layer Object
		"""
		
		self.neurons = []
		for i in range(n_p):
			self.neurons.append(pc.Perceptron(act, n_i, lr))
				
		self.act = act
		self.lr = lr
		
		self.prev = None
		self.next = None
		
	def feed(self, inputs):
		out = []
		for n in self.neurons:
			out.append(n.feed(inputs))
		
		if self.next != None:
			result = self.next.feed(out)
			return result
			
		else:
			return out
		
	def initialDelta(self, expected):
		"""
		Calculates the delta of the neurons in the output layer, propagates the error through the network 
		
		expected: Integer list, expected behaviour
		"""
		for n in range(len(self.neurons)):
			error = expected[n] - self.neurons[n].out
			self.neurons[n].delta = error * self.act.derivative(self.neurons[n].out)
		
		if self.prev != None:
			self.prev.propagateError()
			
	
	def propagateError(self):
		"""
		Calculates the delta of the neurons in a hidden layer based on the deltas obtained
		in the next layer
		
		TODO: Reduce trainwrecks (self.a.b.c.d.e....)
		"""
		for n in range(len(self.neurons)):
			error = 0.0
			for m in range(len(self.next.neurons)):
				error += self.next.neurons[m].weights[n] * self.next.neurons[m].delta
			self.neurons[n].delta = error * self.act.derivative(self.neurons[n].out)
		
		if self.prev != None:
			self.prev.propagateError()
			
	def updateWeights(self, inputs):
		"""
		Updates weight and bias considering the new deltas obtaibed by the backpropagation process
		
		inputs: Inputs recieved during the feeding process
		"""
		
		out = []
		for neuron in self.neurons:
			for w in range(len(inputs)):
				neuron.weights[w] += (self.lr * neuron.delta * inputs[w])
			neuron.bias += self.lr * neuron.delta
			out.append(neuron.out)
		
		if self.next != None:
			self.next.updateWeights(out)
			
class Network(object):
	def __init__(self, n_l, n_h, n_i, n_o, act, lr):
		"""
		Neural Network class
		
		n_l: Integer, Number of layers contained in the network
		n_h: Integer List containing number of neurons per hidden layer
		n_i: Integer, Number inputs recieved
		n_o: Integer, Number of outputs returned by the network
		act: Function Object, Activation function used in the network
		lr:  Integer, Learning rate
		"""
		self.layers = []
		self.act = act
		self.lr = lr
		self.nlist = n_l
		
		n_h.append(n_o)
		n_h.insert(0, n_i)
		
		#Layer initialization
		for i in range(1, len(n_h)):
			self.layers.append(Layer(n_h[i], n_h[i-1], act, lr))
		
		#Layer Linking
		self.layers[0].prev = None
		self.layers[0].next = self.layers[1]
		self.layers[-1].next = None
		self.layers[-1].prev = self.layers[-2]
		
		for j in range (1, n_l-1):
			self.layers[j].prev = self.layers[j-1]
			self.layers[j].next = self.layers[j+1]
	
	
	def load_weights(self, precomp):
		"""
		Recieves a weight matrix containing the weights from the input layer neurons
		
		precomp: Integer list of lists, contains weight of each neuron in the input
		
		TODO: Recieve a data cube containing the weights of all neurons in the network
		"""
		for n in range(len(self.layers[0])):
			neuron = self.layers[0].neurons[n]
			neuron.weights = precomp[0]
	
	def feed(self, inputs):
		"""
		Feeds the input vector to the network, returning the output from the last layer
		
		inputs: Integer list, contains inputs to be processed
		"""
		return self.layers[0].feed(inputs)			
		
	def train(self, inputs, expected):
		"""
		Feeds the input vector to the network, after a result is compiled the network 
		compares it with the expected result and learns depending on its accuracy
		
		inputs: Integer list, contains inputs to be processed
		expected; Integer list, expected outcome of the feeding process
		"""
		out = self.layers[0].feed(inputs)
		self.backwardPropagateError(expected)
		self.updateWeights(inputs)
				
	def backwardPropagateError(self, expected):
		"""
		Executes the backpropagtion process depending on the network accuracy
		
		expected: Integer list
		"""
		self.layers[-1].initialDelta(expected)
		
	def updateWeights(self, inputs):
		"""
		Update the weights of each neuron based on the deltas obtained by backpropagation
		
		inputs: Integer list, input recieved in this cycle
		"""
		self.layers[0].updateWeights(inputs)
		
		
		
		