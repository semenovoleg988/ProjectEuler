#Problem 12 #FIXME
#Highly divisible triangular number
"""Description(https://projecteuler.net/problem=12).

    The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number
    would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 

    The first ten terms would be:   1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.
    What is the value of the first triangle number to have over five hundred divisors?"""


def next_triangular(number_of_triangular:int, previous_triangular:int):
    """Calculate next triangular number
    
        Args: index of triangular to find
        Result: triangular number"""
    return previous_triangular + number_of_triangular

def number_of_divisors(number:int):
    """Calculate number of divisors of given number
    
        Args: integer number
        Result: number of divisors"""
    if number < 1: return 0
    elif number == 1: return 1
    else: return sum_of_non_zero_incom(all_divisors(prime_divisors(number)))

def sum_of_non_zero_incom(array):
    """Calculate number of non zero income in array
    
        Args: array of numbers
        Result: integer number of non zero income"""
    sum = 0
    for i in array:
        if array[i] > 0:
            sum += array[i]
    return sum   

def all_divisors(parameter_list):#FIXME
    """Calculate number of combinations of numbers."""
    return None

def prime_divisors(number:int):
    """Calculate all prime divisors of given number
    
        Args: number
        Result: list of income in number(divisors bond with index of list elements)"""
    divisors = [0, 1, 0, 0]
    
    if number == 0:
        divisors[0] = 1 
        divisors[1] = 0
        return divisors

    for divisor in (2, 3):
        while is_devisor(divisor, number):
            number /= divisor
            divisors[divisor] += 1

    i = 5
    while number != 1:
        divisors.append(0, 0, 0, 0)
        for divisor in (i, i + 2):
            while is_devisor(divisor, number):
                number /= divisor
                divisors[divisor] += 1
        i += 6
    return divisors

def is_devisor(number: int, divisor: int) -> bool:
    """ Define is devisor or not."""
    if number == 0 or divisor > number:
        return False
    return number % divisor == 0


def Highly_divisible_triangular(number_of_divisors:int):
    """Calculate first triangular number, wich has over given number of divisors
    
        Args: minimum number of divisors
        Result: the first triangle number to have over five hundred divisors"""
    pass

if __name__ == "__main__":
    for divisors in range(1, 5):
        print(Highly_divisible_triangular(divisors))