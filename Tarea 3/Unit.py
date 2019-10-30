
class Unit(object):
	"""
	Class representing an individual
	"""
	def __init__(self, tree):
		"""
		tree: AST representing a program
		"""
		self.dna = tree
		self.fitness = 0
		
	def __lt__(self, other):
		return self.fitness < other.fitness
		
	def __eq__(self, other):
		return self.fitness == other.fitness