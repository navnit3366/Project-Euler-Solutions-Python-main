#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. 
# Find the sum of all the multiples of 3 or 5 below 1000.


def multiples(number):
    numbers_list = []
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            numbers_list.append(i)
            sum_of_numbers = sum(numbers_list)
    return sum_of_numbers
print(multiples(1000))
