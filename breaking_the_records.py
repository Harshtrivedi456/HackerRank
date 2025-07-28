def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    max_count = 0
    min_count = 0

    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1

    return [max_count, min_count]

# Input reading as per HackerRank format
n = int(input())
scores = list(map(int, input().split()))

# Output
result = breakingRecords(scores)
print(*result)
