from abc import ABC, abstractmethod

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
		pass
	
	def gene_generator(self):
		pass
	
	def individual_generator(self):
		pass
		
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