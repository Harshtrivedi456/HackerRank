
def pickingNumbers(a):
    # Count frequency of each number
    freq = [0] * 101
    for num in a:
        freq[num] += 1

    # Check max length from adjacent frequencies
    max_len = 0
    for i in range(1, 101):
        max_len = max(max_len, freq[i] + freq[i - 1])

    return max_len
