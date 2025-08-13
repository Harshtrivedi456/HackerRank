def viralAdvertising(n):
    day=1
    node=2
    count=2
    while day<n:
        node=node*3
        nextnode=(node//2)
        count=nextnode
        day+=1
    return sum(count)

n=int(input())
print(viralAdvertising(n))
