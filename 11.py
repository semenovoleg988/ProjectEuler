#Problem 11
#Largest product in a grid
""" Derscription(https://projecteuler.net/problem=11)."""


def largest_product_of_n_digits_in_list_of_numbers(list_of_numbers: list, number_of_digits: int) -> int:
    """ Search for biggest product of digits in a big number given by a list."""
    n = number_of_digits
    maximum = 1
    temp = 1
    while True:
        flag_1 = 0
        while True:#search for first nonzero product
            flag = 0
            if len(list_of_numbers) < n:
                return int(maximum)
            temp = 1
            for i in range(n):
                if list_of_numbers[i] == 0:
                    list_of_numbers = list_of_numbers[i+1:]
                    flag = 1
                    break
                temp *= int(list_of_numbers[i])
            if not flag:
                break
            if len(list_of_numbers) == n:
                return max(maximum, temp)
        if temp > maximum: 
            maximum = temp
        for i in range(1, len(list_of_numbers) - n):
            if list_of_numbers[i+n-1] == 0:
                list_of_numbers = list_of_numbers[i+n:]
                flag_1 = 1
                break
            temp /= int(list_of_numbers[i-1]) 
            temp *= int(list_of_numbers[i+n-1])
            if temp > maximum: 
                maximum = temp
        if not flag_1:
            return int(maximum)


def Largest_product_in_a_grid(list_of_numbers: list, number_of_factors: int) -> int:
    """ Search for the greatest product in a grid."""
    if number_of_factors <= 0:
        return 0
    return max(up_down_product(list_of_numbers, number_of_factors), \
        left_right_product(list_of_numbers, number_of_factors), \
        diagonally_r_l_product(list_of_numbers, number_of_factors), \
        diagonally_l_r_product(list_of_numbers, number_of_factors))


def up_down_product(list_of_numbers: list, number_of_factors: int) -> int:
    """ Search for the greatest up-down product in a grid."""
    maximum = 0
    if len(list_of_numbers) < number_of_factors:
        return maximum
    for j in range(len(list_of_numbers[0])):
        temp_list = []
        for i in range(len(list_of_numbers)):
            temp_list.append(list_of_numbers[i][j])
        temp = largest_product_of_n_digits_in_list_of_numbers(temp_list, number_of_factors)
        if maximum < temp: maximum = temp
    print("Max up_down_product:", maximum)
    return int(maximum)


def left_right_product(list_of_numbers: list, number_of_factors: int) -> int:
    """ Search for the greatest left-right product in a grid."""
    maximum = 0
    for i in range(len(list_of_numbers)):
        if len(list_of_numbers[i]) < number_of_factors:
            continue
        else:
            temp = largest_product_of_n_digits_in_list_of_numbers(list_of_numbers[i], number_of_factors)
            if maximum < temp: maximum = temp
    print("Max left_right_product:", maximum)
    return int(maximum)


def diagonally_r_l_product(list_of_numbers: list, number_of_factors: int) -> int:#FIXME work only for square grid
    """ Search for the greatest diagonally right-to-left product in a grid."""
    maximum = 0
    for n in range(number_of_factors-1, len(list_of_numbers)):
        temp_list_1 = []
        temp_list_2 = []
        for i in range(0, n, 1):
            temp_list_1.append(list_of_numbers[i][n-1-i])
            temp_list_2.append(list_of_numbers[len(list_of_numbers)-n+i][len(list_of_numbers)-1-i])
        temp = largest_product_of_n_digits_in_list_of_numbers(temp_list_1, number_of_factors)
        if maximum < temp: maximum = temp
        temp = largest_product_of_n_digits_in_list_of_numbers(temp_list_2, number_of_factors)
        if maximum < temp: maximum = temp
    print("Max diagonally_r_l_product:", maximum)
    return int(maximum)


def diagonally_l_r_product(list_of_numbers: list, number_of_factors: int) -> int:
    """ Search for the greatest diagonally left-to-right product in a grid."""
    maximum = 0
    for n in range(len(list_of_numbers) - number_of_factors):
        temp_list_1 = []
        temp_list_2 = []
        for i in range(n, len(list_of_numbers)):
            temp_list_1.append(list_of_numbers[i][i])
            temp_list_2.append(list_of_numbers[i][i])
        temp = largest_product_of_n_digits_in_list_of_numbers(temp_list_1, number_of_factors)
        if maximum < temp: maximum = temp
        temp = largest_product_of_n_digits_in_list_of_numbers(temp_list_2, number_of_factors)
        if maximum < temp: maximum = temp

    for n in range(len(list_of_numbers) - number_of_factors):
        temp_list_1 = []
        temp_list_2 = []
        for i in range(0, len(list_of_numbers) - n):
            for j in range(n, ):
                temp_list_1.append(list_of_numbers[i][j])
                temp_list_2.append(list_of_numbers[j][i])
        temp = largest_product_of_n_digits_in_list_of_numbers(temp_list_1, number_of_factors)
        if maximum < temp: maximum = temp
        temp = largest_product_of_n_digits_in_list_of_numbers(temp_list_2, number_of_factors)
        if maximum < temp: maximum = temp
    print("Max diagonally_l_r_product:", maximum)
    return int(maximum)


if __name__ == "__main__":
    with open('11_grid', 'r') as f:
        lines = f.readlines()
    grid = [[] for _ in range(len(lines))]
    n_element = ''
    for i in range(len(lines)):#convert strings in a grid of numbers
        for j in range(len(lines[i])):
            if lines[i][j] == " ":
                grid[i].append(int(n_element))
                n_element = ''
            elif lines[i][j] ==  '\n':
                break
            else:
                n_element += lines[i][j]
        grid[i].append(int(n_element))
        n_element = ''
    print(Largest_product_in_a_grid(grid, 4))