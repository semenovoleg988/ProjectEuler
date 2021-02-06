#Problem 6
#Sum square difference
'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_square_difference(last_number: int):
    """
    docstring
    """
    return square_of_sum(last_number) - sum_of_squares(last_number)

def sum_of_squares(last_number: int):
    """
    docstring
    """
    n = last_number

    sum = n * (n + 1) * (2*n + 1) / 6
    
    sum = int(sum)

    return sum

def square_of_sum(last_number: int):
    """
    Calculate square of sum of the Terms of an Arithmetic Sequence
    
    Args: last number of Sequence
    
    Result: square of sum of Arithmetical Sequence
    """

    sum =  sum_of_arithmetical_sequence(1, last_number) 

    return sum**2

def sum_of_arithmetical_sequence(first_number: int, last_number: int):
    """
    Calculate Sum of the Terms of an Arithmetic Sequence (Arithmetic Series)
    
    Args: first and last number of sequence
    
    Result: sum of the first n terms of an arithmetic sequence
    """
    n = last_number - first_number + 1

    return int(n * (first_number + last_number) / 2) 

print(sum_of_arithmetical_sequence(1, 100))