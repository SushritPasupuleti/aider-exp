import unittest
from functions import salt_n_encrypt, decrypt

class TestFunctions(unittest.TestCase):
    def test_encryption_decryption(self):
        text = "hello"
        key = 3
        encrypted_text = salt_n_encrypt(text, key)
        decrypted_text = decrypt(encrypted_text, key)
        self.assertEqual(decrypted_text, text)

if __name__ == "__main__":
    unittest.main()
