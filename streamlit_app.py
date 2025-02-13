import streamlit as st
from functions import salt_n_encrypt

def main():
    st.title("Encrypt Text")
    
    user_input = st.text_input("Enter text to encrypt (no spaces): ").strip()
    
    if ' ' in user_input:
        st.error("Input contains spaces. Please try again.")
        return
    
    key = random.randint(1, 25)  # Generate a random key between 1 and 25
    encrypted_text = salt_n_encrypt(user_input, key)
    st.success(f"Encrypted text: {encrypted_text}")

if __name__ == "__main__":
    main()
