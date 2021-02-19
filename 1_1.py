# Problem 1
# Multiples of 3 and 5
"""Description(https://projecteuler.net/problem=1).
   
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000."""


def sum_of_multiple_of_3_or_5(upper_limit: int) -> int:
    """Find the sum of all the multiples of 3 or 5.
        
        Args:the upper limit
        Result:sum of multiples"""
    if 0 < upper_limit and upper_limit < 3:
        return 0
    if upper_limit < 0:
        upper_limit = -upper_limit
    result = sum_of_multiple_of_3(upper_limit) + sum_of_multiple_of_5(upper_limit)
    result -= sum_of_multiple_of_3_and_5(upper_limit)
    return result


def sum_of_multiple_of_3(upper_limit: int) -> int:
    """Find the sum of all the multiples of 3.
        
        Args:the upper limit
        Result:sum of multiples"""
    n = upper_limit // 3
    result = 3 * (n * (n + 1) / 2)
    return result


def sum_of_multiple_of_5(upper_limit: int) -> int:
    """Find the sum of all the multiples of 5.
        
        Args:the upper limit
        Result:sum of multiples"""
    if 5 <= upper_limit:
        n = upper_limit // 5
        return 5 * (n * (n + 1) / 2)
    else: return 0


def sum_of_multiple_of_3_and_5(upper_limit: int) -> int:
    """Find the sum of all the multiples of 5
        Args:the upper limit
        Result:sum of multiples"""
    if 15 <= upper_limit:
        n = upper_limit // 15
        return 15 * (n * (n + 1) / 2)
    return 0


if __name__ == "__main__":
    print("The sum of all the multiples of 3 or 5 below 1000.", sum_of_multiple_of_3_or_5(999))
