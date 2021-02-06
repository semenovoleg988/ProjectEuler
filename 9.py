#Problem 9
#Special Pythagorean triplet
'''
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
'''

from math import sqrt as sqrt

def Pythagorian_triplet(sum:int):
    """Calculate definition of numbers in Pythagorian triplet, sum of which = sum
        
        Args: sum of a, b, c
        Result:  (a, b, c)
    """
    a, b, c = 3, 4, 5   #the lowest Pythagorian triplet
    if sum // 3 > 5:
        c = int(sum // 3) + 1
        b = int(sqrt(c**2 - a**2))
    sum_a_b = sum - c
    while a + b + c <= sum:
        if c % 2 == 0:                                              #for odd c , a and b both even or odd
            for j in range(b, c):
                for i in range(j - 2, a, -2):
                    if i + j < sum_a_b:
                        break
                    if i + j == sum_a_b and i**2 + j**2 == c**2:
                        return i, j, c

        else:                                                       #for even c, a and b neither odd 
            for j in range(b, c):
                for i in range(j - 1, a, -2):
                    if i + j < sum_a_b:
                        break
                    if i + j == sum_a_b and i**2 + j**2 == c**2:
                        return i, j, c

        c += 1
        sum_a_b = sum - c
    return


def product_of_Pythagorian_triplet(pythagorian_triplet):
    """Calculate the product of Pythagorian triplet
    
        Args: Pythagorian triplet (a, b, c)
        Result: product of Pythagorian triplet
    """
    return pythagorian_triplet[0] * pythagorian_triplet[1] * pythagorian_triplet[2] 

#print(product_of_Pythagorian_triplet(Pythagorian_triplet(12)))

#print(product_of_Pythagorian_triplet(Pythagorian_triplet(1000)))

print(product_of_Pythagorian_triplet(Pythagorian_triplet(1000)))