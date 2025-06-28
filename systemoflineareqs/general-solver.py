# Problem: Solve a system of linear equations Ax = b using Gaussian elimination

def gaussian_elimination(A, b):
    n = len(A)

    # Forward elimination
    for i in range(n):
        # Make A[i][i] == 1 by dividing row
        factor = A[i][i]
        if factor == 0:
            raise ValueError("Singular matrix")
        for j in range(i, n):
            A[i][j] = A[i][j] / factor
        b[i] = b[i] / factor

        # Eliminate other rows
        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            b[k] -= factor * b[i]

    # Back substitution
    x = [0 for _ in range(n)]
    for i in reversed(range(n)):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
    return x

# Example usage
if __name__ == "__main__":
    A = [
        [2, 1],
        [1, 3]
    ]
    b = [8, 13]
    solution = gaussian_elimination([row[:] for row in A], b[:])
    print("Solution:", solution)
