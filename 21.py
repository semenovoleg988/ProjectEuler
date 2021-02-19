# Problem 21
# Amicable numbers.
"""Description(https://projecteuler.net/problem=21).
    
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000."""


def amicable_number(number: int):
    """Calculate Amicable number for given one.
    
        Args: integer number
        Result: integer number if amicable exist or False otherwise"""
    amicable = sum_of_divisors(number)
    if amicable != number and sum_of_divisors(amicable) == number : 
        return amicable
    else: return False

def sum_of_divisors(number:int) -> int:
    """Calculate sum of divisors of given number."""
    if number < 0:
        number = -number
    if number <= 1:
        return 1
    sum_of_divisors = 1
    for divisor in range(2, int(number/2) + 1):
        if number % divisor == 0: 
            sum_of_divisors += divisor
    return sum_of_divisors


def sum_of_amicable_numbers(upper_limit:int) -> int:
    """Calculate sum of amicable numbers under given upper limit."""
    sum = 0
    list_of_amicable_numbers = []
    for number in range(upper_limit):
        if number not in list_of_amicable_numbers:
            amicable = amicable_number(number)
            if amicable:
                print(number, amicable)
                list_of_amicable_numbers.append(amicable)
                list_of_amicable_numbers.append(number)
                sum += number + amicable
                print("sum =", sum)
    return sum

if __name__ == '__main__':
    number = int(input("Enter number "))
    while(number != 0):
        print(sum_of_amicable_numbers(number))
        number = int(input("Enter number "))