import sys
input = sys.stdin.readline
from collections import deque

m,n=map(int,input().split())
tomato=[list(map(int,input().split())) for _ in range(n)]
if not any(1 in row for row in tomato):
    print(-1)
    sys.exit()
if not any(0 in row for row in tomato):
    print(0)
    sys.exit()

visited = [[False]*m for _ in range(n)]
def bfs():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    
    for y in range(n):
        for x in range(m):
            if tomato[y][x] == 1:
                q.append((y, x))
                visited[y][x] = True
    
    while q:
        qy,qx = q.popleft()
        visited[qy][qx]=True
        for d in range(4):
            nx = qx+dx[d]
            ny = qy+dy[d]
            if 0<=nx<m and 0<=ny<n:
                if not visited[ny][nx]:
                    if tomato[ny][nx] == 0:
                        q.append((ny,nx))
                        tomato[ny][nx]=tomato[qy][qx]+1                       
    return


bfs()

ans = 0
for i in tomato:
    if 0 in i:
        print(-1)
        sys.exit()
    if ans<max(i):
        ans=max(i)

print(ans-1)