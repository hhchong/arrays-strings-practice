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


def convert_zero(matrix):

    #find len width of matrix

    #now we have width and len of matrix

    #interate matrix and find index of 0
    #store col, row of 0 in col dict row dict

    # for item in dict.keys, m[dict.keys][range width] -> 0
    #for item in row, m[range width][item] -> 0

    # width = len(m[0])

    # hm = {}

    # for i,j in enumerate(m):
    #     for k,l in enumerate(j):
    #         if l == 0:
    #             hm[i] = k

    # for i,j in enumerate(m):
    #     for k,l in enumerate(j):
    #         if i in hm.keys():
    #             m[i][k] = 0
    #         elif k in hm.values():
    #             m[i][k] = 0

    # return m

    #time complexity is O(M x N) space O(M+N), use the matrix itself as data storage to get space to O(1)

    #instead we can use the first cell of every row and col as a flag, set to 0

    m = len(matrix) #2
    n = len(matrix[0]) #3

    #use left most to mark rows to convert, use top most to mark cols to convert
    row_zero = False
    for i in range(m):
        if matrix[i][0] == 0:
            row_zero = True

    col_zero = False
    for j in range(n):
        if matrix[0][j] == 0:
            col_zero = True

    #mark where row/col should be flagged as 0 rows
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    #now actually convert them to 0
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0
    # if col_zero:
    #     for j in range(n):
    #         matrix[0][j] = 0

    # if row_zero:
    #     for i in range(m):
    #         matrix[i][0] = 0
    return matrix





print(convert_zero([[1,2,3,4],[5,2,1,0],[6,1,8,6]]))

print(convert_zero([[1,2,3,4],[5,2,1,0],[6,0,8,6]]))






