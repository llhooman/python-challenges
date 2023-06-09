# Challenge
# Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(str):
    hasMid = 1 if len(str)%2 else 0
    if(hasMid):
        mid = int(len(str)/2)
        return(str[mid])
    return("")  

print(mid("abc"))


# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]