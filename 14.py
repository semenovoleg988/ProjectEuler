#Filename:14.py
#Problem 14
#Longest Collatz sequence
'''
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def Collatz_sequence_len(starting_point:int):
    """
    Calculate len of a Collatz sequence with given starting point
    Args: starting point
    Result: len
    """
    point = starting_point
    len = 1
    while point != 1:
        if point % 2 == 0:
            point /= 2
        else:
            point = point * 3 + 1
        len += 1
    return len


def Longest_Collatz_sequence(upper_point:int):
    """
    Calculate len of the longest Collatz sequence with starting point under given
    Args: upper starting point
    Result: len
    """
    max_len = 0
    for point in range(2, upper_point):
        len = Collatz_sequence_len(point)
        if len > max_len:
            max_len = len
            print(point, max_len)
    return max_len

print(Longest_Collatz_sequence(1000000))