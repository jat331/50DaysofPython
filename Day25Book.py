#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:26:03 2024

@author: jamesturner
"""

#Day 25

import pandas as pd

# Load the datasets
df = pd.read_csv('/Users/jamesturner/Desktop/retail_shop_data.csv')

# Display the first 5 rows of the dataset, check how many rows and columns are there, and check for duplicates
print(df.head())

print(df.shape)

print(df.duplicated().sum())

print(f"There are {df.duplicated().sum()} duplicates")

print(df.isnull().sum())

#Rename the column Total to Revenue, Cost to Cost per Product and Price to Price per Product
df.rename(columns={'Total':'Revenue', 'Cost':'Cost per Product', 'Price':'Price per Product'}, inplace=True)

#Multiply Cost per Product by Quantity to get the total cost, and Price per Product by Quantity to get the total price
df['Total Price'] = df['Price per Product'] * df['Quantity']
df['Total Cost'] = df['Cost per Product'] * df['Quantity']


#add a profit column that shows the profit of each product by subtracting the total cost from the total price
df['Profit'] = df['Total Price'] - df['Total Cost']

#Create a column called filter. If the profit is greater than 15, the value is true, otherwise false 
df['filter'] = df['Profit'] > 15

#Which products have a profit over 15? Print the product name
print(df[df['filter'] == True]['Product Name'])
 
#Day 26


#Find the difference in profit between jackets and sneakers
jackets_profit = df[df['Product'] == 'Jackets']['Profit'].sum()
sneakers_profit = df[df['Product'] == 'Sneakers']['Profit'].sum()
print(jackets_profit - sneakers_profit)

