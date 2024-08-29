#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:53:10 2024

@author: jamesturner
"""

import pandas as pd

data = {'Name': ['Joe', 'Phil', 'Ken', 'Jos', 'Luke'],
        'miles_run': [120, 80, 100, 90, 85],
        'time_in_hours': [40, 38, 45, 50, 50]}
df = pd.DataFrame(data)

print(df)

#Now I have their ages and gender. They are "45, 28, 21, 55, 62" and for gender "M, M, Fm F, M"

df['age'] = [45, 28, 21, 55, 62]

#Now add the gender to the dataframe
df['gender'] = ['M', 'M', 'F', 'F', 'M']

# Shuffle the DataFrame and reset the index
shuffled_df = df.sample(frac=1).reset_index(drop=True)

print(shuffled_df)

#Shuffling data is crucial in machine learning for the following reasons:

#Prevents Bias: If the data is ordered in a specific pattern (e.g., sorted by age or any feature), the model might learn this pattern rather than the actual underlying relationships, leading to poor generalization.

#Improves Training Performance: Shuffling ensures that batches used for training are representative of the entire dataset, helping the model avoid overfitting to specific sequences.

#Cross-Validation: For techniques like k-fold cross-validation, shuffling ensures that each fold is representative, reducing the risk of biased performance estimates.

#In summary, shuffling helps the model learn patterns more effectively by reducing the risk of bias and ensuring the training data is representative of the overall dataset.

# Reshape the dataframe to long format using melt
long_df = pd.melt(df, id_vars=['Name'], value_vars=['miles_run', 'time_in_hours', 'age', 'gender'],
                  var_name='Metric', value_name='Value')

print(long_df)