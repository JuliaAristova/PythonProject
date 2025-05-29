#print(help(str))

# single or double quotes
name = 'John Smith'
phrase = "Python is high-level programming language"

# string is an array
print(name[0])
for ch in name:
    print(ch, end="-")

print()

# Length
result = len(name)
print(f"Length of '{name}' = {result}")

# check smth is in / not in string - retruns Boolean
print("Smith" in name)

if "Python" in phrase:
    print("True, Python is in phrase")
if "Java" not in phrase:
    print("True, Java is not in phrase")

# find() - returns first occurrence, -1 if not found
ind = name.find(" ")
print(ind)

print(name.find('a'))           # first occurrence, -1 if not found
print(name.rfind('a'))          # last occurrence

# String modification methods:
name = name.upper();
print(name)

name = name.lower()
print(name)

name = name.capitalize()
print(name)


print(phrase.replace("Python", "Java"))

# strip - removes white spaces from the beginning and the end
word = "     Python     "
print(word)
print(word.strip())

print(phrase.split(" "))

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

# indexing - accessing elements of a sequence using [ ] (indexing operator { start : end : step ]
credit_number = '1234-5678-9012-3456'
print(credit_number[4])
# slicing
print("First 4 numbers: ", credit_number[0:4])       # end index is exclusive
print("First 4 numbers: ",credit_number[:4])         # if omitted, starts from 0 index
print(credit_number[5:9])
print(credit_number[5:])                             # to the end
print(credit_number[-1])                             # if negative - counts from the end
print(credit_number[-3:])
print(credit_number[-9:-5])
print(credit_number[::2])       # :: - only step ==> from the beginning to the end

# extract lase 4 digit of credit card number

last_four = credit_number[-4:]
print(last_four)
print(f"xxxx-xxxx-xxxx-{last_four}")

# reverse string
credit_number = credit_number[::-1]
print(credit_number)
