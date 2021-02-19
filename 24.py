# Problem 24
# Lexicographic permutations
"""Description(https://projecteuler.net/problem=24).

    A permutation is an ordered arrangement of objects. 
    For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
    If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
    The lexicographic permutations of 0, 1 and 2 are:
    012   021   102   120   201   210
    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

permutations = []

def lexicographic_permutations(N:int):
    """ Generate lexicographic permutations of given list of numbers without repeat.
    
        Args:list of integer number
        Result:2-d list"""
    permutations_of_numbers(N)



def permutations_of_numbers(N:int, M:int=-1, prefix=None):
    """Generate permutations of N numbers in M positions.

        Args:N number of numbers, M number of positions, prefix - list for generated permutation
        Result:None"""
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        permutations.append(permutations)
        print(permutations)
        return
    for number in range(1, N+1):
        if number in prefix:
            continue
        prefix.append(number)
        permutations_of_numbers(N, M-1, prefix)
        prefix.pop()

def test(list_of_numbers:list):
    """ """
    if len(list_of_numbers[0]) == 3:
        print("Test result: ", end='')
        if list_of_numbers == [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]:
            print("Ok")
            return 
        print("Fail")
        return


if __name__ == '__main__':
    lexicographic_permutations(3)
    print(permutations)

#    print(lexicographic_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    