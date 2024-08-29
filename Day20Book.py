#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:07:36 2024

@author: jamesturner
"""


import pandas as pd
import matplotlib.pyplot as plt

products = ["sugar", "salt", "oil", "diapers", "ice"]
costs = [2450, 1989, 6745, 9807, 8743]
sales = [27908, 4508, 6734, 9976, 9000]

df = pd.DataFrame({"products": products, "costs": costs, "sales": sales})

#Calculate profatibility for each product by doing sales - costs

df["profitability"] = df["sales"] - df["costs"]

#Tell me what the most profitable product is 

most_profitable = df["products"][df["profitability"].idxmax()]
print(f"The most profitable product is {most_profitable}")


#Plot the profitability of each product
plt.bar(df["products"], df["profitability"])
plt.xlabel("Products")
plt.ylabel("Profitability")
plt.title("Product profitability")
plt.show()

least_profitable = df["products"][df["profitability"].idxmin()]
print(f"The least profitable product is {least_profitable}")

difference = df["profitability"].max() - df["profitability"].min()
print(f"The difference between the most profitable and least profitable product is {difference}")

#Create a line graph of the costs and profits of each product

plt.plot(df["products"], df["costs"], label="Costs")
plt.plot(df["products"], df["sales"], label="Sales")
plt.xlabel("Products")
plt.ylabel("Amount")
plt.title("Product costs and sales")
plt.legend()
plt.show()

average_cost = df["costs"].mean()
average_profit = df["profitability"].mean()
print(f"The average cost per product is {average_cost} and the average profit per product is {average_profit}")