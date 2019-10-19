# Genetic Algorithm

Python implementation of a genetic implementation for Assignement N°2

## Prerequisites
This project requires python 3.7 to execute properly. Libraries used include numpy , matplotlib and abc.

## Analysis
Each problem was modeled as a subclass of the Problem class, which includes all problem-dependant methods. The file Test.py will use the genetic algorithm modeled in the Board class to solve each problem. The Unbound Knapsack problem was selected to be resolved in this assignement.

For the exercises the cromosomes of each individual contain the charcter of the string, on the other hand the Knapsack problem uses 5 genes to represent the 5 available boxes, each gene contain the number of boxes of a certain type are present.

Shown below are the results for the second exercise using the string "helloworld". The performance for all excercises is measured by the number of generations the program took to find the problem's solution. In the case of the graph shown below we can see that the best configuration uses 100 individuals while mutating 7 characters after crossover while the worst performer uses 250 individuals while mutating only 4 characters (Results may vary).

![""](https://raw.githubusercontent.com/Julioalbornozv/cc5114/master/Tarea%202/Figures/P2_fit.png?raw=true)
![""](https://raw.githubusercontent.com/Julioalbornozv/cc5114/master/Tarea%202/Figures/P2_perf.png?raw=true)
