#Problem 16
#Power digit sum
'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000
'''

number = str(pow(2, 1000))
print(number)

sum = 0
for i in number:
    sum += int(i)
print(sum)