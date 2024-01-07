import hashlib
import math
import random
import string

block_size = 1 << 15

def my_hash(b: bytes):
    hashes = bytearray()
    blocks_count = math.ceil(len(b) / block_size)
    for i in range(blocks_count):
        h = hashlib.sha256(b[i * block_size : (i + 1) * block_size ])
        hashes.extend(h.digest())
        
    return hashlib.blake2b(bytes(hashes))

if __name__ == "__main__":
    s = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(1 << 24)]).encode()
    print(my_hash(s).hexdigest())