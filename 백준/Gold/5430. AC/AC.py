from collections import deque
import sys
input = sys.stdin.readline
t=int(input())
for tc in range(t):
    fx=input().strip()
    n=int(input())
    arr = input().strip()[1:-1]
    if arr:
        arr = deque(list(map(int, arr.split(','))))
    else:
        arr=[]
    q=deque([])
    for i in fx:
        q.append(i)
    
    reverse=False
    error=False
    
    while q:
        now=q.popleft()
        
        if now=='R':
            reverse = not reverse
        else:
            if arr:
                if not reverse:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                error=True
                break
    
    if error:
        print('error')
    else:
        if reverse:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")