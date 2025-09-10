from collections import deque
def solution(maps):
    n = len(maps[0])
    m = len(maps)
    visited = [[False]*n for _ in range(m)]
    
    def bfs(x,y):
        # 델타
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        q = deque([(x,y)])
        while q:
            qx,qy = q.popleft()
            for i in range(4):
                nx = qx+dx[i]
                ny = qy+dy[i]
                
                if 0<=nx<m and 0<=ny<n:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        if maps[nx][ny]==1:
                            maps[nx][ny]=(maps[qx][qy]+1)
                            q.append((nx,ny))
                            if nx == (m-1) and ny == (n-1):
                                return maps[nx][ny]
        return -1
    
    maps[0][0]=1
    visited[0][0]=True                                

    return bfs(0,0)

        
            