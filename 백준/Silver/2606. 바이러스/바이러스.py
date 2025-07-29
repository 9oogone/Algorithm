import sys
input = sys.stdin.readline
from collections import deque
 
n = int(input()) # 7
m = int(input()) # 6
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    # 1번 컴퓨터는 웜바이러스에 무조건 걸린다
    # 1이랑 연결된 애들 다 걸린다 너비우선탐색임
    
visited = [False]*(n+1)

def bfs(start):    
    q = deque([start])
    visited[start]=True
    
    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

bfs(1)
    
cnt = 0 
for j in visited:
    if j:
        cnt += 1

print(cnt-1)