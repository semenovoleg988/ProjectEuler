# Problem 20
# Factorial digit sum
"""Description(https://projecteuler.net/problem=20).

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!"""


def Factorial_digit_sum(number:int) -> int:
    """Calculate sum of digits in factorial of given number."""
    fact = str(factorial(number))
    print(fact)
    sum = 0
    for i in fact:
        sum += int(i)
    return sum


def factorial(number:int) -> int:
    """Calculate factorial of given number."""
    if number < 1:
        return 0
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)


if __name__ == "__main__":
    print(Factorial_digit_sum(100))