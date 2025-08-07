import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
p1, p2 = map(int,input().split())
m = int(input())
fam = [list(map(int,input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
for i in fam:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

visited = [False] * (n + 1)
res = -1

def dfs(current, depth):
    global res
    visited[current] = True
    
    if current == p2:
        res = depth
        return
    
    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)

dfs(p1, 0)
print(res)
