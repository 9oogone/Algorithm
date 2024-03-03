bulb = list(input())
bulb.insert(0,'N')
cnt = 0

for i in range(1,len(bulb)): # 모든 전구를 확인
    if bulb[i] == 'Y': # 현재 전구가 켜져있으면
        for j in range(i, len(bulb), i): # 현재 전구의 배수만큼 확인
            if bulb[j] == 'Y':
                bulb[j] = 'N'
            else:
                bulb[j] = 'Y'
        cnt += 1

print(cnt)
