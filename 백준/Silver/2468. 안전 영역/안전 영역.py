import sys
input = sys.stdin.readline
from collections import deque

n=int(input())
area = [list(map(int,input().split())) for _ in range(n)]
# 
max_h = max(max(row) for row in area)

def bfs(sx, sy, h, vis):
    q = deque([(sx, sy)])
    vis[sx][sy] = True
    while q:
        x, y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and not vis[nx][ny] and area[nx][ny] > h:
                vis[nx][ny] = True
                q.append((nx, ny))

ans = 0
for h in range(0, max_h):  # 0 포함, max_h 제외
    vis = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not vis[i][j] and area[i][j] > h:
                cnt += 1
                bfs(i, j, h, vis)
    ans = max(ans, cnt)

print(ans)