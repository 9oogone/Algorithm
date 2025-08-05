import sys
input = sys.stdin.readline
m = int(input())
bit = 0
for i in range(m):
    parts = input().split()
    if parts[0]=='add':
        x=int(parts[1])
        bit |= (1<<x)
    elif parts[0]=='remove':
        x=int(parts[1])
        bit &= ~(1<<x)
    elif parts[0]=='check':
        x=int(parts[1])
        print(1 if bit&(1<<x) else 0)
    elif parts[0]=='toggle':
        x=int(parts[1])
        bit ^= (1 << x)
    elif parts[0]=='all':
        bit=((1<<21)-1)
    else:
        bit = 0
        