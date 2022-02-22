# Perform standard imports

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# Load the MNIST dataset
transforms = transforms.ToTensor()
# Load the training set
train_data = datasets.MNIST(root = '../data', train =True, download = True, transform = transforms)
# Load the test set
train_data = datasets.MNIST(root = '../data', train =False, download = True, transform = transforms)
train_loader =DataLoader(train_data, batch_size=10, shuffle=True)
test_loader =DataLoader(test_data, batch_size=10, shuffle=True)
# Breaking down the convolutional layers for illustration purpose
# input image --> conv1 --> pooling --> conv2
# Define layer1 - 1 color channel, 6 filters (output channels), kernel size 3 and stride 1, no padding.
conv1 = nn.Conv2d(1,6,3,1)
# Define layer2 - 6 channel, 16 filters (output channels) , kernel size 3 and stride 1, no padding.
conv2 = nn.Conv2d(6,16, 3,1)
# Grab the first MNIST record
X_train = train_data[0][0]
y_train = train_data[0][1]
print(X_train.shape)
print(y_train)
x = X_train.view(1,1,28,28)

# Perform the first convolution/activation
x=F.relu(conv1(x))
print(x.shape)
# Run the first pooling layer

# Perform the second convolution/activation

# Run the second pooling layer

# Flatten the data

# Create the actual model class
class CNN1(nn.Module):
    def __init__(self):
        self.conv1= nn.Conv2d(1,6,3,1)
        self.conv2= nn.Conv2d(6,16,3,1)
        self.fc1 = nn.Linear(2*2*16,120)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10)

    def forward(self,X):
        X = F.relu(self.conv1(X))
        X = F.max_pool(X,2,2)
        X = F.relu(self.conv2(X))
        X = F.max_pool2d(X,2,2)
        X = X.view(-1,2*2*16)
        X = F.relu(self.fc1(X))
        X = F.relu(self.fc2(X))
        X = F.log_softmax(self.fc3(X), dim=1)
        return  X
# Initiate our model and print out the parameters
model = CNN1()
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