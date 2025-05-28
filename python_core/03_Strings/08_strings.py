# name = input("Enter you full name:")
name = 'John Smith'
result = len(name)

print(result)
ind = name.find(" ")
print(ind)

print(name.find('a'))           # first occurrence, -1 if not found
print(name.rfind('a'))          # last occurrence

print("Smith" in name)

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
