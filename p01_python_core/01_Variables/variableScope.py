'''
variable scope - where a variable is visible and accessible
scope resolution - (LEGB) Local --> Enclosed --> Global --> Built-in
'''
from math import e

print("***** Local var *****")

def func1():
    x = 1                       # local to func1
    print(x)

def func2():
    x = 2                       # local to func2
    print(x)

func1()
func2()


print("***** Local & Enclosed var *****")
x = 1111
def func3():
    x = 2222
    def func4():
        x = 3333
        print(x)
    def func5():
        print(x)                # enclosed
    func4()
    func5()

func3()

print("***** Local & Global var *****")
y = 333                         # global

def func6():
    print(y)

def func7():
    y=777
    print(y)

func6()
func7()

print("***** Import constant & Global var *****")
def func8():
    print(e)            # built-in (math module)

func8()

e = 4                   # e - global
func8()                 # will print global e

print("***** Creating global inside function *****")

def func9():
    global s
    s = "Python"
    print(s)

func9()
print(f"variable {s} created in function")

s2 = 'awesome'
def myfunc():
  global s2
  s2 = 'fantastic'

print('Python is ' + s2)
myfunc()
print('Python is ' + s2)
print(s2)