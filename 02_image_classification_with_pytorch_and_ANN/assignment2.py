# Import torch and NumPy
import torch
import torch.nn as nn
import numpy as np

# Set the random seed for NumPy and PyTorch both to "42"
#   This allows us to share the same "random" results.
torch.manual_seed(42)
np.random.seed(42)
# Create a NumPy array called "arr" that contains 6 random integers between 0 (inclusive) and 5 (exclusive)
arr = np.random.randint(0,5, 6)
print(arr)
# Create a tensor "x" from the array above
x = torch.tensor(arr)
print(x)
# Change the dtype of x from 'int32' to 'int64'
x = torch.tensor(arr, dtype=torch.int64)
print(x)
print(x.shape)
# Reshape x into a 3x2 tensor
print(x.reshape(3,2))
x = x.reshape(3,2)
# Return the left-hand column of tensor x
print(x[:,1])

# Without changing x, return a tensor of square values of x
print(torch.mm(x,x.reshape(2,3)))

# Create a tensor "y" with the same number of elements as x, that can be matrix-multiplied with x
arr_y = np.random.randint(0,5, 6)
y = torch.tensor(arr_y, dtype= torch.int64)
y= y.reshape(2,3)
# Find the matrix product of x and y
print(torch.mm(x,y))

# Create a Simple linear model using torch.nn
# the model will take 1000 input and output 20 multi-class classification results.
# the model will have 3 hidden layers which include 200, 120, 60 respectively.
class Model(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features)

        def forward(self,x):
            x_pred = self.Linear(x)
# initiate the model and printout the number of parameters
model_felix = Model(1000, 20)
print(model_felix)
print(model_felix.linear.weight)
print(model_felix.linear.bias)