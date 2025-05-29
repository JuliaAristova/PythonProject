# raise - to throw (or raise) an exception

# Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

print("Program is stopped")

# you can define error type and message
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")