# Challenge
# Thousands separator
# Write a function named format_number that takes a non-negative number as its only parameter.

# Your function should convert the number to a string and add commas as a thousands separator.

# For example, calling format_number(1000000) should return "1,000,000".
def format_number(num):
    num = str(num)
    finalNumber = ""
    flag = 0
    for i in reversed(range(0, len(num))):
        if (flag == 3):
            flag = 0
            finalNumber += ","
        finalNumber += num[i]
        flag +=1
    return finalNumber[::-1]


print(format_number(10000))



# DIY solution
def format_number(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

# built-in solution
def format_number(n):
    return "{:,}".format(n)
