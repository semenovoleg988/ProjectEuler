# Problem 21
# Amicable numbers.
"""Description(https://projecteuler.net/problem=21).
    
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000."""


def sum_of_proper_divisors(number: int) -> int:
    """Calculate sum of prime divisors of given number.
    Prime divisors are divisors of given number without itself."""
    if number < 0:
        number = -number
    if number == 0:
        return 0
    if number == 1:
        return 1
    sum_of_divisors = 1
    for divisor in range(2, number//2 + 1):
        if number % divisor == 0: 
            sum_of_divisors += divisor
    return sum_of_divisors


def __main__():
    max_number = 10000
    l = [0] * (max_number + 1) #list of sum of proper divisors 
    sum_of_amicable = 0
    for i in range(max_number + 1):
        l[i] = sum_of_proper_divisors(i)
    
    for i in range(max_number + 1):
        if l[i] < i and l[l[i]] == i:
            sum_of_amicable += l[i] +l[l[i]]
    
    print("Sum of amicable numbers under {} is {}.".format(max_number, sum_of_amicable))

if __name__ == '__main__':
    __main__()