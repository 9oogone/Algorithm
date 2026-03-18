import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split()) # n = 4(행 개수) m = 6(열 개수, 한 행에 몇 개 들어가는지)
maze = [list(map(int,input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def bfs(x,y):
    q = deque([(x,y)])
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    while q:
        qx,qy = q.popleft()
        if qx == n-1 and qy == m-1:
            return
        for i in range(4):
            nx = qx+dx[i]
            ny = qy+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if maze[nx][ny]==1 and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    maze[nx][ny]=maze[qx][qy]+1
                    
visited[0][0] = True
bfs(0,0)
print(maze[n-1][m-1])