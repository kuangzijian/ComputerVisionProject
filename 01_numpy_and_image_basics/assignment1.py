# import numpy
import numpy as np

# Create and print a 3 by 3 array where every number is a 15
a1 = np.ones((3,3))*15
print('a1\n',a1)
# print out what are the largest and smalled values in the array below
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('largest value is', arr.max())
print('smallest value is',arr.min())
# import pyplot lib from matplotlib and Image lib from  PIL
import matplotlib.pyplot as plt
from PIL import Image

# use PIL and matplotlib to read and display the ../data/zebra.jpg image
pic1 =  Image.open('../data/zebra.jpg')
# convert the image to a numpy arrary and print the shape of the arrary
pic1_arr = np.array(pic1)
print(pic1_arr.shape)
# use slicing to set the RED and GREEN channels of the picture to 0, then use imshow() to show the isolated blue channel
#RGB 012
pic1_arr[:,:,0 ]=0
pic1_arr[:,:,1 ]=0
plt.imshow(pic1_arr)
plt.show()
#picture only show blue