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
	if time_limit(board):
		print("Algorithm took too long\n")
		print("Result:\t{}".format(top.dna))
		return True
	board.rank()
	top = max(board.collection)
	if top.fitness == len(top.dna):
		print("Result:\t{}".format(top.dna))
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
	
def bit_sequence_test():

	target = 989898989898989
	bit = Pb.Bit_Seq(np.array(list(bin(target))[2:]).astype(int))
	gen = GA.Board(bit.fitness_function, bit.gene_generator, bit.individual_generator, 100, 2, fitness_limit)

	gen.run()
	plot_results(gen.fit_record)

	
def string_search_test():
	target = "supercalifragilisticoesprialidoso"
	ss = Pb.Word_Search(np.array(list(target)))
	gen = GA.Board(ss.fitness_function, ss.gene_generator, ss.individual_generator, 100, 1, fitness_limit)

	gen.run()
	plot_results(gen.fit_record)
	
def knapsack_test():
	UK = Pb.Unbound_Knapsack(15)
	gen = GA.Board(UK.fitness_function, UK.gene_generator, UK.individual_generator, 10, 2, time_limit)

	gen.run()
	plot_results(gen.fit_record)

bit_sequence_test()
string_search_test()
#knapsack_test()
