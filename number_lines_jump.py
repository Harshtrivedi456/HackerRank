def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return "YES"
    return "NO"

# Read input from stdin
x1, v1, x2, v2 = map(int, input().split())

# Call and print the result
print(kangaroo(x1, v1, x2, v2))
