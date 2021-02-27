# Problem 30
# Digit fifth powers
# Description(https://projecteuler.net/problem=30)


def is_digit_power(number: int, power: int, flag = 0):
    """ Calculate doesor given number or transposition of its digits equal to sum of its digits in given power."""
    sum = 0
    for n in str(number):
        sum += pow(int(n), power)
    if sum == int(number):
        return sum
    if not flag and is_digit_power(sum, power, 1):
        return sum
    return False


def is_ascending(number: int) -> bool:
    """ Calculate does digits in given number are ascending."""
    number = str(number)
    for i in range(1,len(number)):
        if number[i] < number[i-1]:
            return False
    return True


def digit_powers_sum(power: int) -> int:
    """ Calculate sum of number equal to given power of its digits."""
    magic = 0
    max_number_of_digits = 1
    i = 0
    while True:
        magic += 9 * (pow(9, power - 1) - pow(10,i))
        if magic < 0: 
            max_number_of_digits += 1
            break
        else:
            max_number_of_digits += 1
            i += 1
    list_of_numbers = []
    for x in [i for i in range(2, 10**max_number_of_digits) if is_ascending(i)]:
        temp = is_digit_power(x, power)
        if temp and not temp in list_of_numbers:
            list_of_numbers.append(temp)
    return sum(list_of_numbers)


if __name__ == "__main__":
    print(digit_powers_sum(5))