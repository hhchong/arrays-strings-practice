#Given two strings, write a smethod to decide if one is a permutation of the other.
#is anagraM

def check_permutation(str1, str2):

    #bc dictionaries are not ordered, we can create two hash tables for each str
    #and see if they are equal, if they are, they are anagram
    
    str1_dict = {}

    str2_dict = {}

    for char in str1:
        str1_dict[char] = 1

    for char in str2:
        str2_dict[char] = 1

    return str1_dict == str2_dict

    #return Counter(str1) == Counter(str2) also works


print (check_permutation('abc', 'bca'))
print (check_permutation('abc', 'ab'))
print (check_permutation('abc','b'))
print (check_permutation('abc', 'cba'))