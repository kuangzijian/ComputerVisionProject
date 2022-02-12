#This section covers:
# Indexing and slicing
# Reshaping tensors (tensor views)
# Tensor basic operations
# Dot products
# Matrix multiplication
# Additional, more advanced operations

import torch
print('Indexing and slicing')
x = torch.arange(6).reshape(3,2)
print(x)

print('Grabbing the right hand column values')
print(x[:,1])

print('Grabbing the right hand column as a (3,1) slice')
print(x[:,1].reshape(3,1))
print(x[:,1].view(3,1))
# view() and reshape() do essentially the same thing by returning a reshaped tensor
# without changing the original tensor in place.
x1 = torch.arange(9).reshape(3,3)
print(x1)
print(x1.shape)
print(x.view(-1,6))

print('Views can infer the correct size')


print('Tensor basic operations')
a = torch.tensor([1,2,3], dtype=torch.float) #ctrl+c
b = torch.tensor([4,5,6], dtype=torch.float)
a+b
print('Changing a tensor in-place')
a.add_(b)
print(a)
print('Dot products')
a = torch.tensor([1,2,3], dtype=torch.float) #ctrl+c
b = torch.tensor([4,5,6], dtype=torch.float)
print(a.dot(b))

print('Matrix multiplication')
a = torch.tensor([[0,2,4],[1,3,5]])
b = torch.tensor([[6,7],[8,9],[10,11]])
print(a.size())
print(b.size())
print(torch.mm(a,b))
print(a.mm(b))
print('L2 or Euclidean Norm')
# The L2 norm calculates the distance of the vector coordinate from the origin of the vector space.
# As such, it is also known as the Euclidean norm as it is calculated as the Euclidean distance from the origin.
# The result is a positive distance value.
x = torch.tensor([2.,5.,8.,14.])#as float dtype, default is float
print(x.norm())


