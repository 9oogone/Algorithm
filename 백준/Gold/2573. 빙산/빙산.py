import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 빙산 좌표만 따로 추출하여 집합(Set)으로 관리
ice_coords = set()
for i in range(1, N-1):
    for j in range(1, M-1):
        if iceberg[i][j] > 0:
            ice_coords.add((i, j))

def check_bfs(start_x, start_y, current_ice_set):
    visit = set()
    visit.add((start_x, start_y))
    q = deque([(start_x, start_y)])
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 범위를 확인할 필요 없음 (current_ice_set 안에 존재하는지만 확인하면 O(1)로 처리 가능)
            if (nx, ny) in current_ice_set and (nx, ny) not in visit:
                visit.add((nx, ny))
                q.append((nx, ny))
                cnt += 1
    return cnt

year = 0
while ice_coords:
    melt_info = [] # (x, y, 녹을 양) 기록
    
    # 1. 융해량 계산 (살아있는 빙산 좌표만 순회)
    for x, y in ice_coords:
        zero_count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iceberg[nx][ny] == 0:
                zero_count += 1
        if zero_count > 0:
            melt_info.append((x, y, zero_count))
            
    # 2. 융해 적용 및 죽은 빙산 좌표 제거
    for x, y, melt_amt in melt_info:
        iceberg[x][y] -= melt_amt
        if iceberg[x][y] <= 0:
            iceberg[x][y] = 0
            ice_coords.remove((x, y)) # 빙산이 소멸하면 추적 집합에서 제거
            
    year += 1 

    # 3. 종료 조건 검사
    if not ice_coords: # 남은 빙산이 없으면
        print(0)
        break
        
    # 4. 분리 여부 판별
    # 집합에 남아있는 아무 빙산이나 하나 골라서 탐색 시작 (순회 불필요)
    sx, sy = next(iter(ice_coords)) 
    connect = check_bfs(sx, sy, ice_coords)
    
    if connect < len(ice_coords):
        print(year)
        break