import sys
input=sys.stdin.readline
from collections import deque
me,little = map(int,input().split())

max_spot = 100000
memo = [-1]*(max_spot+1)

q=deque([me])
memo[me]=0

while q:
    now=q.popleft()
    
    if now == little:
        print(memo[now])
        break
    
    for next in (now-1, now+1, now*2):
        if 0<= next <= max_spot and memo[next]<0:
            memo[next]=memo[now]+1
            q.append(next)