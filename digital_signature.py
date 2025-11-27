from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

#1. Generate a key pair using RSA
private_key = rsa.generate_private_key(
    #Why are we using 65537 here?
    #65537 is used because its a large prime number, and 65537 = 2^16 + 1 
    #So why is this important? Why not use the prime number 3?
    public_exponent=65537,
    key_size=2048 #in bits
)

#Generate the public key using RSA also
public_key = private_key.public_key()

#2. Message to be signed
message = b"This document is officially approved."

#3. Sign the message (using private key)
signature = private_key.sign(
    message,
    #The padding.PSS(takes in )
    padding.PSS(
        #a mask-generation function that uses SHA-256 as its internal hash
        mgf=padding.MGF1(hashes.SHA256()),
        #uses the maximum allowable salt length
        #Why do we need salting?
        #Salting prevents deterministic signatures and certain attack classes by introducing randomness
        #This also makes it so if 2 signatures of the same messages will produce different bytes
        salt_length=padding.PSS.MAX_LENGTH
    ),
    #hash algorithm used to hash the message before signing
    hashes.SHA256()
)

#Displays the signature in hex
print("Signature:", signature.hex())
message = b"This document is FAKE"
#4. Verify the signature (using public key)
try:
    #.verify takes in 4 parameters, the digital signature, the message, the mask-generation function and the hashes.
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ Signature is VALID. Message is authentic.")
except:
    print("❌ Signature is INVALID. Message has been altered or sender is fake.")