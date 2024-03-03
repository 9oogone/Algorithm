num = int(input())
order = list(map(int,input().split())) # 학생들이 뽑은 번호 수
line = [] 
for i in range(num):
    line.insert(i-order[i],i+1)

print(*line)
