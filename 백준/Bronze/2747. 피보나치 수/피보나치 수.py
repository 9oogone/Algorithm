import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print(1)
    sys.exit()
a = 0 # 앞앞
b = 1 # 앞
tmp = 0 # 현재
for _ in range(n-1):
    tmp = a+b
    a,b = b,tmp
print(tmp)