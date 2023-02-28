#Problem 18
#Maximum path sum I
"""Description(https://projecteuler.net/problem=18).
    
    By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
    the maximum total from top to bottom is 23.
    3
    7 4
    2 4 6
    8 5 9 3
    That is, 3 + 7 + 4 + 9 = 23.
    Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
    However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
    it cannot be solved by brute force, and requires a clever method! ;o)"""

def list_of_lists_of_numbers_from_file(file_dist: str) -> list:
    """returns list with lists with numbers from file where numbers separeted by spaces"""
    l =[]
    with open(file_dist) as f:
        for line in f:
            l.append(line.split())
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j] = int(l[i][j])
    return l


def maximum_path_sum(l: list) -> int:
    arr = [0]*len(l)
    for i in range(len(l)):
        arr[i] = [0]*len(l[i])
    
    arr[0][0] = l[0][0]
    for i in range(1, len(l)):
        arr[i][0] = arr[i-1][0] + l[i][0]
        arr[i][-1] = arr[i-1][-1] + l[i][-1]

    for i in range(2, len(l)):
        for j in range(1, len(l[i]) - 1):
            arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + l[i][j]
    
    return(max(arr[-1]))

def __main__():
    l = list_of_lists_of_numbers_from_file("18.txt")
    print(maximum_path_sum(l))


if __name__ == "__main__":
    __main__()