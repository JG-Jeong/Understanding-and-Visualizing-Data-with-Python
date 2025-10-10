import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mean_nogym = 155
sd_nogym = 5
mean_gym = 185 
sd_gym = 5 
gymperc = .3
popSize = 40000

nogym = np.random.normal(mean_nogym, sd_nogym, int(popSize * (1 - gymperc)))
gym = np.random.normal(mean_gym, sd_gym, int(popSize * gymperc))

all_students = np.concatenate([nogym, gym])
gym_01 = np.concatenate((np.zeros(len(nogym)), np.ones(len(gym))))


da = pd.DataFrame({"weight": all_students, "gym": gym_01})

# sns.displot(da[da["gym"] == 0], x = "weight", kde = True)
# plt.title("Non gym-goers only")
# plt.grid(True)
# plt.xlim([140, 200])
# plt.show()

# sns.displot(da, x = "weight", kde = True)
# plt.axvline(x = np.mean(da["weight"]), color = "red")
# plt.grid(True)
# plt.xlim([140, 200])
# plt.show()  


## What happens if we sample from the entire population? 중심극한정리 (Central Limit Theorem)
numberSamps = 5000
sampSize = 50

mean_distribution = np.empty(numberSamps)
for i in range(numberSamps):
    student_sample = np.random.choice(da["weight"], sampSize)
    mean_distribution[i] = np.mean(student_sample)


# sns.histplot(mean_distribution)
# plt.axvline(x=np.mean(da["weight"]), color = "red")
# plt.grid(True)
# plt.xlim([140, 200])
# plt.show()


## what happens if we take a non-representative sample? 비준규모표본 (Non-representative sample)

biased_mean_distribution = np.empty(numberSamps)
db = da[da["gym"] == 1]
for i in range(numberSamps):
    student_sample = np.random.choice(db["weight"], sampSize)
    biased_mean_distribution[i] = np.mean(student_sample)
    
sns.histplot(biased_mean_distribution)
plt.axvline(x = np.mean(da["weight"]), color = "red")
plt.axvline(x = np.mean(biased_mean_distribution), color = "blue")
plt.grid(True)
plt.xlim([140, 200])
plt.show()














