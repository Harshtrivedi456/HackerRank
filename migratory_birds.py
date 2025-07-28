def migratoryBirds(arr):
    bird_count = [0] * 6  # bird types are 1 to 5

    for bird in arr:
        bird_count[bird] += 1

    max_count = max(bird_count)
    for i in range(1, 6):
        if bird_count[i] == max_count:
            return i

# HackerRank Input Format
n = int(input())
arr = list(map(int, input().rstrip().split()))
print(migratoryBirds(arr))
