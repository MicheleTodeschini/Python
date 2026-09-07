import random
import string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()

random.shuffle(key)

#ENCRYPT

plain_text = input("Enter the massage to encrypt: ")
cipher_text = ""

for letter in plain_text:
    i = chars.index(letter)
    cipher_text += key[i]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

#DECRYPT

for letter in cipher_text:
    i = key.index(letter)
    cipher_text += key[i]