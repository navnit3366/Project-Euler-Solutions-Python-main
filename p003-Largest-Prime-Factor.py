#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math

# Finding Largest Prime Factor

def maxPrimeFactors (n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
            
    if n > 2:
        maxPrime = n
    return int(maxPrime)

# Largest prime factor of the number 60085147514
  
n = 600851475143
print(maxPrimeFactors(n))
