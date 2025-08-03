import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
estate = [list(map(int,input().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def bfs(x,y,num):
    #델타
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    q = deque([(x,y)])
    while q:
        qx,qy = q.popleft()
        for i in range(4):
            nx = qx+dx[i]
            ny = qy+dy[i]
        
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if estate[nx][ny]==1:
                        num+=1
                        q.append((nx,ny))               
    return lst.append(num)
cnt = 0 # 단지 수
lst = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and estate[i][j]==1:
            visited[i][j] = True
            bfs(i,j,1)

print(len(lst))
lst.sort()
for i in lst:
    print(i)