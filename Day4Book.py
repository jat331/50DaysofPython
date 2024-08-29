#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:15:56 2024

@author: jamesturner
"""

import numpy as np
import matplotlib.pyplot as plt

#Create two arrays of random number between 0 and 20. the shape of the first array must be (2,3) and (1,3) for the second. Check he shape of the arrays

np.random.seed(42)
array1 = np.random.randint(0, 20, (2, 3))
array2 = np.random.randint(0, 20, (1, 3))

print(array1)
print(array2)

#Check the shape of the arrays
print(array1.shape)
print(array2.shape)

#Add the two arrays and check the shape of the new array
array3 = array1 + array2
print(array3)
print(array3.shape)

array4 = np.dot(array1, array2.T)
print(array4)
print(array4.shape)

#create a 1-dimensional array of 100 random integers from 0 to 10. Use the array to create a histogram of the data and calculate the median and moe. create a seed too

import matplotlib.pyplot as plt


# Generating data
rng = np.random.default_rng(seed = 42)
random_data = rng.integers(low = 0, high = 11, size=(100))

# Ploting the data
plt.figure(figsize=(12,8))
plt.hist(random_data, bins=10)
plt.title("Hist Plot", fontsize = 20)
plt.show()

# To calculate the median
median = np.median(random_data)
print("Median : ", median)

from statistics import mode

# To calculate the mode
mode = mode(random_data)
print("Mode : ", mode)



#Create a 3-dimensional rray of 100 rnadom floats between 0 and 1. create a 3-d scatterplot of the data
np.random.seed(42)
np.random.seed(42)
array6 = np.random.rand(100, 3)
print(array6)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(array6[:,0], array6[:,1], array6[:,2])
plt.show()

# Creating an array
lst =[[0, 1, 3, 0, 4], [8, 9, 0, 9, 6]]
array = np.array(lst)

# Flattening the list and returning indices of non-zero numbers
np.flatnonzero(array)

#print
print(np.flatnonzero(array))