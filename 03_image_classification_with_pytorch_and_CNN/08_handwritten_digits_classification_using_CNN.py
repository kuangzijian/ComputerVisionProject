# Perform standard imports

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# Load the MNIST dataset
# Load the training set

# Load the test set

# Breaking down the convolutional layers for illustration purpose
# Define layer1 - 1 color channel, 6 filters (output channels), kernel size 3 and stride 1, no padding.

# Define layer2 - 6 channel, 16 filters (output channels) , kernel size 3 and stride 1, no padding.

# Grab the first MNIST record

# Perform the first convolution/activation

# Run the first pooling layer

# Perform the second convolution/activation

# Run the second pooling layer

# Flatten the data

# Create the actual model class

# Initiate our model and print out the parameters

# Define loss function & optimizer

# Train the model
import time
start_time = time.time()
epochs = 3

for i in range(epochs):
    trn_corr = 0
    tst_corr = 0

    # Run the training batches

    # Run the testing batches

# Evaluate the model