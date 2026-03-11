import sys
input = sys.stdin.readline
# N=소의 수 M=축사 수
N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
barn = [0]*(M+1) # 축사에 들어있는 소 번호 표기

def dfs(cow):
    # 지금 보는 cow가 들어갈 수 있는 축사 후보들
    cand = graph[cow][1:]
    
    for i in cand:
        # 이번 소가 이번 탐색에서 확인한 축사면
        if visited[i]:
            # 다음 cand로 넘어간다 
            continue
        # 아니면 검토 중 표시
        visited[i]=True
        
        # 그 축사가 비었거나, 그 축사에 있는 소가 다른 데로 비켜줄 수 있다면
        if barn[i]==0 or dfs(barn[i]-1):
            barn[i]=(cow+1) # 소 번호를 1부터 기록
            return True
    return False

cnt = 0
for i in range(N):
    # 매 소마다 축사 방문 배열 초기화(증가 경로 탐색)
    visited=[False]*(M+1)
    if dfs(i):# True 반환되면(소가 빈자리를 찾았거나 협상을 성공하면)
        cnt += 1

print(cnt)