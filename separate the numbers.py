def separateNumbers(s):
    n = len(s)
    
    for i in range(1, n // 2 + 1):
        first = int(s[:i])
        next_num = first
        temp = s[:i]
        
        while len(temp) < n:
            next_num += 1
            temp += str(next_num)
        
        if temp == s:
            print(f"YES {first}")
            return
    
    print("NO")

# Input
q = int(input())
for _ in range(q):
    s = input().strip()
    separateNumbers(s)
