N = int(input()) # 첫 수
best = []
if N == 1:
    best = [1,1,0,1]
for i in range(1,N):
    test = [N, i]
    while True:
        if test[-2]-test[-1]>=0:
            test.append(test[-2]-test[-1])
        else:
            break
    if len(test) > len(best):
        best = test
print(len(best))
print(*best)