import re

# clean user's input
'''
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)   # groups - what is in () will be returned

if matches:
    #last, first = matches.groups()
    #name = f"{first} {last}"
    #last = matches.group(1)
    #first = matches.group(2)
    #name = f"{first} {last}"
    name = matches.group(2)+ " " + matches.group(1)

print(f"Hello, {name}")

'''
name = input("What's your name? ").strip()

# := assign and ask for boolean (walrus operator)
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2)+ " " + matches.group(1)

print(f"Hello, {name}")