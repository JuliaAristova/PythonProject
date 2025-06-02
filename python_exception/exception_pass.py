def get_int():
    while True:
        try:
            return int(input("What's x? "))  # breaks the loop and return value
        except ValueError:
            print("x is not an integer")

def get_int_pass(prompt):
    while True:
        try:
            return int(input(prompt))  # breaks the loop and return value
        except ValueError:
            pass

def main():
    print("Main method")
    x = get_int()
    print(f"x is {x}")

    print("*************")

    x = get_int_pass("Enter an integer: ")
    print(f"Number you entered is {x}")

main()

