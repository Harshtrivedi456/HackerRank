def utopianTree(cycles):
    height = 1
    for i in range(cycles):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1
    return height

t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Number of growth cycles
    print(utopianTree(n))
