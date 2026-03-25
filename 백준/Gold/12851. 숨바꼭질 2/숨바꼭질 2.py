import sys
from collections import deque


me, little = map(int, sys.stdin.readline().split())
max_spot = 100000
memo = [-1] * (max_spot + 1)

q = deque([me])
memo[me] = 0

fastest_time = -1
count = 0

while q:
    now = q.popleft()
    
    # 목적지 도달 시
    if now == little:
        if fastest_time == -1: # 처음 도달했을 때
            fastest_time = memo[now]
            count = 1
        elif memo[now] == fastest_time: # 최단 시간과 같은 시간으로 도달했을 때
            count += 1
        continue # 목적지 이후의 이동은 계산할 필요 없음
        
    for nxt in (now - 1, now + 1, now * 2):
        if 0 <= nxt <= max_spot:
            # 1. 처음 방문하거나 
            # 2. 이미 방문했더라도 현재 경로가 기존 최단 시간과 같다면 큐에 추가
            if memo[nxt] == -1 or memo[nxt] == memo[now] + 1:
                memo[nxt] = memo[now] + 1
                q.append(nxt)

print(fastest_time)
print(count)
