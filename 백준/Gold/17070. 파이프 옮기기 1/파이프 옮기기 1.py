import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

# 방향 조절
right = (0,1)   # 가로
slide = (1,1)   # 대각선
up = (1,0)      # 세로

# dp[x][y][0] = (x,y)에서 가로 상태일 때 경로 수
# dp[x][y][1] = 대각선 상태일 때 경로 수
# dp[x][y][2] = 세로 상태일 때 경로 수
dp = [[[-1]*3 for _ in range(n)] for _ in range(n)]

def dfs(x,y,pos):
    # 종료 조건
    if x == n-1 and y == n-1:
        return 1
    
    # pos를 인덱스로 변환
    if pos == right:
        p_idx = 0
    elif pos == slide:
        p_idx = 1
    else:  # up
        p_idx = 2
    
    # 이미 계산된 값이 있으면 반환
    if dp[x][y][p_idx] != -1:
        return dp[x][y][p_idx]
    
    ways = 0
    
    if pos == right:  # 가로
        # 1. 오른쪽
        rx = x+right[0]
        ry = y+right[1]
        if 0<=rx<n and 0<=ry<n and graph[rx][ry]==0:
            ways += dfs(rx,ry,right)
        # 2. 대각선
        sx = x+slide[0]
        sy = y+slide[1]
        if 0<=sx<n and 0<=sy<n and graph[sx][sy]==0 and graph[sx][y]==0 and graph[x][sy]==0:
            ways += dfs(sx,sy,slide)
    
    elif pos == up:  # 세로
        # 1. 아래
        ux = x+up[0]
        uy = y+up[1]
        if 0<=ux<n and 0<=uy<n and graph[ux][uy]==0:
            ways += dfs(ux,uy,up)
        # 2. 대각선
        sx = x+slide[0]
        sy = y+slide[1]
        if 0<=sx<n and 0<=sy<n and graph[sx][sy]==0 and graph[sx][y]==0 and graph[x][sy]==0:
            ways += dfs(sx,sy,slide)
    
    else:  # slide (대각선)
        # 1. 오른쪽
        rx = x+right[0]
        ry = y+right[1]
        if 0<=rx<n and 0<=ry<n and graph[rx][ry]==0:
            ways += dfs(rx,ry,right)
        # 2. 대각선
        sx = x+slide[0]
        sy = y+slide[1]
        if 0<=sx<n and 0<=sy<n and graph[sx][sy]==0 and graph[sx][y]==0 and graph[x][sy]==0:
            ways += dfs(sx,sy,slide)
        # 3. 아래
        ux = x+up[0]
        uy = y+up[1]
        if 0<=ux<n and 0<=uy<n and graph[ux][uy]==0:
            ways += dfs(ux,uy,up)
    
    dp[x][y][p_idx] = ways
    return ways

print(dfs(0,1,right))
