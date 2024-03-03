N = int(input()) # 회의의 수
meeting_lst = [list(map(int,input().split())) for _ in range(N)]
meeting_lst.sort(key=lambda x:(x[1],x[0])) # 끝나는 시간 기준 정렬
cnt = 1 # 첫 회의실은 추가했다고 상정
end = meeting_lst[0][1]
for i in range(1,N):
    if meeting_lst[i][0]>=end:
        end = meeting_lst[i][1]
        cnt += 1
print(cnt)