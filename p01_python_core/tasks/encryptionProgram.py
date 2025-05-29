import random
import string

# using constants of string module and white space
chars = " " + string.punctuation + string.digits + string.ascii_letters
#print(chars)

#casting to have a list
chars = list(chars)
# creating a copy
key = chars.copy()

#print(f"chars: {chars}")
#print(f"key  : {key}")

random.shuffle(key)

#ENCRYPTION
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message:  {plain_text}")
print(f"Enctipted message: { cipher_text}")


#DECRYPTION
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Enctipted message: { cipher_text}")
print(f"Decripted message:  {plain_text}")
