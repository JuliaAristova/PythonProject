import sys

#print string - can be in single & double quotes

print('Hello World!')
print()
print("Hello Python!")

#inserting new line  \n  --> to start a new output line
print("The itsy bitsy spider\nclimbed up the waterspout.")
#print("\")  --> error
print("\\")
print(sys.version)

'''
multiline comment
indentation in python is important
Python uses indentation to indicate a block of code.
'''
if(5 > 3):
    print("Five is greater than three")

print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")
print()
print("Down came the rain\tand washed the spider out.")
print()
print("Down came the rain\n\tnand washed the spider out.")

'''
print with multiple arguments

a print() function invoked with more than one argument outputs them all on one line;
the print() function puts a space between the outputted arguments on its own initiative.

the positional way - the argument is dictated by its position,
 e.g., the second argument will be outputted after the first, not the other way round
 
keyword arguments. The name stems from the fact that the meaning of these arguments is taken not from its location (position) but from the special word (keyword) used to identify them.

The print() function has two keyword arguments. The first of them is named end.

any keyword arguments have to be put after the last positional argument (this is very important)
'''
print()
print("The itsy bitsy spider", "climbed up", "the waterspout.")
print()

#default  end="\n"
print("My name is", "Python.", end=" ")
print("Monty Python.")
print("My name is ", end="")   #space after 'is'
print("Monty Python.")

#separator sep="-"
print()
print("My", "name", "is", "Monty", "Python.", sep="-")

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print('0----')
print(' ||||')
print('*' * 10)