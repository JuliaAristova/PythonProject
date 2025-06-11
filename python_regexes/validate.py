import re

email = (input("What's your email? ")).strip()

'''
if '@' in email and "." in email:
    print("Valid")
else:
    print("Invalid")

username, domain = email.split('@')

if (username) and ("." in domain):       # contains at least 1 character
    print("Valid")
else:
    print("Invalid")
 
if username and domain.endswith(".edu"):       # contains at least 1 character
    print("Valid")
else:
    print("Invalid")
    
#multiple @ will be allowed
if re.search(r"^.+@.+\.edu$", email):    # can be used..*@..*; r - raw string, \ - escape character
    print("Valid")
else:
    print("Invalid")


# only 1 @
if re.search(r"^[^@]+@[^@]+\.edu$", email):    # can be used..*@..*; r - raw string, \ - escape character
    print("Valid")
else:
    print("Invalid")
    
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):    # can be used..*@..*; r - raw string, \ - escape character
    print("Valid")
else:
    print("Invalid")


# we can use email.lower() or use a flag

if re.search(r"^\w+@\w+\.(edu|org|net|gov|com)$", email, re.IGNORECASE):    # can be used..*@..*; r - raw string, \ - escape character
    print("Valid")
else:
    print("Invalid")

'''
# for email with subdomains name@domain.subdomain.dom (\w+\.)?  - can be 0 or more time

if re.search(r"^\w+@(\w+\.)?\w*\.(edu|org|net|gov|com)$", email, re.IGNORECASE):    # can be used..*@..*; r - raw string, \ - escape character
    print("Valid")
else:
    print("Invalid")

''' browser uses this 
^
[a-zA-Z0-9.!#$%&'*+\/=?^{|}~-]+                   #username
@
[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}
[a-zA-Z0-9]?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*
 $
 '''
