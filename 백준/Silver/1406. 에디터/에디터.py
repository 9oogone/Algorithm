import sys
input=sys.stdin.readline
from collections import deque
left=deque(input().strip())
right=deque()
M=int(input())
cmd=deque([]) # 명령어
value=deque([]) # 삽입한다면 이거를...


for _ in range(M):
    line=input().split()
    a=line[0]
    if a=='P':
        value.append(line[1])
    cmd.append(a)

# 초기 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

for j in range(M):
    c=cmd.popleft()
    if c=='P':
        v=value.popleft()
        left.append(v)
    elif c == 'L' and left:
        right.appendleft(left.pop())
    elif c == 'D' and right:
        left.append(right.popleft())
    elif c == 'B' and left:
         left.pop()

print("".join(left+right)) 