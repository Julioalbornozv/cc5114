from abc import ABC, abstractmethod
from Unit import Unit
import random
import numpy as np

class Problem(ABC):
	"""
	Class which contains all problem-dependent methods/classes, define each problem by inheriting from this abstract class and defining the methods required by the algorithm
	"""
	def __init__(self, target):
		"""
		target: Expected outcome of the algorithm
		"""
		self.target = target
		
	@abstractmethod
	def fitness_function(self, unit):
		"""
		Calculates the fitness of a given individual
		"""
		pass
	
	@abstractmethod
	def gene_generator(self):
		"""
		Returns a gene of the problem
		"""
		pass
	
	@abstractmethod
	def individual_generator(self):
		"""
		Generates an individual
		"""
		pass
		

class Bit_Seq(Problem):
	"""
	Find a bit sequence using a genetic algorithm
	"""
	def fitness_function(self, unit):
		diff = np.bitwise_xor(unit.dna, self.target)
		__, count = np.unique(diff, return_counts = True)
		unit.fitness = count[0]
		
	def gene_generator(self):
		return random.randint(0,1)
	
	def individual_generator(self):
		l = len(self.target)
		new = np.zeros((l), dtype=int)
		for i in range(l):
			new[i] = self.gene_generator()
			
		unit = Unit(new)
		self.fitness_function(unit)
		return unit
		
class Word_Search(Problem):
	"""
	Find a string using a genetic algorithm
	"""
	def fitness_function(self, unit):
		match = 0
		wor = self.target
		exp = unit.dna
		for i in range(len(wor)):
			if wor[i] == exp[i]:
				match += 1
			
		unit.fitness = match
	
	def gene_generator(self):
		valid = "abcdefghijklmnopqrstuvwxyz"
		return valid[random.randint(0,len(valid)-1)]
	
	def individual_generator(self):
		l = len(self.target)
		fill = ["a"]*l
		new = np.array(fill)
		for i in range(l):
			new[i] = self.gene_generator()
		
		unit = Unit(new)
		self.fitness_function(unit)
		return unit
		
class Unbound_Knapsack(Problem):
	"""
	Find the combination of boxes of fixed weight and value which maximize the value contained in a backpack of limited capacity using a genetic algorithm
	"""
	def fitness_function(self, unit):
		weights = np.array([12,2,1,1,4])
		values = np.array([4,2,2,1,10])
		
		data = unit.dna
		
		load_w = np.multiply(weights, data)
		load_v = np.multiply(values, data)
		
		unit.fitness = np.sum(load_v) - (np.sum(load_w) * abs(self.target - np.sum(load_w)))
	
	def gene_generator(self):
		return random.randint(0,15)
	
	def individual_generator(self):
		l = 5	#Generalize for n box types
		new = np.zeros((l))
		for i in range(l):
			new[i] = self.gene_generator()
		
		unit = Unit(new)
		self.fitness_function(unit)
		return unit

