import pandas as pd
import seaborn as sns
import numpy as np
# import os
import matplotlib.pyplot as plt

"""
print(os.listdir())
['data.csv', 'data.py', 'data_cleaning_in_excel.txt']
"""

df = pd.read_csv("data.csv")
print(df)
"""
Output:    
    
    
       Unnamed: 0 Tmprature  Humidity
0           0         1       1.0
1           1       NaN       NaN
2           2         3      31.0
3           3         2      22.0
4           4         3      33.0
5           5         1      11.0
6           6         2      21.0
7           7       N/a      24.0
8           8         1      12.0
9           9        na      32.0
"""
print("\nPrint which fields are null")
print(df.isnull())

""" 
Output:

   Unnamed: 0  Tmprature  Humidity
0       False      False     False
1       False       True      True
2       False      False     False
3       False      False     False
4       False      False     False
5       False      False     False
6       False      False     False
7       False      False     False
8       False      False     False
9       False      False     False

You can see "NaN" came as True.. "na", "N/A" comes as false

"""
print("\nPrint sum of fields that are null")
print(df.isnull().sum())

""" 
Unnamed: 0    0
Tmprature     1
Humidity      1
dtype: int64

Only on field in Temp and one field in Humidity is NaN
"""

# We need to solve the problem
print("\nAfter Solving the problem ")
missing_values = ["nan", "na", "N/A", "n/a", "N/a", np.nan] # All thesse values will be changed to NaN
df = pd.read_csv("data.csv", na_values= missing_values)
print(df.isnull().sum())
print()
print(df.isnull().any())
""" 
Output:

Unnamed: 0    0
Tmprature     3
Humidity      1
dtype: int64

Unnamed: 0    False
Tmprature      True
Humidity       True
dtype: bool

Our problem is solved

sns.heatmap(df.isnull(), yticklabels=True,annot=True)
plt.show()
Gets the plot of     
"""


## Lets try to remove these vallues
print(df)
""" 
Output:

   Unnamed: 0  Tmprature  Humidity
0           0        1.0       1.0
1           1        NaN       NaN
2           2        3.0      31.0
3           3        2.0      22.0
4           4        3.0      33.0
5           5        1.0      11.0
6           6        2.0      21.0
7           7        NaN      24.0
8           8        1.0      12.0
9           9        NaN      32.0
"""
print("\n -----------------------------------------\n")
print("\n Plotting the graph")
sns.heatmap(df.isnull(), yticklabels=False,annot=True)
# plt.show()

print("\nLets try to remove NaN values")


#print(df.dropna())
"""
   Unnamed: 0  Tmprature  Humidity
0           0        1.0       1.0
2           2        3.0      31.0
3           3        2.0      22.0
4           4        3.0      33.0
5           5        1.0      11.0
6           6        2.0      21.0
8           8        1.0      12.0

"""
print("\n Remove only rows with all Nan Columns")
print(df.dropna(how="all"))
"""
 Remove only rows with all Nan Columns
   Unnamed: 0  Tmprature  Humidity
0           0        1.0       1.0
1           1        NaN       NaN
2           2        3.0      31.0
3           3        2.0      22.0
4           4        3.0      33.0
5           5        1.0      11.0
6           6        2.0      21.0
7           7        NaN      24.0
8           8        1.0      12.0
9           9        NaN      32.0
"""

print("\n Fill NA values")
print(df.fillna(0))
"""
 Fill NA values
   Unnamed: 0  Tmprature  Humidity
0           0        1.0       1.0
1           1        0.0       0.0
2           2        3.0      31.0
3           3        2.0      22.0
4           4        3.0      33.0
5           5        1.0      11.0
6           6        2.0      21.0
7           7        0.0      24.0
8           8        1.0      12.0
9           9        0.0      32.0   
"""

print("\nFill NA values using FOrward fill method")
print(df.fillna(method= 'ffill'))

"""
   Fill NA values using FOrward fill method
   Unnamed: 0  Tmprature  Humidity
0           0        1.0       1.0
1           1        1.0       1.0
2           2        3.0      31.0
3           3        2.0      22.0
4           4        3.0      33.0
5           5        1.0      11.0
6           6        2.0      21.0
7           7        2.0      24.0
8           8        1.0      12.0
9           9        1.0      32.0
"""

print("\nFill NA values using Backward fill method")
print(df.fillna(method= 'bfill'))
"""
Fill NA values using Backward fill method
   Unnamed: 0  Tmprature  Humidity
0           0        1.0       1.0
1           1        3.0      31.0
2           2        3.0      31.0
3           3        2.0      22.0
4           4        3.0      33.0
5           5        1.0      11.0
6           6        2.0      21.0
7           7        1.0      24.0
8           8        1.0      12.0
9           9        NaN      32.0   
   
"""

print("\nInterpolate NA values ")
print(df.interpolate())
"""
Output: 
\Interpolate NA values
   Unnamed: 0  Tmprature  Humidity
0           0        1.0       1.0
1           1        2.0      16.0
2           2        3.0      31.0
3           3        2.0      22.0
4           4        3.0      33.0
5           5        1.0      11.0
6           6        2.0      21.0
7           7        1.5      24.0
8           8        1.0      12.0
9           9        1.0      32.0

It takes the average of upper and lower values   
   
"""
print("\n Fill Custom values to each column")
print(df.fillna({
   'Tmprature': '00000000',
   'Humidity':'9999999'
}))

"""
 Fill Custom values to each column
   Unnamed: 0 Tmprature Humidity
0           0       1.0      1.0
1           1  00000000  9999999
2           2       3.0     31.0
3           3       2.0     22.0
4           4       3.0     33.0
5           5       1.0     11.0
6           6       2.0     21.0
7           7  00000000     24.0
8           8       1.0     12.0
9           9  00000000     32.0   
   
   """