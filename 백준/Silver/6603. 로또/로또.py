import sys
input = sys.stdin.readline
from itertools import combinations

while True:
    nums = list(map(int,input().split()))
    if nums[0]==0:
        break
    
    k = nums[0]
    s = nums[1:]
    ans = list(combinations(s,6))
    for i in ans:
        print(*i)
    print()