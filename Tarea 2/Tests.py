import Problem as Pb
import Gen_Alg as GA
import Unit as U
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm


"""
End Conditions
"""

def time_limit(board):
	if board.generation > 300:
		return True
	else:
		return False

def fitness_limit(board):
	board.rank()
	top = max(board.collection)
	
	if time_limit(board):
		#print("Algorithm took too long\n")
		#print("Result:\t{}".format(top.dna))
		return True
	
	elif top.fitness == len(top.dna):
		#print("Result:\t{}".format(top.dna))
		return True
	else:
		return False

"""
Use Cases
"""

def plot_results(fitness):
	fit_reg = np.asarray(fitness)
	best = fit_reg[:,0]
	avg = fit_reg[:,1]
	worst = fit_reg[:,2]
	
	
	plt.plot(best)
	plt.plot(avg)
	plt.plot(worst)
	plt.show()
	
def bit_sequence_test(pop, mut):

	target = 989898989898989
	bit = Pb.Bit_Seq(np.array(list(bin(target))[2:]).astype(int))
	gen = GA.Board(bit.fitness_function, bit.gene_generator, bit.individual_generator, 100, 2, fitness_limit)

	gen.run()
	plot_results(gen.fit_record)

	
def string_search_test(pop, mut):
	target = "supercalifragilisticoesprialidoso"
	ss = Pb.Word_Search(np.array(list(target)))
	gen = GA.Board(ss.fitness_function, ss.gene_generator, ss.individual_generator, 100, 1, fitness_limit)

	gen.run()
	plot_results(gen.fit_record)
	
def knapsack_test(pop, mut):
	UK = Pb.Unbound_Knapsack(15)
	gen = GA.Board(UK.fitness_function, UK.gene_generator, UK.individual_generator, 100, 2, time_limit)

	gen.run()
	print("Result:\t{}\t{}".format(gen.best.dna, gen.best.fitness))
	plot_results(gen.fit_record)

def configuration_test():
	"""
	Solves each problem by generating a set of configuration/mutation_rate pairs and analysing the efficacy of each combination. Generates a heatmap with the results
	"""
	
	# Problem 1
	# Eficiency measured by the number of generations the algorithm took to solve the problem
	
	target = 76489
	bit = Pb.Bit_Seq(np.array(list(bin(target))[2:]).astype(int))
	gen = GA.Board(bit.fitness_function, bit.gene_generator, bit.individual_generator, 100, 2, fitness_limit)
	
	populations = list(range(50,300,50))
	mutability = list(range(0,10))
	matrix = np.zeros((len(mutability),len(populations)))
	
	i, j = 0, 0
	for p in populations:	# Population range
		for m in mutability:		# 0 to 90%
			gen.pop = p
			gen.mut = m
			gen.run()
			matrix[j,i] = gen.generation
			gen.reset()
			
			print(".", end="")
			j += 1
		print(":", end="")
		j = 0
		i += 1
					
	fig, ax = plt.subplots()
	for k in range(len(populations)):
		for l in range(len(mutability)):
			text = ax.text(k, l, int(matrix[l , k]), ha="center", va="center", color="w")
	
	im = ax.imshow(matrix, cmap=cm.copper)
	
	ax.set_yticks(np.arange(len(mutability)))
	ax.set_xticks(np.arange(len(populations)))
	ax.set_yticklabels(mutability)
	ax.set_xticklabels(populations)
	
	fig.tight_layout()
	plt.show()
	
# First attempts
#bit_sequence_test(100, 2)
#string_search_test(100, 1)
#knapsack_test(100, 2)

configuration_test()



