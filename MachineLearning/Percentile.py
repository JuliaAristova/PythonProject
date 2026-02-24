# Percentile is used in statistic to give you a number that describes
# the vale that a given percent of the values are lower than

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# 75 percentile  - 43 - 75% of people are 43 or younger
perc75 = numpy.percentile(ages, 75)
print(perc75)

# 90% of people younger than perc90 - age 61
perc90 = numpy.percentile(ages, 90)
print(perc90)