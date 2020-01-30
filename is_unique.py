#Implement an algorithm to determine if a string has all unique characters. 


def is_unique(str):
    #create a seen dictionary, for fast lookup if a char has been seen
    seen = {}

    #in order to return False, otherwise leaving this out will return None for empty string
    if len(str) == 0:
        return False

    #iterate through str and check if it's in the dictionary
    for char in str:

        if char in seen:
            return False

        #if not seen, add to set dictionary
        else:
            seen[char] = seen.get(char, 0) + 1
    #if we check all the char in str and they were all not in seen, means it is unique
    #return True
    return True

print (is_unique('aaaaa'))
print (is_unique('abcdefg'))
print (is_unique(''))
print (is_unique('abdefgg'))