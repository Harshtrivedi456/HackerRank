def flatlandSpaceStations(n, c):
    c.sort()
    max_distance = 0

    # Check distance for first city (before first station)
    max_distance = max(max_distance, c[0] - 0)

    # Check distances between stations
    for i in range(1, len(c)):
        # distance to nearest city is half the gap between two stations
        gap = (c[i] - c[i - 1]) // 2
        max_distance = max(max_distance, gap)

    # Check distance for last city (after last station)
    max_distance = max(max_distance, (n - 1) - c[-1])

    return max_distance


# reading inputs in HackerRank style
n, m = map(int, input().split())  # n: number of cities, m: number of stations
c = list(map(int, input().split()))

print(flatlandSpaceStations(n, c))
