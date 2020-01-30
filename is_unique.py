def is_unique(str):

    seen = {}

    if len(str) == 0:
        return False

    for char in str:

        if char in seen:
            return False

        else:
            seen[char] = seen.get(char, 0) + 1

    return True

print (is_unique('aaaaa'))
print (is_unique('abcdefg'))
print (is_unique(''))
print (is_unique('abdefgg'))