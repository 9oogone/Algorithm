N, K = map(int,input().split())
#학생 수 N, 한 방에 배정할 수 있는 최대 인원 수 K
room = list(map(lambda x: [0,0], range(7)))
cnt = 0
for room_assign in range(N):
    S, Y =map(int,input().split())
    # 성별 S 학년 Y # 여학생 0 남학생 1 room에서는 room[Y][S]
    room[Y][S] += 1 # 방배정 끝
for rc in range(1,7):
    for sex in range(2): # 성별
        if 0 <room[rc][sex] <= K:
            cnt += 1
        elif room[rc][sex] > K: # 최대 방 인원 수 넘었으면
            while room[rc][sex] > K:
                cnt += 1
                room[rc][sex] -= K
            cnt+=1
        else: # 방에 0명 있으면
            continue
print(cnt)
