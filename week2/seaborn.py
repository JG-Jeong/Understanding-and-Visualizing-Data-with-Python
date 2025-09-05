# Seaborn - high-level interface to Matplotlib to make statistical data visualization

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

url = "Cartwheeldata.csv"

df = pd.read_csv(url)

sns.scatterplot(x='Wingspan', y='CWDistance', data = df);

sns.scatterplot(x='Wingspan', y='CWDistance', hue="Gender", data=df);
## sns_scatterplot.png

sns.swarmplot(x="Gender", y="CWDistance", data=df);
## sns_swarmplot