import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print(1%10007)
    sys.exit()
if n == 2:
    print(3%10007)
    sys.exit()
if n == 3:
    print(5%10007)
    sys.exit()
#2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램
dp = [0]*(n+1)
dp[1]=1
dp[2]=3
dp[3]=5

for i in range(4, n + 1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007 

print(dp[n] % 10007)