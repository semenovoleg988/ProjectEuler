#Problem 1
#Multiples of 3 and 5
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
def sum_of_multiple_of_one_of_two_numbers(first_number, second_number, upper_limit):
    """Find the sum of all the multiples of one of numbers under the upper limit.
    
        args:first and second number to multiply and the upper limit
        result:sum of multiples under the upper limit
    """
    result = 0
    result += sum_of_multiple_of_one_number(first_number, upper_limit)
    result += sum_of_multiple_of_one_number(second_number, upper_limit)
    result -= sum_of_multiple_of_two_numbers(first_number, second_number, upper_limit)
    return result

def sum_of_multiple_of_one_number(number, upper_limit):
    """Find the sum of all the multiples of one number under the upper_limit.
    
        args:first and second number to multiply and the upper limit
        result:sum of multiples under the upper limit
    """
    result = 0
    if number < upper_limit:
        for i in range(number, upper_limit, number):
            result += i
    return result

def sum_of_multiple_of_two_numbers(first_number, second_number, upper_limit):
    """Find the sum of all the multiples of two numbers under the upper limmit.
    
        args:first and second number to multiply and the upper limit
        result:sum of multiples under the upper limit
    """
    mult = first_number * second_number
    result = 0
    if mult < upper_limit:
        for i in range(mult , upper_limit , mult):
            result += i
    return result

print(sum_of_multiple_of_one_of_two_numbers(3, 5, 10))
print(sum_of_multiple_of_one_of_two_numbers(3, 5, 100))
print(sum_of_multiple_of_one_of_two_numbers(3, 5, 1000))
