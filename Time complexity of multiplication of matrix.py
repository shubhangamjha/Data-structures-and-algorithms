# to implement and analyze the time complexity of matrix multiplication in python

def matrix_multiply(A, B):
    """This function calls 1st matrix as A and 2nd as B"""
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        print("Incompatible matrices. Can't perform multiplication.")
        return

    # Create result matrix and fill with zeros
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    # Perform multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or we could use rows_B
                C[i][j] += A[i][k] * B[k][j]
    return C

# Test the function
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(matrix_multiply(A, B))


print("The time complexity of this algorithm is O(n^3) because there are three nested loops: each loop runs n times in the worst-case scenario, \nwhere n is the number of rows or columns in the input matrices.")