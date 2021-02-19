# Problem 1
# Multiples of 3 and 5
"""Description(https://projecteuler.net/problem=1).
   
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000."""


def sum_of_multiple_of_one_of_two_numbers(first_number: int, second_number: int, upper_limit: int) -> int:
    """Find the sum of all the multiples of one of numbers under the upper limit.
    
        Args: first and second number to multiply and the upper limit
        Result: sum of multiples under the upper limit"""
    if upper_limit < min(first_number, second_number):
        return 0
    if upper_limit < 0:
        upper_limit -= upper_limit
    result = sum_of_multiple_of_one_number(first_number, upper_limit)
    result += sum_of_multiple_of_one_number(second_number, upper_limit)
    result -= sum_of_multiple_of_two_numbers(first_number, second_number, upper_limit)
    return int(result)


def sum_of_multiple_of_one_number(number: int, upper_limit: int) -> int:
    """Find the sum of all the multiples of one number under the upper limit.
    
        Args:first and second number to multiply and the upper limit
        Result:sum of multiples under the upper limit"""
    if number < upper_limit:
        n = upper_limit // number
        return int(number * (n * (n + 1) / 2))
    else: return 0

def sum_of_multiple_of_two_numbers(first_number: int, second_number: int, upper_limit: int) -> int:
    """Find the sum of all the multiples of two numbers under the upper limmit.
    
        Args:first and second number to multiply and the upper limit
        Result:sum of multiples under the upper limit"""
    mult = first_number * second_number
    if mult <= upper_limit:
        n = upper_limit // mult
        return int(mult * (n * (n + 1) / 2))
    else: return 0


if __name__ == "__main__":
    print(sum_of_multiple_of_one_of_two_numbers(3, 5, 10))
    print(sum_of_multiple_of_one_of_two_numbers(3, 5, 100))
    print(sum_of_multiple_of_one_of_two_numbers(3, 5, 1000))
