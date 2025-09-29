def gridSearch(G, P):
    R, C = len(G), len(G[0])
    r, c = len(P), len(P[0])
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            if all(G[i+k][j:j+c] == P[k] for k in range(r)):
                return "YES"
    return "NO"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        R, C = map(int, input().split())
        G = [input() for _ in range(R)]
        r, c = map(int, input().split())
        P = [input() for _ in range(r)]
        print(gridSearch(G, P))
