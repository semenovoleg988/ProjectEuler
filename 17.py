#Problem 17
#Number letter counts
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

def Number_letter_counts(first:int, last:int):
    """
    Calculate number of letters in generated sequence of numbers
    Arg: first and last number of sequence
    Result: sum of number of letters in sequence 
    """
    result = 0
    for i in range(first, last + 1):
        result += len(number_in_words(i))
    return result


def number_in_words(number:int):
    """
    Translate number into words
    Args: integer number
    Result: string name of number 
    """
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
            return word_arr[0][number // 100] + "hundred" + word_arr[1][(number % 100) // 10]
        else: 
            if number % 100 < 19:
                return word_arr[0][number // 100] + "hundred" + word_arr[0][(number % 100)]
            else:
                return word_arr[0][number // 100] + "hundred" + word_arr[1][(number % 100) // 10] + word_arr[0][number % 10]
    if number == 1000:
        return "onethousend"
print(Number_letter_counts(1, 1000))