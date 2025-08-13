def beautifulDays(i, j, k):
    count = 0
    for num in range(i, j+1):
        rev = int(str(num)[::-1])   # reverse the number
        pro = abs(num - rev)        # absolute difference
        if pro % k == 0:
            count += 1
    return count

# Input in one line
i, j, k = map(int, input().split())

print(beautifulDays(i, j, k))
