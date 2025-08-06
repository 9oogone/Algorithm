import sys
input = sys.stdin.readline
from itertools import combinations
from itertools import permutations

l,c = map(int,input().split())
txt = list(input().split())
txt.sort() 

vowels = {'a', 'e', 'i', 'o', 'u'}

for comb in combinations(txt, l):
    v_cnt = sum(1 for ch in comb if ch in vowels)
    c_cnt = l - v_cnt
    if v_cnt >= 1 and c_cnt >= 2:
        print(''.join(comb))