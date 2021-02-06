#Problem 7
#10001st prime
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def prime_number(n:int):
    """
    Calculate n-th prime number
    
    Args: index of prime number
    
    Result: n-th prime number
    """
    if n < 1: return -1
    
    if n <= 2 : return n + 1
    
    prime = 5
    
    if n == 3: return prime


    if n > 3:
        for _ in range(3,n):
            prime += 2
            if prime % 3 == 0:
                prime += 2
            while not is_prime(prime):
                prime += 2
                if prime % 3 == 0:
                    prime += 2


        
    return prime

def is_prime(number:int):
    """
    Define number prime or not
    Args: integer number
    Result: True or False
    """
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


number = input("Enter number ")
while(int(number) != 0):
    print(prime_number(int(number)))
    number = input("Enter number ")