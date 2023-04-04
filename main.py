# Challenge
# Anagrams
# Two strings are anagrams if you can make one from the other by rearranging the letters.

# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
def is_anagram(str1,str2):
    if(len(str1)!= len(str2)):
        return False
    
    for i in range(0,len(str1)):
        for j in range(0,len(str2)):
            if(str1[i] == str2[j]):
                str2 = str2.replace(str2[j], '', 1)
                break
    if(str2 == ""):
        return True
    else:
        return False
print(is_anagram("typhoon", "opython"))


# easy solution
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# harder solution:
# count how many times each letter appears in each string,
# and make sure all the counts are the same.
def count_letters(string):
    return {l: string.count(l) for l in string}
def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)