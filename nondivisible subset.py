def nonDivisibleSubset(k, s):
    freq = [0] * k
    for num in s:
        freq[num % k] += 1
    count = min(freq[0], 1)
    for i in range(1, (k//2)+1):
        if i != k - i:
            count += max(freq[i], freq[k-i])
        else:
            count += 1
    return count

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    print(nonDivisibleSubset(k, s))
