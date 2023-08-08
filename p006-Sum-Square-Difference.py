# Sum square difference
# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10^2) = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

nlist = list(range(1, 101))

sum_square = 0
for n in nlist:
    sum_square += (n ** 2)

square_sum = sum(nlist) ** 2

print(square_sum - sum_square)
