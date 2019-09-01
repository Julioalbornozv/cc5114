import Network as ntk
import Perceptron as pc
import Functions as fc
import numpy as np
import matplotlib.pyplot as plt
import pdb

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
LA = np.array([1,0,0])
LB = np.array([0,1,0])
LC = np.array([0,0,1])

for j in range(len(dataset[:-1])):
	if dataset[j,-1] == 1:
		expected.append(LA)
	elif dataset[j,-1] == 2:
		expected.append(LB)
	else:
		expected.append(LC)
		
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
pl_acc = []
pl_rms = []
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
	pl_acc.append(int(hits*100/len(input)))
	pl_rms.append(rms/len(input))
	
### Network Test data feed

confusion = np.zeros((3,3))
garbage = 0

frms = 0
facc = 0
for t in range(len(test)):
	out = Neural.feed(test[t])
	print("Exp:\t{}\tPred:\t{}\n".format(expected[t+167],out))
	
	#Succeds
	if np.array_equal(out, expected[t+167]):
		#pdb.set_trace()
		facc += 1
		if np.array_equal(out, LA):
			confusion[0][0] += 1
		elif np.array_equal(out, LB):
			confusion[1][1] += 1
		else:
			confusion[2][2] += 1
	#Fails an A
	elif np.array_equal(expected[t+167], LA):
		if np.array_equal(out, LB):
			confusion[1][0] += 1
		elif np.array_equal(out, LC):
			confusion[2][0] += 1
		else:
			garbage += 1
	#Fails a B
	elif np.array_equal(expected[t+167], LB):
		if np.array_equal(out, LA):
			confusion[0][1] += 1
		elif np.array_equal(out, LC):
			confusion[2][1] += 1
		else:
			garbage += 1
	#Fails a C
	elif np.array_equal(expected[t+167], LC):
		if np.array_equal(otp, LB):
			confusion[0][2] += 1
		elif np.array_equal(out, LC):
			confusion[1][2] += 1
		else:
			garbage += 1
	
	otp = Neural.layers[-1].cache
	frms += np.sum((otp-expected[t+167])**2)/3.0
		
print("Test Results:\nAccuracy: {}%\t RMS: {}\t Failed predictions: {}".format(int(facc*100/len(test)), frms/len(test), garbage))

### Plots
#Confusion matrix
fig, ax = plt.subplots()
im = ax.imshow(confusion)
for i in range(3):
	for j in range(3):
		text = ax.text(j, i, confusion[i, j], ha="center", va="center", color="w")

ax.set_title("")

fig.tight_layout()
plt.show()

#Accuracy
plt.plot(pl_acc)
plt.ylabel("Accuracy '%'")
plt.show()

#RMS
plt.plot(pl_rms)
plt.ylabel("RMS")
plt.show()

