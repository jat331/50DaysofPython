import pandas as pd
import numpy as np

data = {'Name': ["Carol", "Kate", "Jane", "Kuda", "Tito", "Kuku"],
        'Age': [23, np.nan, 34, 56, np.nan, 44]}
df = pd.DataFrame(data)

# Check for missing values
print(df.isnull().sum())
print(df)

# Drop rows with missing values
df2 = df.dropna()
print(df2)

# Fill missing values in the numeric columns only
df3 = df.copy()
df3['Age'] = df['Age'].fillna(df['Age'].mean())

# Adding the 'gender_values' column
df3['gender_values'] = ["F", "F", "F", "M", "M", "M"]
print(df3)
