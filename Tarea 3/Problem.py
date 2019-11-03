from abc import ABC, abstractmethod
from Unit import Unit
import random
import numpy as np
import Tree as T
import pdb
class Problem(ABC):
	"""
	Class which contains all problem-dependent methods/classes, define each problem by inheriting from this abstract class and defining the methods required by the algorithm
	"""
	def __init__(self, target, env = {}, **kwargs):
		"""
		target: Expected outcome of the algorithm
		"""
		self.target = target
		self.env = env
		self.specs = kwargs
		
	@abstractmethod
	def fitness_function(self, unit):
		"""
		Calculates the fitness of a given individual
		"""
		pass
	
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

class Find_Number(Problem):
	"""
	Find a tree structure that when evaluated it will return a specific number
	"""
	def fitness_function(self, unit):
		counters = unit.dna.count({})
		repeats, growth = 1, 1
		
		if self.specs.get("repetition") == False:
			repeats = sum(counters.values()) - len(counters.values())
			
		if self.specs.get("prune") == True:
			growth = unit.dna.measure()
			
		unit.fitness = 1.0 / (growth*repeats + np.abs(unit.dna.eval() - self.target))

class Variable_Terminals(Problem):
	def fitness_function(self, unit):
		counters = unit.dna.count({})
		growth = unit.dna.measure()
		
		unit.fitness = 1.0 / (growth + np.abs(unit.dna.eval_env(self.env) - self.target))
		
		
class Symbolic_Regression(Problem):
	def fitness_function(self, unit):
		growth = unit.dna.measure()
		expected = self.target.eval_env(self.env)
		try:
			unit.fitness = 1.0 / (growth + np.abs(unit.dna.eval_env(self.env)-expected))
		except ZeroDivisionError:
			unit.fitness = 0.0