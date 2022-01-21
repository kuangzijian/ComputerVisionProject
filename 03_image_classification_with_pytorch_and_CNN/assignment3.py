import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import make_grid
import numpy as np
import matplotlib.pyplot as plt

transform = transforms.ToTensor()

train_data = datasets.FashionMNIST(root='../data', train=True, download=True, transform=transform)
test_data = datasets.FashionMNIST(root='../data', train=False, download=True, transform=transform)
class_names = ['T-shirt','Trouser','Sweater','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Boot']

# Create data loaders


# Examine a batch of images
# Use DataLoader, make_grid and matplotlib to display the first batch of 10 images.
# display the labels as well


# Downsampling
# If a 28x28 image is passed through a Convolutional layer using a 5x5 filter, a step size of 1, and no padding,
# create the conv layer and pass in one data sample as input, then printout the resulting matrix size


# If the sample from question 3 is then passed through a 2x2 MaxPooling layer
# create the pooling layer and pass in one data sample as input, then printout the resulting matrix size



# Define a convolutional neural network
# Define a CNN model that can be trained on the Fashion-MNIST dataset.
# The model should contain two convolutional layers, two pooling layers, and two fully connected layers.
# You can use any number of neurons per layer so long as the model takes in a 28x28 image and returns an output of 10.
# and then printout the count of parameters of your model



# Define loss function & optimizer
# Define a loss function called "criterion" and an optimizer called "optimizer".
# You can use any loss functions and optimizer you want,
# although we used Cross Entropy Loss and Adam (learning rate of 0.001) respectively.



# Train and test the model
# try with any epochs you want
# and printout some interim results


# Remember, always experiment with different architecture and different hyper-parameters, such as
# different activation function, different loss function, different optimizer with different learning rate
# different size of convolutional kernels, and different combination of convolutional layers/pooling layers/FC layers
# to make the best combination for solving your problem in real world

