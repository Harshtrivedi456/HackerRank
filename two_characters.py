def alternate(s):
    max_length = 0
    unique_chars = list(set(s))

    # Try every pair of distinct characters
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            ch1, ch2 = unique_chars[i], unique_chars[j]

            # Filter the string to only contain the current pair
            filtered = [c for c in s if c == ch1 or c == ch2]

            # Check if the filtered string alternates properly
            valid = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k - 1]:
                    valid = False
                    break

            if valid:
                max_length = max(max_length, len(filtered))

    return max_length if max_length > 1 else 0


# Input handling like on HackerRank
if __name__ == '__main__':
    n = int(input())              # Length of the string
    s = input().strip()          # The string
    result = alternate(s)
    print(result)
