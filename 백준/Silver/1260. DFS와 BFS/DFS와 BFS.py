from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

# DFS
visited = [False] * (N+1)
dfs_ans = ''

def dfs(V, graph, visited):
    global dfs_ans
    visited[V] = True
    dfs_ans += str(V) + ' '
    for visit in graph[V]:
        if not visited[visit]:
            dfs(visit, graph, visited)

dfs(V, graph, visited)
print(dfs_ans.strip())

# BFS
visited = [False] * (N+1)

def bfs(V, graph, visited):
    queue = deque()
    queue.append(V)
    visited[V] = True
    bfs_ans = ''

    while queue:
        v = queue.popleft()
        bfs_ans += str(v) + ' '

        for next in graph[v]:  
            if not visited[next]:
                queue.append(next)
                visited[next] = True

    return bfs_ans.strip()

print(bfs(V, graph, visited))

