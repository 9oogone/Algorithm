N = int(input())
arr = [[0]*1001 for _ in range(1001)] # 도화지

for p in range(N): # 색종이 개수만큼
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x1+x2):
        for j in range(y1,y1+y2):
            arr[i][j] = p+1
# 색종이 붙이기 끝
for d in range(N):
    result = 0
    for k in range(1001):
        result += arr[k].count(d+1)
    print(result)
        
        