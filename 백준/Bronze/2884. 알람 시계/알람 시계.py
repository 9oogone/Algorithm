import sys
H, M = map(int,sys.stdin.readline().split())
# H시 M분
# H시 M분보다 45분 일찍 일어나기

if M >= 45:
    M = M-45
elif M < 45:
    # 당일에 일어나야 할 때
    if H > 0:
        H = H-1
        M = 60-abs(M-45)
    else:
        H = 23
        M = 60-abs(M-45)
        
print(f'{H} {M}')
        