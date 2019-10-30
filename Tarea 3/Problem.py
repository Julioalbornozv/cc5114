from abc import ABC, abstractmethod
from Unit import Unit
import random
import numpy as np
import Tree as T

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
	def gene_generator(self, f_set, var_set):
		"""
		Returns a tree based on the sets given
		"""
		pass
	
	@abstractmethod
	def individual_generator(self, f_set, var_set):
		"""
		Generates an individual
		"""
		pass
		
class Find_Number(Problem):
	"""
	Find a tree structure that when evaluated it will return a specific number
	"""
	def fitness_function(self, unit):
		self.target - np.abs(unit.dna.eval() - self.target)
	
	def gene_generator(self, function_set, value_set):
		"""
		In this case the genes are replaced with a tree
		"""
		return T.AST(function_set, value_set)
		
	def individual_generator(self, func_set, val_set):
		tree = self.gene_generator(func_set, val_set)
		unit = Unit(tree())
		self.fitness_function(unit)
		return unit
	
class Variable_Teminals(Problem):
	def fitness_function(self, unit):
		pass
		
	def gene_generator(self, function_set, value_set):
		"""
		In this case the genes are replaced with a tree
		"""
		return T.AST(function_set, value_set)
		
	def individual_generator(self, func_set, val_set):
		tree = self.gene_generator(func_set, val_set)
		unit = Unit(tree)
		self.fitness_function(unit)
		return unit
		
class Symbolic_Regression(Problem):
	def fitness_function(self, unit):
		pass
		
	def gene_generator(self, function_set, value_set):
		"""
		In this case the genes are replaced with a tree
		"""
		return T.AST(function_set, value_set)
		
	def individual_generator(self, func_set, val_set):
		tree = self.gene_generator(func_set, val_set)
		unit = Unit(tree)
		self.fitness_function(unit)
		return unit

class Division_Nodes(Problem):
	def fitness_function(self, unit):
		pass
		
	def gene_generator(self, function_set, value_set):
		"""
		In this case the genes are replaced with a tree
		"""
		return T.AST(function_set, value_set)
		
	def individual_generator(self, func_set, val_set):
		tree = self.gene_generator(func_set, val_set)
		unit = Unit(tree)
		self.fitness_function(unit)
		return unit
	
	