import Problem as Pb
import Gen_Alg as GA
import Unit as U
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm

import Nodes as N

import pdb
"""
Termination Conditions
"""

def time_limit(board):
	"""
	Terminates process after a number of generations have passed
	"""
	if board.generation > 150:
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
	
	elif top.fitness == 1: # Normalized fitness maxmum
		return True
	else:
		return False

def variation_limit(board):
	"""
	Terminates the process if the best unit fitness remain the same for a fixed number of generations
	"""
	if board.generation-board.best_time > 50:
		return True
	
	return False
	
"""
Problem Analysis
"""

def solve(Problem, fit_pair, range, term_func, func_set, val_set, heatmap=False):
	"""
	Solves a problem using a genetic algorithm, returns a fitness plot and a performance heatmap.

	@param Problem: Object representing a problem
	@param fit_pair: Tuple containing the population and mutation rate used for the fitness analysis
	@param range: Tuple containing the population and mutation ranges to be analysed
	@param term_func: Termination function to be used
	
	"""
	
	gen = GA.Board(Problem.fitness_function, Problem.gene_generator, Problem.individual_generator, fit_pair[0], fit_pair[1], term_func, func_set, val_set)

	gen.run()
	print("Result found:\t{}\tF:\t{}".format(gen.best.dna, gen.best.fitness))
	plot_results(gen.fit_record)	

	#Performance analysis
	if heatmap:
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
targets = [65346,
			N.AddNode(N.MultNode(N.TerminalNode('x'),N.TerminalNode('x')),N.AddNode(N.TerminalNode('x'),N.TerminalNode(6)))
			]
			
P1_a = Pb.Find_Number(targets[0], repetition = True, prune = False)	# Multiple Repetitions
P1_b = Pb.Find_Number(targets[0], repetition = True, prune = True)	#Anti-growth fitness
P1_c = Pb.Find_Number(targets[0], repetition = False, prune = True)	# No Repetitions

P2 = Pb.Variable_Terminals(targets[0], env = {"x": 12, "y": 5, "z": 18})
P3 = Pb.Symbolic_Regression(targets[1], env = {})

#Generate ranges to be evaluated for each problem

R = np.arange(50,300,50), np.arange(0,8)

#Define sets to be used

S1_ab = ([N.AddNode, N.SubNode, N.MultNode, N.MaxNode], [25, 7, 8, 100, 4, 2])
S1_c = ([N.AddNode, N.SubNode, N.MultNode], [25, 7, 8, 100, 4, 2])
S2 = ([N.AddNode, N.SubNode, N.MultNode], [25, 7, "x", 100, "y", "z"])

temp = list(range(-10,11))
for _ in range(20):
	temp.append("x")
S3 = ([N.AddNode, N.SubNode, N.MultNode], temp)
S4 = ([N.AddNode, N.SubNode, N.MultNode, N.DivNode], temp)

#Run algorithms
print("P1\na)")
solve(P1_a, (100, 2), R, fitness_limit, S1_ab[0], S1_ab[1])
print("b)")
solve(P1_b, (100, 2), R, fitness_limit, S1_ab[0], S1_ab[1])
print("c)")
solve(P1_c, (100, 2), R, variation_limit, S1_c[0], S1_c[1])

print("P2")
solve(P2, (100, 2), R, variation_limit, S2[0], S2[1])

print("P3")
for x in range(0,10):
	print("x = {}".format(x))
	P3.env = {'x': x}
	solve(P3, (100, 2), R, fitness_limit, S3[0], S3[1])

print("P4")
for x in range(0,10):
	print("x = {}".format(x))
	P3.env = {'x': x}
	solve(P3, (100, 2), R, fitness_limit, S4[0], S4[1])
