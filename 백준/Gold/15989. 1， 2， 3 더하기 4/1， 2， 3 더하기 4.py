import sys 
input=sys.stdin.readline

MAX=10001
dp = [1]*MAX

for i in range(2,MAX):
    dp[i]+=dp[i-2]

for j in range(3,MAX):
    dp[j]+=dp[j-3]

t = int(input())
for tc in range(t):
    N=int(input())
    print(dp[N])
