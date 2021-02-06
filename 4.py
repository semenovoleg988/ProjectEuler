#Problem 4
'''
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def largest_palindrome_product_of_two_3digit_numbers():
    """
    Find largest palindrom
    Args:--
    Result: palindrome
    """
    largest = 0
    n = 100
    for i in range(999, n, -1):
        for j in range(999, n, -1):
            if is_palindrome(i*j):
                largest = i * j
                n = j
    return largest

def is_palindrome(number):
    """
    Define is number palindrome or not
    Args: number
    Result: True or False
    """
    number = str(number)

    for i in range(len(number)):
        if number[i] == number[len(number) - i - 1]: pass
        else: return False
    return True

print(largest_palindrome_product_of_two_3digit_numbers())