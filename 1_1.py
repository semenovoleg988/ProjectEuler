#Problem 1
#Multiples of 3 and 5
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiple_of_3_or_5(upper_limit):
    """
    Find the sum of all the multiples of 3 or 5
    args:the upper limit
    result:sum of multiples
    """
    result = 0
    result += sum_of_multiple_of_3(upper_limit) + sum_of_multiple_of_5(upper_limit)
    result -= sum_of_multiple_of_3_and_5(upper_limit)
    return result

def sum_of_multiple_of_3(upper_limit):
    """
    Find the sum of all the multiples of 3
    args:the upper limit
    result:sum of multiples
    """
    result = 0
    for i in range(3 , upper_limit , 3):
        result += i
    return result

def sum_of_multiple_of_5(upper_limit):
    """
    Find the sum of all the multiples of 5
    args:the upper limit
    result:sum of multiples
    """
    result = 0
    for i in range(5 , upper_limit , 5):
        result += i
    return result

def sum_of_multiple_of_3_and_5(upper_limit):
    """
    Find the sum of all the multiples of 5
    args:the upper limit
    result:sum of multiples
    """
    result = 0
    if 15 < upper_limit:
        for i in range(15 , upper_limit , 15):
            result += i
    return result

print(sum_of_multiple_of_3_or_5(1000))
