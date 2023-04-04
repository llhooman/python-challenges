# Challenge
# Adding and removing dots
# Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

# (You may assume that the input to add_dots does not itself contain any dots.)


#add dots starts here
def add_dots(str):
    finalString = ""
    for i in range(0,len(str)):
        finalString += str[i]
        if(i == len(str)-1):
            break
        finalString +="."
    return finalString
    
#remove dots starts here
def remove_dots(str):
    finalString = ""
    for i in range(0,len(str)):
        if(str[i] == "."):
            continue
        finalString += str[i]
    return finalString
print(remove_dots("xx"))


# the longer way
def add_dots(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1]

def remove_dots(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out


# the short way
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")