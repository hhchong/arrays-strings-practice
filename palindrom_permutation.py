#given a string, write a function to check if it is a permutation of a palindrome. A You can ignore casing and non-letter characters.

#try to do it O(N) time

#hints: char in strings that is a permutation of a palindrome have equal # instances >1 and even for each char or all even except one char is odd # instance
def check_permutation_palindrome(string):

    #first lower case all char in the string
    lowered = string.lower()
    
    #create ht
    ht = {}

    #ht with key of char and value of counts of occurence
    for char in lowered:
        ht[char] = ht.get(char, 1) + 1

    #create a variable to keep track of how many odd values there are ... a palindrome only allows 1 odd value
    odds = 0

    #let's check the counts of each char using the ht
    for count in ht.values():
        #if the count is odd.. so when % 2 it will be 1
        if count % 2 > 0:
            #increment odds counter
            odds += 1
            #a palindrome can only have one odd occurence, so if there's more than one, it's not a palindrome
            if odds > 1:
                return False
    return True


    
print (check_permutation_palindrome('String'))
print (check_permutation_palindrome('Tact Coa'))
