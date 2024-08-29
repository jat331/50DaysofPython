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
jackets_profit = df[df['Product Name'] == 'Jackets']['Profit'].sum()
sneakers_profit = df[df['Product Name'] == 'Sneakers']['Profit'].sum()
print(jackets_profit - sneakers_profit)

#What is the difference in costs between the most profitable proudct and the least profitable product?
most_profitable = df['Profit'].max()
least_profitable = df['Profit'].min()
most_profitable_cost = df[df['Profit'] == most_profitable]['Total Cost'].sum()
least_profitable_cost = df[df['Profit'] == least_profitable]['Total Cost'].sum()
print(most_profitable_cost - least_profitable_cost)

#What are the products that are most profitable and least profitable 
print(df[df['Profit'] == most_profitable]['Product Name'])
print(df[df['Profit'] == least_profitable]['Product Name'])

#Write is ___ profitable statements for both
print(f"{df[df['Profit'] == most_profitable]['Product Name']} is the most profitable product")
print(f"{df[df['Profit'] == least_profitable]['Product Name']} is the least profitable product")

#Acess total costs of jackets using .loc
print(df.loc[df['Product Name'] == 'Jackets', 'Total Cost'])

import matplotlib.pyplot as plt

#Create a bar chart of the 6 least profitable products with their sales, costs, and profits included. Chart should be sorted by profit in ascending order
least_profitable_products = df.sort_values(by='Profit', ascending=True).head(6)
least_profitable_products.plot(x='Product Name', y=['Total Price', 'Total Cost', 'Profit'], kind='bar')
plt.show()

#Day 27

#Using .loc calculate the profit of sunglasses, hoodies, and return 2 least profitable products
sunglasses_profit = df.loc[df['Product Name'] == 'Sunglasses', 'Profit'].sum()
print(sunglasses_profit)

hoodies_profit = df.loc[df['Product Name'] == 'Hoodies', 'Profit'].sum()
print(hoodies_profit)

least_profitable_products = df.sort_values(by='Profit', ascending=True).head(2)
print(least_profitable_products['Product Name'])

#Using .loc, return a dataframe subset with the most profitable product
most_profitable_product = df.loc[df['Profit'] == most_profitable]
print(most_profitable_product)

#Using seaborn, create a scatterplot to visualize relationship between sales and cost
import seaborn as sns
sns.scatterplot(x='Total Price', y='Total Cost', data=df)
plt.show()



