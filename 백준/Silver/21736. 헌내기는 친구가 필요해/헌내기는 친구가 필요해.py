import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
campus = [list(input().strip())for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다
def bfs(x,y):
    global p
    # 델타
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque([(x,y)])
    while q:
        qx,qy = q.popleft()
        visited[qx][qy]=True
        for i in range(4):
            nx = qx+dx[i]
            ny = qy+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny]=True
                if campus[nx][ny]!='X':
                    q.append((nx,ny))
                    if campus[nx][ny]=='P':
                        p+=1 
    return
p = 0
for i in range(n):
    for j in range(m):
        if campus[i][j]=='I':
            bfs(i,j)
            break
print(p) if p>0 else print('TT')