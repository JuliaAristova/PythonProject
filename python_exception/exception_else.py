'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print("**************")

try:
  print(1/0)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print("**************")
while True:
  try:
    x = int(input("What's x? "))
  except ValueError:
    print("x is not an integer")
  else:
    break
print(f"x is {x}")

#minimized version
while True:
  try:
    x = int(input("What's x? "))
    break
  except ValueError:
    print("x is not an integer")

print(f"x is {x}")

