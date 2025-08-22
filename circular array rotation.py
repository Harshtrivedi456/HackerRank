def circularArrayRotation(a, k, queries):
    n = len(a)
    k = k % n   # Effective rotations
    result = []
    
    for q in queries:
        result.append(a[(q - k) % n])
    
    return result


# ---- Taking input from user ----
# First line: n (size), k (rotations), q (number of queries)
n, k, q = map(int, input().split())

# Second line: array elements
a = list(map(int, input().split()))

# Next q lines: queries (indices)
queries = []
for _ in range(q):
    queries.append(int(input()))

# Call function and print results
output = circularArrayRotation(a, k, queries)
for val in output:
    print(val)
