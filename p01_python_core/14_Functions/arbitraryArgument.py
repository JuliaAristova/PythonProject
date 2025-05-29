'''
* args      - allows you to pass multiple non-key arguments
**kwargs    - allows you to pass multiple key-words arguments
        - unpacking operator

1. positional
2. default
3. keywordD
4. ARBITRARY
'''


def add(a, b):
    return a + b

print(add(1,2))

# to pass any amount of parameters
def addNum(*nums):                  # can be any name, *args is commonly used
    #print(type(args))    - tuple
    total = 0
    for num in nums:
        total += num
    return total

print(addNum(1,2,3, 4))

def display_name(*args):
    for arg in args:
        print(arg, end = ' ')

display_name("Dr.","Spongebob", "Harold", "Squarepants", "III")

print()
# kew-args

def print_address(**kwargs):
   # print(type(kwargs))         <class 'dict'>

    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street = "124 Fake St.",
              apt = "100",
              city = "Detroit",
              state = "MI",
              zip = "54321")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pbox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pbox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


print()

print("***** SHIPPING LABEL *****")
shipping_label("Dr.", "Spongebob", "Squarepants", "III",   # args
               street="124 Fake St.",                            # kwargs
               apt="100",
               city="Detroit",
               state="MI",
               zip="54321"
               )

print("***** SHIPPING LABEL *****")
shipping_label("Miss.", "Pantera", "Pink", "II",   # args
               street="12 Fake St.",                            # kwargs
               city="Detroit",
               state="MI",
               zip="54321"
               )

print("***** SHIPPING LABEL *****")
shipping_label("Mr.", "Ronald", "Mighty", "I",   # args
               street="12 Fake St.",
               pbox = "PO Box 101",
               city="Detroit",
               state="MI",
               zip="54321"
               )