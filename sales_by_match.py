def sockMerchant(n, ar):
    color_count = {}
    for sock in ar:
        if sock in color_count:
            color_count[sock] += 1
        else:
            color_count[sock] = 1

    pairs = 0
    for count in color_count.values():
        pairs += count // 2

    return pairs

# Input section
n = int(input())
ar = list(map(int, input().split()))

print(sockMerchant(n, ar))
