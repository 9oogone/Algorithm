import sys
input=sys.stdin.readline
n=int(input())
come=[input().strip() for _ in range(n)]
out=[input().strip() for _ in range(n)]
cd={v:idx for idx,v in enumerate(come)}

visited = [False] * n
p = 0
ans = 0

for car in out:
    cur_idx = cd[car]
    if cur_idx != p:
        ans += 1
    visited[cur_idx] = True
    while p < n and visited[p]:
        p += 1

print(ans)