import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

N, M = map(int, input().split())
staff = [list(map(int, input().split()))[1:] for _ in range(N)]
work = [0] * (M + 1)

# 전역에서 단 1번만 생성
visited = [-1] * (M + 1)

def dfs(a, call_id):
    for i in staff[a]:
        # True/False 대신 고유 식별자(call_id)로 이번 턴의 방문 여부 확인
        if visited[i] == call_id:
            continue
        visited[i] = call_id
        
        if work[i] == 0 or dfs(work[i] - 1, call_id):
            work[i] = a + 1
            return True
    return False

cnt = 0
for i in range(N):
    # i번째 직원의 첫 번째 탐색 (고유 식별자: i * 2)
    if dfs(i, i * 2):
        cnt += 1
    # i번째 직원의 두 번째 탐색 (고유 식별자: i * 2 + 1)
    if dfs(i, i * 2 + 1):
        cnt += 1

print(cnt)