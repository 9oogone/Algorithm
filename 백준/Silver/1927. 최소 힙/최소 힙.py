import sys
input=sys.stdin.readline
import heapq

N=int(input()) # 연산의 개수

heap = []

for i in range(N):
    num = int(input())
    if num == 0:
        if not heap:
            print(0)
        else:
            result=heapq.heappop(heap)
            print(result)
    else:
        heapq.heappush(heap,num)