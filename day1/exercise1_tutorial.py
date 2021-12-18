#todo: import numpy
import numpy as np

#todo: creating list [0,1,2,3,4] in python and print the type of your list
my_list = [0,1,2,3,4]
print(type(my_list))

#todo: cast your list into a numpy arrary and print the type of your array
my_arr = np.array(my_list)
print(type(my_arr))

#todo: create a 3x3 array filled with zeros
a = np.zeros((3,3))
print('a', a)

#todo: create a 2x4 array filled with ones
b = np.ones((2,4))
print('b', b)

#todo: create a 3x4 array filled with ones
c = np.ones((3,4)) * 10
print('c', c)

#todo: create a 3x2 array filld with random numbers
arr = np.random.rand(3,2)
print('array', arr)

#todo: create a 3x2 arrary filled with random integers
arr = np.random.randint(low=0, high=100, size=(3,2) )
print('int array', arr)

#todo: print the maximum number in your matrix
print('max', arr.max())

#todo: print the minimum number in your matrix
print('min', arr.min())

#todo: print the mean value in your matrix
print('mean', arr.mean())

#todo: reshape your array into a 2x3 matrix
print('reshape', arr.reshape(2,3))

#todo: create an 9 elements array [1,2,3,4,5,6,7,8,9]
# Values are generated within the half-open interval [start, stop) (in other words, the interval including start but excluding stop)
arr = np.arange(1,10)
print('mat', arr)

#todo: reshape your array into a 3x3 matrix
mat = arr.reshape(3,3)
print('mat', mat)

# row and column variables
row = 0
col = 1

#todo: retrieve the element on first row, second column
print('retrieve first row, second column element', mat[row,col])

#todo: retrieve all the elements on second column
print('retrieve second column', mat[:,col])

#todo: retrieve all the elements on first row
print('retrieve first row', mat[row,:])

#todo: retrieve all the elements on first two rows and last two columns
print(mat[0:2,1:3])

