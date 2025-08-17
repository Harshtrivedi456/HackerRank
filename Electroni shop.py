def getMoneySpent(keyboards, drives, b):
    max_spend = -1  
    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= b and total > max_spend:
                max_spend = total
    return max_spend




b, n, m = map(int, input().split())           # e.g. 10 2 3
keyboards = list(map(int, input().split()))   # e.g. 3 1
drives = list(map(int, input().split()))      # e.g. 5 2 8

# Output
print(getMoneySpent(keyboards, drives, b))
