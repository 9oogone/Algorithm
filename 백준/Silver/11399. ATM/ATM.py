import sys
input=sys.stdin.readline
N=int(input())
ans = list(map(int,input().split()))

ans.sort()
current=0
total=0
for i in ans:
    current += i
    total += current

print(total)