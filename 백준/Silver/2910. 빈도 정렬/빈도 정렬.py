from collections import Counter
import sys
input = sys.stdin.readline
n,c = map(int, input().split())
ary = list(map(int,input().split()))
counter = Counter(ary)
result = sorted(ary,key=lambda x: (-counter[x],ary.index(x)))
print(*result)