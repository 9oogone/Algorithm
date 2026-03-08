import sys
input = sys.stdin.readline
from collections import deque

tc = int(input()) #테스트케이스의 수
for _ in range(tc):
    m, n, k = map(int,input().split()) # m = 가로 길이 # n = 세로 길이 # k = 배추 개수
    ground = [[0]*m for _ in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        ground[y][x] = 1

    visited = [[False]*m for _ in range(n)]
    worm = 0


    def bfs(x,y): 
        global worm
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        
        q=deque([(x,y)])
        visited[x][y] = True # 방문 처리
        
        while q:
            qx, qy = q.popleft()
            for i in range(4):
                nx = qx + dx[i]
                ny = qy + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if ground[nx][ny]==1 and not visited[nx][ny]:
                        q.append([nx,ny])
                        visited[nx][ny]=True
        
        worm += 1
    
    for i in range(n): # 8 # 몇 행의
        for j in range(m): # 10 # 몇 열인지
            if ground[i][j] == 1 and not visited[i][j]: 
                bfs(i,j)

    print(worm)