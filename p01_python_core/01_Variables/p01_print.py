'''
name = input("Enter your name: ")

print("Hello, " + name)
print("Hello,", name)
print(f"Hello, {name}")
'''
phrase = "Python"
print("Hello,", end="")
print(phrase)
print("Hello", "Pyhon", sep=" * ")

#negative number produces an empty string
print("*" + (-5)*"-" + "*"*3)