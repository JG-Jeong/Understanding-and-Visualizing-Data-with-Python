import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

da = pd.read_csv("nhanes_2015_2016.csv")

# r = {1: "Married", 2: "Widowed", 3: "Divorced", 4: "Separated", 5: "NeverMarried", 6: "Cohabitating", 77: "Refused", 99: "Unknown"}

# da["DMDMARTLx"] = da["DMDMARTL"].replace(r)

# print("All subjects:")
# x = da["DMDMARTLx"].value_counts()
# print(x / x.sum())

# for ky,db in da.groupby("RIAGENDR"):
#     print("\nRIAGENDR=", ky)
#     x = db["DMDMARTLx"].value_counts()
#     print(x / x.sum())
    
# da3040 = da.query('RIDAGEYR >= 30 & RIDAGEYR <= 40')
# for ky,db in da3040.groupby("RIAGENDR"):
#     print("\nRIAGENDR=", ky, " 30 <= RIDAGEYR <= 40")
#     x = db["DMDMARTLx"].value_counts()
#     print(x / x.sum())

# # Q1.

# r = {1: "Married", 2: "Widowed", 3: "Divorced", 4: "Separated", 5: "NeverMarried", 6: "Cohabitating", 77: "Refused", 99: "Unknown"}
# da["DMDMARTLx"] = da["DMDMARTL"].replace(r)

# da["agegrp"] = pd.cut(da.RIDAGEYR, [10,20,30,40,50,60,70,80])

# da_fem = da.query('RIAGENDR == 2').copy()
# # x = da_fem.groupby("agegrp")["DMDMARTLx"].value_counts(normalize=True)
# # print("\n", x/x.sum()) 


# dist = (da_fem.groupby("agegrp")["DMDMARTLx"]
#               .value_counts(normalize=True)
#               .rename("prop")
#               .reset_index())

# table = (dist.pivot(index="agegrp", columns="DMDMARTLx", values="prop")
#               .fillna(0.0))

# print(table.round(3))
# print("\nRow sums (should be 1.0):")
# print(table.sum(axis=1).round(6))

# Q2.
# Q2-1
# x = sns.displot(da["BMXWT"])

# plt.show()

# Q2-2

# da_male = da.query('RIAGENDR == 1').copy()
# da_female = da.query('RIAGENDR == 2').copy()

# x = sns.displot(da_male["BMXHT"])
# y = sns.displot(da_female["BMXHT"])
# plt.show()

# da_male['Gender'] = 'Male'
# da_female['Gender'] = 'Female'
# da_combined = pd.concat([da_male, da_female])

# plt.figure(figsize=(6,8))
# sns.boxplot(x='Gender', y = 'BMXHT', data = da_combined, palette={'Male': 'blue', 'Female': 'pink'}, width=0.4)
# plt.title('Side-by-Side Boxplot of Heights by Gender')
# plt.xlabel("Gender")
# plt.ylabel("Height (BMXHT)")
# plt.show()

# Q4

# da["BPXSY_diff"]  = da['BPXSY2'] - da['BPXSY1']

# plt.figure(figsize = (8,6))
# sns.boxplot(y='BPXSY_diff', data = da)
# plt.title("Distribution of Within-Subject Differences in Systolic Blood Pressure")
# plt.ylabel("Diffence (BPXSY1 - BPXSY2) in mmHg")
# plt.show()

# Q4-2
# da["BPXSY_diff"] =  da['BPXSY2'] - da["BPXSY1"] 

# lower_sbp_proportion= len(da[da["BPXSY_diff"] < 0]) / len(da)

# print(f"{lower_sbp_proportion}")

# Q4-b

# da["BPXSY_diff"] = da["BPXSY1"] - da['BPXSY2']
# sns.boxplot(y='BPXSY1', data=da)
# plt.show()
# sns.boxplot(y='BPXSY2', data=da)
# plt.show()

# da_long = pd.melt(da, value_vars = ["BPXSY1", "BPXSY2"], var_name="Measurement", value_name="Blood_Pressure")

# plt.figure(figsize=(8,6))
# sns.boxplot(x="Measurement", y="Blood_Pressure", data=da_long)
# plt.show()

# Q5

# da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 
#                                        7: "Refused", 9: "Don't know" })

# # DMDEDUC2와 DMDHHSIZ의 빈도표 생성
# freq_table = pd.crosstab(da["DMDEDUC2x"], da["DMDHHSIZ"])

# # 빈도를 비율로 변환 (각 행의 합으로 나누기)
# prop_table = freq_table.div(freq_table.sum(axis=1), axis=0)

# # 결과 출력
# print("Frequency Table:")
# print(freq_table)
# print("\nProportion Table:")
# print(prop_table)

# Q5b. Restrict the sample to people between 30 and 40 years of age. Then calculate the median household size for women and men within each level of educational attainment.
da_30_40 = da.query("RIDAGEYR >=30 and RIDAGEYR <=40")

da_male = da_30_40.query('RIAGENDR == 1').copy()
da_female = da_30_40.query('RIAGENDR == 2').copy()

da_male["DMDEDUC2x"] = da_male.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 7: "Refused", 9: "Don't know" })
da_female["DMDEDUC2x"] = da_female.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 7: "Refused", 9: "Don't know" })

median_male = da_male.groupby('DMDEDUC2x')['DMDHHSIZ'].median()
median_female = da_female.groupby('DMDEDUC2x')['DMDHHSIZ'].median()

# 결과 출력
print(median_male)
print(median_female)




















