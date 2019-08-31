import Network as ntk
import Perceptron as pc
import numpy as np
import Functions as fc

"""
TODO: (Post-release)
	+ Replace lists with numpy arrays
	+ Generalize for multiple datasets
	+ Modularize code and generalize inputs
"""

### Parse data
dataset = []
path = "seeds_dataset.txt"
with open(path, 'r') as data:
	for line in data:
		dataset.append(np.asarray(list(map(float, (line.strip("\n")).split("\t")))))
	
dataset = np.asarray(dataset)

### Normalize data 

for i in range(len(dataset[0])-1):
	dataset[:,i] = (dataset[:,i] - np.amin(dataset[:,i]))/(np.amax(dataset[:,i])-np.amin(dataset[:,i]))
	
### One-hot encoding
expected = []
for j in range(len(dataset[:-1])):
	if dataset[j,-1] == 1:
		expected.append(np.array([1,0,0]))
	elif dataset[j,-1] == 2:
		expected.append(np.array([0,1,0]))
	else:
		expected.append(np.array([0,0,1]))
		
expected = np.asarray(expected)

### Input prep
# 80% for training, 20% for test

input, test = [], []
split = len(dataset)*4/5

for r in range(len(dataset)):
	if r < split:
		input.append(dataset[r][0:7].copy())
	else:
		test.append(dataset[r][0:7].copy())
	
	
input = np.asarray(input)
test = np.asarray(test)

### Network Training

iter = 1000
Neural = ntk.Network(5, [4, 3, 5, 2], 7, 3, fc.Sigmoid(), 0.1)

while iter != 0:
	iter -= 1
	for s in range(len(input)):
		Neural.train(input[s], expected[s])
	print("\rTraining...\t\t\tE:{} I:{}".format(1000-iter),end="")
	
### Network Test data feed
	
for t in range(len(test)):
	out = Neural.feed(test[t])
	print("Exp:\t{}\tPred:\t{}\n".format(expected[t+167],out))


