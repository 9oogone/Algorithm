from collections import Counter
import sys
input=sys.stdin.readline
n,m =map(int,input().split())
l=[input().strip() for _ in range(n+m)]
lc=Counter(l)
ans = []
for k,v in lc.items():
    if v==2:
        ans.append(k)
ans.sort()
print(len(ans))
for i in ans:
    print(i)