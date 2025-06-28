# Problem: Solve a system of linear equations Ax = b where A is binary (0/1), using XOR-based Gaussian Elimination
# This simulates low-level linear algebra over GF(2), useful in cryptography and error correction.

def solve_binary_system(matrix, vector):
    n = len(matrix)
    A = matrix[:]
    b = vector[:]

    for i in range(n):
        # Find row with a 1 in current column
        for j in range(i, n):
            if A[j] & (1 << (n - 1 - i)):
                A[i], A[j] = A[j], A[i]
                b[i], b[j] = b[j], b[i]
                break
        else:
            raise ValueError("Singular matrix or no unique solution")

        # Eliminate below
        for j in range(i + 1, n):
            if A[j] & (1 << (n - 1 - i)):
                A[j] ^= A[i]
                b[j] ^= b[i]

    # Back substitution
    x = [0] * n
    for i in reversed(range(n)):
        x[i] = b[i]
        for j in range(i + 1, n):
            if A[i] & (1 << (n - 1 - j)):
                x[i] ^= x[j]
    return x

# Example usage
if __name__ == "__main__":
    # Matrix A: binary 3x3 system
    # A = [
    #   [1, 0, 1],
    #   [1, 1, 0],
    #   [0, 1, 1]
    # ]
    A = [0b101, 0b110, 0b011]
    b = [1, 0, 1]
    solution = solve_binary_system(A, b)
    print("Solution over GF(2):", solution)
