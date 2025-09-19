from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
nc = list(map(int,input().split()))
m = int(input())
mc = list(map(int,input().split()))
nc = Counter(nc)
ans = []
for i in mc:
    ans.append(nc[i])
print(*ans)