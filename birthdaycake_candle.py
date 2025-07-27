def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = 0
    for height in candles:
        if height == tallest:
            count += 1
    return count

size = int(input())
candles = list(map(int, input().split()))

occurrence = birthdayCakeCandles(candles)
print(occurrence)
