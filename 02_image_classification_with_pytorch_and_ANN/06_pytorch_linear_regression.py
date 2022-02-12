# Perform standard imports
import torch
import torch.nn as nn  # we'll use this a lot going forward!\
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Create a column matrix of X values
X = torch.arange(1.0,51.0).reshape(-1,1)
print(X)
# Create a "random" array of error values
# 50 random integer values that collectively cancel each other out.
torch.manual_seed(71)
e = torch.randint(-8,9,(50,1),dtype=torch.float)
print(e)
print(e.sum())
# Create a column matrix of y values
# Here we'll set our own parameters of weight = 2 , bias = 1 , plus the error amount.
# y will have the same shape as X and e
y = 2*X + 1 + e
print(y)
print(y.shape)
# Plot the results
plt.scatter(X.numpy(),y.numpy())
plt.ylabel('y')
plt.xlabel('x')
plt.show()

# Create a Simple linear model using torch.nn
torch.manual_seed(59)
model= nn.linear(in_features=1, out_features = 1)
print(model.weight)
print(model.bias)

# Lets create our first model class that has single linear layer.
class Model(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.linear = nn.linear(in_features, out_features) #attribute of our model

        def forward(self,x):
            y_pred = self.linear()

# When Model is instantiated, we need to pass in the size (dimensions) of the incoming and outgoing features. For our purposes we'll use (1,1).
# As above, we can see the initial hyperparameters.
model = Model(1,1)
print(model)
print(model.linear.weight)
print(model.linear.bias)

x = torch.tensor([2,0])
print(model.forward(x))
# Now let's see the result when we pass a tensor [2.0] into the model.
x1 = np.array([X.min(),X.max()])
print(x1)
# Plot the initial model, We can plot the untrained model against our dataset to get an idea of our starting point.
w1, b1 = model.linear.weight.item(), model.linear.bias.item()
y1 = x1*w1 + b1
print(y1)
# Set the loss function
plt.scatter(X.numpy(), y.numpy())
plt.plot(x1,y1, 'r')
plt.show()


# Train our model.
# An epoch is a single pass through the entire dataset.
# We want to pick a sufficiently large number of epochs to reach a plateau close to
# our known parameters of weight = 2 , bias = 1
cost = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001) #schoatistic
opochs = 50
losses = []
for i in range(epochs):
    i+=1
    y_pred = model.forward(x)

    loss = cost(y_pred, y)
    losses.append(loss)
    print(f'epoch: {i:2} loss:{loss.item():10.8f} weight:{model.linear.weight.item():10:8f}'
          f'bias:{model.linear.bias.item():10.9f}')
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Plot the result
w1, b1 = model.linear.weight.item(), model.linear.bias.item()
print(w1, b1)
y1 = x1*w1+b1
plt.scatter(X.numpy(),y.numpy())
plt.plot(x1, y1,'r')
plt.show()
