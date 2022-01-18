# Before we start working with Convolutional Neural Networks (CNN), let's model the MNIST dataset using only linear layers.
# In this project we'll reshape the MNIST data from a 28x28 image to a flattened 1x784 vector to mimic a single row of 784 features.

# Perform standard imports


# Load the MNIST dataset
# Load the training set


# Load the test set


# Examine a training record


# Batch loading with DataLoader


# Define the ANN model


# Check our model and Count the model parameters


# Define loss function & optimizer


# How to Flatten the training data? [1,28,28] --> [784]


# Train the model
# First thing that I want to do is I'm going to import time.


# let's define some variables for tracking purpose and for visualization the result later on


# Run the training batches


# Apply the model


# Tally the number of correct predictions


# Update parameters


# Print interim results


# Update train loss & accuracy for the epoch


# Run the testing batches


# Update test loss & accuracy for the epoch