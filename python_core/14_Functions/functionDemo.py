# Function - a block of reusable code
# place() after the function name to invoke it

# function to print n-times

def happy_birthday():
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

happy_birthday()

def happy_birthday_personilized(name):
    print(f"Happy birthday to {name}!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

happy_birthday_personilized("Tom")

# two parameters
def happy_birthday_personilized_age(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday_personilized_age("Tom", 40)

# positional parameters
def display_invoice(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

# provided arguments should match the position
display_invoice("Tom", 42.58, "June-11-2025")