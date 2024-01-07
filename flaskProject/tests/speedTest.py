import random
import string
import hashlib
import time
from entities.optimizedHash import my_hash

seconds_to_test = 10
def test(f):
    randomString = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(1 << 24)]).encode()
    print(f"String bytes is: {len(bytes(randomString))}")
    time_start = time.time()
    completed = 0
    while time.time() - time_start < seconds_to_test:
        s = f(randomString).hexdigest()
        completed += 1
    
    print(f"Num of completed hashes in {seconds_to_test}s is: {completed}")

print("Testing SHA256:")
test(hashlib.sha256)
print("\nTesting MD5:")
test(hashlib.md5)
print("\nTesting BLAKE2:")
test(hashlib.blake2b)
print("\nTesting optimization:")
test(my_hash)