# Normal Dstribution (Gaussian Distribution)
# fits the probability of many events (IQ Scores, Hearbeat, etc.)
# 3 parameteres:
# loc - (Mean) where the pick of the bell exists
# scale - (Standard deviation) how flat the grap dstribution should be
# size - the shape of the returned array
# curve of a Normal Distribuiton = Bell Curve because od its shape
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# generate a random normal distributon of size 2x3
x = random.normal(size=(2, 3))
print(x)

# generate a random normal distributon of size 2x3 with mean at 1 and standard deviation of 2
y = random.normal(loc=1, scale=2, size=(2,3))
print(y)

sns.displot(random.normal(size=1000), kind="kde")
plt.show()