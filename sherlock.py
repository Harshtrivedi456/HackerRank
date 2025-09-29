import math

def squares(a, b):
    return int(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        print(squares(a, b))
