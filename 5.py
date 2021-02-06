#Problem 5
'''
Smallest multiple 

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def smallest_multiple_of_all_of_the_numbers_under(number):
    """
    Calculate smallest number that can be divided by each of the numbers under given one
    
    Args: integer number
    
    Result: integer number  
    """
    smallest_multiple = number

    for i in range(1, number):
    
        if not is_devisor(smallest_multiple, i):
    
            smallest_multiple *= int(i / gcd(smallest_multiple, i))
    
    return smallest_multiple

def gcd(a, b):
    """
    Calculete Greatest Common Divisor for two numbers

    Args: two numbers
    
    Result: Greatest Common Divisor
    """
    while b:

        (a, b) = (b, a % b)
    
    return a 

def is_devisor(number, divisor):
    """
    Define is devisor or not
    
    Args: numver to devid and devisor
    
    Result: True or False
    """
    if number == 0:             return False
    elif number % divisor == 0: return True
    else:                       return False

print(smallest_multiple_of_all_of_the_numbers_under(10))