import streamlit as st
import functions

def main():
    st.title("Encryption and Decryption Tool")
    
    text = st.text_input("Enter text to encrypt:")
    key = st.number_input("Enter encryption key (integer):", min_value=1, step=1)
    
    if st.button("Encrypt"):
        encrypted_text = functions.salt_n_encrypt(text, key)
        st.write(f"Encrypted Text: {encrypted_text}")
        
    if st.button("Decrypt"):
        decrypted_text = functions.decrypt(encrypted_text, key)
        st.write(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
