import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
N,M = map(int,input().split()) # N행 M열 # 한 줄에 M 개 입력됨
r,c,d = map(int,input().split()) # 처음 위치 (r,c) 바라보는 방향 d
room = [list(map(int,input().split())) for _ in range(N)] # 청소해야 하는 방
visited = [[False]*M for _ in range(N)] # 청소 여부 기록
clean = 0 # 청소 횟수 기록

def simulation(x,y):
    global d
    global clean
    # 델타
    dx = [-1, 0, 1, 0] # 북 동 남 서 
    dy = [0, 1, 0, -1]

    # 1. 현재 칸이 아직 청소되지 않은 경우(0), 현재 칸을 청소(2)한다.
    if room[x][y]==0:
        room[x][y]=2
        clean += 1
        
    # 사방 살피기
    for _ in range(4):
        d = (d+3) % 4 # 반시계 회전
        nx = x+dx[d]  # 바라보는 방향의 앞칸
        ny = y+dy[d]
        
        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
            # 3-1. 반시계 방향으로 90도 회전한다.
            # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            # 앞칸이 청소되지 않은 빈 칸이면 전진!
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            simulation(nx, ny) # 전진 # 1번으로 돌아간다
            return # 종료
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    # 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    bx = x - dx[d]
    by = y - dy[d]
    if 0 <= bx < N and 0 <= by < M and room[bx][by] != 1:
        simulation(bx,by)
    # 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
    else:
        return

simulation(r,c)

print(clean)