from collections import Counter
import sys
input = sys.stdin.readline
n = input().strip().upper()
n = Counter(n).most_common(2)
if len(n)==1:
    print(n[0][0])
    sys.exit()
if n[0][1]==n[1][1]:
    print('?')
else:
    print(n[0][0])