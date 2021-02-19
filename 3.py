# Problem 3
# Largest prime factor
""" Description(https://projecteuler.net/problem=3).
    
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?"""


def largest_prime_factor(number: int) -> int:
    """ Find the largest prime divisor of given number."""
    divisor = 2
    max_prime_factor = 1
    if is_devisor(number, divisor):#divide by 2 if possible
        number /= divisor
        if is_devisor(number, divisor):
            number /= divisor
            while is_devisor(number, divisor):
                number /= divisor
            divisor += 1
        else:
            max_prime_factor = divisor; divisor += 1
    else: divisor += 1
    if is_devisor(number, divisor):#divide by 3 if possible
        number /= divisor
        if is_devisor(number, divisor):
            number /= divisor
            while is_devisor(number, divisor):
                number /= divisor
            divisor += 2
        else:
            max_prime_factor = divisor; divisor += 2
    else: divisor += 2

    while divisor <= number:#for all even without 3
        if is_devisor(number, divisor):
            number /= divisor
            if is_devisor(number, divisor):
                number /= divisor
                while is_devisor(number, divisor):
                    number /= divisor
            else:
                max_prime_factor = divisor
        elif is_devisor(number, divisor + 2):
            divisor_2 = divisor + 2
            number /= divisor_2
            if is_devisor(number, divisor_2):
                number /= divisor_2
                while is_devisor(number, divisor_2):
                    number /= divisor_2
            else:
                max_prime_factor = divisor_2
        divisor += 6
    return max_prime_factor


def is_devisor(number: int, divisor: int) -> bool:
    """ Define is devisor or not."""
    if number == 0 or divisor > number:
        return False
    return number % divisor == 0


if __name__ == "__main__":
    number = input("Enter number ")
    while(int(number) != 0):
        print(largest_prime_factor(int(number)))
        number = input("Enter number ")