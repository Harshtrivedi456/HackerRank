def pageCount(n, p):
    return min(p // 2, n // 2 - p // 2)

# Input
n = int(input())
p = int(input())

# Output
print(pageCount(n, p))
