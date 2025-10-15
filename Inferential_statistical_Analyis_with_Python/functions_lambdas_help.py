import numpy as np
import seaborn as sns

# def get_max(x):
#     current_max = x[0]
#     for i in x[1:]:
#         if i > current_max:
#             current_max = i
#     return current_max


# print(get_max(np.random.choice(400,100)))

# def make_plot(x):
#     g = sns.histplot(x, kde=True, color="green")

# make_plot(np.random.normal(size=500))

f = (lambda x: x**2)(3)

print(f)

f = lambda x : np.sin(x)
x = np.linspace(-np.pi, np.pi, 100)
y = [f(i) for i in x]








