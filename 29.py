# Problem 29
# Distinct powers
# Description(https://projecteuler.net/problem=29)


def is_prime(number: int) -> bool:
    """Define number prime or not"""
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


def is_divisor(number: int, divisor: int) -> bool:
    """ Define is divisor or not."""
    if number == 0 or divisor > number:
        return False
    return number % divisor == 0


def prime_divisors(number: int) -> list:
    """ Search for all prime divisors of given number."""	
    divisor = 2
    divisors = [1]
    if is_divisor(number, divisor):#divide by 2 if possible
        divisors.append(divisor)
        divisor += 1
    else: divisor += 1
    if is_divisor(number, divisor):#divide by 3 if possible
        divisors.append(divisor)
        divisor += 2
    else: divisor += 2
    while divisor <= number//2:#for all even without 3
        if is_divisor(number, divisor) and is_prime(divisor):
            divisors.append(divisor)
        if is_divisor(number, divisor + 2) and is_prime(divisor + 2):
            divisors.append(divisor + 2)
        divisor += 6
    if is_prime(number):
        divisors.append(number)
    return divisors


def is_power_of_one_base(first: int, second: int) -> bool:
    "Define is given numbers are powers of one number."
    if first * second == 0:
        return False
    if first == 1 or second == 1:
        return True
    if first > second:
        if first % second == 0 and is_power_of_one_base(first // second, second):
            return True
    else:
        if second % first == 0 and is_power_of_one_base(first, second // first):
            return True
    return False


def distinct_powers(a_min: int, a_max: int, b_min: int, b_max: int) -> int:
    """ Calculate number of distinct terms in the sequence generated by pow(a,b)."""
    if a_max < a_min or b_max < b_min:
        return -1
    number = 1
    number = (a_max - a_min) * (b_max - b_min)
    for i in range(a_min, a_max):
        if not is_prime(i):
            for j in range(a_min + i % 2, i, 2):
                if is_divisor(i, j):
                    pass
    return number


if __name__ == "__main__":
    print(is_power_of_one_base(2,-2))
    """
    for i in range(2,10):
        for j in range(2, 9):
            print(pow(i,j), end="\t")
        print()
    print(prime_divisors(15))"""
#	distinct_powers(2, 5, 2, 5)`