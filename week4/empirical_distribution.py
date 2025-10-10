import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(12345)

mu = 7
sigma = 1.7

Observations = np.random.normal(mu, sigma, size=10000)

# plt.axvline(np.mean(Observations) + np.std(Observations), color = 'g')
# plt.axvline(np.mean(Observations) - np.std(Observations), color = 'g')

# plt.axvline(np.mean(Observations) + 2 * np.std(Observations), color = 'y')
# plt.axvline(np.mean(Observations) - 2 * np.std(Observations), color = 'y')

# sns.histplot(Observations, kde=True)
# plt.show()

print(pd.Series(Observations).describe())

# 무작위 표본 추출 (Subsampling and Empirical Rule Verification)
SampleA = np.random.choice(Observations, 400)
SampleB = np.random.choice(Observations, 400)
SampleC = np.random.choice(Observations, 400)

fig, ax = plt.subplots()

sns.histplot(SampleA, ax = ax, color = "orange", alpha = 0.2)
sns.histplot(SampleB, ax = ax, color = "purple", alpha = 0.2)
sns.histplot(SampleC, ax = ax, color = "green", alpha = 0.2)


expdata = np.random.exponential(size=1000)
print((np.abs(expdata - 1) <1).mean)
print((np.abs(expdata - 1) <2).mean)


tdata = np.random.standard_t(3, size = 1000)
print((np.abs(tdata) < np.sqrt(3)).mean())
print((np.abs(tdata) < 2*np.sqrt(3)).mean())

sns.displot(Observations)
plt.axvline(np.mean(Observations) + np.std(Observations), 0, .59, color = 'g')
plt.axvline(np.mean(Observations) - np.std(Observations), 0, .59, color = 'g')

plt.axvline(np.mean(Observations) + (np.std(Observations) * 2), 0, .15, color = 'y')
plt.axvline(np.mean(Observations) - (np.std(Observations) * 2), 0, .15, color = 'y')


from statsmodels.distributions.empirical_distribution import ECDF
import matplotlib.pyplot as plt

ecdf = ECDF(Observations)

plt.plot(ecdf.x, ecdf.y)

plt.axhline(y = 0.025, color = 'y', linestyle='-')
plt.axvline(x = np.mean(Observations) - (2 * np.std(Observations)), color = 'y', linestyle='-')

plt.axhline(y = 0.975, color = 'y', linestyle='-')
plt.axvline(x = np.mean(Observations) + (2 * np.std(Observations)), color = 'y', linestyle='-')