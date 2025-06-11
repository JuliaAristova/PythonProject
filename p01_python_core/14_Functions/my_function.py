from datetime import datetime


def main():
    hello()
    name = input("What is your name? ")
    hello(name)

    show_date()

    print(add(11.24, 45.89))

def hello(to='world'):
    print("Hello,", to)


def show_date() -> None:
    print('This is the current date and time:')
    print(datetime.now())

def add(a: float, b: float) -> float:
    return a + b

if __name__ == '__main__':
    main()
