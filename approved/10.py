# Problem 10
# Summation of primes
"""Description(https://projecteuler.net/problem=10).
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million."""


def is_prime(number:int) -> bool:
    """Define number prime or not"""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if (number % 2 == 0 or number % 3 == 0) :
        return False
    i = 5
    while(i * i <= number) :
        if (number % i == 0 or number % (i + 2) == 0) :
            return False
        i = i + 6
    return True

def sum_of_primes(upper_limit: int) -> int:
    """Calculate summation of primes."""
    sum = 0 
    if upper_limit <= 1:
        return sum
    sum += 2
    if upper_limit == 2:
        return sum
    sum += 3
    if upper_limit == 3:
        return sum
    elif upper_limit >= 5:
        for i in range(5, upper_limit, 6):
            if is_prime(i):
                sum += i
            if is_prime(i + 2):
                sum += i + 2 
    return sum


if __name__ == "__main__":
    print(sum_of_primes(2000000))