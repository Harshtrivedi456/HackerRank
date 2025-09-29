def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n+1))
    if n % (2*k) != 0:
        return [-1]
    res = []
    add = True
    for i in range(1, n+1):
        if add:
            res.append(i + k)
        else:
            res.append(i - k)
        if i % k == 0:
            add = not add
    return res

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ans = absolutePermutation(n, k)
        print(' '.join(map(str, ans)))
