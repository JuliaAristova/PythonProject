# name = input("Enter you full name:")
name = 'John Smith'
result = len(name)

print(result)
ind = name.find(" ")
print(ind)

print(name.find('a'))           # first occurence, -1 if none found
print(name.rfind('a'))          # last occurence

name = name.upper();
print(name)

name = name.lower()
print(name)

name = name.capitalize()
print(name)

# phone = input("Enter you phone number: ")
phone = '571-431-2481'
isDigit = phone.isdigit()

print(isDigit)

isChars = phone.isalpha()
print(isChars)

result = phone.count("-")
print(result)

phone = phone.replace("-", "")
print(phone.isdigit())

#print(help(str))

# indexing - accessing elements of a sequence using [ ] (indexing operator { start : end : step ]

credit_number = '1234-5678-9012-3456'
print(credit_number[4])
print(credit_number[0:4])       # end index is exclusive
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::2])       # :: - only step ==> from the beginning to the end

# extract lase 4 digit of credit card number

last_four = credit_number[-4:]
print(last_four)
print(f"xxxx-xxxx-xxxx-{last_four}")

# reverse string
credit_number = credit_number[::-1]
print(credit_number)

# Format specifier - {:flag} format a value based on what flags are inserted
'''
.(number)f  = round to that many decimal places (fixed pont)
:(number)   = allocate that many spaces
:03         = allocate and zero pad that many spaces
:<          = left justify
:>          = right justify
:^          = center align
:+          = use a plus sugn to indicate positive value
:=          = place sign to leftmost position
:           = insert a space before positive numbers
:,          = comma separator
'''

price1 = 3000.12159
price2 = -9870.65
price3 = 1200.34

print(f"price1 is ${price1:.2f}")
print(f"price2 is ${price2:.1f}")
print(f"price2 is ${price2:.2f}")
print(f"price2 is ${price2:.3f}")
print(f"price3 is ${price3:.2f}")
print(f"price3 is ${price3:10}")            # allocated 10 spaces to display the price

print(f"price1 is ${price1:012}")
print(f"price1 is ${price2:012}")
print(f"price3 is ${price3:012}")

print(f"price1 is ${price1:>12}")
print(f"price1 is ${price2:>12}")
print(f"price3 is ${price3:>12}")

print(f"price1 is ${price1:<12}")
print(f"price1 is ${price2:<12}")
print(f"price3 is ${price3:<12}")

print(f"price1 is ${price1:^12}")
print(f"price1 is ${price2:^12}")
print(f"price3 is ${price3:^12}")

print(f"price1 is ${price1:+}")
print(f"price1 is ${price2:+}")
print(f"price3 is ${price3:+}")

print(f"price1 is ${price1: }")
print(f"price1 is ${price2: }")
print(f"price3 is ${price3: }")

print(f"price1 is ${price1:,}")
print(f"price1 is ${price2:,}")
print(f"price3 is ${price3:,}")

#mixing
print(f"price1 is ${price1:+,.2f}")
print(f"price1 is ${price2:+,.2f}")
print(f"price3 is ${price3:+,.2f}")