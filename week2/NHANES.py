import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

da = pd.read_csv("nhanes_2015_2016.csv")

print(da.DMDEDUC2.value_counts())
# DMDEDUC2
# 4.0    1621
# 5.0    1366
# 3.0    1186
# 1.0     655
# 2.0     643
# 9.0       3
# Name: count, dtype: int64

print(da.DMDEDUC2.value_counts().sum) #5474
print(1621+1366+1186+655+643+3) # Manually sum the frequencies
print(da.shape) #(5735, 28)

pd.isnull(da.DMDEDUC2).sum() #261
# replace text label
da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 
                                       7: "Refused", 9: "Don't know" })
print(da.DMDEDUC2x.value_counts())
# Some college/AA    1621
# College            1366
# HS/GED             1186
# <9                  655
# 9-11                643
# Don't know            3
# Name: DMDEDUC2x, dtype: int64

# Replacing numeric to string values
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male",  2: "Female"})

# proportion of the category
x = da.DMDEDUC2x.value_counts() 
print(x/x.sum())

# fillna - fill up N/A value
da["DMDEDUC2x"] = da.DMDEDUC2.fillna("Missing")
x = da.DMDEDUC2x.value_counts()
print(x/x.sum())

# Numerical summary - dropna
print(da["BMXWT"].dropna().describe())
# count    5666.000000
# mean       81.342676
# std        21.764409
# min        32.400000
# 25%        65.900000
# 50%        78.200000
# 75%        92.700000
# max       198.900000
# Name: BMXWT, dtype: float64

# Pandas/ Numpy
x = da["BMXWT"].dropna()
x.mean() # Pandas method
np.mean(x)  # Numpy method

x.median()
np.percentile(x, 50)
np.percentile(x, 75)
x.quantile(0.75) # Pandas method for quatiles, equivalent to 75th percentile

a = np.mean((da.BPXSY1 >= 120) & (da.BPXSY1 <= 139))
b = np.mean((da.BPXDI1 >=80) & (da.BPXDI2 <= 89)) # 혈압이 이 사이에 값을 전고혈압으로 함.
np.mean(a or b) # 전고혈압인 사람들의 합

np.mean(da.BPXSY1 - da.BPXSY2)
np.mean(da.BPXDI1 - da.BPXDI2)

sns.displot(da.BMXWT.dropna())

sns.displot(da.BPXSY1.dropna())

bp = sns.boxplot(data = da.loc[:, ["BPXSY1", "BPXSY2", "BPXDI1", "BPXDI2"]])
_ = bp.set_ylabel("Blood pressure in mm/Hg")

da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80]) # Create age stratea based on these cut points
plt.figure(figsize=(12,5)) # Mkae the figure wider than default (12cm wide, 5cm tall)
sns.boxplot(x="agegrp", y="BPXSY1", data=da)

da["agegrp"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])
plt.figure(figsize = (12, 5))   
sns.boxplot(x="agegrp", y="BPXSY1", hue="RIAGENDRx", data=da)

da["agegrp"] = pd.cut(da.RIDAGEYR, [18,30,40,50,60,70,80])
plt.figure(figsize = (12,5))
sns.boxplot(x="RIAGENDRx", y="BPXSY1", hue="agegrp", data=da)
plt.show()

da.groupby("agegrp")["DMDEDUC2x"].value_counts()

dx = da.loc[~da.DMDEDUC2x.isin(["Don't know", "Missing"]), :]  # Eliminate rare/missing values
dx = dx.groupby(["agegrp", "RIAGENDRx"])["DMDEDUC2x"]
dx = dx.value_counts()
dx = dx.unstack() # Restructure the results from 'long' to 'wide'
dx = dx.apply(lambda x: x/x.sum(), axis=1) # Normalize within each stratum to get proportions
print(dx.to_string(float_format="%.3f"))  # Limit display to 3 decimal places













