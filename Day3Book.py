#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 12:10:05 2024

@author: jamesturner
"""

import numpy as np
import matplotlib.pyplot as plt 


#Generate an array using random numbers between 0 and 1. The shape of the array must be (3,4)
np.random.seed(42)
array = np.random.rand(3,4)
print(array)

#now generate an array of random integers between 0 and 10 with shape (3,4)
np.random.seed(42)
array = np.random.randint(0, 10, (3,4))
print(array)

np.random.seed(42)
array = np.random.randn(1000)
plt.hist(array, bins=30)
plt.show()

arr = ["Orange","Apple","Pear"]
np.random.seed(42)
#Using random choice, generate a (3,4) array of the fruit names
array = np.random.choice(arr, (3,4))
print(array)