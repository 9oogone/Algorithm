from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    s1,s2 = input().split()
    if Counter(s1)==Counter(s2):
        print('Possible')
    else:
        print('Impossible')