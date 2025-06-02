'''
Exception - an event that interrupts the flow of a program
    (ZeroDivisionError, TypeError, ValueError)
    1. try          1/0
    2. except       1 + '1'
    3. finally      int("pizza")
'''

# user input - dangerous code
'''
not good practice:
try:
    number = int(input("Enter a number (not 0): "))
    print(1/number)
except Exception:
    print("Something went wrong!")

'''
# print("hello, world)  - SyntaxError - must be fixed

try:
    number = int(input("Enter a number (not 0): "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("You did not enter a number")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some clean up here")    # always executed if there is an exception or not