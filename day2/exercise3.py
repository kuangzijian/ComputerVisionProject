#This section covers:
# Converting NumPy arrays to PyTorch tensors
# Creating tensors from scratch

# import libs torch, numpy


print('converting NumPy arrays to PyTorch tensors')
# A torch.Tensor is a multi-dimensional matrix containing elements of a single data type.
# Calculations between tensors can only happen if the tensors share the same dtype.

print('lets simply create a numpy array with value 1,2,3,4,5')


print('now lets create a 4x3 2D array (matrix)')


print('lets convert this 2D array into a torch tensor')


print('lets create a tensor from scratch')
#   Uninitialized tensors with .empty()


#   Initialized tensors with .zeros() and .ones()


print('Tensors from ranges')


print('Tensors from data')


print('Random number tensors that follow the input size')


print('Set random seed which allows us to share the same "random" results.')


print('Tensor attributes')

# PyTorch supports use of multiple devices, harnessing the power of one or more GPUs in addition to the CPU.
# We won't explore that here, but you should know that operations between tensors can only happen for tensors installed on the same device.