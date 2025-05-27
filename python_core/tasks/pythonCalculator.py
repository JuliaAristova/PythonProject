# Python Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator  (+, -, *, /): ")

if(operator == '+'):
    print(num1 + num2)
elif(operator == '-'):
    print(num1 - num2)
elif(operator == '/'):
    if(num2 == 0):
        print("Cannot divide by 0")
    else:
        print(num1/num2)
elif(operator == '*'):
    print(num1*num2)
else:
    print("Wrong operator")

