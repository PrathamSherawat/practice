def subsets(s): 
    res = []
    for i in range(len(s) + 1):
        for j in range(len(s)- i+ 1):
            res.append(s[j:j+i])
    return list(set(res))

def longest_prefix_palindrome(string):
    current = ""
    current_length = 0
    for i in range(len(string)):
        if string[i] == string[len(string) - 1 - i]:
            current = string[i] + current
            current_length += 1
        else:
            current = ""
            current_length = 0
    return current

from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

anagrams = filter(lambda x: is_anagram(longest_prefix_palindrome("malaylam"), x), subsets('malaylam'))

print (subsets('malaylam'))
print(longest_prefix_palindrome("malaylam"))
print(list(anagrams))