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
    # Hash the plaintext parameter and return its digest
    # Remove the pass statement
    pass

def run_dictionary_attack(target):
    print(f"Starting Dictionary Attack on: {target} (sha256)")
    start_time = time.time()
    
    wordlist = get_wordlist()
    
    for word in wordlist:
        # TODO
        # 1. For each word in the list, compute its hash
        # 2. Check if the digest from 1. is the same as the target hash
        # 3. Output accordingly
        # 4. Remove the pass statement
        # 5. (BONUS) Compute the total time taken
        pass
        
    print(f"\n[-] Password not found in wordlist.")
    return None

if __name__ == "__main__":
    found_password = run_dictionary_attack(TARGET_HASH)
