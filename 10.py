#Filename:10.py

#Problem 10
#Summation of primes
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def is_prime(number:int):
    """Define number prime or not
    
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

def sum_of_primes(upper_limit):
    """Calculate summation of primes
    
        Args: max number velow wich we will look for prime numbers
        Result: sum of prime numbers
    """
    sum = 0 
    if upper_limit <= 1:
        return sum
    sum += 2
    if upper_limit == 2:
        return sum
    sum += 3
    if upper_limit == 3:
        return sum
    elif upper_limit >= 5:
        for i in range(5, upper_limit, 6):
            if is_prime(i):
                sum += i
            if is_prime(i + 2):
                sum += i + 2 
    return sum

print(sum_of_primes(2000000))