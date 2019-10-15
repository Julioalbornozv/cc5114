import Problem as Pb
import Gen_Alg as GA
import Unit as U
import numpy as np

def bit_sequence_test():
	
	def end(gen):
		if gen > 10:
			return True
		else:
			return False
	
	bit = Pb.Bit_Seq(np.array([0,0,1,0,1,0,1,0,1,1,0,1,0,1]))
	gen = GA.Board(bit.fitness_function, bit.gene_generator, bit.individual_generator, 10, 10, end)
	
	gen.run()
	
	
bit_sequence_test()