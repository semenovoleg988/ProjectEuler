# Problem 25
# 1000-digit Fibonacci number
""" Description(https://projecteuler.net/problem=25).

    The Fibonacci sequence is defined by the recurrence relation: Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""

def n_digit_Fibonacci_number(number_of_digits: int) -> int:
    """ Calculate the index of the first term in the Fibonacci sequence to contain given number of digits."""
    first = 1
    second = 1
    if number_of_digits == 1:
        return 1
    else:
        i = 3
        number = first + second
        while len(str(number)) != number_of_digits:
            first = second
            second = number
            number = first + second
            i += 1
        return i


if __name__ == "__main__":
    print(n_digit_Fibonacci_number(1000))