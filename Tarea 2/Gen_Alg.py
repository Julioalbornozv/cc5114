
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
		mut_rate:		Mutation Rate
		termination:	Termintion Condition
		----------------------------------------
		
		Local Sets:
		-----------
		collection:		Set of individuals being simuated
		generation:		Current generation being simulated
		
		
		"""
		self.fitness = fitness_func
		self.gene = gene_gen
		self.unit = unit_gen
		self.pop = pop_size
		self.mut = mutation rate
		self.term = termination
		
		self.collection = []	
		self.generation = 0		
		
		for unit in range(pop_size):
			self.collection.append(self.unit(self.gene, self.fitness))
			
	def rank(self):
		"""
		Updates the fitness value of each individual and sorts them depending on the results
		"""
		pass
	
	def tournament(self):
		"""
		Selects which individuals will be selected for crossover
		"""
		pass
		
	def crossover(self):
		"""
		Given two individuals, the method will split their genetic code and generate an offspring which will inherit from both parents
		"""
		pass
		
	def mutate(self):
		"""
		Replaces certain genes of an individual with new data
		"""
		pass