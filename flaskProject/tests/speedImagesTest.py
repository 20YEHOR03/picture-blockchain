import os
import time
import hashlib
from entities.optimizedHash import my_hash

def test(h):
    time_start = time.time()
    for filename in os.listdir(os.getcwd() + "\\images"):
        with open(os.path.join(os.getcwd() + "\\images", filename), 'rb') as f:
            data = f.read()
            hash_data = h(data).hexdigest()
    time_elapsed = time.time() - time_start
    print(f"Elapsed time of hashing all images is {time_elapsed} seconds")

for filename in os.listdir(os.getcwd() + "\\images"):
    with open(os.path.join(os.getcwd() + "\\images", filename), 'rb') as f:
        continue
    
print("Testing SHA256:")
test(hashlib.sha256)
print("\nTesting MD5:")
test(hashlib.md5)
print("\nTesting BLAKE2:")
test(hashlib.blake2b)
print("\nTesting optimization:")
test(my_hash)