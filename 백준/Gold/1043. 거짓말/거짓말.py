import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split()) # n=사람 수 m=파티 수
truth = list(map(int,input().split())) # 진실을 아는 사람의 고유 번호

if truth[0]==0:
    print(m)
    sys.exit()
else:
    truth = truth[1:]

party = [list(map(int,input().split()))for _ in range(m)]

graph = [[] for _ in range(n+1)]
# 네트워크
for network in range(m):
    if len(party[network]) > 2:
        for i in range(1, len(party[network])):
            for j in range(1, len(party[network])):
                if i != j:
                    graph[party[network][i]].append(party[network][j])

graph = [list(set(normalization))for normalization in graph]

# 연결 리스트 찾기
# 진실 확산
visited = [False]*(n+1)
def bfs(rumor):
    q = deque()
    q.append(rumor)
    
    while q:
        idx = q.popleft()
        if len(graph[idx])>0:
            for i in graph[idx]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True
                    truth.append(i)

for i in truth:
    if not visited[i]:
        visited[i]=True
        bfs(i)

ik = []
for i in range(m):
    for j in party[i][1:]:
        if j in truth:
            ik.append(i)
print(m-(len(set(ik))))