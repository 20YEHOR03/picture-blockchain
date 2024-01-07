import random
import string
import hashlib
from entities.optimizedHash import my_hash

def test(f):
    HASH_VALUE = ''.join([random.choice("0123456789abcdef") for n in range(6)])
    numTrials = 0
    while True:
        randomStr = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(20)])
        hash_object = f(randomStr.encode())
        hash_string = hash_object.hexdigest()
        numTrials += 1
        if hash_string[0:6] == HASH_VALUE:
            break
    print(f"num trials to break one-way property = {numTrials}")

print("Testing SHA256:")
test(hashlib.sha256)
print("\nTesting MD5:")
test(hashlib.md5)
print("\nTesting BLAKE2:")
test(hashlib.blake2b)
print("\nTesting optimization:")
test(my_hash)