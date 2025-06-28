# Problem: Solve N-Queens using backtracking and bit vector (bit hack) method

# General method: classic backtracking
def solve_nqueens_backtracking(n):
    def is_safe(queens, row, col):
        for r in range(row):
            if queens[r] == col or abs(queens[r] - col) == row - r:
                return False
        return True

    def backtrack(row, queens):
        if row == n:
            solutions.append(list(queens))
            return
        for col in range(n):
            if is_safe(queens, row, col):
                queens[row] = col
                backtrack(row + 1, queens)

    solutions = []
    backtrack(0, [0] * n)
    return len(solutions)

# Bit hack method
def solve_nqueens_bitwise(n):
    def solve(row, cols, diag1, diag2):
        if row == n:
            return 1
        count = 0
        available = (~(cols | diag1 | diag2)) & ((1 << n) - 1)
        while available:
            p = available & -available
            available -= p
            count += solve(row + 1, cols | p, (diag1 | p) << 1, (diag2 | p) >> 1)
        return count

    return solve(0, 0, 0, 0)

# Example usage
n = 8
print("General (backtracking):", solve_nqueens_backtracking(n))
print("Bit Hack (bit vector):", solve_nqueens_bitwise(n))
