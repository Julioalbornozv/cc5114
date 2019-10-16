import Problem as Pb
import Gen_Alg as GA
import Unit as U
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm

def end(gen):
	if gen > 1000:
		return True
	else:
		return False

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

	bit = Pb.Bit_Seq(np.array([0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0]))
	gen = GA.Board(bit.fitness_function, bit.gene_generator, bit.individual_generator, 100, 2, end)

	gen.run()
	plot_results(gen.fit_record)

	
def string_search_test():
	ss = Pb.Word_Search(np.array(["h","e","l","l","o","w","o","r","l","d"]))
	gen = GA.Board(ss.fitness_function, ss.gene_generator, ss.individual_generator, 100, 1, end)

	gen.run()
	plot_results(gen.fit_record)
	
def knapsack_test():
	UK = Pb.Unbound_Knapsack(15)
	gen = GA.Board(UK.fitness_function, UK.gene_generator, UK.individual_generator, 10, 2, end)

	gen.run()
	plot_results(gen.fit_record)

#bit_sequence_test()
#string_search_test()
#knapsack_test()
