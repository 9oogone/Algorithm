import sys
input=sys.stdin.readline
N,X=map(int,input().split())
s=list(map(int,input().split()))
# 종료 조건
if sum(s)==0:
    print('SAD')
    exit()
# 초기 창문 세팅 
# 맨 앞 값
f=s[0]
# 최대 방문자 빈도
cnt=1
# 최대 방문자
mv=0
# 현재 방문자
cv=0
for i in range(X):
    mv+=s[i]
    cv+=s[i]

# 전체 돌기 
for j in range(X,N):
    # 현재 방문자 수 계산
    cv-=f
    cv+=s[j]
    f=s[j-X+1]
    # 최대방문자일까?
    if mv < cv:
        mv=cv
        cnt=1
    elif mv==cv:
        cnt+=1
print(mv)
print(cnt) 