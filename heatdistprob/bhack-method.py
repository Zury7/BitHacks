# Problem: Bit-level approximation of heat spread using binary states (0=cold, 1=hot)
# Suitable for embedded or hardware-constrained systems

def heat_distribution_bitwise(grid, max_iter=10):
    rows = len(grid)
    cols = len(grid[0])
    curr = [int("".join(str(cell) for cell in row), 2) for row in grid]

    for _ in range(max_iter):
        new = [0] * rows
        for i in range(1, rows - 1):
            row_above = curr[i - 1]
            row_curr  = curr[i]
            row_below = curr[i + 1]

            next_row = 0
            for j in range(1, cols - 1):
                # Extract neighborhood
                mask = 0b111 << (cols - j - 2)
                nb = ((row_above & mask) >> (cols - j - 2)) + \
                     ((row_curr & mask) >> (cols - j - 2)) + \
                     ((row_below & mask) >> (cols - j - 2))

                # If at least 4 of 9 bits are hot, turn on
                if bin(nb).count('1') >= 4:
                    next_row |= (1 << (cols - j - 1))
            new[i] = next_row
        curr = new

    # Convert back to grid
    return [[(curr[i] >> (cols - j - 1)) & 1 for j in range(cols)] for i in range(rows)]

# Example usage
if __name__ == "__main__":
    # 5x5 binary grid, center hot
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    result = heat_distribution_bitwise(grid)
    print("Binary heat pattern:")
    for row in result:
        print(" ".join(str(cell) for cell in row))
