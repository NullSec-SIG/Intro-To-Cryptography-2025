import hashlib

# another way to turn a string into bytes, is with .encode() 
password = "hello123".encode()
hash = hashlib.sha256(password).hexdigest()

# hashing with another password
password2 = b"hello124"
hash2 = hashlib.sha256(password2).hexdigest()

print("=============================First Hash=======================================")
print("Password:", password)
print("Hash:",hash)
print("=============================Second Hash======================================")
print("Password:",password2)
print("Hash:",hash2)
print("==============================================================================")
