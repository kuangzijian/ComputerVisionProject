#todo: import numpy
import numpy as np

#todo: creating list [0,1,2,3,4] in python and print the type of your list
list = [0,1,2,3,4]
print(type(list))

#todo: cast your list into a numpy arrary and print the type of your array
arr = np.array(list)
print(type(arr))

#todo: return evenly spaced values within a given interval [start, stop).
a = np.arange(3)
print(a)

b = np.arange(0,10,2)
print(b)

c = np.zeros((5,5))
print(c)

d = np.ones((2,4))
print(d)

np.random.seed(101) # watch video for details
arr = np.random.randint(0,100,10)

arr

arr2 = np.random.randint(0,100,10)

arr2

arr.max()

arr.min()

arr.mean()

arr.argmin()

arr.argmax()

arr.reshape(2,5)

mat = np.arange(0,100).reshape(10,10)

mat

row = 0
col = 1

mat[row,col]

mat[:,col]

mat[row,:]

mat[0:3,0:3]

