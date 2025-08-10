import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
r,c,k = map(int,input().split()) # r = 열의 수 c = 한 행에 몇 개 들어있는지 k=k만큼만 움직여서 도착해야됨
board = [list(input().strip()) for _ in range(r)]
# T는 못 가는 부분임
# k만큼 이동해야 됨
# 시작점 = 왼쪽 아래 (r-1)(0)
# 도착점 = 오른쪽 맨 위 (0)(c-1)
# 3x4면 (rxc) 
visited = [[False]*c for _ in range(r)]
ans = 0
# 델타
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 도착점
hx = 0
hy = c-1

def dfs(x,y,move):
    global ans    
    # 움직임
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<r and 0<=ny<c: # out of range 검사
            if nx==hx and ny==hy: # 집 검사
                if move == k-1: # 집인데 거리도 맞으면
                    ans+=1 # 개수 +1
                continue            
            if not visited[nx][ny] and board[nx][ny]!='T': # 벽인지, 이미 간 곳인지 검사
                visited[nx][ny] = True
                if move+1 < k:
                    dfs(nx,ny,move+1)
                visited[nx][ny] = False # 다른 경로에서는 방문할수도 있으니까
    return
# 시작점에서 출발
visited[r-1][0] = True
dfs(r-1,0,1)
                
print(ans)                