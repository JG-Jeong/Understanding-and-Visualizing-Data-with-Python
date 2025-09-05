import seaborn as sns # For plotting
import matplotlib.pyplot as plt # For showing plots

# use it to construct a Pandas dataframe.
tips_data = sns.load_dataset("tips")

tips_data.head()

# Descript data - Summary statistics, including the mean, minimum, and maximum of the data, can be useful to get a feel for the central tendency and dispersion of each variable.
tips_data.describe()

# Creating Histogram
sns.histplot(tips_data["total_bill"], kde = False).set_title("Histogram of Total Bill");

sns.histplot(tips_data["tip"], kde = False).set_title("Histogram of Total Tip");

sns.scatterplot(x="total_bill", y="tip", data=tips_data);
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=tips_data);

# Creating boxplot
sns.boxplot(x=tips_data["total_bill"]).set_title("Box plot of the Total Bill");

sns.boxplot(x=tips_data["tip"]).set_title("Box plot of the Tip")
plt.show()

# Creating histograms and boxplots stratified by groups
sns.boxplot(x = tips_data["tip"], y = tips_data["smoker"])
plt.show()

# Create a boxplot and histogram of the tips grouped by time of day
sns.boxplot(x = tips_data["tip"], y = tips_data["time"])

# Dinner / Lunch tip difference
g = sns.FacetGrid(tips_data, row = "time")
g = g.map(plt.hist, "tip")
plt.show()

# <AxesSubplot:xlabel='tip', ylabel='day'>
sns.boxplot(x = tips_data["tip"], y = tips_data["day"])

g = sns.FacetGrid(tips_data, row = "day")
g = g.map(plt.hist, "tip")
plt.show()











