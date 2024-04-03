class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        res = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                res[c][r] = matrix[r][c]
        
    return res

# This method takes a matrix as input, which is represented as a list of lists of integers. The goal of the method is to transpose the matrix, which means to swap the rows and columns.

# Here is a step-by-step explanation of the code:


# The method starts by getting the number of rows and columns in the input matrix using the len function. It assigns these values to the variables rows and cols, respectively.



# It then creates a new matrix called res using a nested list comprehension. The outer list comprehension creates a list of length cols, and the inner list comprehension creates a list of length rows. Each element in the res matrix is initialized to 0.



# The method then enters two nested loops, one for iterating over the rows and the other for iterating over the columns of the input matrix.



# Inside the nested loops, the method assigns the value of the element at the current row and column of the input matrix to the corresponding element at the current column and row of the res matrix. This effectively transposes the matrix.



# Finally, the method returns the transposed matrix res.

