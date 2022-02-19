# Perform standard imports
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import make_grid
import numpy as np
import matplotlib.pyplot as plt
# ignore harmless warnings
import warnings
warnings.filterwarnings("ignore")

# Define transforms for training and testing dataset

# Load in our train and test set using dataloader objects

# Display a batch of images

# Define the model

# Instantiate the model, define loss and optimization functions

# Looking at the trainable parameters

# Train and test the model

# Save the trained model (so you can continue to train with more epochs later on,
# or you can grab those weight to perform evaluation on new images anytime you want)

# Evaluation using one test example
