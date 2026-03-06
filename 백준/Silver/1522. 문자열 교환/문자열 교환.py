import sys
input=sys.stdin.readline
from itertools import count

n = input().strip()
an= n.count('a')
t = n*2

bn = int(1e9)

for i in range(len(t)-an):
    ans = t[i:i+an].count('b')
    if bn > ans:
        bn = ans

print(bn)