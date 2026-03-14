import sys
input=sys.stdin.readline
from collections import deque

N,M=map(int,input().split())# 총 N줄 한 줄에 M개 있음 
iceberg=[list(map(int,input().split())) for _ in range(N)]
year = 0
# 델타
dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 빙산 분리됐는지 아닌지 확인하기
def check_bfs(x,y):
    visit=[[False]*M for _ in range(N)]
    visit[x][y]=True
    q=deque([(x,y)])
    cnt=1
    while q:
        qx,qy=q.popleft()
        for i in range(4):
            nx=qx+dx[i]
            ny=qy+dy[i]
            if 0 < nx <(N-1) and 0 < ny <(M-1) and not visit[nx][ny] and iceberg[nx][ny]>0:
                visit[nx][ny]=True
                q.append((nx,ny))
                cnt+=1
    return cnt
    
# 시뮬레이션 전 초기 빙산 개수 파악
ice_cnt = 0
for i in range(1, N-1):
    for j in range(1, M-1):
        if iceberg[i][j] > 0:
            ice_cnt += 1
            
while True:
    melt=[[0]*M for _ in range(N)] #녹일 거 기록장
    # 1. 빙산 주변 0 개수 카운트
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if iceberg[i][j] > 0: # 빙산인 경우에만 4방향 확인
                zero_count = 0
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    
                    # 주변 4방향 중 바다(0)가 있다면 카운트 증가
                    if iceberg[ni][nj] == 0:
                        zero_count += 1
                
                # 빙산이 녹을 양을 기록장에 저장
                melt[i][j] = zero_count
    # 기록된 메모장을 보고 빙산 녹이기
    for c in range(1,N-1):
        for r in range(1,M-1):
            if iceberg[c][r] > 0: # 빙산인 경우에만
                if iceberg[c][r] <= melt[c][r]:
                    iceberg[c][r] = 0
                    ice_cnt -= 1
                else:
                    iceberg[c][r] -= melt[c][r]
    # 전부 녹았으면
    if ice_cnt==0:
        print(0)
        break
    year += 1 
    # 빙산이 분리됐는지 확인하기
    # 시작점 찾기
    sx,sy=-1,-1
    for z in range(1,N-1):
        for x in range(1,M-1):
            if iceberg[z][x]:
                sx=z
                sy=x
                break
        if sx != -1:
            break
    connect=check_bfs(sx,sy)
    # 분리 여부 판별
    if connect<ice_cnt:
        print(year)
        break