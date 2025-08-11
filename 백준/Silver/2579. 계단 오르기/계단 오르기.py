import sys
input = sys.stdin.readline
n = int(input())
a = [0] + [int(input()) for _ in range(n)] 

if n < 3:
    print(sum(a))
    sys.exit()

dp = [0]*(n+1)
# 초기 값
dp[1]=a[1]
dp[2]=a[1]+a[2]
dp[3]=max(a[1]+a[3],a[2]+a[3])
for i in range(4,n+1):
    dp[i]=max(dp[i-2] + a[i], dp[i-3] + a[i-1] + a[i])

print(dp[n])