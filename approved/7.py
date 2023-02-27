#Problem 7
#10001st prime
"""Description(https://projecteuler.net/problem=7).
    
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?"""


def prime_number(n: int) -> int:
    """Calculate n-th prime number"""
    if n < 1: return -1
    if n <= 2 : return n + 1
    prime = 5
    if n == 3: return prime
    if n > 3:
        number = 5
        for _ in range(3,n):
            number += 2
            if number % 3 == 0:
                number += 2
                while not is_prime(number):
                    number += 2
                    if is_prime(number):
                        break
                    else:
                        number += 4
                prime = number
            elif number - 2 % 3 == 0:
                while not is_prime(number):
                    number += 2
                    if is_prime(number):
                        break
                    else:
                        number += 4
                prime = number
            else:#number + 2 % 3 == 0
                while not is_prime(number):
                    number += 4
                    if is_prime(number):
                        break
                    else:
                        number += 2
                prime = number
    return prime


def is_prime(number: int) -> bool:
    """Define number prime or not."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if (number % 2 == 0 or number % 3 == 0) :
        return False
    i = 5
    while(i * i <= number) :
        if (number % i == 0 or number % (i + 2) == 0) :
            return False
        i = i + 6
    return True


if __name__ == "__main__":
    number = int(input("Enter number "))    
    while(number != 0):
        print(prime_number(number))
        number = int(input("Enter number "))