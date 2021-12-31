#This section covers:
# Indexing and slicing
# Reshaping tensors (tensor views)
# Tensor basic operations
# Dot products
# Matrix multiplication
# Additional, more advanced operations

import torch
import numpy as np

print('Indexing and slicing')
x = torch.arange(6).reshape(3,2)
print(x)

print('Grabbing the right hand column values')


print('Grabbing the right hand column as a (3,1) slice')


# view() and reshape() do essentially the same thing by returning a reshaped tensor
# without changing the original tensor in place.


print('Views can infer the correct size')


print('Tensor basic operations')


print('Changing a tensor in-place')


print('Dot products')


print('Matrix multiplication')


print('L2 or Euclidean Norm')
# The L2 norm calculates the distance of the vector coordinate from the origin of the vector space.
# As such, it is also known as the Euclidean norm as it is calculated as the Euclidean distance from the origin.
# The result is a positive distance value.



