import sys
input = sys.stdin.readline
n = int(input())
arr = [0]+list(map(int, input().split()))
if n == 1:
    print(arr[1])
    sys.exit()
dp = [0]*(n+1)
dp[1]=arr[1]
for i in range(2, n + 1):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp[1:n+1]))