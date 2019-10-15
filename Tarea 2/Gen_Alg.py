import Unit as U
import numpy as np

class Board(object):
	"""
	Genetic algorithm class
	"""
	def __init__(self, fitness_func, gene_gen, unit_gen, pop_size, mut_rate, termination):
		"""
		Methods:
		--------
		fitness_func:	Calculates the problem's fitness value of an individual
		gene_gen:		Generates genetic information
		unit_gen:		Generates the initial population
		
		Params:
		-------
		pop_size:		Population size
		mut_rate:		Mutation Rate (As percentage)
		termination:	Termintion Condition
		----------------------------------------
		
		Local Sets:
		-----------
		collection:		Set of individuals being simuated
		generation:		Current generation being simulated
		
		
		"""
		self.fitness = fitness_func
		self.gene_gen = gene_gen
		self.unit_gen = unit_gen
		self.pop = pop_size
		self.mut = mut_rate
		self.term = termination
		
		self.collection = []	
		self.generation = 0		
		
		for unit in range(pop_size):
			self.collection.append(self.unit_gen())
			
	def run(self):
		"""
		Executes the algorithm until the end condition is met
		"""
		while(self.term(self.generation) == False):	#Generalize termination condition check
			self.generation += 1
			
			### Evaluation Phase
			self.rank()
			
			### Selection Phase  #TODO: Merge this phases
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
		n_set = 10 #TODO: Make it customizable
		indexes = np.random.randint(low=0, high=len(self.collection)-1, size=n_set)
		for i in indexes:
			selected.append(self.collection[i])
		
		return max(selected)
			
	def crossover(self,pair):
		"""
		Given two individuals, the method will split their genetic code and generate an offspring which will inherit from both parents
		"""
		pivot = 5 #TODO: Make it customizable
		dna = np.concatenate((pair[0].dna[0:pivot], pair[1].dna[pivot:]))
		off = U.Unit(dna)
		return off
		
	def mutate(self, unit):
		"""
		Replaces certain genes of an individual with new data
		"""
		l = len(unit.dna)
		mod = (l * self.mut) / 100	#Number of genes to be modified
		index_list = np.asarray(range(l))
		np.random.shuffle(index_list)
		
		for i in index_list:
			mut = self.gene_gen()
			unit.dna[i] = mut
		