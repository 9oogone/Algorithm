import sys
input=sys.stdin.readline
from collections import deque
N=int(input())
a=[]
for i in range(1,N+1):
    a.append(i)

q=deque(a)

while len(q)>1:
    # 우선 제일 위를 버리고
    q.popleft()
    #그 다음 거는 맨 밑으로
    b=q.popleft()
    q.append(b)

print(*q)