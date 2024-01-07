import random
import string
import hashlib
from entities.optimizedHash import my_hash

def test(f):
	numTrials = 0
	while True:
		randomString1 = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(20)])
		randomString2 = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(20)])
		if randomString1 == randomString2: 
			continue
		else:
			hash_object_1 = f(randomString1.encode())
			hash_string_1 = hash_object_1.hexdigest()
			hash_object_2 = f(randomString2.encode())
			hash_string_2 = hash_object_2.hexdigest()
			numTrials += 1
			if (hash_string_1[0:6] == hash_string_2[0:6]):
				break

	print(f"num trials to break collision-resistant property = {numTrials}")

print("Testing SHA256:")
test(hashlib.sha256)
print("\nTesting MD5:")
test(hashlib.md5)
print("\nTesting BLAKE2:")
test(hashlib.blake2b)
print("\nTesting optimization:")
test(my_hash)