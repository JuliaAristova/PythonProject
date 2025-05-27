# return - statement used to end a function and send a result
#          back to the caller


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def add(n1, n2):
    return n1 + n2

z = add(1, 2)
print(z)

print(subtract(4, 9))
print(multiply(3, 8))
print(divide(9, 3))

def full_name(fName, lName):
    return fName.capitalize() + " " + lName.capitalize()

print(full_name("tom", "smith"))