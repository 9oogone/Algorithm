import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 
while True:
    w, h = map(int, input().split()) #w개씩 h줄 
    if w == 0 and h == 0:   # 종료 조건
        break
    # h줄에 걸쳐 w개의 0/1이 공백으로 주어짐
    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
        
    def dfs(x,y):
        # 델타
        dx = [0,0,-1,1,-1,1,-1,1]
        dy = [-1,1,0,0,-1,-1,1,1]
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    if grid[nx][ny]==1:
                        dfs(nx,ny)
        return
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and grid[i][j]==1:
                dfs(i,j)
                cnt +=1
    
    print(cnt)