import Problem as Pb
import Gen_Alg as GA
import Unit as U
import numpy as np

def end(gen):
	if gen > 100:
		return True
	else:
		return False

def bit_sequence_test():

	bit = Pb.Bit_Seq(np.array([0,0,1,0,1,0,1,0,1,1,0,1,0,1]))
	gen = GA.Board(bit.fitness_function, bit.gene_generator, bit.individual_generator, 100, 2, end)

	gen.run()
	print(gen.fit_record)


def string_search_test():
	ss = Pb.Word_Search(np.array(["h","e","l","l","o","w","o","r","l","d"]))
	gen = GA.Board(ss.fitness_function, ss.gene_generator, ss.individual_generator, 100, 2, end)

	gen.run()
	print(gen.fit_record)

def knapsack_test():
	UK = Pb.Unbound_Knapsack(15)
	gen = GA.Board(UK.fitness_function, UK.gene_generator, UK.individual_generator, 10, 10, end)

	gen.run()

bit_sequence_test()
#string_search_test()
#knapsack_test()
