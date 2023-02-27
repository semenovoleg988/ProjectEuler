# Problem 15
# Lattice paths
"""Description(https://projecteuler.net/problem=15).

    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.
    How many such routes are there through a 20×20 grid?"""


def Latice_path_number(x:int, y:int) -> int:#recursion method
    """Calculate number of all routes."""
    if x == 1 or y == 1:#for exaple in (1, 4) we have 5 routes
        return x + y
    elif x == y:#if matrix is square                            
        return 2 * Latice_path_number(x - 1, y) #No matter going we right or down(ways will be transpose)
    else:#not square
        return Latice_path_number(x - 1, y) + Latice_path_number(x, y - 1) #right or down


def Latice_pathes(length: int, height: int) -> int:#faster method
    """Calculate number of all routes."""
    array = [[]for i in range(0, length + 1)]
    for x in range(0, length + 1):
        for y in range(0, height + 1):
            if x * y == 0:
                array[x].append(1)
            else: 
                array[x].append(array[x - 1][y] + array[x][y - 1])
    return array[length][height]


if __name__ == "__main__":
    print(Latice_pathes(20, 20))