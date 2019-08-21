import numpy as np

class Step:
	def apply(x):
		if x < 0:
			return 0
		else:
			return 1
		
	def derivative(x):
		return 0
		
class Sigmoid:
	def apply(x):
		return 1 / (1 + np.exp(-x))
	
	def derivative(x):
		return self.apply(x) * (1 - self.apply(x))

class Tanh:
	def apply(x):
		return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
	
	def derivative(x):
		return 1 - np.tanh**2(x)