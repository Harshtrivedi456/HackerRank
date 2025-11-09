a= input().strip()
n= int(input())
b= input().split()

length = len(a)
dp =[False]*(length+1)
dp[0]=True

for i in range(1,length+1):
    for j in range(i):
        word=a[j:i]
        if dp[j] and word in b:
            dp[i]=True
            break
            
if dp[length]:
    print(1)
else:
    print(0)
