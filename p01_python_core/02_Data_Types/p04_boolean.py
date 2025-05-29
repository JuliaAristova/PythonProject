'''
bool() function allows to evaluate any value and returns True or False
most values is evaluated to True if they have some sort of content
Evaluates to False:
    None - False
    bool(False)
    bool(None)
    bool(0)
    bool("")
    bool(())
    bool([])
    bool({})
'''
print(bool("Hello"))  #true
print(bool(15))       #true
a = ""
print(bool(a))      #false
print(bool(0))      #false

print(bool(2<1))

#any list, tuple, set, and dictionary are True , except empty one
print(bool(["apple", "cherry", "banana"]))

print("FALSE VALUES")
print("False", bool(False))
print("None",bool(None))
print("0",bool(0))
print('""',bool(""))
print("()",bool(()))
print("[]",bool([]))
print("{}",bool({}))

#function can return a boolean
def myFunction():
    return True

print(myFunction())

if(myFunction()):
    print("Yes")
else:
    print("No")

#built-in functions returning boolean
x = 200
print(isinstance(x, int))

print(2 == 2.)   #true


class myclass():
# # object evaluate to False if -->
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))