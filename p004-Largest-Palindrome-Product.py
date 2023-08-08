#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

n = 0
# Two 3-digit numbers
for a in range(1000, 100, -1):
    for b in range(1000, 100, -1):
      #Product of two 3-digit numbers
        x = a * b
        #Finding the largest of the product of two 3-digit numbers
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
print(n)
