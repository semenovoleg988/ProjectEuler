# Problem 5
# Smallest multiple
""" Description(https://projecteuler.net/problem=5).

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


def smallest_multiple_of_all_of_the_numbers_under_given(number: int) -> int:
    """Calculate smallest number that can be divided by each of the numbers under given one."""
    smallest_multiple = number
    for i in range(1, number):
        if not is_devisor(smallest_multiple, i):
            smallest_multiple *= int(i / gcd(smallest_multiple, i))
    return smallest_multiple


def gcd(a: int, b: int) -> int:
    """Calculete Greatest Common Divisor for two integer numbers."""
    while b:
        (a, b) = (b, a % b)
    return a 


def is_devisor(number: int, divisor: int) -> bool:
    """ Define is devisor or not."""
    if number == 0 or divisor > number:
        return False
    return number % divisor == 0


if __name__ == "__main__":
    print(smallest_multiple_of_all_of_the_numbers_under_given(20))