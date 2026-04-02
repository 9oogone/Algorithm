import sys
input=sys.stdin.readline
import heapq

start,end=map(int,input().split())

dist=[1e9]*100001
dist[start]=0
pq=[(0,start)] # (누적,위치)        

while pq: 
    time,pos=heapq.heappop(pq)
    
    if time > dist[pos]:
        continue
    
    for next_pos, weight in [(pos*2,0),(pos+1,1),(pos-1,1)]:
        if 0 <= next_pos <= 100000:
            if dist[next_pos] > time + weight:
                dist[next_pos] = time+weight
                heapq.heappush(pq,(dist[next_pos],next_pos))

print(dist[end])


