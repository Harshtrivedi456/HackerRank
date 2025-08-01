
def hurdleRace(k, height):
    # Write your code here
    max_height=max(height)
    if max_height>k:
        return max_height-k
    else:
        return 0            
n,k=list(map(int,input().split()))
# k=int(input())
height=list(map(int,input().split()))
print(hurdleRace(k,height))
