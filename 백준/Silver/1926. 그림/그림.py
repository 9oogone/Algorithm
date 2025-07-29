import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split()) # n 세로 m 가로
picture = [list(map(int,input().split())) for _ in range(n)] # 그림
 
visited = [[False]*m for _ in range(n)] # 방문 처리
cnt = 0 # 그림의 개수 
width = 0 # 가장 넓은 그림의 넓이

def bfs(x,y):
    global cnt 
    global width
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    q = deque([(x,y)]) 
    visited[x][y] = True # 첫 번째 1 방문처리
    area = 1 # 한 그림의 넓이
    
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if picture[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    area += 1  # 연결된 그림이므로 넓이 증가

    cnt += 1              # 이 BFS로 하나의 그림 탐색 완료
    width = max(width, area)  # 가장 넓은 그림 갱신

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

print(cnt)
print(width)