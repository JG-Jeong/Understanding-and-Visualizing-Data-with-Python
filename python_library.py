"""
Numpy - working with arrays of data
Pandas - working with tabular data (CSV, Excel, etc.)
Scipy - working with scientific data
Matplotlib - working with data visualization(graphs, charts, etc.)
Seaborn - working with data visualization
Statsmodels - working with statistical data(statistics, probability, etc.)
Scikit-learn - working with machine learning(machine learning, deep learning, etc.)
TensorFlow - working with deep learning(deep learning, etc.)
PyTorch - working with deep learning

"""

import numpy as np
import pandas as pd

a = np.arrray([0,1,2,3,4,5,6,7,8,9,10])
np.mean(a) # 5.5

# Data management with Pandas
fname = "CartWheeldata.csv"

df = pd.read_csv(fname)

type(df) # pandas.core.frame.DataFrame

# view DataFrame by calling the head() function
df.head()
# view columns
df.columns
# view dtypes
df.dtypes
# Indexing with .loc()
# Return all observations of the variable CWDistance
df.loc[:,"CWDistance"]
"""
0      79
1      70
2      85
3      87
4      72
5      81
6     107
7      98
8     106
9      65
10     96
11     79
12     92
13     66
14     72
15    115
16     90
17     74
18     64
19     85
20     66
21    101
22     82
23     63
24     67
Name: CWDistance, dtype: int64 
"""
# .iloc() - slicing, whereas .loc() used lables/column names.
df.iloc[:4]
df.iloc[1:5,2:4]

df.Gender.unique()
df.groupby(['Gender', 'GenderGroup']).size()
