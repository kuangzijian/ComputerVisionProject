# Perform standard imports
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
from IPython.display import display
# Filter harmless warnings
import warnings
warnings.filterwarnings("ignore")

# Run this cell. If you see a picture of a cat you're all set!
with Image.open('../data/CATS_DOGS/test/CAT/10107.jpg') as im:
    im.show()

# Create a list of image filenames

# Transformations (data augmentation)

# Resize

# CenterCrop

# Random Flip

# Random Rotate

# Put all transformations together
