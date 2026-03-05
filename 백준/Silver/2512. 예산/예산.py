import sys
input=sys.stdin.readline
import heapq

N=int(input())
budget=list(map(int,input().split()))
upper=int(input())

if sum(budget)<=upper:
    print(max(budget))
    sys.exit()

# 힙으로 바꾸기
heapq.heapify(budget)
cnt = N # 남은 지방 수

while budget:
    now=heapq.heappop(budget)
    # 지금 보고 있는 지방에 예산을 다 줄 수 있다면
    if now*cnt <= upper:
        upper -= now
        cnt -= 1
    # 다 못 주면
    else:
        print(upper//cnt)
        break