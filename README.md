# matrix_class
Create Matrix class with following methods:

__ init__ (self, 2d_array) must get 2d array in argument
1.1. befor creating Matrix should be checked if matrix
. has only numerical items
. rows have same length
if not then raise Exception with corresponding message

__ add__(self, other_matrix) method should add current instance to matrix instanse that pass as argument

__ sub__(self, other_matrix) method should subtract from current instance a matrix instanse that pass as argument

__ mul__(self, other_matrix) method should multiply current instance with matrix instanse that pass as argument

__ str__(self, other_matrix) method shuld return string of matrix as follows:


⌈ 1.60  3.1 42.34 ⌉
|  4.0 5.00   6.9 |
⌊ 43.0  2.4  3.99 ⌋

determinant() calculates determinant of matrix
inverse() calculate inverse of matrix
same_dimention_with(other_matrix) makes sure other matrix has the same dimension as instance matrix
is_square() check if matrix is square
random_matrix() static method returns instance of Matrix by
