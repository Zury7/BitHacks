# Problem: Multiply two square matrices using the general method

def matrix_multiply_general(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):            # row of A
        for j in range(n):        # column of B
            for k in range(n):    # iterate over shared dimension
                result[i][j] += A[i][k] * B[k][j]
    return result

# Example usage
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = matrix_multiply_general(A, B)
    print("Matrix A x B:")
    for row in C:
        print(row)
