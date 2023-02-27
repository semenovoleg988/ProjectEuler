# Problem 4
# Largest palindrome product
""" Description(https://projecteuler.net/problem=4).
    
    A palindromic number reads the same both ways. The largest palindrome made from the product
    of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers."""


def largest_palindrome_product_of_two_n_digits_numbers(number_of_digits: int) -> int:
    """Find the largest palindrom made of product of two numbers with given number of digits."""
    largest = 0
    if number_of_digits <= 1:
        return 0
    n = 10**(number_of_digits - 1)
    largest_n_digits_number = n * 10 - 1
    n += 1
    for i in range(largest_n_digits_number, n, -1):
        for j in range(largest_n_digits_number, n, -1):
            if is_palindrome(i * j):
                if i * j > largest:
                    largest = i * j
                print(largest, i, j)
                n = j#this will change lower limit for j
                break
        if i < n: break
    return largest


def is_palindrome(number: int) -> bool:
    """Define is number palindrome or not."""
    number = str(number)
    for i in range(len(number)):
        if number[i] == number[len(number) - i - 1]: pass
        else: return False
    return True

if __name__ == "__main__":
    print(largest_palindrome_product_of_two_n_digits_numbers(3))