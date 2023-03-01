# Problem 20
# Factorial digit sum
"""Description(https://projecteuler.net/problem=20).

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!"""


def digits_sum(number:int) -> int:
    """Returns sum of digits in given number.
    number should be positive integer or string with positive integer"""
    number = str(number)
    sum = 0
    for i in number:
        sum += int(i)
    return sum

def factorial(n: int) -> int:
    """Returns factorial of given number.
        Arg: integer or zero."""
    if n <= 1:
        return 1
    else:
        result = 1
        for i in range(1, n):
            result *= i
        return result

def __main__():
    print(digits_sum(factorial(100)))

if __name__ == "__main__":
    __main__()