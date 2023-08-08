# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def sumOfPrimes(n):
	# list of the prime numbers
	prime = [True] * (n + 1)
	p = 2
	while p * p <= n:
		if prime[p] == True:

			i = p * 2
			while i <= n:
				prime[i] = False
				i += p
		p += 1
	sum = 0
	for i in range (2, n + 1):
		if(prime[i]):
			sum += i
	return sum

# Solution
n = 2000000
print(sumOfPrimes(n))
