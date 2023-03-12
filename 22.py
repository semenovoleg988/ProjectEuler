# Problem 22
# Names scores
""" Description(https://projecteuler.net/problem=22).

    Using names.txt, a 46K text file containing over five-thousand first names, 
    begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this 
    value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
    is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?"""


def __main__():
    l = []
    total = 0

    with open("22.txt") as f:
        for line in f:
            l.extend(line.split(sep=","))
    
    for i in range(len(l)):
        l[i] = l[i].strip("\"")
    

    l.sort()
    for i in range(len(l)):
        score = 0
        for char in l[i]:
            score += ord(char) - 64
        score *= (i+1)
        total += score
    print(total)


if __name__ == "__main__":
    __main__()
