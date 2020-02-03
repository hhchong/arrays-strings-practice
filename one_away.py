#There are three types of edits that can be performed on strings: insert a character, remove a characer, or replace a character. Given two strings, write a function to chck if they are one edit (or zero edits) away.

#characteristics of a ht has insert, remove, replace so maybe we can do it all at the same time?
#have an edit counter

#edge - are they ever the same string? capitalization?

#efficient solution : traverse both strings at the same time and keep track of count of different characters

def one_away(str1, str2):

    #we use len(str1) and len(str2) a lot so just assign them to variables
    m = len(str1)
    n= len(str2)

    if abs(m - n) > 1:
        return False

    edits = 0
    #if length difference more than one, false
    #traverse both strings at the same time starting index 0
    i = 0
    j = 0

    while i < m and j < n:
        if str1[i] != str2[j]:
            edits += 1
            if edits > 1:
                return False
            if m > n:
                i += 1
            elif n > m:
                j += 1
            else:
                i += 1
                j += 1
        i += 1
        j += 1
    #if don't match
        #increment edit by 1
        #return false if count is more than 1
        #if one is longer, then increment up that one by 1
        #if both same length, then move ahead both by 1
    #else move ahead both

    #if there is extra last character (like an s) after completing double traversal while loop
    if i < m or j < n:
        edits += 1

    return edits == 1


#time complexity is O(n)
#space complexity O(1)
print (one_away('pale', 'ple')) #true
print (one_away('pales', 'pale')) #true
print (one_away('pale', 'bale')) #true
print (one_away('pale', 'bake')) # false
print (one_away('pale', 'pale')) #false

