import sys
input=sys.stdin.readline
import heapq

n=int(input()) # 도시 개수
m=int(input()) # 버스 개수
graph = [[] for _ in range(n+1)]
distance = [int(1e9)]*(n+1)
# 버스 정보 
for i in range(m):
    s,e,w=map(int,input().split())
    graph[s].append([e,w])
    
# ts에서 출발해서 te로 도착해야 한다
ts,te=map(int,input().split())

def dijkstra(start,distance,graph):
    q=[]
    heapq.heappush(q, (0,start))
    distance[start]=0
    
        
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(ts,distance,graph)	

print(distance[te])	

 