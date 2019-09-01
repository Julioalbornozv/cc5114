import Network as ntk
import Perceptron as pc
import Functions as fc
import numpy as np
import matplotlib.pyplot as plt


def parse(path):
	"""
	Extracts data from a tab-separated txt file
	
	path: File to be opened
	@return: numpy matrix containing the data
	"""
	dataset = []
	with open(path, 'r') as data:
		for line in data:
			dataset.append(np.asarray(list(map(float, (line.strip("\n")).split("\t")))))
	
	dataset = np.asarray(dataset)
	return dataset
	

def prepare_data(dataset):
	"""
	Normalizes, splits and applies One-hot encoding to the dataset
	
	dataset: np.array containing the data
	@returns Training and Test sets, each containing the input and the expected output of each row
	@returns Labels obtained from the one-hot encoding process
	"""
	### Normalize data 
	
	height, width = dataset.shape
	for i in range(width-1):
		column = dataset[:,i]
		dataset[:,i] = (column - np.amin(column))/(np.amax(column)-np.amin(column))
	
	np.random.shuffle(dataset)
		
	### One-hot encoding
	expected = np.zeros((height,3))
	Lab = np.eye(3)
	tag = dataset[:,-1] - 1
	for j in range(height):
		expected[j] = Lab[int(tag[j])]
	
	### Splits data
	# 80% for training, 20% for test
	
	input, test = [], []
	split = height*4/5
	
	for r in range(height):
		if r < split:
			input.append((dataset[r][0:7].copy(), expected[r]))
		else:
			test.append((dataset[r][0:7].copy(), expected[r]))
		
		
	input = np.asarray(input)
	test = np.asarray(test)
	return input, test, Lab

def train_NN(Neural, iter, input):
	"""
	Trains a neural network with its input set, returns training metrics
	
	Neural: Neural network to be trained
	iter: Number of epochs for the training
	input: Data being fed to the NN
	
	@return: acc: Accuracy over time
	@return: rms: RMS over time
	"""
	### Network Training
	max = iter
	size = len(input)
	
	acc, rms = [], []
	while iter != 0:
		iter -= 1
		hits, err = 0.0, 0.0
		for s in range(size):
			Neural.train(input[s][0], input[s][1])
			out = Neural.layers[-1].cache
			if np.array_equal(out, input[s][1]):
				hits += 1
			
			err += np.sum((out-input[s][1])**2)/3.0
		print("\rTraining...\t\t\tEpoch: {}\tAccuracy: {}%\tCost: {}".format(max-iter, int(hits*100/size), err/size),end="")
		acc.append(int(hits*100/size))
		rms.append(err/size)
	
	return acc, rms
	
def test_NN(Neural, test, Lab):
	"""
	Evaluates the network performance using the test set given
	
	Neural: Neural Network to be tested
	test: Test set used in the evaluation
	Lab: Labels obtained from the one-hot encoding process
	
	@return Confusion matrix
	"""
	print("\nTesting...")
	conf = np.zeros((3,3))
	
	rms, acc, garbage = 0, 0, 0
	size = len(test)
	for t in range(size):
		out = Neural.feed(test[t][0])
		exp = test[t][1]
		
		if np.sum(out) == 1:
			conf[np.nonzero(out)[0][0], np.nonzero(exp)[0][0]] += 1

		rms += np.sum((out-exp)**2)/3.0
			
	acc = conf[0][0]+conf[1][1]+conf[2][2]
	print("\n\n>> Test Results:\nAccuracy: {}%\t RMS: {}\t Undefined output: {}".format(int(acc*100/size), rms/size, int(size-np.sum(conf))))
	return conf
	
def plot_results(Acc, RMS, confusion):
	"""
	Plots the confusion matrix obtained after a test, and the accuracy/rms from the training period
	
	Acc: Porcentual accuracy during training 
	RMS: Error of the network during training
	confusion: 3x3 matrix with the test results
	"""
	#Confusion matrix
	fig, ax = plt.subplots()
	im = ax.imshow(confusion)
	for i in range(3):
		for j in range(3):
			text = ax.text(j, i, int(confusion[i, j]), ha="center", va="center", color="w")
	
	ax.set_title("")
	
	fig.tight_layout()
	plt.show()
	
	#Accuracy
	plt.plot(Acc)
	plt.ylabel("Accuracy '%'")
	plt.show()
	
	#RMS
	plt.plot(RMS)
	plt.ylabel("RMS")
	plt.show()


dataset = parse("seeds_dataset.txt")							#Data extraction
input, test, Lab = prepare_data(dataset)						#Data curation

Neural = ntk.Network(2, [12], 7, 3, fc.Sigmoid(), 0.01)		#NN Structure 7-12-3 
acc, rms = train_NN(Neural, 500, input)						#NN Training

confusion = test_NN(Neural, test, Lab)							#NN Testing
plot_results(acc, rms, confusion)								#Results
