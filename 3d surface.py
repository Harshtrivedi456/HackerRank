def surfaceArea(A):
    H, W = len(A), len(A[0])
    total = 0
    for i in range(H):
        for j in range(W):
            total += 2  # top and bottom
            # front
            total += A[i][j] if i == 0 else max(0, A[i][j] - A[i-1][j])
            # back
            total += A[i][j] if i == H-1 else max(0, A[i][j] - A[i+1][j])
            # left
            total += A[i][j] if j == 0 else max(0, A[i][j] - A[i][j-1])
            # right
            total += A[i][j] if j == W-1 else max(0, A[i][j] - A[i][j+1])
    return total

if __name__ == "__main__":
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    print(surfaceArea(A))
