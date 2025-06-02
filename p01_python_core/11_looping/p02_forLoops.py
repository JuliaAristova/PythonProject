'''
for loops - execute a block of code a fixed number of times.
            You can iterate over a range, string, sequnce, etc.

range - start(inclusive), end(exclusive)
'''

for x in range (3):
    print(x, end=" ")
print("\n********")

# pythonic - to use underscore
for _ in range(3):
    print("meow", end=" ")

print("\n********")
for x in range(1, 11):
    print(x, end=" ")

print("\n********")

for x in reversed(range(1, 11)):
    print(x, end=" ")
print("\n********")

for x in range(1, 11, 2):
    print(x, end=" ")
print("\n********")

text = "Python"

for x in text:
    print(x, end=" ")

print("\n********")

for x in range (1, 21):
    if x == 13:
        continue
    if x == 15:
        break
    print(x, end=" ")

print("\n********")

def main():
    number = get_number()
    meow(number)
    meow(get_number())
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range (n):
        print("meow")

main()