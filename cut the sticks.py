def cutTheSticks(arr):
    res = []
    while arr:
        res.append(len(arr))
        min_val = min(arr)
        arr = [x - min_val for x in arr if x - min_val > 0]
    return res

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    res = cutTheSticks(arr)
    for r in res:
        print(r)
