# Regression - you try to find the relationship between variables
# in ML / Statistic  to predict the outcome of the future event

# Linear regression uses the relationship between the data-points to draw a straight line through all them

import matplotlib.pyplot as plt
from scipy import stats

# x represents age
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

# y represents speed
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#plt.scatter(x, y)
#plt.show()

# execute a method that returns some important key values of Linear Regression
slope, intercept, r, p, str_err = stats.linregress(x, y)

# create a function that uses the slope and intercept values to return a new value
# where on the y-axos tje corresponding x-value will be placed
def myfunc(x):
    return  slope * x + intercept

# run function for each value of the x array
# will result in a new array with new values for the y-axis
mymodel = list(map(myfunc, x))

# draw the original scatter plot
plt.scatter(x, y)

# draw the lne of linear regression
plt.plot(x, mymodel)

# display the diagram
plt.show()

# r - coefficient of correlation (between x and y)
# range -1 to 1; 0 - no relationship; 1 (-1) - 100% related
# compute by Python and Scipy module

print(r)  # -0.76 - not perfect, but we could use linear regression in future predictions

# Predict future value

speed = myfunc(10)
print(speed)    # 85.6, also could read it from the diagram