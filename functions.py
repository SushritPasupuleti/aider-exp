import random

def salt_n_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + key)

    return encrypted_text

def decrypt(text, key):
    decrypted_text = ""
    for char in text[:-2]:
        decrypted_text += chr(ord(char) - key)

    return decrypted_text
