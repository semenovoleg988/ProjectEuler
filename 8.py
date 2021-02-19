#Problem 8
#Largest product in a series
"""Description(https://projecteuler.net/problem=8).

    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
    What is the value of this product?"""


def largest_product_of_n_digits_in_big_number(big_number: str, number_of_digits: int) -> int:
    """ Search for biggest product of digits in big number given by string."""
    n = number_of_digits
    maximum = 1
    print(maximum)
    temp = 1
    while True:
        flag_1 = 0
        while True:#search for first nonzero product
            flag = 0
            if len(big_number) < n:
                return maximum
            temp = 1
            for i in range(n):
                if big_number[i] == '0':
                    big_number = big_number[i+1:]
                    flag = 1
                    break
                temp *= int(big_number[i])
            if len(big_number) == n:
                return max(maximum, temp)
            if not flag:
                break
        if temp > maximum: 
            maximum = temp
            print("max is", maximum)
        for i in range(1, len(big_number) - n):
            if big_number[i+n-1] == '0':
                big_number = big_number[i+n:]
                flag_1 = 1
                break
            temp /= int(big_number[i-1]) 
            temp *= int(big_number[i+n-1])
            if temp > maximum: 
                maximum = temp
                print("max is", maximum)
        if not flag_1:
            return maximum


if __name__ == "__main__":
    with open('8_numbers', 'r') as f:
        lines = f.readlines()
    for n in range(len(lines)):
        lines[n] = int(lines[n])
    str(lines)
    string = ""
    for n in lines:
        string += str(n)
    print(largest_product_of_n_digits_in_big_number(string, 13))