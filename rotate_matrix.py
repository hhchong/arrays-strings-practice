#Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer, write a method to rotate the image by 90 degrees. Can you do this in place?


#rotate 100% in place, starting form top left of quadrant

def rotate_matrix(m):

#all index 0 of arrays turn into last row
#all index 1 turn into second to last row
#all index 2 turn into second row
#last index of arrays turn into first row
    n = len(m) # 3
    for i in range(n//2): #0, 1
        for j in range(n-n//2): #0, 1, 2
            m[i][j], m[j][n-1-i], m[n-1-i][n-1-j], m[n-1-j][i] = m[j][n-1-i], m[n-1-i][n-1-j], m[n-1-j][i], m[i][j]

            # i is 0 j is 0
            # m[0][0], m[0][2], m[2][2], m[2][0] = m[0][2], m[2][2], m[2][0], m[0][0]
            # corners rotate right: 1 -> 3, 3-> 9, 9 -> 7, 7 -> 1

            #i is 0 j is 1
            #m[0][1], m[1][2], m[1][2], m[1][0] = m[1][2], m[1][2], m[1][0], m[0][1]
            # next index rotates: 2 -> 6, 6 -> 6, 6 -> 4

            #doesn't work, we need 6 to turn into 8, so m[1][2] = m[2][1]

            #m[1][1], m[1][1], m[1][1], m[1][1] = m[1][1], m[1][1], m[1][1], m[1][1]
            #middle stays the same

    return m

# n = len(A)
#         for i in range(n/2):
#             for j in range(n-n/2):
#                 A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
#                          A[~j][i], A[~i][~j], A[j][~i], A[i][j]
print (rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))
