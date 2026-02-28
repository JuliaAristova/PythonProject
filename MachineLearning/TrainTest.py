# Train/Test is a method to measure the accuracy of your model
# use 80% of data for training (creating the model), 20% - for testing

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

# our data to illustrate 100 customes in a shop and their shopping habbits
# x - number of minutes before making a puchase
x = numpy.random.normal(3, 1, 100)

# y - the amount of money spent on the purchase
y = numpy.random.normal(150, 40, 100)/x
plt.scatter(x, y)
plt.show()

# split data for trainng and testing
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# display training data
plt.scatter(train_x, train_y)
plt.show()

# display testing data
plt.scatter(test_x, test_y)
plt.show()

# fit the data set

myModel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myLine = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myLine, myModel(myLine))
plt.show()
# note: the data set fitting polynominal regression, but it would give some weird results
# if we try to predict values outside of the data set --> a customer wll spent 6 mim to make a purchase worth 200 - overfitting