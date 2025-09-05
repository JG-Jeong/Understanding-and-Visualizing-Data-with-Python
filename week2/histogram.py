# Histogram

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# imaginary url to explain libraries
url = "CartWheeldata.csv"
# 
df = pd.read_csv(url)

sns.displot(df.CWDistance)






















