# Problem 23
# Non-abundant sums
""" Description(https://projecteuler.net/problem=23).

    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
    For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
    which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n 
    and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the 
    sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 
    can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by 
    analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant 
    numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""


import time


def propdivsum(number: int) -> int:
    """Calculate sum of prime divisors of given number.
    Prime divisors are divisors of given number without itself."""
    if number < 0:
        number = -number
    if number == 0:
        return 0
    if number == 1:
        return 1
    sum_of_divisors = 1
    if number % 2 == 0:
        for divisor in range(2, number//2 + 1):
            if number % divisor == 0:
                sum_of_divisors += divisor
    else:
        for divisor in range(3, number//2 + 1, 2):
            if number % divisor == 0:
                sum_of_divisors += divisor
    return sum_of_divisors

def abundants(n = 2123) -> list:
     
    pass


def __main__():
    """TODO: переписати алгоритм пошуку. Я написав Алгоритм знаходження всіх abundant чисел і зберіг їх в файл. Далі дістаю їх з файлу і заповнюю масив сум по два з цього файлу.
    сортую його і далі шукаю всі числа яких там немає. До 28123, бо всі числа після нього повинні бути в цьому масіві, якщо його розширити. Алгоритм пошуку треба переписати.
    """

    number = 28123
    abundants = []
    abundantssum =[]
    result = 0
    start_time = time.time()


    '''for i in range(number):
        divsum = propdivsum(i)
        if divsum > i:
            abundants.append(i)

    with open("23.txt", "w") as f:
        for i in abundants:
            f.write(str(i) + "\n")'''

    with open("23.txt", "r") as f:
        for i in f:
            if i != "":
                abundants.append(int(i))

    for i in range(len(abundants)):
        for j in range(i):
            abundantssum.append(abundants[i] + abundants[j])
    
    abundantssum.sort()
    for n in range(number):#need to improve search
        i = 0
        while abundantssum[i] <= n:
            if abundantssum[i] == n:
                flag = 1
            i += 1
        if flag == 1:
            flag = 0
        else:
            print(n)
            result += n

    print(result)
    print(time.time() - start_time)
            
if __name__ == "__main__":
    __main__()