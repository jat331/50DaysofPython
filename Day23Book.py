#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:53:47 2024

@author: jamesturner
"""

import pandas as pd
import numpy as np


names = ["Kelly", np.nan, 'Jon', 'Ken', 'Tim', 'Pel']
grades = [30, 40, 30, 67, np.nan, 55]
age =[15, np.nan, 18, 17, np.nan, 16]

df = pd.DataFrame({'Names': names,'Grades':grades,'Age': age})
df
print(df)

#Using sklearn, fill the missing "names" with 'Paul', and use the mean of the "grades" and "age" to fill the missing values in the respective columns.
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
df['Grades'] = imp.fit_transform(df[['Grades']])
df['Age'] = imp.fit_transform(df[['Age']])
df['Names'] = df['Names'].fillna('Paul')
print(df)

#using the original dataframe, drop any column that has 30% or more missing values. Save this as a new variable
df.dropna(thresh=0.7*len(df), axis=1, inplace=True)
print(df)


#Check for any duplicates in the dataframe
print(df.duplicated())

#Calculate summary statistics (Mean, max, min) for the dataframe grouped `by` the "Names" column
print(df.groupby('Names').agg(['mean', 'max', 'min']))