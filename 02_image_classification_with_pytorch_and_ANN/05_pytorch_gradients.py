# Back-propagation on one step
# We'll start by applying a single polynomial function y = f (x) to tensor x.
# Then we'll do backpropagation and print the gradient dy/dx.
# Function:y=2x^4 + x^3 + 3x^2 + 5x + 1
# Derivative:y′=8x^3 + 3x^2 + 6x + 5

import torch

# Create a tensor float 2.0 with requires_grad set to True
x = torch.tensor(2.0, requires_grad=True)
print(x)

# Define a function y=2x^4 + x^3 + 3x^2 + 5x + 1
y = 2*x**4 + x**3 + 3*x**2 + 5*x + 1
print(y)
# Backprop and Display the resulting gradient
y.backward()
print(x.grad)
# that x.grad is an attribute of tensor x, so we don't use parentheses. The computation is the result of
#y′=8(2)^3+3(2)^2+6(2)+5=64+12+12+5=93

# Now let's do something more complex, involving layers y and z between input x and our output layer
# Create a tensor of [[1.,2,3],[3,2,1]]
x = torch.tensor([[1.,2.,3.],[3.,2.,1.]],requires_grad=True)
print(x)
# Create the first layer with y=3x+2
y = 3*x+2
print(y)
# Create the second layer with z = 2y^2
z = 2*y**2
print(z)
# Set the output to be the matrix mean
out = z.mean()
print(out)
# Now perform back-propagation to find the gradient of x w.r.t output
out.backward()
print(x.grad)
# You can reset a tensor's requires_grad attribute in-place using .requires_grad_(True) (or False) as needed.
# When performing evaluations, it's often helpful to wrap a set of operations in with torch.no_grad():