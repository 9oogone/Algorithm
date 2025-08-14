import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0]*n
for i in range(n):
    dp[i] = arr[i]  # 기본값: 자기 자신만 선택
    for j in range(i):  # 과거만 참조
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))