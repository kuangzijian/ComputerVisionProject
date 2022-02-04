# Perform standard imports
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models # add torchvision models to use pretrained AlexNet model
import numpy as np
import matplotlib.pyplot as plt
# ignore harmless warnings
import warnings
warnings.filterwarnings("ignore")

# Define transforms for training and testing dataset
train_transform = transforms.Compose([
        transforms.RandomRotation(10),
        transforms.RandomHorizontalFlip(),
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor()
        # add normalization here
    ])

test_transform = transforms.Compose([
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor()
        # add normalization here
    ])

# Load in our train and test set using these data loader objects.
train_data = datasets.ImageFolder('../data/CATS_DOGS/train', transform=train_transform)
test_data = datasets.ImageFolder('../data/CATS_DOGS/test', transform=test_transform)

train_loader = DataLoader(train_data, batch_size=10, shuffle=True)
test_loader = DataLoader(test_data, batch_size=10)
class_names = train_data.classes

# Setup a pretrained model

# Freeze feature parameters

# Modify the classifier

# Define loss function & optimizer

# Train the modified classifiers on a pretrained AlexNet

# Evaluation using one test example
