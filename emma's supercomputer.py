def twoPluses(grid):
    n, m = len(grid), len(grid[0])
    def max_arm(i, j):
        if grid[i][j] != 'G': return 0
        arm = 0
        while i-arm >= 0 and i+arm < n and j-arm >= 0 and j+arm < m:
            if grid[i-arm][j] == grid[i+arm][j] == grid[i][j-arm] == grid[i][j+arm] == 'G':
                arm += 1
            else:
                break
        return arm

    pluses = []
    for i in range(n):
        for j in range(m):
            arm = max_arm(i, j)
            for a in range(1, arm+1):
                cells = {(i,j)}
                for d in range(1, a):
                    cells.update({(i+d,j),(i-d,j),(i,j+d),(i,j-d)})
                pluses.append(cells)
    max_prod = 0
    for i in range(len(pluses)):
        for j in range(i+1, len(pluses)):
            if pluses[i].isdisjoint(pluses[j]):
                max_prod = max(max_prod, len(pluses[i])*len(pluses[j]))
    return max_prod

if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    print(twoPluses(grid))
