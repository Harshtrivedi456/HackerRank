def serviceLane(n, cases, width):
    return [min(width[i:j+1]) for i, j in cases]

if __name__ == "__main__":
    n, t = map(int, input().split())
    width = list(map(int, input().split()))
    cases = [tuple(map(int, input().split())) for _ in range(t)]
    result = serviceLane(n, cases, width)
    print('\n'.join(map(str, result)))
