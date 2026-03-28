import sys
input=sys.stdin.readline

N=int(input())
ary=list(map(int,input().split()))
ans = []

# 거꾸로 보자
for i in range(N-1,-1,-1):
    ans.insert(ary[i],i+1)

print(*ans)