import functions

def main():
    text = input("Enter text to encrypt: ")
    key = int(input("Enter encryption key (integer): "))
    
    encrypted_text = functions.salt_n_encrypt(text, key)
    print(f"Encrypted Text: {encrypted_text}")
    
    decrypted_text = functions.decrypt(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
