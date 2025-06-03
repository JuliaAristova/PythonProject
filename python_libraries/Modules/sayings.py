def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

# to run only main is called
# when hello or goodbye are imported it won't be called

if __name__ == '__main__':
    main()