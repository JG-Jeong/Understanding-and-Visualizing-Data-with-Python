import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# MatPlotLibrary
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# Plot the points using matplotlib
plt.plot(x, y)

plt.grid(True)
plt.plot(x, y, ":", lw=5, color="orange")
plt.ylabel("Y", size=15)
plt.xlabel("X", size=15)

# ------------------------------------------------------------------------------------------------------------------------------ #
# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
























