#Implement a method to perform basic string compression using the counts of repeated characters. 

#aabcccccaaa turns into a2b1c5a3.

#if compressed string would not become smaller than original string, method should return original string

def compress_string(string):

    #create empty array
    compressed = []

    #two pointers -- i and newtail. newtail will be behind i, starting at 0
    newtail = 0

    #i starts at 1
    for i in range(1, len(string)):
        #if they don't match OR if i reaches the end of the length
        if string[i] != string[newtail] or i ==  len(string) -1:
            #append the letter beginning of its repeats
            compressed.append(string[newtail])
            #append the # of times it repeats by subtracting pointers
            compressed.append(str(i-newtail))
            #newtail moves to location of i pointer
            newtail = i 

    if len("".join(compressed)) < len(string):
        return "".join(compressed)

    else:
        return string


print (compress_string('aabcccccaaa'))
