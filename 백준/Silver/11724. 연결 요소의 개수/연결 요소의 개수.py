import sys
sys.setrecursionlimit(10**6)

node,edge = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(node+1)]
visited = [False]*(node+1)

for _ in range(edge):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

depth = 0

def dfs(now):
    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            dfs(next)


for i in range(1,node+1):
    if not visited[i]:
        dfs(i)
        depth += 1

print(depth)