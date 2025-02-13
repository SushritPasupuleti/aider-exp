from fastapi import FastAPI
import random
from functions import salt_n_encrypt, decrypt

app = FastAPI()

@app.post("/encrypt/")
def encrypt_text(text: str):
    key = random.randint(1, 25)  # Generate a random key between 1 and 25
    encrypted_text = salt_n_encrypt(text, key)
    return {"encrypted_text": encrypted_text, "key": key}

@app.post("/decrypt/")
def decrypt_text(text: str, key: int):
    decrypted_text = decrypt(text, key)
    return {"decrypted_text": decrypted_text}
