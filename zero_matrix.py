# write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0.

#[[1,2,3,4]
# [5,2,1,0]
# [6,1,8,6]]

#0 is at m[1][3]
#all m[1][whatever] -> 0
#all m[whatever][3] -> 0


#[[1,2,3,0]]
# [0,0,0,0],
# [6,1,8,0]]

#[[1,2,3,4]
# [5,2,1,0]
# [6,0,8,6]]

#0 is at m[1][3] and m[3][1]
# {1:3, 3:1}
#all m[1][whatever] -> 0
#all m[whatever][3] -> 0
#all m[3][whatever] -> 0
#all m[whatever][2] -> 0

#[[1,0,3,0]]
# [0,0,0,0],
# [0,0,0,0]]


# we need to find locations of all original 0's first, otherise if we turn to 0 as we keep going it will be more 0's than we need

#use dictionaries to store the location of y and the location of x?


def convert_zero(m):

    #find len width of matrix

    #now we have width and len of matrix

    #interate matrix and find index of 0
    #store col, row of 0 in col dict row dict

    # for item in dict.keys, m[dict.keys][range width] -> 0
    #for item in row, m[range width][item] -> 0

    width = len(m[0])

    hm = {}

    for i,j in enumerate(m):
        for k,l in enumerate(j):
            if l == 0:
                hm[i] = k

    for i,j in enumerate(m):
        for k,l in enumerate(j):
            if i in hm.keys():
                m[i][k] = 0
            elif k in hm.values():
                m[i][k] = 0

    return m


print(convert_zero([[1,2,3,4],[5,2,1,0],[6,1,8,6]]))

print(convert_zero([[1,2,3,4],[5,2,1,0],[6,0,8,6]]))






