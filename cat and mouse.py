def catAndMouse(x, y, z):
    if abs(x - z) < abs(y - z):
        return "Cat A"
    elif abs(x - z) > abs(y - z):
        return "Cat B"
    else:
        return "Mouse C"

n = int(input())
for _ in range(n):
    x, y, z = map(int, input().split())
    print(catAndMouse(x, y, z))
