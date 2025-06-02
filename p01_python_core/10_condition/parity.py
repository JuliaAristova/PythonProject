# parity - if a number is even or odd

def main():
    num = int(input("Enter your number: "))

    is_even(num)

    if is_odd(num):
        print("Number is odd")
    else:
        print("Number is even")

def is_even(num):
    print("Even" if num % 2 == 0 else "Odd")

def is_odd(num):
    # return True if num%2 ==1 else False
    return num % 2 == 1

main()