import sys
input=sys.stdin.readline
N=int(input())
stand=list(input().strip())
ans = 0

# 두 단어가 같은 구성을 갖는 경우 (그 글자 있을 때) 
# 한 단어에서 한 문자를 더하거나 빼거나 (한 개 많거나 부족할 때)
# 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우 (한 개 다를 때)
for _ in range(N-1):
    comp=input().strip()
    copy= stand[:]
    cnt = 0
    
    for i in comp:
        if i in copy:
            copy.remove(i)
        else:
            cnt += 1
    
    if len(copy) <= 1 and cnt <= 1:
        ans +=1 

print(ans)