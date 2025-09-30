def jumpingOnClouds(c):
    jumps = 0
    i = 0
    n = len(c)

    while i < n - 1:  # stop before last cloud
        # if possible, jump 2 steps, otherwise jump 1
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1

    return jumps


# Input handling for HackerRank
n = int(input().strip())
c = list(map(int, input().rstrip().split()))

print(jumpingOnClouds(c))
