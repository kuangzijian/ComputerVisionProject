# Perform standard imports
import torch
import torch.nn as nn  # we'll use this a lot going forward!

import numpy as np
import matplotlib.pyplot as plt

# Create a column matrix of X values


# Create a "random" array of error values
# 50 random integer values that collectively cancel each other out.


# Create a column matrix of y values
# Here we'll set our own parameters of weight = 2 , bias = 1 , plus the error amount.
# y will have the same shape as X and e


# Plot the results


# Create a Simple linear model using torch.nn


# Lets create our first model class that has single linear layer.


# When Model is instantiated, we need to pass in the size (dimensions) of the incoming and outgoing features. For our purposes we'll use (1,1).
# As above, we can see the initial hyperparameters.


# Now let's see the result when we pass a tensor [2.0] into the model.


# Plot the initial model, We can plot the untrained model against our dataset to get an idea of our starting point.


# Set the loss function


# Train our model.
# An epoch is a single pass through the entire dataset.
# We want to pick a sufficiently large number of epochs to reach a plateau close to
# our known parameters of weight = 2 , bias = 1


# Plot the result