arr = [[0]*100 for _ in range(100)] # 흰 도화지
paper = int(input()) # 색종이의 수
for _ in range(paper):
    y,x = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j]=1

result = 0
for k in range(100):
    result += arr[k].count(1)
print(result)