import cryptography
from cryptography.fernet import Fernet

#key generation
key = Fernet.generate_key()
cipher = Fernet(key)

#plaintext, the b in front turns it into the class byte
message = b"I love nullsec"

#encryption
encrypted = cipher.encrypt(message)
print("Encrypted:", encrypted)

#decryption
decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted)

#the == behind represents base-64