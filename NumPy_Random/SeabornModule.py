# Seaborn is a library that uses Matplotlib underneath to plot graphs

# displots = distribution plot.
# input - array
# plots a urve corresponding to the distribution of points in the array

import matplotlib.pyplot as plt
import seaborn as sns

# plotting a displot
sns.displot([0, 1, 2, 3, 4, 5])
plt.show()

# plotting a displot without the Histogram
sns.displot([0, 1, 2, 3, 4, 5], kind = "kde")
plt.show()