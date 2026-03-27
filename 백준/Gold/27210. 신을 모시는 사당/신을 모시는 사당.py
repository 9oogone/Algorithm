import sys
input=sys.stdin.readline

N=int(input())
sculpture=list(map(int,input().split()))

arr = []
for x in sculpture:
    if x == 1:
        arr.append(1)
    else:
        arr.append(-1)

ans_min = 0
ans_max = 0
current_min = 0
current_max = 0

for i in arr:
    current_max = max(i,current_max+i)
    ans_max = max(current_max, ans_max)
    
    current_min = min(i, current_min+i)
    ans_min = min(current_min,ans_min)
    
print(max(ans_max,abs(ans_min)))