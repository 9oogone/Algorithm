import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split()) # n=사람 수 m=친구 관계 수
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)    

visited = [False] * n 

def dfs(idx, connect):
    if connect + 1 == 5:  # 노드 5개 연결되면 종료
        print(1)
        sys.exit()

    for i in graph[idx]:
        if not visited[i]:       # 이웃이 방문 안 됐으면
            visited[i] = True
            dfs(i, connect + 1)
            visited[i] = False   # 백트래킹

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)