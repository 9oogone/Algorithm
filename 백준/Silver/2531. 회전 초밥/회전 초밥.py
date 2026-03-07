import sys
input=sys.stdin.readline
from collections import deque
from collections import defaultdict
# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N,d,k,c=map(int,input().split())
sushi=[int(input()) for _ in range(N)]
memo = defaultdict(int)
sushi=sushi*2
window=deque([])
cnt = 0 # 초밥 개수

# 1. 처음에 k 개만큼 창문 채우기
for i in range(k):
    window.append(sushi[i])
    memo[sushi[i]]+=1 # 장부 기록
    # 첫 창문에서 쿠폰 확인 
if c not in memo:
    cnt = len(memo)+1
else:
    cnt = len(memo)
    
# 2. 회전 초밥 돌리기
for i in range(k,len(sushi)):
    a = window.popleft()
    memo[a]-=1
    if memo[a]==0:
        del memo[a]
    window.append(sushi[i])
    memo[sushi[i]]+=1
    
    if c not in memo: # 쿠폰 초밥이 윈도우에 없으면
        cnt = max(len(memo)+1,cnt)
    else: # 쿠폰 초밥이 윈도우에 있으면
        cnt = max(len(memo),cnt)

print(cnt)