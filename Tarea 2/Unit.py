
class Unit(object):
	"""
	Class representing an individual
	"""
	def __init__(self, genes):
		"""
		genes: Numpy array. Genetic information provided by the algorithm 
		"""
		self.dna = genes
		self.fitness = 0
		
	def __lt__(self, other):
		return self.fitness < other.fitness
		
	def __eq__(self, other):
		return self.fitness == other.fitness