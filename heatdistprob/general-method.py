# Problem: Simulate steady-state heat distribution on a 2D plate using the finite difference method

def heat_distribution_general(grid, tolerance=0.01, max_iter=1000):
    rows = len(grid)
    cols = len(grid[0])
    iteration = 0

    while iteration < max_iter:
        diff = 0
        new_grid = [row[:] for row in grid]

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                avg = 0.25 * (grid[i+1][j] + grid[i-1][j] +
                              grid[i][j+1] + grid[i][j-1])
                diff = max(diff, abs(avg - grid[i][j]))
                new_grid[i][j] = avg

        grid = new_grid
        iteration += 1
        if diff < tolerance:
            break

    return grid, iteration

# Example usage
if __name__ == "__main__":
    # 5x5 grid with boundary heat = 100 and interior = 0
    grid = [[100 if i == 0 or i == 4 or j == 0 or j == 4 else 0 for j in range(5)] for i in range(5)]
    final_grid, iterations = heat_distribution_general(grid)
    print(f"Converged in {iterations} iterations")
    for row in final_grid:
        print(["{:.2f}".format(cell) for cell in row])
