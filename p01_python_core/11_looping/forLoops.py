'''
for loops - execute a block of code a fixed number of times.
            You can iterate over a range, string, sequnce, etc.

range - start(inclusive), end(exclusive)
'''

for x in range(1, 11):
    print(x)
print("********")

for x in reversed(range(1, 11)):
    print(x)
print("********")

for x in range(1, 11, 2):
    print(x)
print("********")

text = "Python"

for x in text:
    print(x)

print("********")

for x in range (1, 21):
    if x == 13:
        continue
    if x == 15:
        break
    print(x)