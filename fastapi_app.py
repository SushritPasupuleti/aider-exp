from fastapi import FastAPI
import functions

app = FastAPI()

@app.post("/encrypt/")
def encrypt(text: str, key: int):
    encrypted_text = functions.salt_n_encrypt(text, key)
    return {"encrypted_text": encrypted_text}

@app.post("/decrypt/")
def decrypt(encrypted_text: str, key: int):
    decrypted_text = functions.decrypt(encrypted_text, key)
    return {"decrypted_text": decrypted_text}
