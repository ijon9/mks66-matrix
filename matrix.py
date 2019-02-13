"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    result = ""
    for col in matrix:
        result += str(col[0]) + " "
    result += "\n"
    for col in matrix:
        result += str(col[1]) + " "
    result += "\n"
    for col in matrix:
        result += str(col[2]) + " "
    result += "\n"
    for col in matrix:
        result += str(col[3]) + " "
    print(result)

# #Test for print_matrix
# print_matrix([[55,200,150,1],
#               [100, 255, 33, 1],
#               [50, 130, 234, 1]])
# should return:
# 55 100 50
# 200 255 130
# 150 33 234
# 1 1 1

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(0, len(matrix)):
        for i2 in range(0, len(matrix)):
            matrix[i][i2] = 0
        matrix[i][i] = 1

#Test for ident
a = [[255, 30, 123, 1],
     [132, 24, 32, 1],
     [54, 23, 243, 1]]
print_matrix(a)
ident(a)
print_matrix(a)

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
