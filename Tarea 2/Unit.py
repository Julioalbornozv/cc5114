
class Unit(object):
	"""
	Class representing an individual
	"""
	def __init__(self, genes):
		"""
		genes: Genetic information provided by the algorithm
		"""
		self.dna = genes
		self.fitness = 0
		