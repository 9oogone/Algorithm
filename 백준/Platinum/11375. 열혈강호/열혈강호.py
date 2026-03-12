import sys
input=sys.stdin.readline

# 직원 수 N, 일의 개수 M
N,M=map(int,input().split())
staff=[list(map(int,input().split())) for _ in range(N)]
duty = [0]*(M+1) # 어떤 일(인덱스)을 하는 담당자(그 인덱스 값) 메모

def dfs(work):
    # 지금 보고 있는 staff가 할 수 있는 일의 후보
    cand=staff[work][1:]
    for i in cand:
        # 방문 확인
        if visited[i]:
            continue
        visited[i]=True
        
        # 지금 보고 있는 일을 아무도 안 하고 있거나 하고 있는 사람이 양보할 수 있으면
        if duty[i]==0 or dfs(duty[i]-1):
            duty[i]=(work+1)
            return True
    return False
    

cnt = 0
for i in range(N):
    # 매 직원마다 방문 배열 초기화
    visited=[False]*(M+1)
    if dfs(i): # 직원에게 일 배정 성공하면
        cnt+=1
print(cnt)