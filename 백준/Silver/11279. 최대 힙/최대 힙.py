import sys
input=sys.stdin.readline
import heapq

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    
    if num == 0:
        if not heap:
            print(0)
        else:
            ans = heapq.heappop(heap)
            print(abs(ans))
    else:
        heapq.heappush(heap,num*-1)