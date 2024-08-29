#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:03:05 2024

@author: jamesturner
"""

#Day 5

list_numbers = [[12,23,-45],[18,-77,-44]]

#Using numpy, create an array from the list. Return all negative numbers

import numpy as np
arr = np.array(list_numbers)
print(arr[arr<0])


#Now multiply each element in the negative array by 2
arr[arr<0] *= 2
print(arr)

print(np.sum(arr, axis=1))


arr = np.arange(100).reshape(2,5,10)
print(arr)

print(arr[1,0:1,0:10])

arr = np.array(list_numbers)
print(np.sum(arr[0]>arr[1]))