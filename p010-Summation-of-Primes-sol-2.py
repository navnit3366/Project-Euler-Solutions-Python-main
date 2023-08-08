# This question also can be solved easily by importing eulerlib library and using prime number function:

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import eulerlib
def compute():
	ans = sum(eulerlib.list_primes(2000000))
	return str(ans)

if __name__ == "__main__":
	print(compute())
