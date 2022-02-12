#This section covers:
# Converting NumPy arrays to PyTorch tensors
# Creating tensors from scratch

# import libs torch, numpy
import torch
import numpy as np

print('converting NumPy arrays to PyTorch tensors')
# A torch.Tensor is a multi-dimensional matrix containing elements of a single data type.
# Calculations between tensors can only happen if the tensors share the same dtype.

print('lets simply create a numpy array with value 1,2,3,4,5')
arr = np.array([1,2,3,4,5])
print(arr)
print(arr.dtype)
print(type(arr))

print('now lets create a 4x3 2D array (matrix)')
x = torch.tensor(arr)
print(x)
print(x.dtype)
print(type(x))
arr2 = np.arange(0,12).reshape(4,3)
print(arr2)
print('lets convert this 2D array into a torch tensor')
x2 = torch.tensor(arr2)
print(x2)
print(x2.type())

print('lets create a tensor from scratch')
#   Uninitialized tensors with .empty()
x = torch.empty(4,3)
print(x)
print(x.type())
#   Initialized tensors with .zeros() and .ones()
x = torch.zeros(4,3,dtype = torch.int32)
print(x)
x1 = torch.ones(4,3)
print(x1)
print('Tensors from ranges')
x = torch.arange(0,9).reshape(3,3)
print(x)
print('Tensors from data')
x = torch.tensor([1,2,3,4,5])
print(x)
print('Random number tensors that follow the input size')
x48 = torch.randint(0,10,[4,3])
print(x48)
x50 = torch.randn(4,3)
print(x50)
print('Set random seed which allows us to share the same "random" results.')
np.random.seed(1)
torch.manual_seed(1)
print(np.random.randint(0,5,4))
print(torch.randint(0,5,[2,2]))
print('Tensor attributes')
print(x.shape)
print(x.size())
print(x.device)
# PyTorch supports use of multiple devices, harnessing the power of one or more GPUs in addition to the CPU.
# We won't explore that here, but you should know that operations between tensors can only happen for tensors installed on the same device.