import sys
input=sys.stdin.readline

# 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(N)]

# 장부
memo = [0]*(d+1)
# 초밥 가짓수
cnt = 0

# 초기 창문
for i in range(k):
    if memo[sushi[i]]==0:
        cnt+=1
    memo[sushi[i]]+=1

# 초기 창문의 쿠폰 고려
if memo[c]==0: # 쿠폰 초밥이 창문에 없으면
    maxcnt = cnt+1
else:
    maxcnt = cnt

# 회전 초밥
for i in range(N):
    # popleft
    out=sushi[i]
    memo[out]-=1
    if memo[out]==0:
        cnt-=1
    # append
    come=sushi[(i+k)%N]
    if memo[come]==0:
        cnt+=1
    memo[come]+=1
    # 쿠폰 고려
    if memo[c]==0:
        current = cnt+1
    else:
        current = cnt
    # 최댓값 갱신
    if maxcnt<current:
        maxcnt=current
        if maxcnt==(k+1):
            break

print(maxcnt)