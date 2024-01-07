import hashlib
import math
import string
import random
from entities.optimizedHash import my_hash

def test(f): 
	different_bits = 0
	num_of_bits = 0
	runs = 100_000
	for i in range(runs):
		randomStr = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(20)])
		hash_object1 = f(randomStr.encode())
		hash_object2 = f((randomStr + 'a').encode())
		hashString1 = (hash_object1.hexdigest())
		hashString2 = (hash_object2.hexdigest())
		file1Binary = int(hashString1, 16)
		file2Binary = int(hashString2, 16)
	
		bits = max(math.ceil(math.log2(file1Binary)), math.ceil(math.log2(file2Binary))) 
		for x in range(0, bits):
			y = 1 << x
			num_of_bits += 1
			if (file1Binary & y) != (file2Binary & y):
				different_bits += 1
	print(f'Bits difference = {different_bits / num_of_bits}')

print("Testing SHA256:")
test(hashlib.sha256)
print("\nTesting MD5:")
test(hashlib.md5)
print("\nTesting BLAKE2:")
test(hashlib.blake2b)
print("\nTesting optimization:")
test(my_hash)