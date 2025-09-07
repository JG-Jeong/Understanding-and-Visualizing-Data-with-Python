import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np

da = pd.read_csv("nhanes_2015_2016.csv")

r = {1: "Married", 2: "Widowed", 3: "Divorced", 4: "Separated", 5: "NeverMarried", 6: "Cohabitating", 77: "Refused", 99: "Unknown"}

da["DMDMARTLx"] = da["DMDMARTL"].replace(r)

print("All subjects:")
x = da["DMDMARTLx"].value_counts()
print(x / x.sum())

for ky,db in da.groupby("RIAGENDR"):
    print("\nRIAGENDR=", ky)
    x = db["DMDMARTLx"].value_counts()
    print(x / x.sum())
    
da3040 = da.query('RIDAGEYR >= 30 & RIDAGEYR <= 40')
for ky,db in da3040.groupby("RIAGENDR"):
    print("\nRIAGENDR=", ky, " 30 <= RIDAGEYR <= 40")
    x = db["DMDMARTLx"].value_counts()
    print(x / x.sum())

# Q1.

r = {1: "Married", 2: "Widowed", 3: "Divorced", 4: "Separated", 5: "NeverMarried", 6: "Cohabitating", 77: "Refused", 99: "Unknown"}
da["DMDMARTLx"] = da["DMDMARTL"].replace(r)

da["agegrp"] = pd.cut(da.RIDAGEYR, [10,20,30,40,50,60,70,80])

da_fem = da.query('RIAGENDR == 2').copy()
# x = da_fem.groupby("agegrp")["DMDMARTLx"].value_counts(normalize=True)
# print("\n", x/x.sum()) 


dist = (da_fem.groupby("agegrp")["DMDMARTLx"]
              .value_counts(normalize=True)
              .rename("prop")
              .reset_index())

table = (dist.pivot(index="agegrp", columns="DMDMARTLx", values="prop")
              .fillna(0.0))

print(table.round(3))
print("\nRow sums (should be 1.0):")
print(table.sum(axis=1).round(6))

# Q2.
x = da["BMXWT"]

da_mal = da.query('RIAGENDR == 1').copy()
da_fem = da.query('RIAGENDR == 2').copy()

sns.boxplot(x="BMXHT", data=da_mal)






































