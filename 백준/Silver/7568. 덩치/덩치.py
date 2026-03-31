import sys
input=sys.stdin.readline

N=int(input())
p=[]
for i in range(N):
    a,b=map(int,input().split())
    p.append((a,b))

for j in p:
    rank = 1
    for x in p:
        if j[0]< x[0] and j[1]< x[1]:
            rank += 1
    print(rank, end=' ')