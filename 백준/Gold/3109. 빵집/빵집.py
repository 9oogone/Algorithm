import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
r,c = map(int,input().split())
board = [list(input().strip()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]

dx = [-1,0,1]
dy = [1,1,1]

cnt = 0
def dfs(x,y):
    visited[x][y]=True
    
    if y == c-1:
        global cnt
        cnt += 1
        return True
    
    for i in range(3):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<r and 0<=ny<c: # out of range 방지
            if not visited[nx][ny] and board[nx][ny]!='x':
                if dfs(nx,ny):
                    return True # 재귀            
    return False

for i in range(r):
    visited[i][0]=True
    dfs(i,0) 

print(cnt)