# We can scale data into new values that are easier to compare
# it can be difficult to compare volume with weight, but if we scale them both
# into comparable values, we can see how much one value is compared to the other.

# Standardization - one of the method to scale the data
# z = (x -  u) / s
# x - original value, u - mean, s - standard deviation, z - new value

# weight: (790 - 1292.23) / 238.74 = -2.1
# volume: (1.0 - 1.61) / 0.38 =  1.59
# we compare -2.1 with 1.59 instead of 790 kg and 1.0 l
# StandardScaler() - returns Scaler object with methods for transforming data sets

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv("C:/Users/julia/PycharmProjects/PythonProject/python_files/data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)
print(scaledX)

# predict CO2 emission from 1.3 l car that weighs 2300 kg

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
