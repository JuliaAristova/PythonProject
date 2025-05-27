'''
keyword arguments - an argument preceded by an identifier
    helps with readability
    order of arguments doesn't matter
1. positional
2. default
3. KEYWORD
4. arbitrary
'''



def hello(greeting, title, f_name, l_name):
    print(f"{greeting}, {title} {f_name} {l_name}")

hello("Hello", "Mr.","Spongebob", "Squarepants")

# positional (greeting)
hello("Hello", l_name= "Squarepants", f_name = "Spongebob", title ="Mr.")

for x in range (1, 6):
    print(x,  end=" ", sep="-")       #sep, end - keyword argument
print()
print("1", "2", "3", sep=" - ")

def get_phone(country, area, first, last):
    return  f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)