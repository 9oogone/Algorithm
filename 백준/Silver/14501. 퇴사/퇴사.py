import sys
input=sys.stdin.readline
n=int(input())
table=[[]]+[list(map(int,input().split())) for _ in range(n)]

dp=[0]*(n+2)

for i in range(n,0,-1):
    t,p=table[i]
    
    if i+t>n+1:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(p+dp[i+t],dp[i+1])

print(dp[1]) 