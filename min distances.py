def minimumDistances(a):
    min_dist = float('inf')
    pos = {}
    for i, val in enumerate(a):
        if val in pos:
            min_dist = min(min_dist, i - pos[val])
        pos[val] = i
    return min_dist if min_dist != float('inf') else -1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(minimumDistances(a))
