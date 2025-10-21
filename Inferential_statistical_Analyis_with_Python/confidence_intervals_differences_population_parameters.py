import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

da = pd.read_csv("../nhanes_2015_2016.csv")

da["SMQ020x"] = da.SMQ020.replace({1: "smoke", 2: "nosmoke", 7: np.nan, 9: np.nan })
da["SMQ020x"].value_counts()


da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
da["RIAGENDRx"].value_counts()

dx = da[['SMQ020x', 'RIAGENDRx']].dropna()
ct = pd.crosstab(dx.RIAGENDRx, dx.SMQ020x)

ct['total'] = ct['nosmoke'] + ct['smoke']   
ct['nosmoke_prop'] = ct['nosmoke']/ct['total']
ct['smoke_prop'] = ct['smoke']/ct['total']

###########################################################################

# Difference of two population proportions

di = ct.loc['Male', 'smoke_prop'] - ct.loc['Female', 'smoke_prop']

pf = ct.loc['Female', 'smoke_prop']
nf = ct.loc['Female', 'total']
se_female = np.sqrt(pf * (1-pf) / nf)

pm = ct.loc['Male', 'smoke_prop']
nm = ct.loc['Male', 'total']
se_male = np.sqrt(pm * (1-pm)/ nm)

se_diff = np.sqrt(se_female**2 + se_male**2)

lcb = di - 1.96 * se_diff
ucb = di - 1.96 * se_diff


# Difference of Two Population Means
da['BMXBMI'].head()

ta = da.groupby('RIAGENDRx').agg({'BMXBMI': ['mean', 'std', 'size']})
print(ta)
sns.boxplot(x='RIAGENDRx', y='BMXBMI', data=da);
# plt.show()

sem_female = ta.loc['Female', ('BMXBMI', 'std')] / np.sqrt(ta.loc['Female', ('BMXBMI', 'size')])
sem_male = ta.loc['Male', ('BMXBMI', 'std')] / np.sqrt(ta.loc['Male', ('BMXBMI', 'size')])

sem_diff = np.sqrt(sem_female ** 2 + sem_male ** 2)

di = ta.loc['Female', ('BMXBMI', 'mean') - ta.loc['Male', 'mean']]

lcb = di - 1.96 * sem_diff
ucb = di - 1.96 * sem_diff

















