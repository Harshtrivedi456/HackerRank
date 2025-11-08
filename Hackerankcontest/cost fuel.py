def costfuel(A, B):
    n = len(A)
    intial = 0
    tank = 0
    total = 0

    for i in range(n):
        diff = A[i] - B[i]
        tank += diff
        total += diff

        if tank < 0:
            intial = i + 1
            tank = 0

    if total >= 0:
        return intial % n
    else:
        return -1


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(costfuel(A, B))
