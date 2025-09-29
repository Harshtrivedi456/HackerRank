def howManyGames(p, d, m, s):
    count = 0
    while s >= p:
        s -= p
        count += 1
        p = max(p - d, m)
    return count

if __name__ == "__main__":
    p, d, m, s = map(int, input().split())
    print(howManyGames(p, d, m, s))
