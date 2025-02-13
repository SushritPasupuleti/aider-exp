
import sys
from functions import salt_n_encrypt, decrypt

def main():
    user_input = input("Enter text to encrypt (no spaces): ").strip()
    
    if ' ' in user_input:
        print("Input contains spaces. Please try again.")
        return
    
    key = random.randint(1, 25)  # Generate a random key between 1 and 25
    encrypted_text = salt_n_encrypt(user_input, key)
    print(f"Encrypted text: {encrypted_text}")

if __name__ == "__main__":
    main()
