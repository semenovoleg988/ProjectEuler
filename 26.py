# Filename:26.py
# Problem 26
# Reciprocal cycles(https://projecteuler.net/problem=26)
"""Reciprocal cycles
    A unit fraction contains 1 in the numerator. 
    The decimal representation of the unit fractions with denominators 2 to 10 are given:
    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
    It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

def longest_reciprocal_cycles(upper_limit:int = 1000) -> list:
    """ Calculate longest recyprocal cycle"""
    if upper_limit == 0:
        return None
    if upper_limit <= 2:
        return 0
    if upper_limit < 0:
        upper_limit = - upper_limit
    longest = [3, 1]
    i = 7
    i_cycle_len = 0
    while(i <= upper_limit) :
        i_cycle_len = reciprocal_cycle(i)
        if i_cycle_len > longest[1]:
            longest = [i, i_cycle_len]
        if i + 2 <= upper_limit:
            i_cycle_len = reciprocal_cycle(i+2)
            if i_cycle_len > longest[1]:
                longest = [i+2, i_cycle_len]
        i +=4

    return longest

        

def reciprocal_cycle(denominator:int, numerator:int = 1) -> int:
    """ Calculate length of recyprocal cycle"""
    print(numerator/denominator)
    return 0

if __name__ == "__main__":
    print(longest_reciprocal_cycles())