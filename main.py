from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
C = new_matrix()
ident(C)
matrix_mult(A,B)
print_matrix(A)
print_matrix(B)
matrix_mult(B,A)
print_matrix(A)
print_matrix(B)
matrix_mult(C,A)
print_matrix(A)

#Body of house
add_point(matrix, 125, 125)
add_point(matrix, 125, 250)
add_point(matrix, 125, 250)
add_point(matrix, 250, 250)
add_edge(matrix, 250, 250, 0, 250, 125, 0)
add_edge(matrix, 125, 125, 0, 250, 125, 0)

#Roof of house
add_edge(matrix, 125, 250, 0, 188, 350, 0)
add_edge(matrix, 188, 350, 0, 250, 250, 0)

#Door of house
add_edge(matrix, 188, 125, 0, 188, 175, 0)
add_edge(matrix, 188, 175, 0, 220, 175, 0)
add_edge(matrix, 220, 175, 0, 220, 125, 0)

draw_lines( matrix, screen, color )
display(screen)
