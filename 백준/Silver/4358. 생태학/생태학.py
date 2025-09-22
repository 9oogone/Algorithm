from collections import Counter
import sys
input =sys.stdin.readline
trees = []
while True:
    line=input().strip()
    if not line:
        break
    trees.append(line)
num=len(trees)
cnt=Counter(trees)
ans = sorted(cnt.items(), key=lambda x: x[0])

for name,count in ans:
    print(f"{name} {count / num * 100:.4f}")