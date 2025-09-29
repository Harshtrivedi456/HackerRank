def equalizeArray(arr):
    from collections import Counter
    freq = Counter(arr)
    return len(arr) - max(freq.values())

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(equalizeArray(arr))
