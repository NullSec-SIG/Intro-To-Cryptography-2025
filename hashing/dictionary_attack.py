import hashlib
import time

# The hash we want to crack. 
TARGET_HASH = "c2ba33409c75f19fb24fd8b6a6f4c62b9bf717015cd9ae609b974d54144d1898"

def get_wordlist():
    try:
        with open("100k-most-used-passwords-NCSC.txt", "r") as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print("[-] File not found.")

def hash_password(plaintext):
    return hashlib.sha256(plaintext.encode('utf-8')).hexdigest()

def run_dictionary_attack(target):
    print(f"[*] Starting Dictionary Attack on: {target} (sha256)")
    start_time = time.time()
    
    wordlist = get_wordlist()
    
    for word in wordlist:
        
        computed_hash = hash_password(word)
        
        if computed_hash == target:
            end_time = time.time()
            print(f"\n[+] PASSWORD FOUND: {word}")
            print(f"[*] Time elapsed: {end_time - start_time:.4f} seconds")
            return word
            
    print(f"\n[-] Password not found in wordlist.")
    return None

if __name__ == "__main__":
    found_password = run_dictionary_attack(TARGET_HASH)
