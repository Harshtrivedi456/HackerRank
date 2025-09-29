def repeatedString(s, n):
    count_a = s.count('a')
    full = n // len(s)
    rem = n % len(s)
    return count_a * full + s[:rem].count('a')

if __name__ == "__main__":
    s = input()
    n = int(input())
    print(repeatedString(s, n))
