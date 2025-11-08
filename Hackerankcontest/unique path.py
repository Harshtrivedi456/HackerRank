
a, b = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(a)]

if mat[0][0] == 1 or mat[a-1][b-1] == 1:
    print(0)
else:
    ab = [[0]*b for _ in range(a)]
    ab[0][0] = 1

    for i in range(a):
        for j in range(b):
            if mat[i][j] == 1:
                ab[i][j] = 0
            else:
                if i > 0:
                    ab[i][j] += ab[i-1][j]
                if j > 0:
                    ab[i][j] += ab[i][j-1]
    print(ab[a-1][b-1])
