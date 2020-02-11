#assume you have a method is_substring which checks if one word is a substring of another. given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to is_substring (i.e. "waterbottle" is a rotation of "erbottlewat")

#create two functions , isrotation and issubstring, where rotation will call on is_substring once

def is_rotation(s1, s2):

    #if you concat s1 to s1, s2 will be somewhere in there
    #if their length is different then it's not a rotation

    if len(s1) != len(s2):
        return False

    return is_substring(s1+s1, s2)

def is_substring(s1, s2):

    # if s1 is not longer than s2 then can't contain s2 as a substring

    if len(s1) <= len(s2):
        return False

    #else if it is longer, check if s2 in s1. we can is if s2 in s1 return true, but without using in, we can iterate over s1 and check if it is equal to s2

    #erbottlewaterbottlewat


    for i in range(0, len(s1) - len(s2) + 1):
        #i in range( 0, 22 - 11 + 1) (0, 12)
        #use slicing, with size of len s2, keep moving one to the right to check if s2 appears in s1
        if s1[i:i+len(s2)] == s2:
            return True 
    return False

print(is_rotation("waterbottle", "erbottlewat"))