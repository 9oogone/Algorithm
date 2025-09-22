from collections import Counter
import sys
input =sys.stdin.readline
n,m = map(int,input().split())
w = [input().strip() for _ in range(n)]
w = Counter(w)
words = sorted(w.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in words:
    if len(i[0])>=m:
        print(i[0])