from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
books = [input().strip() for _ in range(n)]
books=Counter(books)
maxcnt = max(books.values())
ans = []
for i in books.items():
    if i[1]==maxcnt:
        ans.append(i[0])
ans.sort()
print(ans[0])