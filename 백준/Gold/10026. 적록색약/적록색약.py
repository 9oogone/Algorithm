import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
art = [list(input().strip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
rgvisited = [[False]*n for _ in range(n)]

# 일반인 BFS
def bfs(x,y):
    # 델타
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque([(x,y)])
    visited[x][y]=True
    while q:
        qx,qy = q.popleft()
        for i in range(4):
            nx = qx+dx[i]
            ny = qy+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and art[qx][qy]==art[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny]=True        
    return

general = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            general += 1

# 적록색약 (R=G)
def rgbfs(x,y):
    # 델타
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque([(x,y)])
    rgvisited[x][y]=True
    while q:
        qx,qy = q.popleft()
        for i in range(4):
            nx = qx+dx[i]
            ny = qy+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not rgvisited[nx][ny]:
                    # 아닐 때
                    if art[qx][qy]=='B' and art[nx][ny]=='B':
                        q.append((nx,ny))
                        rgvisited[nx][ny] = True
                    if (art[qx][qy]=='R'or art[qx][qy]=='G') and (art[nx][ny]=='R'or art[nx][ny]=='G'):
                        q.append((nx,ny))
                        rgvisited[nx][ny] = True    
    return

rg = 0
for i in range(n):
    for j in range(n):
        if not rgvisited[i][j]:
            rgbfs(i,j)
            rg += 1
print(general,rg) 