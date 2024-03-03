w, h = map(int,input().split()) # 격자판 가로 세로
p, q = map(int,input().split()) # 개미의 현재 위치
t = int(input())

# 행부터
# 홀짝 분별 기준
tc = (p+t)//w
if tc%2 == 0:
    print((p+t)%w, end = ' ')
else:
    a = (p+t)%w
    print(w-a, end = ' ')

# 열
tc = (q+t)//h
if tc%2 == 0:
    print((q+t)%h)
else:
    a = (q+t)%h
    print(h-a)

