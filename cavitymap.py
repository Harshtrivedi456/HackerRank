def cavityMap(grid):
    n = len(grid)
    grid = [list(row) for row in grid]
    for i in range(1, n-1):
        for j in range(1, n-1):
            if (grid[i][j] > grid[i-1][j] and
                grid[i][j] > grid[i+1][j] and
                grid[i][j] > grid[i][j-1] and
                grid[i][j] > grid[i][j+1]):
                grid[i][j] = 'X'
    return [''.join(row) for row in grid]

if __name__ == "__main__":
    n = int(input())
    grid = [input() for _ in range(n)]
    result = cavityMap(grid)
    print('\n'.join(result))
