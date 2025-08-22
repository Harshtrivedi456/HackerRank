def saveThePrisoner(n, m, s):
    return ((s - 1 + m - 1) % n) + 1

# Input
t = int(input())  # number of test cases
for _ in range(t):
    n, m, s = map(int, input().split())
    print(saveThePrisoner(n, m, s))
