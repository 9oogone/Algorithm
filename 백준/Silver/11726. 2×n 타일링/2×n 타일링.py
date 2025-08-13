import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

# n이 1, 2일 때 예외 처리
if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)
