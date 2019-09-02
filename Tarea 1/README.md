# Wheat Seeds Clasifier

Implementation of a Neural Network classifier for the [seeds dataset](https://archive.ics.uci.edu/ml/datasets/seeds) obtained from the UCI Machine Learning Repository

## Prerequisites
This project requires python 3.7 to execute properly. Libraries used include numpy and matplotlib.

## Analysis
The Dataset analysis is done by executing the file "Processor.py". The dataset contained three types of seeds with 70 instances for each category. After testing different structures it seems that using only one hidden layer is enough to obtain decent results over this dataset, adding more hidden layers causes a more erratic behaviour which can greatly reduce the performance of the network. For the following example I used a Neural Network with 7 inputs, a hidden layer with 12 neurons and an output layer of 3 neurons, training took 500 iterations with a learning rate of 0.01 and using a sigmoid curve for its activation function. In this particular case the Neural Network reached an accuracy of 83%, a MSE of 0.08. Accuracy obtained after 500 iterations varies between 60% to 80%

![""](https://raw.githubusercontent.com/Julioalbornozv/cc5114/master/Tarea%201/Images/tr_acc.png?raw=true)

![""](https://raw.githubusercontent.com/Julioalbornozv/cc5114/master/Tarea%201/Images/tr_mse.png?raw=true)

![""](https://raw.githubusercontent.com/Julioalbornozv/cc5114/master/Tarea%201/Images/confusion.png?raw=true)
