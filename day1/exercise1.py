import numpy as np

## Creating Arrays
my_list = [0,1,2,3,4]

arr = np.array(my_list)

print(arr)

np.arange(0,10)

np.arange(0,10,2)

np.zeros((5,5))

np.ones((2,4))

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

