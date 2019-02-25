"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1   1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    result = ""
    for i in range(0, len(matrix)):
        for col in matrix:
            result += str(col[i]) + " "
        result += "\n"
    print(result)

#Test for print_matrix
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
# a = [[255, 30, 123],
#      [132, 24, 32],
#      [54, 23, 243]]
# print_matrix(a)
# ident(a)
# print_matrix(a)

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    finalMatrix = []
    for eachColInM2 in range(0, len(m2)): #Iterates through cols in m2
        matrixEntry = []
        for eachRowInM1 in range(0, len(m1[0])): #Iterates through rows in m1, since one col in m2 is evaluated with each row in m1
            entryElement = 0
            for currPos in range(0,len(m2[0])):
                entryElement += m1[currPos][eachRowInM1] * m2[eachColInM2][currPos]
            matrixEntry.append(entryElement) #Builds the matrixEntry, appends each number calculated into a list
        finalMatrix.append(matrixEntry) #Builds the entire matrix, appends each list created into the outer list, forming the matrix
    m2.clear()
    m2.extend(finalMatrix) #Modifies m2 to the new product

# #Test for matrix_mult
# matrix1 = [[1,4],
#            [2,5],
#            [3,6]]
#
# matrix2 = [[10,30,50],
#            [20,40,60]]
#
# print_matrix(matrix2)
# matrix_mult(matrix1, matrix2)
# print_matrix(matrix2)


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
