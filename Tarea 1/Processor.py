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
	np.random.shuffle(dataset)
	
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
max = 1000

Neural = ntk.Network(2, [8], 7, 3, fc.Sigmoid(), 0.01)

iter = 1000
while iter != 0:
	iter -= 1
	hits = 0
	rms = 0.0
	for s in range(len(input)):
		Neural.train(input[s], expected[s])
		otp = Neural.layers[-1].cache
		if np.array_equal(otp, expected[s]):
			hits += 1
		rms += np.sum((otp-expected[s])**2)/3.0
	print("\rTraining...\t\t\tEpoch: {}\tAccuracy: {}%\tCost: {}".format(max-iter, int(hits*100/len(input)), rms/len(input)),end="")
	
### Network Test data feed

frms = 0
facc = 0
for t in range(len(test)):
	out = Neural.feed(test[t])
	print("Exp:\t{}\tPred:\t{}\n".format(expected[t+167],out))
	otp = Neural.layers[-1].cache
	if np.array_equal(otp, expected[s]):
		facc += 1
	otp = Neural.layers[-1].cache
	frms += np.sum((otp-expected[s])**2)/3.0
		
print("Test Results:\nAccuracy: {}\t RMS: {}".format(int(facc*100/len(test)), frms/len(test)))
