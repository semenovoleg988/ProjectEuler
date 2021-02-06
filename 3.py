# Filename: 3.py
# Problem 3
# Largest prime factor
''' Largest prime factor.
    
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?'''

def largest_prime_factor(number, max_prime_factor=1):
    """ Find the largest divisor

        Args: 
        Result:"""
    divisor = 2                                             #loop for 2
    if is_devisor(number, divisor):
        number /= divisor
        if is_devisor(number, divisor):
            number /= divisor
            while is_devisor(number, divisor):
                number /= divisor
            divisor += 1
        else:   max_prime_factor = divisor; divisor += 1
    else: divisor += 1

    while divisor <= number:                                #for all even less than number
        if is_devisor(number, divisor):
            number /= divisor
            if is_devisor(number, divisor):
                number /= divisor
                while is_devisor(number, divisor):
                    number /= divisor
                divisor += 1
            else:   max_prime_factor = divisor; divisor += 2
        else: divisor += 2
    return max_prime_factor

def is_devisor(number:int, divisor:int):
    """ Define is devisor or not.
        
        Args: numver to devid and devisor
        Result: True or False"""
    if number == 0:             return False
    elif number % divisor == 0: return True
    else:                       return False


number = input("Enter number ")
while(int(number) != 0):
    print(largest_prime_factor(int(number)))
    number = input("Enter number ")