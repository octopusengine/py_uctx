#!/usr/bin/env python3
#$ pip install cryptography

from cryptography.fernet import Fernet

input_file = "data/nostr1b.txt"

key = Fernet.generate_key()
print("key",key)

cipher_suite = Fernet(key)

# plaintext = "This is the text I want to encrypt."
with open(input_file, "r", encoding="utf-8") as file:
    #text = file.read().replace("\n", " ")
    plaintext = file.read()

ciphertext = cipher_suite.encrypt(plaintext.encode())
encrypted_text = ciphertext.decode()

print("-"*39)
print("Encrypted text:", encrypted_text)
print(len(encrypted_text))

print("-"*39)
decrypted_text = cipher_suite.decrypt(ciphertext).decode()
print("Original text:", decrypted_text)
print(len(decrypted_text))
