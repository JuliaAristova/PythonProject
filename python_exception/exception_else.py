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
