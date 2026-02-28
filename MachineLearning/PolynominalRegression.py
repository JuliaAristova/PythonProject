# Polinominal Regression , like linear regression, uses the relationship
# between the variables x and y to fnd the best way to draw the line
# through the data points.
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# x arrays represent hours of the day
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y array represents the speed
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

#plt.scatter(x, y)
#plt.show()

# creating a polinominal model
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# line starts at position 1 and ends at positon 22
myline = numpy.linspace(1, 22, 100)

# draw the original scatter plot
plt.scatter(x, y)

# draw the line of polynominal regression
plt.plot(myline, mymodel(myline))

# display the diagram
plt.show()

# R-Squared - to measure the relationship between x and y (range from 0 to 1)
# 1 - 100% related, 0 - no relationship

print(r2_score(y, mymodel(x)))  # 0.94  - very good relationship

# predict future value

speed = mymodel(17)
print(speed)   # 88.87, also can read from the diagram