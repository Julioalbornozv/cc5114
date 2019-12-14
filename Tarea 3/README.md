# Genetic Programming

Python implementation of a genetic programming algoritm for Assignement N°3

## Prerequisites
This project requires python 3.7 to execute properly. Libraries used include numpy , matplotlib and abc.

## Analysis
The problems for this assignement were modeled by using a modified version of the Problem class from the previous Assignement, similarly the genetic algorithm was extended to support individuals which encode their DNA through a tree. The trees are represented using the code from AST.py seen in class.

### Exercise 1: Finding a number
For the first problem, the program is able to find a tree with the exact result, as a downside the trees used in the simulation can grow dramatically on each generation, resulting in slow performance and in trees with high depth .

![""](https://raw.githubusercontent.com/Julioalbornozv/cc5114/master/Tarea%202/Figures/P2_fit.png?raw=true)

For the next section of this problem we added a growth constraint which punished trees which grew too much, the performance of the genetic algorithm increased significantly but it came with a cost in the result acuraccy, requiring more generations to reach a result closer to the expected outcome.

![""](https://raw.githubusercontent.com/Julioalbornozv/cc5114/master/Tarea%202/Figures/P2_fit.png?raw=true)

Finally a uniqueness restriction was partially implemented, while trees with repetitions resulted in lower fitness scores, this implementation wasn't able to ensure the uniquenss of the terminals.

![""](https://raw.githubusercontent.com/Julioalbornozv/cc5114/master/Tarea%202/Figures/P2_fit.png?raw=true)

### Excercise 2: Variable implementation
Terminals with variable values where implemented by first including a dictionary with each variable value during the Problem initialization, then the tree value was calculated using an extended version of the eval method from the Node class, which would translate a terminal using the included dictionary.

![""](https://raw.githubusercontent.com/Julioalbornozv/cc5114/master/Tarea%202/Figures/P2_fit.png?raw=true)

### Excercise 3: Symbolic Regression
For this poblem, the target function was given to the Problem object in its tree representation, this AST would then be evaluated and compared with the genetic algorithm individual values to calculate their fitness. The test will solve the problem multiple times, changing the value of the x variable on each iteration.
Results will vary depending on th evalue of x

![""](https://raw.githubusercontent.com/Julioalbornozv/cc5114/master/Tarea%202/Figures/P2_fit.png?raw=true)

### Excercise 4: Division Nodes
The division node was implemented in a similar way to the other nodes, during the fitness calculation process, the Problem object will use a try-catch block to catch any DivisionByZero Error, giving a fitness of 0.0 to that individual

![""](https://raw.githubusercontent.com/Julioalbornozv/cc5114/master/Tarea%202/Figures/P2_perf.png?raw=true)
