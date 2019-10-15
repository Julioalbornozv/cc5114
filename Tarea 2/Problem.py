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
		target: Expected outcome of the algorithm, represented as a numpy array
		"""
		self.target = target
		
	@abstractmethod
	def fitness_function(self, unit):
		pass
	
	@abstractmethod
	def gene_generator(self):
		pass
	
	@abstractmethod
	def individual_generator(self):
		pass
		

class Bit_Seq(Problem):
	"""
	Find a bit sequence using a genetic algorithm
	"""
	def fitness_function(self, unit):
		diff = np.bitwise_xor(unit.dna, self.target)
		__, count = np.unique(diff, return_counts = True)
		unit.fitness = count[0]  # count = #0, #1
		
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
		pass
	
	def gene_generator(self):
		pass
	
	def individual_generator(self):
		pass

class Unbound_Knapsack(Problem):
	"""
	Find a combination of boxes of fixed weight which maximize the capacity of backpack of limited capacity using a genetic algorithm
	"""
	def fitness_function(self, unit):
		pass
	
	def gene_generator(self):
		pass
	
	def individual_generator(self):
		pass