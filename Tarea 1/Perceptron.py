import numpy as np
import Functions as func
import random

class Perceptron(object):
	def __init__(self, function, n_in, learn):
		"""
		Perceptron class
		"""
		self.seed = random.seed()
		self.activation = function
		self.bias = random.uniform(-2.0,2.0)
		self.weights = np.zeros((n_in))
		self.lr = learn
		self.out = 0.0
		self.delta = 0.0
		
		for i in range(n_in):
			self.weights[i] = random.uniform(-50.0, 50.0)
		
	def feed(self, input):
		assert len(self.weights) == len(input), "Error: Largo de vectores no coincide"
		
		result = 0
		for i in range(len(self.weights)):
			result += self.weights[i] * input[i]
		
		self.out = self.activation.apply(result + self.bias)
		return self.out
		
	def train(self, input, expected):
		output = self.feed(input)
		diff = expected - output
		for n in range(len(self.weights)):
			self.weights[n] += (self.lr * input[n] * diff)
			
		self.bias += self.lr * diff