def main():
    name = input("What's your name? ")
    #hello(name)
    print(hello(name))
'''
def hello(to="world"):
    print("Hello,", to)
'''

def hello(to="world"):
    return f"Hello, {to}"
if __name__ == '__main__':
    main()