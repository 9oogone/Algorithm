import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

r,c = map(int,input().split()) #세로 r칸 가로 c칸
board = [list(input().strip()) for _ in range(r)]
visited = set()

def dfs(x,y,mask,length):
    global ans
    if (x, y, mask) in visited:
        return
    visited.add((x, y, mask))
    ans = max(ans,length)
    # 델타
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            b = 1 << ord(board[nx][ny])-ord('A')
            if not (mask & b):
                dfs(nx,ny,mask|b,length+1)

bit = 1 << (ord(board[0][0]) - ord('A'))
ans = 0
dfs(0, 0, bit, 1)

print(ans)