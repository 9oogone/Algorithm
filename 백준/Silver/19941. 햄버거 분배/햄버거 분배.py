import sys
input=sys.stdin.readline
from collections import deque

N,K=map(int,input().split())
table=input().strip()

ham=deque([])
sa=deque([])

for i in range(N):
    if table[i] == 'H':
        ham.append(i)
    else:
        sa.append(i)
 
def eat():
    cnt = 0
    while sa and ham:
        x=ham[0]
        y=sa[0]
        if (y-K)<=x<=(y+K):
            cnt += 1
            x= ham.popleft()
            y = sa.popleft()
        elif x < y:
            x=ham.popleft()
        else:
            y=sa.popleft()
    return cnt

print(eat())