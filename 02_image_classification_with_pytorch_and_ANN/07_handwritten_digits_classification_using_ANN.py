# Before we start working with Convolutional Neural Networks (CNN), let's model the MNIST dataset using only linear layers.
# In this project we'll reshape the MNIST data from a 28x28 image to a flattened 1x784 vector to mimic a single row of 784 features.

# Perform standard imports
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F          # adds some efficiency
from torch.utils.data import DataLoader  # lets us load data in batches
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# Load the MNIST dataset
# Load the training set
transform = transforms.ToTensor()

# Load the test set
train_data = datasets.MNIST(root='./data',train=True,download=True, transform= transform)
test_data = datasets.MNIST(root='./data',train=False,download=True, transform= transform)
# Examine a training record
print(train_data)
print(test_data)
print(train_data[0])
image, label = train_data[0]
print('Shape:', image.shape, '\nLabel:', label)
plt.imshow(train_data[0][0].reshape((28,28)))
plt.show()
train_loader = DataLoader(train_data, batch_size=100, shuffle=True)
test_loader = DataLoader(test_data,patch_size = 500, shuffle=False)

# Define the ANN model, most important part
class MultiLayerPcercepton(nn.Module):
    def __init__(self, in_sz = 784, out_sz = 10, layers=[120,84]):
        super.__init__()
        self.fc1 = nn.linear(in_sz, layers[0]) #fully connected layer 1
        self.fc2 = nn.linear(layers[0], layers[1])
        self.fc2 = nn.linear(layers[1],out_sz)

    def forward(self,X):
        X = F.relu(self.fc1(X))
        X = F.relu(self.fc2(X))
        X = F.log_softmax(self.fc3(X), dim=1)
        return X
# Check our model and Count the model parameters
model=MultiLayerPcercepton()
print(model)
for param in model.parameters():
    print(param.numel())

# Define loss function & optimizer
cost  = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr= 0.001)


# How to Flatten the training data? [1,28,28] --> [784]
for images, labels in train_loader:
    print(images.shape)
    break
print(images.view(100, -1).shape)
# Train the model
# First thing that I want to do is I'm going to import time.
epochs = 3
import time
start_time = time.time()
for i in range(epochs):
    train_corr = 0
    test_corr = 0

    for b,(X, y) in enumerate(train_loader):
        y_pred = model(X.view(100,-1))
        loss = cost(y_pred, y)
        predicted = torch.max(y_pred.data,1)[1]
        batch_corr = (predicted == y).sum
        train_corr + batch_corr
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # Print interim results
        if b%200 == 0:
            print(f'epoch:{i} batch{b} loss:{loss.item()} accuracy:{train_corritem()*100/(100+b)}%')
# let's define some variables for tracking purpose and for visualization the result later on


# Run the training batches


# Apply the model


# Tally the number of correct predictions


# Update parameters





# Update train loss & accuracy for the epoch


# Run the testing batches
    with torch.no_grad():
        for b, (X, y) in enumerate(test_loader):
            y_val = model|(X.view(500,-1))
            predicted = torch.max(y_val.data,1)[1]
            test_corr += (predicted == y).sum()


# Update test loss & accuracy for the epoch
    print(f'Test accuraccy:{test_corr.item()*100/(len(test_data))}')
print(f'\nDuration:{time.time()-start_time: .0f} seconds')

x = 2019
plt.figure(figsize=(1,1))
plt.imshow(test_data[x][0].reshape((28,28)))
plt.show()

model.eval()
with torch.no_grad():
    new_pred = model(test_data[x][0].view(1,-1)).argmax()
print(new_pred.item(0))