#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:51:56 2024

@author: jamesturner
"""



import numpy as np

list1 = [2,3,4,6]
arr1 = np.array(list1)

#write a function that takes the array and returns reversed

def reverse_array(arr):
    return arr[::-1]

print(reverse_array(arr1))


list2 = [8,10,12,14]

#Create an array from list1 and list2

arr2 = np.array([list1, list2])

print(arr2)

list3 = [16,18,20,22.1]
         
#Create an array from list1, list2, and list3

arr3 = np.array([list1, list2, list3])

list1 = [2, 3, 4, 6]
list2 = [8, 10.1, 12, 14]
list3 = [16, 18, 20, 22.1]

# Create an array from the three lists
arr4 = np.array([list1, list2, list3])


# Convert the array to int64 data type
arr4 = arr4.astype(np.int64)
print(arr4)