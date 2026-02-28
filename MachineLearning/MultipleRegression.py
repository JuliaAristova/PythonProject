# Multiple Regression is like linear regression, but with more than one independent value
# you try to predict based on 2 or more variables

import pandas   # allows to read csv files and return DataFrame object
from  sklearn import linear_model

df = pandas.read_csv("C:/Users/julia/PycharmProjects/PythonProject/python_files/data.csv")

# create a list of independent values (common name 'X')
X = df[['Weight', 'Volume']]

# create a list of dependent values (common name 'y')
y = df['CO2']

# create a linear regression object
regr = linear_model.LinearRegression()

# fit() takes independent and dependent values and
# fills the regression object with data that describes the relationship
regr.fit(X, y)

# predict CO2 emssion of a car where the weight is 2300 kg, and the colume is 1200cm3
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)

# Coefficient  - a factor that describes the relationshop with an unknown variable
# example: variable - x; 2x - unknown variable, 2 - coefficient

print (f"Coefficient: {regr.coef_}")
# result weight: 0.00755095 Volume: 0.00780526 --> if weight increase by 1 kg, the CO2 emisson increases by 0.00755095 g
# if engine size increase nu 1 cm3 --> CO2 emission encreases by 0.00780526 g

# to check
predictedCO2_2 = regr.predict([[3300, 1300]])
print(f"Predicted 2: {predictedCO2_2}")

calculated = 107.2087328 + (1000*0.00755095)
print(f"Calculated: {calculated}")
