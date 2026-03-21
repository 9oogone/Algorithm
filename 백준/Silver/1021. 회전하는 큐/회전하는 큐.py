import sys 
input=sys.stdin.readline
from collections import deque
# 큐의 크기 N 
# 뽑아내려고 하는 수의 개수 M
N,M=map(int,input().split())
cand=list(map(int,input().split()))
q = deque([i for i in range(1,N+1)])
ans = 0
# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
    # q.rotate(-1)
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
    # q.rotate(1)
for target in range(M):
    # 찾는 게 첫 번째 원소면
    while True:
        if cand[target]==q[0]:
            q.popleft()
            break
        # 더 찾아야 되면?
        else:
            # 타겟의 인덱스가 큐 길이의 절반 이하이면 왼쪽으로 회전
            if q.index(cand[target]) <= len(q) // 2:
                q.rotate(-1)
                ans += 1
            else:
                q.rotate(1)
                ans += 1
print(ans)