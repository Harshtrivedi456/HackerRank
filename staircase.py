n = int(input())# height of staircase

for i in range(1, n+1):
    print(" " * (n - i) + "#" * i)
