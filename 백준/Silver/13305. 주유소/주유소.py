import sys
input=sys.stdin.readline

N=int(input())
road=list(map(int,input().split()))
price=list(map(int,input().split()))

cost=0
minprice=price[0]

for i in range(N-1):
    if price[i]<minprice:
        minprice=price[i]
    cost+=road[i]*minprice

print(cost)