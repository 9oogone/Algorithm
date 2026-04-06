import sys
input = sys.stdin.readline

n, k = map(int, input().split())
countries = []

for _ in range(n):
    countries.append(list(map(int, input().split())))


target_country = []
for i in range(n):
    if countries[i][0] == k:
        target_country = countries[i]
        break

rank = 1
for i in range(n):
    # 금메달 비교
    if countries[i][1] > target_country[1]:
        rank += 1
    elif countries[i][1] == target_country[1]:
        # 은메달 비교
        if countries[i][2] > target_country[2]:
            rank += 1
        elif countries[i][2] == target_country[2]:
            # 동메달 비교
            if countries[i][3] > target_country[3]:
                rank += 1

print(rank)