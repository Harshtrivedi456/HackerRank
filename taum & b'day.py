def taumBday(b, w, x, y, z):
    cost_black = min(x, y + z)
    cost_white = min(y, x + z)
    return b * cost_black + w * cost_white


if __name__ == "__main__":
    t = int(input().strip())   # number of test cases
    for _ in range(t):
        b, w = map(int, input().split())
        x, y, z = map(int, input().split())
        print(taumBday(b, w, x, y, z))
