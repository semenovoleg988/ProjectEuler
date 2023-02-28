# Problem 17
#NOT SOLVED. RIGHT ASWER 21124
# Number letter counts
"""Description(https://projecteuler.net/problem=17).

    If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
    contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
    The use of "and" when writing out numbers is in compliance with British usage."""

def Number_letter_counts(first: int, last: int) -> int:
    """Calculate number of letters in generated sequence of numbers"""
    result = 0
    for i in range(first, last + 1):
        print(i, number_in_words(i))
        result += len(number_in_words(i))
    return result


def number_in_words(number:int) -> str:
    """Translate number into words."""
    word_arr = [["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
    ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]]

    if number <= 19:
        return word_arr[0][number]
    if number < 100:
        if number % 10 == 0:
            return word_arr[1][number // 10]
        else:
            return word_arr[1][number // 10] + word_arr[0][number % 10]
    if number < 1000:
        if number % 100 == 0:
            return word_arr[0][number // 100] + "hundred"
        elif number % 10 == 0:
            return word_arr[0][number // 100] + "hundredand" + word_arr[1][(number % 100) // 10]
        else: 
            if number % 100 < 19:
                return word_arr[0][number // 100] + "hundredand" + word_arr[0][(number % 100)]
            else:
                return word_arr[0][number // 100] + "hundredand" + word_arr[1][(number % 100) // 10] + word_arr[0][number % 10]
    if number == 1000:
        return "onethousand"



if __name__ == "__main__":
    print(Number_letter_counts(1, 100))