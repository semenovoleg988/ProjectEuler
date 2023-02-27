#Problem 13
#Large sum
"""Description(https://projecteuler.net/problem=13).

    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."""

def __main__():
    lines = []
    with open('13_big_number', 'r') as f:
        lines = f.readlines()
    for n in range(len(lines)):
        lines[n] = int(lines[n])
    
    print(sum(lines))

if __name__ == "__main__":
    __main__()