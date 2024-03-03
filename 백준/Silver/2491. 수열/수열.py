N = int(input()) # 수열의 길이
num_lst = list(map(int,input().split()))

d = [[1]*N for _ in range(2)]
for i in range(1,N):
    if num_lst[i-1]<= num_lst[i]: # 증가
        d[0][i] = d[0][i-1]+1
    if num_lst[i-1] >= num_lst[i]:
        d[1][i] = d[1][i-1]+1 # 감소
print(max(map(max,d)))