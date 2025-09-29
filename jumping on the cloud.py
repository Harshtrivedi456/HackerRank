def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    i = 0
    while True:
        # jump to next cloud
        i = (i + k) % n
        # decrease energy: 1 for jump + 2 if thunderhead
        energy -= 1 + 2 * c[i]
        if i == 0:
            break
    return energy

# Input
n, k = map(int, input().split())
c = list(map(int, input().split()))
print(jumpingOnClouds(c, k))
