# Input the string
s = input()

# Input the number of queries
n = int(input())

# Read all queries into a list
queries = [int(input()) for _ in range(n)]

# Set to store all possible uniform weights
weights = set()

count = 0
prev = ''

# Loop through each character in the string
for ch in s:
    if ch == prev:
        count += 1
    else:
        count = 1
        prev = ch
    weight = (ord(ch) - 96) * count
    weights.add(weight)

# Check each query
for q in queries:
    if q in weights:
        print("Yes")
    else:
        print("No")
