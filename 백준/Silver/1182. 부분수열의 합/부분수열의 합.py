import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,s = map(int,input().split())
ary = list(map(int,input().split()))

cnt = 0
def dfs(idx,total,total_cnt):
    global cnt
    if idx == n:

        if  total == s and total_cnt>0:
            cnt += 1
        return

    dfs(idx+1,total+ary[idx],total_cnt+1) 
    dfs(idx+1,total,total_cnt) 

dfs(0,0,0)
print(cnt)