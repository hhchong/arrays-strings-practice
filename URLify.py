#Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

#try to do it in place???
#strings are immutable so need to turn into array then join
#return string.strip().replace(' ', '%20')

def create_url(string, int):

    string = string[:int]

    return "%20".join(string.split(" "))

print (create_url('Mr John Smith      ', 13))