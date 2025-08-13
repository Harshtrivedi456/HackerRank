def angryProfessor(k, a):
    # k = threshold (minimum students on time)
    # a = arrival times list
    on_time = sum(1 for time in a if time <= 0)
    return "NO" if on_time >= k else "YES"

t = int(input())  # number of test cases
for _ in range(t):
    n_students, k = map(int, input().split())  # n = total students, k = threshold
    a = list(map(int, input().split()))  # arrival times
    print(angryProfessor(k, a))
