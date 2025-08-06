import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
a = []
for i in range(1,n+1):
    a.append(i)
b = permutations(a)

for i in b:
    print(*i)