from collections import Counter

def happyLadybugs(b):
    count = Counter(b)
    if '_' in count:
        for k, v in count.items():
            if k != '_' and v == 1:
                return "NO"
        return "YES"
    else:
        for i in range(len(b)):
            if (i > 0 and b[i] == b[i-1]) or (i < len(b)-1 and b[i] == b[i+1]):
                continue
            else:
                return "NO"
        return "YES"

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        b = input().strip()
        print(happyLadybugs(b))
