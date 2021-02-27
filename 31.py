# Problem 31
# Coin sums
# Description(https://projecteuler.net/problem=31)


def pound_and_pences_combinations(pounds: int, pences: int, coins = [1, 2, 5, 10, 20, 50, 100, 200]):
    """ Calculate number of combinations of pounds and pences."""
    sum = pounds * 100 + pences
    number_of_results = 0
    if sum == 0:
        return 1
    if sum < 0 or coins == []:
        return number_of_results
    for i in range(sum // coins[-1] + 1):
        number_of_results += pound_and_pences_combinations(0, sum - i*coins[-1], coins = coins[:-1])
    return number_of_results


if __name__ == "__main__":
    print(pound_and_pences_combinations(2, 0))