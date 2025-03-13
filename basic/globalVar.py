#global variables - variables created outside of a function
#can be used inside of function and outside

x = 'awesome'

def myFunction():
    print("Python is " + x)

def myFunction2():
    x = 'cool'                   #local variable with the same name
    print("Python is " + x)

def myFunction3():
    global x                    #global - to change var inside a function
    x = 'fantastic'                   #
    print("Python is " + x)


myFunction()
print(x)

myFunction2()
print(x)

myFunction3()
print(x)