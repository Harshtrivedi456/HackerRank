import math

def encryption(s):
    s = s.replace(" ", "")
    L = len(s)
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))
    if rows*cols < L:
        rows += 1
    res = []
    for c in range(cols):
        res.append(''.join(s[r*cols + c] for r in range(rows) if r*cols + c < L))
    return ' '.join(res)

if __name__ == "__main__":
    s = input()
    print(encryption(s))
