import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

da = pd.read_csv("nhanes_2015_2016.csv")

da = da.dropna(subset=["BPXSY2"])

print(round(da["BPXSY2"].describe(),1))
print(round(da["BPXSY2"].median(),1))