def extraLongFactorials(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    print(fact)

# Input
n = int(input())
extraLongFactorials(n)
