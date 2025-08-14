import sys
input = sys.stdin.readline
n = int(input())
cost = [[0]]+[list(map(int,input().split())) for _ in range(n)]
r, g, b = cost[1]
for i in range(2,n+1):
    cr,cg,cb = cost[i]
    nr = min(g, b) + cr
    ng = min(r, b) + cg
    nb = min(r, g) + cb
    r,g,b = nr,ng,nb
print(min(r,g,b))