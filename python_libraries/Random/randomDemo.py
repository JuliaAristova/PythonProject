import random

#print(help(random))

# Random Integer
num = random.randint(1, 6)   # inclusive

print(num)

low = 1
high = 100
num2 = random.randint(low, high)
print(num2)

# Radom Float
num3 = random.random()  # 0 - 1
print(num3)

options = ('rock', 'paper', 'scissors')
option = random.choice(options)

print(option)
print("------------------")
for n in range(0, 5):
    option = random.choice(options)
    print(option)
    n +=1

print("------------------")

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(cards)

print("------------------")

random.choice(["heads", "tails"])