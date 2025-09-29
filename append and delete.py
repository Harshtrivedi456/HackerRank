def appendAndDelete(s, t, k):
    # Find common prefix length
    commonLength = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            commonLength += 1
        else:
            break
    
    # Minimum operations needed
    minOps = (len(s) - commonLength) + (len(t) - commonLength)
    
    if k < minOps:
        return "No"
    elif (k - minOps) % 2 == 0:
        return "Yes"
    elif k >= len(s) + len(t):
        # Can delete all of s and write t from scratch
        return "Yes"
    else:
        return "No"

# Input handling
s = input()
t = input()
k = int(input())
print(appendAndDelete(s, t, k))
