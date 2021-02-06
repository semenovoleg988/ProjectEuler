def permutations_of_numbers(N:int, M:int=-1, prefix=None):
    """Generate permutations of N numbers in M positions.

        Args:N number of numbers, M number of positions, prefix - list for generated permutation
        Result:None"""
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        if number in prefix:
            continue
        prefix.append(number)
        permutations_of_numbers(N, M-1, prefix)
        prefix.pop()

if __name__ == "__main__":
    permutations_of_numbers(4)