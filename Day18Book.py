#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:14:51 2024

@author: jamesturner
"""

import pandas as pd

# Load the datasets
running_data = pd.read_csv('/Users/jamesturner/Desktop/running_data.csv')
runner_rest = pd.read_csv('/Users/jamesturner/Desktop/runner_rest.csv')

# Create a copy of the dataframe and convert kilometers to miles in the Distance (km) column. Change the column name to Distance (miles) in the new dataframe
running_data_miles = running_data.copy()
running_data_miles['Distance (miles)'] = running_data_miles['Distance (km)'] * 0.621371
running_data_miles = running_data_miles.drop(columns=['Distance (km)'])

# Add another column to calculate speed in kilometers per hour using the original distance in kilometers
running_data_miles['Speed (km/h)'] = running_data['Distance (km)'] / running_data_miles['Time (hours)']

# Rename the Time (hours) column to Duration (hours)
running_data_miles = running_data_miles.rename(columns={'Time (hours)': 'Duration (hours)'})

# Merge the two dataframes
merged_data = pd.merge(running_data_miles, runner_rest, left_on='Name', right_on='Runners')

# Drop the Runner column (if you want to keep only 'Name' as the identifier)
merged_data = merged_data.drop(columns=['Runners'])


# Convert "Rest Time (Mins)" to "Rest Time (Hours)" using .apply()
merged_data['Rest Time (Hours)'] = merged_data['Rest Time (Mins)'].apply(lambda x: x / 60)


#Using the pandas.Series.map() create a subset of the data for runners who covered 5 or more miles

subset_data = merged_data[merged_data['Distance (miles)'].map(lambda x: x >= 5)]
print(subset_data.head())

#Drop the Index column and find out who ran the furthest distance

#subset_data = subset_data.drop(columns=['Index'])
max_distance = subset_data['Distance (miles)'].max()
runner = subset_data[subset_data['Distance (miles)'] == max_distance]['Name'].values[0]
print(f'{runner} ran the furthest distance of {max_distance} miles.')