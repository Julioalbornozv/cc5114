import Unit as U
import numpy as np
import random
import Tree as T
import pdb

class Board(object):
	"""
	Genetic algorithm class
	"""
	def __init__(self, fitness_func, gene_gen, unit_gen, pop_size, mut_rate, termination, func_set, var_set):
		"""
		Methods:
		--------
		fitness_func:	Calculates the problem's fitness value of an individual
		gene_gen:		Generates genetic information
		unit_gen:		Generates the initial population

		Params:
		-------
		pop_size:		Population size
		mut_rate:		Mutation Rate (As the number of genes to be modified)
		termination:	Termintion Condition
		func_set:		Function Set for the internal nodes
		var_set:		Concrete values for the leaves
		
		----------------------------------------------------------------------------

		Local Sets:
		-----------
		collection:		Set of individuals being simuated
		generation:		Current generation being simulated
		best:			Individual with the best fitness overall
		best_time:		Generation in which the current best was generated
		fit_record:		Record of the fitness score from the best, worst and average
		                performers
		
		"""
		self.fitness = fitness_func
		self.gene_gen = gene_gen
		self.unit_gen = unit_gen
		self.pop = pop_size
		self.mut = mut_rate
		self.term = termination
		self.func_set = func_set
		self.var_set = var_set

		self.collection = []
		self.generation = 0

		for unit in range(pop_size):
			self.collection.append(self.unit_gen(self.func_set, self.var_set))

		self.fit_record = []
		self.best = U.Unit(None)
		self.best_time = 0		
		
	def reset(self):
		"""
		Resets previous results
		"""
		self.collection = []
		for unit in range(self.pop):
			self.collection.append(self.unit_gen(self.func_set, self.var_set))
			
		self.generation = 0
		self.fit_record = []
		self.best = U.Unit(None)
	
	def recover(self):
		"""
		Saves relevant data
		"""
		#pdb.set_trace()
		if max(self.collection).fitness > self.best.fitness:
			self.best = max(self.collection)
			self.best_time = self.generation
				
		low = min(self.collection).fitness
		high = max(self.collection).fitness
		avg = (high + low)/2

		self.fit_record.append((high,avg,low))
	
	def run(self):
		"""
		Executes the algorithm until the end condition is met
		"""
		while(self.term(self) == False):
			self.generation += 1
			
			### Evaluation Phase
			self.rank()
			self.recover()
			
			### Selection Phase
			pairs = []
			for i in range(len(self.collection)):
				pairs.append((self.tournament(), self.tournament()))

			### Reproduction Phase
			new = []
			for par in pairs:
				offspring = self.crossover(par)
				self.mutate(offspring)

				new.append(offspring)

			self.collection = new
		
		#Saves last generation data
		self.rank()
		self.recover()
		
	def rank(self):
		"""
		Updates the fitness value of each individual and sorts them depending on the results
		"""
		for unit in self.collection:
			self.fitness(unit)

	def tournament(self):
		"""
		Selects a random set of individuals and choose the one with higher fitness
		"""
		selected = []
		n_set = 5
		indexes = np.random.randint(low=0, high=len(self.collection)-1, size=n_set)
		for i in indexes:
			selected.append(self.collection[i])

		return max(selected)

	def crossover(self,pair):
		"""
		Given two individuals, the method will split their genetic code and generate an offspring which will inherit from both parents
		"""
		pdb.set_trace()
		new_element = pair[0].dna.copy()
		p1 = random.choice(new_element.serialize())
		
		p2_node = random.choice(pair[1].dna.serialize())
		p2 = p2_node.copy()
		
		p1.replace(p2)
		
		offspring = U.Unit(new_element)
		return offspring

	def mutate(self, unit):
		"""
		Overrides a number of tree nodes from an individual AST
		"""
		#pdb.set_trace()
		nodes = unit.dna.serialize()
		for i in range(self.mut):
			mutation = T.AST(self.func_set, self.var_set)()
			chosen = random.choice(nodes)
			chosen.replace(mutation)
			
