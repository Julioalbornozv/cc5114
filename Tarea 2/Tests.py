import Problem as Pb
import Gen_Alg as GA
import Unit as U
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm


"""
Termination Conditions
"""

def time_limit(board):
	"""
	Terminates process after a number of generations have passed
	"""
	if board.generation > 300:
		return True
	else:
		return False

def fitness_limit(board):
	"""
	Terminates a process if the maximum fitness has been reached, it will also terminate if the problems takes too long to solve
	"""
	board.rank()
	top = max(board.collection)
	
	if time_limit(board):
		return True
	
	elif top.fitness == len(top.dna):
		return True
	else:
		return False

def variation_limit(board):
	"""
	Terminates the process if the best unit remain the same for a fixed number of generations
	"""
	if board.generation-board.best_time > 300:
		return True
	
	return False
	
"""
Problem Analysis
"""

def solve(Problem, fit_pair, range, term_func):
	"""
	Solves a problem using a genetic algorithm, returns a fitness plot and a performance heatmap.

	@param Problem: Object representing a problem
	@param fit_pair: Tuple containing the population and mutation rate used for the fitness analysis
	@param range: Tuple containing the population and mutation ranges to be analysed
	@param term_func: Termination function to be used
	"""
	
	gen = GA.Board(Problem.fitness_function, Problem.gene_generator, Problem.individual_generator, fit_pair[0], fit_pair[1], term_func)

	gen.run()
	print("Result found:\t{}\tF:\t{}".format(gen.best.dna, gen.best.fitness))
	plot_results(gen.fit_record)	

	#Performance analysis
	gen.reset()
	print("Obtaining performance matrix...")
	configuration_test(gen, range[0], range[1])

def configuration_test(gen, x_range, y_range):
	"""
	Analyses the performance of the algorithm by generating a set of population/mutation_rate pairs and calculating the time of completion for each combination. Generates a heatmap with the results.
	
	@param gen: Genetic Algorithm to be evauated
	@param x_range: List containing the population range used
	@param y_range: List containing the mutation rate range used
	"""
	
	populations = x_range
	mutability = y_range
	
	matrix = np.zeros((len(mutability),len(populations)))
	
	i, j = 0, 0
	for p in populations:
		for m in mutability:
			gen.pop = p
			gen.mut = m
			gen.run()
			matrix[j,i] = gen.best_time	#Moment the algorithm reaches the solution
			gen.reset()
			
			j += 1
		j = 0
		i += 1
					
	plot_heatmap(matrix, populations, mutability)

"""
Plotting Methods
"""

def plot_results(fitness):
	"""
	Plots fitness graph for the best, average and worst solutions of each generation
	
	@param fitness: 3xn matrix containing the relevant data
	"""
	fit_reg = np.asarray(fitness)
	best = fit_reg[:,0]
	avg = fit_reg[:,1]
	worst = fit_reg[:,2]
	
	plt.plot(best)
	plt.plot(avg)
	plt.plot(worst)
	
	plt.title("Population Fitness over time")
	plt.xlabel("Generation")
	plt.ylabel("Fitness")
	plt.show()

def plot_heatmap(matrix, x_axis, y_axis):
	"""
	Plots performance matrix obtained from the "configuration_test" method
	
	@param matrix: Performance data
	@param x_axis: Range used by the problem for the x axis
	@param y_axis: Range used by the problem for the y axis
	"""
	fig, ax = plt.subplots()
	l_x = len(x_axis)
	l_y = len(y_axis)
	for k in range(l_x):
		for l in range(l_y):
			text = ax.text(k, l, int(matrix[l , k]), ha="center", va="center", color="w")

	im = ax.imshow(matrix, cmap=cm.copper_r)
	
	ax.set_title("Performance Matrix  (Mutation Rate vs Population")
	ax.set_yticks(np.arange(l_y))
	ax.set_xticks(np.arange(l_x))
	ax.set_yticklabels(y_axis)
	ax.set_xticklabels(x_axis)
	
	fig.tight_layout()
	plt.show()
	
"""
Main
"""

#Initialize Problem objects
targets = [np.array(list(bin(7548))[2:]).astype(int),
			np.array(list("helloworld")),
			15]
			
P1 = Pb.Bit_Seq(targets[0])
P2 = Pb.Word_Search(targets[1])
P3 = Pb.Unbound_Knapsack(targets[2])

#Generate ranges to be evaluated for each problem

R1 = np.arange(50,300,50), np.arange(0,8)
R2 = np.arange(50,300,50), np.arange(0,8)
R3 = np.arange(50,300,50), np.arange(0,4)

#Run algorithms
print("P1")
solve(P1, (100, 2), R1, fitness_limit)
print("P2")
solve(P2, (100, 1), R2, fitness_limit)
print("P3")
solve(P3, (100, 2), R3, variation_limit)



