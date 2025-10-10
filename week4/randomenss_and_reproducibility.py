import numpy as np

# Uniform Distribution (균등분포)
uniform_distribution = np.random.uniform(25, 50)

mu = 0
sigma = 1
np.random.normal(mu, sigma)

print(np.random.normal(mu, sigma))

import string
x= [_ for _ in string.ascii_lowercase]

rng = np.random.default_rng(12345)
print(rng)
for _ in range(5):
    print(rng.choice(x, 3, replace = False))