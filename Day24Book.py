#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:02:18 2024

@author: jamesturner
"""

import pandas as pd
import matplotlib.pyplot as plt  # Correct import for plotting

# Path to the Excel file
file_path = '/Users/jamesturner/Desktop/Asset_sales_data.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Return the datatypes of the columns
print(df.dtypes)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%m-%d-%Y')

# Extract month and year from the 'date' column
df['Month'] = df['date'].dt.month
df['Year'] = df['date'].dt.year

# Map month numbers to month names
df['Month_Name'] = df['Month'].map({
    1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
})

# Count the number of entries per month
monthly_sales_count = df.groupby('Month_Name').size().reset_index(name='Count')

# Find the month with the highest number of sales
highest_sales_month = monthly_sales_count.loc[monthly_sales_count['Count'].idxmax()]

print(f"The month with the highest number of sales is {highest_sales_month['Month_Name']} with {highest_sales_month['Count']} sales.")

# Return the value of sales between 11-20-2021 and 12-06-2021. Create a dataframe and return the sum of the sales in this period
df_filtered = df[(df['date'] >= '2021-11-20') & (df['date'] <= '2021-12-06')]
total_sales = df_filtered['sales'].sum()

print(f"The total sales between 11-20-2021 and 12-06-2021 is ${total_sales:.2f}.")

# Create a pie chart for each product with the sales value percentage
products_sales = df.groupby('products')['sales'].sum()
products_sales_percentage = products_sales / products_sales.sum() * 100

products_sales_percentage.plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Sales Percentage by Products')
plt.axis('equal')
plt.show()

#Create a pivot table and calculate the sum of sales group by the products column. Plot this on a bar chart with title Total Sales per Product
pivot_table = df.pivot_table(index='products', values='sales', aggfunc='sum')
pivot_table.plot(kind='bar', title='Total Sales per Product')
plt.ylabel('Total Sales')
plt.show()