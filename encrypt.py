from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom
import base64

def encrypt_data(key:bytes,plaintext:str) -> str:
  iv = urandom(16)

  cipher = Cipher(algorithms.AE5(key), modes.CFB(iv), backend=default_backend())
  encryptor = cipher.encryptor()

  ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
  return base64.b64encode(iv + ciphertext).decode('utf-8')

key = urandom(32)
plaintext=input("Text to encrypt?\n")
encrypted_data = encrypt_data(key,plaintext)
print(f"Encrypted: {encrypted_data}"
